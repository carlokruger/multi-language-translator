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
output_language = int(input("Type the number of language you want to translate to:"))
text = input('Type the word you want to translate:')

i_lang = languages[input_language]

if 1 <= output_language <= 13:
    o_lang = languages[output_language]
elif output_language == 0:
    o_lang = languages
    del o_lang[input_language]

user_agent = 'Mozilla/5.0'
out_file = text + ".txt"

s = requests.Session()
with open(out_file, 'w', encoding='utf-8') as out:
    for language in o_lang:
        url = 'https://context.reverso.net/translation/' + i_lang + "-" + language + "/" + text
        site = s.get(url, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(site.content, 'html.parser')

        translations_div = soup.find('div', {'id': 'translations-content'})
        a_tags = translations_div.find_all('a', {'class': 'translation'})
        translated_words = [a.text.strip() for a in a_tags]

        examples_section = soup.find('section', {'id': 'examples-content'})
        example_spans = examples_section.find_all('span', {'class': 'text'})
        example_texts = [span.text.strip() for span in example_spans]

        word_title = language.title() + " Translations:"

        print(word_title)
        out.write(word_title)
        out.write("\n")

        for word in translated_words:
            print(word)
            out.write(word + "\n")

        print()
        out.write("\n")

        phrase_title = language.title() + " Examples:"

        print(phrase_title)
        out.write(phrase_title)
        out.write("\n")
        for index, phrase in enumerate(example_texts):
            out_phrase = phrase + ":"
            if index % 2 == 0:
                print(out_phrase)
                out.write(out_phrase + "\n")
            else:
                print(out_phrase)
                print()
                out.write(out_phrase + "\n")
                out.write("\n")
