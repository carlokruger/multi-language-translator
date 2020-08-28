from bs4 import BeautifulSoup
import requests

language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
text = input('Type the word you want to translate:')

print('You chose "{}" as the language to translate "{}" to.'.format(language, text))

if language == "fr":
    url = 'https://context.reverso.net/translation/english-french/' + text
elif language == "en":
    url = 'https://context.reverso.net/translation/french-english/' + text

print(url)

user_agent = 'Mozilla/5.0'

site = requests.get(url, headers={'User-Agent': user_agent})

print(site.status_code, "OK")

soup = BeautifulSoup(site.content, 'html.parser')

translations_div = soup.find('div', {'id': 'translations-content'})
a_tags = translations_div.find_all('a', {'class': 'translation'})
translated_words = [a.text.strip() for a in a_tags]

examples_section = soup.find('section', {'id': 'examples-content'})
example_spans = examples_section.find_all('span', {'class': 'text'})
example_texts = [span.text.strip() for span in example_spans]

print('Translations')
print(translated_words)
print(example_texts)

