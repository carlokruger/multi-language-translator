from bs4 import BeautifulSoup
import requests

print('''Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish''')

languages = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
             "dutch", "polish", "portuguese", "romanian", "russian", "turkish"]

input_language = int(input('Type the number of your language:')) - 1
output_language = int(input("Type the number of language you want to translate to:")) - 1
text = input('Type the word you want to translate:')

i_lang = languages[input_language]
o_lang = languages[output_language]

url = 'https://context.reverso.net/translation/' + i_lang + "-" + o_lang + "/" + text

user_agent = 'Mozilla/5.0'

site = requests.get(url, headers={'User-Agent': user_agent})

soup = BeautifulSoup(site.content, 'html.parser')

translations_div = soup.find('div', {'id': 'translations-content'})
a_tags = translations_div.find_all('a', {'class': 'translation'})
translated_words = [a.text.strip() for a in a_tags]

examples_section = soup.find('section', {'id': 'examples-content'})
example_spans = examples_section.find_all('span', {'class': 'text'})
example_texts = [span.text.strip() for span in example_spans]

print(o_lang.title(), "Translations:")
for word in translated_words:
    print(word)

print()

print(o_lang.title(), "Examples")
for index, phrase in enumerate(example_texts):
    if index % 2 == 0:
        print(phrase + ":")
    else:
        print(phrase + ":")
        print()
