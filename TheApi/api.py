import inspect
import os
import re
import textwrap
from io import BytesIO
from typing import List, Union

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont, ImageOps

from .errors import InvalidAmountError, RequestError
from .functions import MORSE_CODE_DICT
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TheApi:
    def __init__(self):
        self.session = requests.Session()
        self.base_urls = {
            'carbon': "https://carbonara.solopov.dev/api/cook",
            'quote': "https://api.quotable.io/random",
            'hindi_quote': "https://hindi-quotes.vercel.app/random",
            'random_word': "https://random-word-api.herokuapp.com/word",
            'image': "https://graph.org/file/1f8d00177ac2429b101b9.jpg",
            'font': "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf",
            'upload': "https://envs.sh",
            'chatgpt': "https://chatwithai.codesearch.workers.dev/",
            'advice': "https://api.adviceslip.com/advice",
            'jokes': "https://v2.jokeapi.dev/joke/Any",
            'hindi_jokes': "https://hindi-jokes-api.onrender.com/jokes?api_key=93eeccc9d663115eba73839b3cd9",
            'useless_fact': "https://uselessfacts.jsph.pl/api/v2/facts/random",
            'hashtag_generator': "https://all-hashtag.com/library/contents/ajax_generator.php",
            'wikipedia_search': "https://en.wikipedia.org/w/api.php",

            'words': "https://random-word-api.herokuapp.com/word",
            'cat': "https://api.thecatapi.com/v1/images/search",
            'dog': "https://random.dog/woof.json",
            'pypi': "https://pypi.org/pypi",
            'meme': "https://meme-api.com/gimme",
            'fox': "https://randomfox.ca/floof/",
            'bing_image': "https://www.bing.com/images/async"
        }

    def _make_request(
        self, 
        url: str, 
        method: str = 'GET', 
        params: dict = None, 
        data: dict = None,
        files: dict = None,
        headers: dict = None
    ) -> Union[dict, str]:
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                files=files,
                headers=headers
            )
            response.raise_for_status()
            return response.json() if 'application/json' in response.headers.get('Content-Type', '') else response.text
        except requests.exceptions.RequestException as e:
            raise RequestError(f"Request failed: {str(e)}")

    def chatgpt(self, query):
        url = f"{self.base_urls['chatgpt']}?chat={query}&model=gpt-4o"
        response = self._make_request(url)
        return response['result']

    def get_advice(self):
        response = self._make_request(self.base_urls['advice'])
        return response["slip"]["advice"]

    def get_jokes(self, amount=1):
        url = self.base_urls['jokes']
        params = {"type": "single", "amount": amount}
        response = self._make_request(url, params=params)

        if amount == 1:
            return response["joke"]
        else:
            jokes = [joke["joke"] for joke in response["jokes"]]
            return "\n\n".join(f"{i + 1}. {joke}" for i, joke in enumerate(jokes))

    def get_hindi_jokes(self):
        response = self._make_request(self.base_urls['hindi_jokes'])
        return response["jokeContent"] if response["status"] else "No joke found."

    def get_uselessfact(self):
        response = self._make_request(self.base_urls['useless_fact'])
        return response["text"]

    def gen_hashtag(self, text, similar: bool = False):
        url = self.base_urls['hashtag_generator']
        data = {"keyword": text, "filter": "top"}
        response = self._make_request(url, method="POST", data=data)
        
        soup = BeautifulSoup(response, "html.parser")
        hashtags = soup.find("div", id="copy-hashtags").text.strip() if soup.find("div", id="copy-hashtags") else ""
        
        if similar:
            similar_hashtags = soup.find("div", id="copy-hashtags-similar")
            similar_hashtags_text = similar_hashtags.text.strip() if similar_hashtags else ""
            return hashtags, similar_hashtags_text
        return hashtags

    def quote(self) -> str:
        """Fetch a random quote."""
        data = self._make_request(self.base_urls['quote'])
        return f"{data['content']}\n\nauthor - {data['author']}"

    def hindi_quote(self) -> str:
        """Fetch a random Hindi quote."""
        data = self._make_request(self.base_urls['hindi_quote'])
        return data["quote"]

    def random_word(self) -> str:
        """Fetch a random word."""
        params = {'number': 1}
        try:
            data = self._make_request(self.base_urls['random_word'], params=params)
            return data[0]
        except RequestError:
            return "None"

    def write(self, text):
        tryimg = "https://graph.org/file/1f8d00177ac2429b101b9.jpg"
        tryresp = requests.get(tryimg)
        img = Image.open(BytesIO(tryresp.content))
        draw = ImageDraw.Draw(img)
        font_url = "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf"
        font_response = requests.get(font_url)
        font = ImageFont.truetype(BytesIO(font_response.content), 24)

        x, y = 150, 140
        lines = []
        if len(text) <= 55:
            lines.append(text)
        else:
            all_lines = text.split("\n")
            for line in all_lines:
                if len(line) <= 55:
                    lines.append(line)
                else:
                    k = len(line) // 55
                    lines.extend(
                        line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2)
                    )

        umm = lines[:25]

        line_height = font.getbbox("hg")[3]
        linespacing = 41
        for line in umm:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + linespacing
        a = self.randomword()
        file = f"write_{a}.jpg"
        img.save(file)
        if os.path.exists(file):
            upload_path = self.upload_image(file)

            return upload_path

    def carbon(self, query):
        response = self._make_request(self.base_urls["carbon"], method="POST", data={"code": query})

        image = BytesIO(response)
        image.name = f"{self.randomword()}.png"

        upload_path = self.upload_image(image)
        return upload_path

    def morse_code(self, txt):
        MORSE_CODE_DICT_REVERSED = {
            value: key for key, value in MORSE_CODE_DICT.items()
        }
        is_morse = all(char in ".- /" for char in txt)

        if is_morse:
            decoded_message = ""
            words = txt.split(" / ")
            for word in words:
                for morse_char in word.split():
                    if morse_char in MORSE_CODE_DICT_REVERSED:
                        decoded_message += MORSE_CODE_DICT_REVERSED[morse_char]
                    else:
                        return f"Error: Morse code '{morse_char}' not recognized."
                decoded_message += " "
            return decoded_message.strip()
        else:
            encoded_message = ""
            for char in txt.upper():
                if char in MORSE_CODE_DICT:
                    encoded_message += MORSE_CODE_DICT[char] + " "
                else:
                    return f"Error: Character '{char}' cannot be encoded in Morse code."
            return encoded_message.strip()

    def wikipedia(self, query):
        search_url = self.base_urls['wikipedia_search']

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        search_response = self._make_request(search_url, params=params)
        search_results = search_response.get("query", {}).get("search", [])

        if search_results:
            top_result = search_results[0]
            page_id = top_result["pageid"]
            summary_url = (
                f"{self.base_urls['wikipedia_search']}?action=query&prop=extracts|pageimages"
                f"&exintro&explaintext&piprop=thumbnail&pithumbsize=500&format=json&pageids={page_id}"
            )
            
            summary_response = self._make_request(summary_url)
            pages = summary_response.get("query", {}).get("pages", {})
            page_info = pages.get(str(page_id), {})
            image_url = page_info.get("thumbnail", {}).get("source", "No image available")

            return {
                "title": top_result["title"],
                "summary": page_info.get("extract", "No summary available."),
                "url": f"https://en.wikipedia.org/?curid={page_id}",
                "image_url": image_url,
            }
        else:
            return {"error": "No search results found"}

    def github_search(self, query, search_type="repositories", max_results=3):
        """
        Search GitHub for various types of content.

        Parameters:
            query (str): The search query.
            search_type (str): The type of search (default is "repositories").
            max_results (int): The maximum number of results to return (default is 10).

        Returns:
            list: A list of search results or an error message.

        Examples:
            repositories = api.github_search("machine learning", api.search_type="repositories")

            users = api.github_search("torvalds", search_type="users")

            organization = api.github_search("github", search_type="organizations")

            issues = api.github_search("bug fix", search_type="issues")

            pull_requests = api.github_search("new feature", search_type="pull_requests")

            commits = api.github_search("initial commit", search_type="commits")

            labels = api.github_search("enhancement", search_type="labels")

            topics = api.github_search("python", search_type="topics")
        """
        valid_search_types = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "topics",
        ]

        if search_type not in valid_search_types:
            return {
                "error": f"Invalid search type. Valid types are: {valid_search_types}"
            }

        url_mapping = {
            "pull_requests": "https://api.github.com/search/issues",
            "organizations": "https://api.github.com/search/users",
            "topics": "https://api.github.com/search/topics",
        }

        if search_type in url_mapping:
            url = url_mapping[search_type]
            if search_type == "pull_requests":
                query += " type:pr"
            elif search_type == "organizations":
                query += " type:org"
        else:
            url = f"https://api.github.com/search/{search_type}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get("items", [])

            result_list = []

            for item in items:
                item_info = {}
                if search_type == "repositories":
                    item_info = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "description": item["description"],
                        "url": item["html_url"],
                        "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count"),
                        "forks_count": item.get("forks_count"),
                    }
                elif search_type in ["users", "organizations"]:
                    item_info = {
                        "login": item["login"],
                        "id": item["id"],
                        "url": item["html_url"],
                        "avatar_url": item.get("avatar_url"),
                        "type": item.get("type"),
                        "site_admin": item.get("site_admin"),
                        "name": item.get("name"),
                        "company": item.get("company"),
                        "blog": item.get("blog"),
                        "location": item.get("location"),
                        "email": item.get("email"),
                        "bio": item.get("bio"),
                        "public_repos": item.get("public_repos"),
                        "public_gists": item.get("public_gists"),
                        "followers": item.get("followers"),
                        "following": item.get("following"),
                    }
                elif search_type in ["issues", "pull_requests"]:
                    item_info = {
                        "title": item["title"],
                        "user": item["user"]["login"],
                        "state": item["state"],
                        "url": item["html_url"],
                        "comments": item.get("comments"),
                        "created_at": item.get("created_at"),
                        "updated_at": item.get("updated_at"),
                        "closed_at": item.get("closed_at"),
                    }
                elif search_type == "commits":
                    item_info = {
                        "sha": item["sha"],
                        "commit_message": item["commit"]["message"],
                        "author": item["commit"]["author"]["name"],
                        "date": item["commit"]["author"]["date"],
                        "url": item["html_url"],
                    }
                elif search_type == "topics":
                    item_info = {
                        "name": item["name"],
                        "display_name": item.get("display_name"),
                        "short_description": item.get("short_description"),
                        "description": item.get("description"),
                        "created_by": item.get("created_by"),
                        "url": item.get("url") if "url" in item else None,
                    }

                result_list.append(item_info)

            return result_list

        except requests.exceptions.RequestException as e:
            return {"error": f"Request exception: {e}"}
        except requests.exceptions.HTTPError as e:
            return {
                "error": f"HTTP error: {e.response.status_code} - {e.response.text}"
            }
        except KeyError as e:
            return {"error": f"Key error: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

    def words(self, num_words: int):
        url = f"{self.base_urls['words']}?number={num_words}"
        response = self._make_request(url)
        return response if response else []

    def cat(self):
        response = self._make_request(self.base_urls['cat'])
        return response[0]["url"] if response else None

    def dog(self):
        response = self._make_request(self.base_urls['dog'])
        return response["url"] if response else None

    def pypi(self, package_name):
        url = f"{self.base_urls['pypi']}/{package_name}/json"
        response = self._make_request(url)
        if response:
            info = response["info"]
            relevant_info = {
                "name": info["name"],
                "version": info["version"],
                "summary": info["summary"],
                "author": info["author"],
                "author_email": info["author_email"],
                "license": info["license"],
                "home_page": info["home_page"],
                "package_url": info["package_url"],
                "requires_python": info["requires_python"],
                "keywords": info["keywords"],
                "classifiers": info["classifiers"],
                "project_urls": info["project_urls"],
            }
            return relevant_info
        else:
            return None

    def meme(self):
        response = self._make_request(self.base_urls['meme'])
        return response["preview"][-1] if response else None

    def fox(self):
        response = self._make_request(self.base_urls['fox'])
        return response["link"] if response else None

    def bing_image(self, query: str, limit: int = 3):
        data = {
            "q": query,
            "first": 0,
            "count": limit,
            "adlt": "off",
            "qft": "",
        }
        response = self._make_request(self.base_urls['bing_image'], params=data)
        return re.findall(r"murl&quot;:&quot;(.*?)&quot;", response) if response else []

    def stackoverflow_search(
        self, query, max_results=3, sort_type="relevance", use_cache=True
    ):
        """
        Search Stack Overflow for a given query and return results.

        Args:
            query (str): The search query.
            max_results (int): Maximum number of results to return. Default is 200.
            sort_type (str): The sort type for results. Options are 'activity', 'votes', 'creation', 'relevance'. Default is 'relevance'.
            use_cache (bool): If True, use cached results if available. Default is True.

        Returns:
            list: A list of search results from Stack Overflow.

        Example usage:
           from TheApi import api

           results = api.stackoverflow_search("flask search function", max_results=100, sort_type='votes', use_cache=False)
           for result in results:
               print(f"Title: {result['title']}\nLink: {result['link']}\nScore: {result['score']}\nTags: {', '.join(result['tags'])}\nAnswers: {result['answer_count']}\n")
        """
        cache = {}

        if use_cache:
            cache_key = (query, sort_type)
            if cache_key in cache:
                return cache[cache_key]

        url = "https://api.stackexchange.com/2.3/search/advanced"
        params = {
            "order": "desc",
            "sort": sort_type,
            "q": query,
            "site": "stackoverflow",
            "page": 1,
        }

        all_results = []
        while len(all_results) < max_results:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                break

            results = response.json().get("items", [])
            if not results:
                break

            all_results.extend(results)
            if len(results) < 30:
                break

            params["page"] += 1

        all_results = all_results[:max_results]
        cache[cache_key] = all_results

        return all_results

    def blackpink(self, args, color="#ff94e0", border_color=None):
        text = args
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        initial_font_size = 100

        img_width = 800
        img_height = 600

        dummy_img = Image.new("RGB", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)

        font_size = initial_font_size
        padding = 50
        max_width = img_width - 2 * padding
        max_height = img_height - 2 * padding

        font = ImageFont.truetype(font_path, font_size)
        lines = textwrap.wrap(text, width=40)

        while True:
            text_height = sum(draw_dummy.textsize(line, font=font)[1] for line in lines)
            if text_height <= max_height and all(
                draw_dummy.textsize(line, font=font)[0] <= max_width for line in lines
            ):
                break
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)
            lines = textwrap.wrap(text, width=40)
        gradient = Image.new("RGB", (img_width, img_height), color)
        for i in range(img_height):
            r = int(255 - (255 - int(color[1:3], 16)) * (i / img_height))
            g = int(148 - (148 - int(color[3:5], 16)) * (i / img_height))
            b = int(224 - (224 - int(color[5:7], 16)) * (i / img_height))
            ImageDraw.Draw(gradient).line([(0, i), (img_width, i)], fill=(r, g, b))

        img = Image.new("RGB", (img_width, img_height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        y_text = (img_height - text_height) // 2
        for line in lines:
            line_width, line_height = draw.textsize(line, font=font)
            draw.text(
                ((img_width - line_width) // 2, y_text),
                line,
                fill=color,
                font=font,
                align="center",
            )
            y_text += line_height

        border_color = border_color or color
        border_width = 28
        img_with_border = ImageOps.expand(img, border=border_width, fill=border_color)

        final_img = Image.new(
            "RGB", (img_with_border.width, img_with_border.height), (0, 0, 0)
        )
        final_img.paste(gradient, (0, 0))
        final_img.paste(img_with_border, (0, 0))

        temp_file_path = "temp_blackpink_image.jpg"
        final_img.save(temp_file_path, format="JPEG")
        response = self.upload_image(temp_file_path)

        return response

    def upload_image(self, file_path: Union[str, bytes, BytesIO]) -> str:
        if isinstance(file_path, str):
            try:
                with open(file_path, "rb") as f:
                    image_bytes = f.read()
            except FileNotFoundError:
                raise ValueError(f"File not found: '{file_path}' - Ensure the file path is correct.")
        elif isinstance(file_path, bytes) or isinstance(file_path, BytesIO):
            image_bytes = file_path if isinstance(file_path, bytes) else file_path.getvalue()
        else:
            raise ValueError("Invalid input type - Expected a file path (str), binary data (bytes), or BytesIO object.")

        url = self.base_urls['upload']
        files = {"file": (file_path.name if isinstance(file_path, BytesIO) else "image.png", image_bytes, "image/png")}

        try:
            response = self._make_request(url=url, method="POST", files=files)
            return response.strip() if isinstance(response, str) else "Unexpected response format"
        except RequestError as e:
            raise ValueError(f"Upload failed: {str(e)}")


    @staticmethod
    def riddle() -> dict:
        """
        Fetch a random riddle from the riddles API.

        Returns:
            dict: The riddle data in JSON format.
        """
        response = requests.get("https://riddles-api.vercel.app/random")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Could not fetch riddle"}


api = TheApi()
