from bs4 import BeautifulSoup
import requests
import sys


languages = ["arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
             "dutch", "polish", "portuguese", "romanian", "russian", "turkish"]

args = sys.argv

i_lang = args[1]
output_language = args[2]
text = args[3]
o_lang = []
code = ""

user_agent = 'Mozilla/5.0'
out_file = text + ".txt"

if output_language != "all":
    o_lang.append(output_language)
elif output_language == "all":
    o_lang = languages
    o_lang.remove(i_lang)

if output_language != "all" and output_language not in languages:
    print("Sorry, the program doesn't support " + output_language)

if output_language != "all":
    url = 'https://context.reverso.net/translation/' + i_lang + "-" + output_language + "/" + text
    site = requests.get(url, headers={'User-Agent': user_agent})
    code = site.status_code
elif output_language == "all":
    url = 'https://context.reverso.net/translation/' + i_lang + "-" + o_lang[0] + "/" + text
    site = requests.get(url, headers={'User-Agent': user_agent})
    code = site.status_code


if code != 200 and code != 404:
    print("Something wrong with your internet connection")
elif code == 404:
    print("Sorry, unable to find " + text)
elif code == 200 and (output_language == "all" or output_language in languages):
    s = requests.Session()
    with open(out_file, 'w', encoding='utf-8') as out:
        for language in o_lang:
            url = 'https://context.reverso.net/translation/' + i_lang + "-" + language + "/" + text
            print(url)
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
