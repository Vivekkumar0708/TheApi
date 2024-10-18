##### Installation

```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```

---

# API Documentation

This document provides a list of all functions in `TheApi`, along with their status and usage examples.

## Function List

1. [bing_image](#bing_image)
2. [blackpink](#blackpink)
3. [carbon](#carbon)
4. [cat](#cat)
5. [chatgpt](#chatgpt)
6. [dog](#dog)
7. [fox](#fox)
8. [gemini](#gemini)
9. [gen_hashtag](#gen_hashtag)
10. [get_advice](#get_advice)
11. [get_hindi_jokes](#get_hindi_jokes)
12. [get_jokes](#get_jokes)
13. [get_uselessfact](#get_uselessfact)
14. [github_search](#github_search)
15. [hindi_quote](#hindi_quote)
16. [meme](#meme)
17. [morse_code](#morse_code)
18. [pypi](#pypi)
19. [quote](#quote)
20. [randomword](#randomword)
21. [riddle](#riddle)
22. [stackoverflow_search](#stackoverflow_search)
23. [upload_image](#upload_image)
24. [wikipedia](#wikipedia)
25. [words](#words)
26. [write](#write)

## API Status

| Function Name | Status |
|---------------|--------|
| [bing_image](#bing_image) | ✅ |
| [blackpink](#blackpink) | ✅ |
| [carbon](#carbon) | ✅ |
| [cat](#cat) | ✅ |
| [chatgpt](#chatgpt) | ✅ |
| [dog](#dog) | ✅ |
| [fox](#fox) | ✅ |
| [gemini](#gemini) | ✅ |
| [gen_hashtag](#gen_hashtag) | ✅ |
| [get_advice](#get_advice) | ✅ |
| [get_hindi_jokes](#get_hindi_jokes) | ✅ |
| [get_jokes](#get_jokes) | ✅ |
| [get_uselessfact](#get_uselessfact) | ✅ |
| [github_search](#github_search) | ✅ |
| [hindi_quote](#hindi_quote) | ✅ |
| [meme](#meme) | ✅ |
| [morse_code](#morse_code) | ✅ |
| [pypi](#pypi) | ✅ |
| [quote](#quote) | ✅ |
| [randomword](#randomword) | ✅ |
| [riddle](#riddle) | ✅ |
| [stackoverflow_search](#stackoverflow_search) | ✅ |
| [upload_image](#upload_image) | ✅ |
| [wikipedia](#wikipedia) | ✅ |
| [words](#words) | ✅ |
| [write](#write) | ✅ |

## Code Usage and Results:

### bing_image

```python
from TheApi import api

result = api.bing_image(query='pokemon', limit=3)
print(result)
```

```text
['https://assets.vg247.com/current/2016/07/pokemon_sun_an_moon_rockruff.jpg', 'http://www.animextremist.com/imagenes/pokemon/pokemon97.jpg', 'https://www.pokemon.com/static-assets/app/static3/img/og-default-image.jpeg']
```

### blackpink

```python
from TheApi import api

result = api.blackpink(args='pokemon', color='#ff94e0', border_color=None)
print(result)
```

```text
https://envs.sh/0Ql.jpg
```

### carbon

```python
from TheApi import api

result = api.carbon(query='pokemon')
print(result)
```

```text
https://envs.sh/0Qk.png
```

### cat

```python
from TheApi import api

result = api.cat()
print(result)
```

```text
https://cdn2.thecatapi.com/images/7cm.jpg
```

### chatgpt

```python
from TheApi import api

result = api.chatgpt(query='pokemon')
print(result)
```

```text
Sure! Pokémon is a popular franchise created by Satoshi Tajiri and Ken Sugimori, and it was first introduced by Nintendo, Game Freak, and Creatures in 1996. The franchise includes video games, trading card games, an animated television series, movies, merchandise, and more.

In the Pokémon world, trainers capture and train creatures known as Pokémon to battle each other. Each Pokémon has its own unique abilities, types, and stats. The goal for many trainers is to become a Pokémon Master by defeating Gym Leaders, competing in Pokémon Leagues, and completing the Pokédex, which is a comprehensive Pokémon encyclopedia.

If you have specific questions about Pokémon, such as game mechanics, Pokémon types, strategies, or anything else, feel free to ask!
```

### dog

```python
from TheApi import api

result = api.dog()
print(result)
```

```text
https://random.dog/fb6ff563-8d84-4244-a3b1-24cafe220a35.webm
```

### fox

```python
from TheApi import api

result = api.fox()
print(result)
```

```text
https://randomfox.ca/?i=29
```

### gemini

```python
from TheApi import api

result = api.gemini(query='pokemon')
print(result)
```

```text
Sure! Pokémon is a popular franchise created by Satoshi Tajiri and Ken Sugimori, and it is managed by The Pokémon Company, which is a collaboration between Nintendo, Game Freak, and Creatures Inc. The franchise began with the release of Pokémon Red and Green in Japan in 1996 and has since expanded to include video games, trading card games, an animated television series, movies, merchandise, and more.

In the Pokémon world, trainers catch and train creatures called Pokémon, which they use to battle each other. Each Pokémon has its own unique abilities, types, and characteristics. The goal for many trainers is to become Pokémon Champions by defeating Gym Leaders and the Elite Four, as well as completing their Pokédex, an in-game encyclopedia of Pokémon species.

If you have specific questions about Pokémon, whether it's about games, characters, types, or strategies, feel free to ask!
```

### gen_hashtag

```python
from TheApi import api

result = api.gen_hashtag(text='pokemon', similiar=False)
print(result)
```

```text
#pokemon  #pokemongo  #pokemoncards  #pokemontcg  #pokemoncommunity  #pokemonsun  #pokemonsunandmoon  #pokemonmoon  #pokemonxy  #pokemonart  #pokemon20  #pokemonx  #pokemony  #pokemonmemes  #pokemontrainer  #PokemonMaster  #pokemonoras  #pokemonfanart  #pokemonfan  #pokemoncollector  #pokemonred  #pokemonmeme  #pokemoncenter  #pokemonultrasun  #pokemonblue  #pokemoncard  #pokemoncollection  #pokemonultramoon  #pokemoncardsforsale  #pokemoncosplay
```

### get_advice

```python
from TheApi import api

result = api.get_advice()
print(result)
```

```text
Don't assume anything is possible or impossible until you've asked the people who will be doing the work.
```

### get_hindi_jokes

```python
from TheApi import api

result = api.get_hindi_jokes()
print(result)
```

```text
कागज़ पे लिखी गजल बकरी चबा गयी चर्चा पूरे गांव में हुई की बकरी शेर खा गयी 😆🤣😋😉
```

### get_jokes

```python
from TheApi import api

result = api.get_jokes(amount=1)
print(result)
```

```text
Two reasons I don't give money to homeless people.
1) They are going to spend it all on drugs and alcohol
2) I am going to spend it all on drugs and alcohol.
```

### get_uselessfact

```python
from TheApi import api

result = api.get_uselessfact()
print(result)
```

```text
Rhode Island is the only state which the hammer throw is a legal high school sport.
```

### github_search

```python
from TheApi import api

result = api.github_search(query='pokemon', search_type='repositories', max_results=3)
print(result)
```

```text
[{'name': 'PokemonGo-Map', 'full_name': 'AHAAAAAAA/PokemonGo-Map', 'description': '🌏 Live visualization of all the pokemon in your area... and more! (shutdown)', 'url': 'https://github.com/AHAAAAAAA/PokemonGo-Map', 'language': None, 'stargazers_count': 7530, 'forks_count': 2815}, {'name': 'pokemon-showdown', 'full_name': 'smogon/pokemon-showdown', 'description': 'Pokémon battle simulator.', 'url': 'https://github.com/smogon/pokemon-showdown', 'language': 'TypeScript', 'stargazers_count': 4769, 'forks_count': 2784}, {'name': 'PokemonGo-Bot', 'full_name': 'PokemonGoF/PokemonGo-Bot', 'description': 'The Pokemon Go Bot, baking with community.', 'url': 'https://github.com/PokemonGoF/PokemonGo-Bot', 'language': 'Python', 'stargazers_count': 3864, 'forks_count': 1542}]
```

### hindi_quote

```python
from TheApi import api

result = api.hindi_quote()
print(result)
```

```text
ऐसा नहीं है कि अब तेरी जूस्तजू नहीं रहीं, बस टूट-टूट कर बिखरने की हिम्मत नहीं रही।
```

### meme

```python
from TheApi import api

result = api.meme()
print(result)
```

```text
https://preview.redd.it/0aq88vl81gvd1.png?width=320&crop=smart&auto=webp&s=020a5d71200bf03f220b5aeff91480868fbe54dc
```

### morse_code

```python
from TheApi import api

result = api.morse_code(txt='pokemon')
print(result)
```

```text
.--. --- -.- . -- --- -.
```

### pypi

```python
from TheApi import api

result = api.pypi(package_name='pokemon')
print(result)
```

```text
{'name': 'pokemon', 'version': '0.36', 'summary': 'ascii database of pokemon... in Python!', 'author': 'Vanessa Sochat', 'author_email': 'vsoch@noreply.github.users.com', 'license': 'LICENSE', 'home_page': 'https://github.com/vsoch/pokemon', 'package_url': 'https://pypi.org/project/pokemon/', 'requires_python': '', 'keywords': 'pokemon,avatar,ascii,gravatar', 'classifiers': [], 'project_urls': {'Homepage': 'https://github.com/vsoch/pokemon'}}
```

### quote

```python
from TheApi import api

result = api.quote()
print(result)
```

```text
Never find fault with the absent.

author - Alexander Pope
```

### randomword

```python
from TheApi import api

result = api.randomword()
print(result)
```

```text
appositely
```

### riddle

```python
from TheApi import api

result = api.riddle()
print(result)
```

```text
{'riddle': 'Three playing cards in a row. Can you name them with these clues? There is a two to the right of a king. A diamond will be found to the left of a spade. An ace is to the left of a heart. A heart is to the left of a spade. Now, identify all three cards.', 'answer': 'Ace of Diamonds, King of Hearts, Two of Spades'}
```

### stackoverflow_search

```python
from TheApi import api

result = api.stackoverflow_search(query='pokemon', max_results=3, sort_type='relevance', use_cache=True)
print(result)
```

```text
[{'tags': ['ios', 'flutter', 'dart'], 'owner': {'account_id': 19921816, 'reputation': 3, 'user_id': 14597469, 'user_type': 'registered', 'profile_image': 'https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256', 'display_name': 'Senem Sedef', 'link': 'https://stackoverflow.com/users/14597469/senem-sedef'}, 'is_answered': False, 'view_count': 117, 'answer_count': 0, 'score': 0, 'last_activity_date': 1701515081, 'creation_date': 1622231772, 'last_edit_date': 1701515081, 'question_id': 67744802, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon', 'title': 'The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon'}, {'tags': ['reactjs', 'random', 'axios'], 'owner': {'account_id': 17931576, 'reputation': 1, 'user_id': 13028884, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2', 'display_name': 'GieGie', 'link': 'https://stackoverflow.com/users/13028884/giegie'}, 'is_answered': False, 'view_count': 1935, 'answer_count': 2, 'score': 0, 'last_activity_date': 1652730812, 'creation_date': 1642222168, 'last_edit_date': 1642223800, 'question_id': 70718940, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time', 'title': 'Pokemon API request generate 5 Pok&#233;mon at a time'}, {'tags': ['java'], 'owner': {'account_id': 919945, 'reputation': 43, 'user_id': 951797, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG', 'display_name': 'Brian', 'link': 'https://stackoverflow.com/users/951797/brian'}, 'is_answered': True, 'view_count': 32593, 'accepted_answer_id': 7942409, 'answer_count': 3, 'score': 3, 'last_activity_date': 1577442848, 'creation_date': 1319931614, 'question_id': 7942384, 'content_license': 'CC BY-SA 3.0', 'link': 'https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator', 'title': 'Simple Java Pokemon Fight Simulator'}]
```

### upload_image

```python
from TheApi import api

result = api.upload_image(file_path='file/to/image')
print(result)
```

```text
You will get the URL for the image.
```

### wikipedia

```python
from TheApi import api

result = api.wikipedia(query='pokemon')
print(result)
```

```text
{'title': 'Pokémon', 'summary': 'Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise\'s target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pokémon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed "Pokémania". By 2002, the craze had ended, after which Pokémon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pokémon Go, an augmented reality game developed by Niantic. Pokémon has since been estimated to be the world\'s highest-grossing media franchise and one of the best-selling video game franchises.\nPokémon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pokémon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pokémon Company (TPC) in 1998 to manage the Pokémon property within Asia. The Pokémon anime series and films are co-owned by Shogakukan. Since 2009, The Pokémon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.\n\n', 'url': 'https://en.wikipedia.org/?curid=23745', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png'}
```

### words

```python
from TheApi import api

result = api.words(num_words=5)
print(result)
```

```text
['telamon', 'paroxysm', 'battleground', 'neocortical', 'footstone']
```

### write

```python
from TheApi import api

result = api.write(text='pokemon')
print(result)
```

```text
https://envs.sh/0Q7.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)