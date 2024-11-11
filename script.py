import asyncio
import inspect

import aiofiles

from TheApi import api


async def test_method(method, *args):
    try:
        if inspect.iscoroutinefunction(method):
            result = await method(*args)
        else:
            result = method(*args)
        status = "✅"
        return status, result
    except Exception as e:
        status = "❌"
        return status, str(e)


def format_docstring(docstring):
    lines = docstring.splitlines()
    formatted_lines = []
    in_section = False

    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line in ["Args:", "Returns:", "Raises:"]:
            formatted_lines.append(f"-  **{stripped_line}**")  # Section header with a bullet point
            in_section = True
        elif in_section and line.startswith("    "):
            formatted_lines.append(f"  - {line.strip()}")  # Indented item with a sub-bullet
        elif stripped_line == "":
            formatted_lines.append("")  # Maintain blank lines
            in_section = False
        else:
            formatted_lines.append(f"**Description**:\n{stripped_line}") if not in_section else formatted_lines.append(stripped_line)  # Regular description line
            in_section = False

    return "\n".join(formatted_lines)


async def generate_api_status(methods):
    function_statuses = []
    readme_content = []
    status_content = []
    function_count = 1

    for name, method in methods:
        print(f"Processing {name}")
        if name.startswith("_"):
            continue

        signature = inspect.signature(method)
        docstring = inspect.getdoc(method) or "No description available."
        status_content.append(
            f"| [{name.replace('_', ' ').title()}](#{name.lower()}) | "
        )

        # Preserve Google-style docstring formatting in Markdown
        formatted_docstring = format_docstring(docstring)

        if name == "upload_image":
            status = "✅"
            result = "You will get the URL for the image."
            readme_content.append(
                f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                f"{formatted_docstring}\n\n"
                f"```python\nfrom TheApi import api\n\n"
                f"result = await api.upload_image(file_path='file/to/image.jpg')\n"
                f"print(result)\n```\n\n"
                f"#### Expected Output\n\n"
                f"```text\n{result}\n```\n"
            )
        elif len(signature.parameters) == 0:
            status, result = await test_method(method)
            readme_content.append(
                f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                f"{formatted_docstring}\n\n"
                f"```python\nfrom TheApi import api\n\n"
                f"result = await api.{name}()\n"
                f"print(result)\n```\n\n"
                f"#### Expected Output\n\n"
                f"```text\n{result}\n```\n"
            )
        else:
            params = []
            for param in signature.parameters.values():
                if param.default is not param.empty:
                    param_value = repr(param.default)
                    params.append(f"{param.name}={param_value}")
                elif param.annotation is int:
                    params.append(f"{param.name}=5")
                else:
                    params.append(f"{param.name}='example_value'")

            status, result = await test_method(
                method, *[eval(param.split("=")[1]) for param in params]
            )

            params_str = ", ".join(params)

            if status == "✅":
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom TheApi import api\n\n"
                    f"result = await api.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"#### Expected Output\n\n"
                    f"```text\n{result}\n```\n"
                )
            else:
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom TheApi import api\n\n"
                    f"result = await api.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"#### Expected Output\n\n"
                    f"```text\n# Error:\n{result}\n```\n"
                )

        status_content[-1] += status
        function_statuses.append((name, status))
        function_count += 1

    return status_content, readme_content


async def write_api_status_to_file(
    status_content,
    readme_content,
    readme_file="README.md",
    separator="---",
    license_text="\nThis Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)",
):
    try:
        with open(readme_file, "r") as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = ""

    if separator in existing_content:
        pre_separator_content, _ = existing_content.split(separator, 1)
    else:
        pre_separator_content = existing_content

    status_str = "\n".join(status_content)
    new_content = "\n".join(readme_content)

    preface = "# 📘 API Documentation\n\n"
    preface += (
        "Welcome to the **TheApi**! This library allows you to easily interact with the API using both **synchronous** and **asynchronous** options.\n\n"
        "- **Sync**: `from TheApi.sync import api`\n"
        "- **Async**: `from TheApi import api`\n\n"
        "Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀\n\n"
        "## Status\n\n"
        "| Function           | Status |\n"
        "|--------------------|--------|\n"
        f"{status_str}\n\n"
    )

    updated_content = (
        pre_separator_content.strip() + "\n\n" + separator + "\n\n" + preface
    )
    updated_content += "\n## 🎓 How to Use Each Function\n\n" + new_content
    updated_content += "\n" + license_text

    async with aiofiles.open(readme_file, "w") as f:
        await f.write(updated_content)


async def main():
    methods = inspect.getmembers(
        api, predicate=lambda m: inspect.ismethod(m) or inspect.isfunction(m)
    )
    status_content, readme_content = await generate_api_status(methods)
    await write_api_status_to_file(status_content, readme_content)


if __name__ == "__main__":
    asyncio.run(main())
