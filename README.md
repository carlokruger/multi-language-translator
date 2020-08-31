# Multi Language Translator

## Stage 1: Repeater
### Description
Your very first step is writing a program that begins with an invitation message for choosing the translation direction. It then takes the input from your keyboard as an argument and repeats the same process for the word you want to translate.

Here's what you’re going to do:

  * Add the ability to choose the translation direction between two languages (for instance, English and French)
  * Type the word you want to translate

First, you will get a call from the program to choose the mode. Next, you should be asked to enter the word you want to translate. After that, the program should output the information it gathered.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:

```fr```

Type the word you want to translate:

```hello```

You chose "fr" as the language to translate "hello" to.

We don't really need this output to appear at the end. However, aside from keeping the user informed, it does something else: it's showing us if the arguments were successfully accepted by the function. Keep it in mind while proceeding from stage to stage!

## Stage 2: Over the internet
### Description
Here you will connect your app to an online web service to get the translation data from it. To establish the connection, you have to form the request, send it to the web site, and check the HTTP status of the response. If your status code is 200, then you are good to proceed!

### Create the request
Now, go to ReversoContext and type any word you want to translate. After receiving the result, pay attention to the address bar of your browser. You will see the URL, for example:

[https://context.reverso.net/translation/english-french/cheese](https://context.reverso.net/translation/english-french/cheese)

Here you see the language-translation pair «english-french», which represents the direction of translation, meaning that the translation is from English to French and not the other way around. After the last backslash, you can see the word being translated.

Your goal is to make your program act as if it visits the website for you. To make it happen, tell your program to generate the correct URL with the word you type, determine the translation direction as you chose it at the previous stage, and send the URL to the website using the requests package.

Not familiar with requests? Watch a video tutorial!

So, your last output after the first stage will be:

> 200 OK

This means the program was able to successfully connect to the web site and get the web page for you.

200 is an HTTP status code that comes as a response to the program.

### What is HTTP?
HTTP is a protocol that allows computers to communicate over the web. When you're surfing the web, googling something, or visiting your favorite website, your browser actually does it through the HTTP.

As a protocol, HTTP contains different methods to establish a connection with the websites. For example, one of these methods is Get. It's used to get the actual representation of the data from the remote server so that you see what you usually see in your web browser. There are many more helpful HTTP methods: it might be a good idea to [get familiar](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) with them! Another thing to keep in mind is that each method is used to get a specific response or make a specific task.

Now, knowing all that, let's talk a little about how a request is formed on the web.

You can form the HTTP request with Python's module [requests](https://requests.readthedocs.io/en/master/user/quickstart/77777). Any HTTP request contains a similar set of data. This includes the method, the address and might also require the headers. As the methods and the address were already discussed above, let's deal with the headers.

Headers are the text data you send over HTTP which might contain information about a web browser or application you use to surf the web. Your program doesn't use any web browser as we usually do, but it still has to be some kind of a browser itself to be able to get the web pages. For this purpose, there's a 'User-Agent' field that forms a request.

Think of it as a visit card that your program shows to the web site before it can enter it. It then introduces itself as a web browser to the web site it's trying to get a page from; otherwise, the web site might not allow the connection from something other than a browser. You may find the headers and read more about them on [MDN](https://developer.mozilla.org/ru/docs/Web/HTTP/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B8/User-Agent).

As a result, you will have a request form of method+address+headers.

Select text data
Your program already knows how to send a request. What it still doesn’t know is how to handle incoming data to get the translation examples. This is possible with the BeautifulSoup package.

If you're not familiar with Beautiful Soup, check out a [video](https://youtu.be/87Gx3U0BDlo) on the subject.

Have you already tried ReversoContext? It gives you two types of text data:

Single translated words
Sentences with usage examples

![Reverso page](https://paper-attachments.dropbox.com/s_91860D8CA78B45DEE66EF32279A68E06A5423FF9541F0C8DB4A5138915C378CC_1574232106854_2019-11-20_11-41.png)

Even though both are string data, it makes sense to keep them separated in the code, since there’s a nature of individual objects in the idea behind them.

The main question is how to get these exact data from the web page without everything else. The answer is CSS. You can access this text via CSS classes and tags. All you need is to go to the [web page](https://context.reverso.net/translation/english-spanish/hello), open your browser’s Dev Tools and find these elements in CSS code. You can get access to your browser’s DevTools in three different ways:

Keyboard: Ctrl + Shift + I, except

Internet Explorer and Edge: F12

macOS: ⌘ + ⌥ + I

Menu bar:

Firefox: Menu ➤ Web Developer ➤ Toggle Tools, or Tools ➤ Web Developer ➤ Toggle Tools

Chrome: More tools ➤ Developer tools

Safari: Develop ➤ Show Web Inspector. If you can't see the Develop menu, go to Safari ➤ Preferences ➤ Advanced, and check the Show Develop menu in menu bar checkbox.

Opera: Developer ➤ Developer tools

Context menu: Press-and-hold/right-click an item on a webpage (Ctrl-click on the Mac), and choose Inspect Element from the context menu that appears. (An added bonus: this method highlights the code of the element you right-clicked.)

After you’re done with CSS, check it.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
```fr```
Type the word you want to translate:
```hello```
You chose "fr" as a language to translate "hello".
200 OK
['bonjour', 'allô', 'ohé', 'coucou', 'salut', 'hello', 'bonsoir', "quelqu'un", 'bien le bonjour', 'Oh', 'Enchanté', 'saluer', 'ça', 'salue', 'Oui']
['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.', 'Goodbye England and hello the Netherlands...', "Au revoir l'Angleterre et bonjour les Pays-Bas...", 'Yes, hello. Jackson speaking.', "Oui, allô, Jackson à l'appareil.", 'Hello, hello, hello, hello.', 'Allô, allô, allô, allô.', 'And began appearing hello kitty games online.', 'Et a commencé à apparaître bonjour Kitty jeux en ligne.', 'Tell him hello... and congratulations.', 'Je lui dis bonjour et je le félicite.', 'A special hello to everyone from YouTube Bibi.', 'Un bonjour spécial à tout le monde de la chaîne de beauté YouTube de bibi.', 'Yes, hello, Mr Teodoresco.', 'Oui, bonjour, M. Teodoresco.', 'Well hello, Milan and Eve.', 'Eh bien bonjour, Milan et Eve.', 'Well hello, welcome to the Tree House pond.', "Alors bonjour, bienvenue à l'étang de la Maison de l'arbre.", 'pink hello kitty seat 2,3 - Auto Outlet', 'rose bonjour 2,3 siège de minou - Auto Outlet', 'hello world PL/SQL procedure successfully completed. SQL', 'bonjour procédure monde PL / SQL terminée avec succès. SQL', '"Maido-san" means something like "hello" in Kanazawa dialect.', 'Maido-sans veut dire quelque chose comme bonjour dans le dialecte de Kanazawa.', 'So anyway, hello and goodbye.', 'Donc voilà, bonjour et au revoir.', 'You can hardly hear him saying hello.', "On l'entend à peine dire bonjour.", "Yes, hello. I'd like to blackmail the Prime Minister.", "Oui, bonjour, j'aimerais faire chanter le premier Ministre.", 'Well, please tell her hello for us.', 'Bien, dites lui bonjour de notre part.', 'Homie, I think someone is saying hello.', "Homer, je crois qu'on te dit bonjour.", 'Well, hello, Susan and welcome.', 'Bien, bonjour Susan et bienvenue.', 'Normally, one says "hello" only once.', 'Normalement, on dit bonjour une fois.']

Here you can see the results that are almost readable, but there’s a lot of quotes and commas. They came from the web page you received with requests. The next stage is all about the presentation!

## Stage 3/7: Translations
### Description
To get readable results, you need to format all the data you get from the web. Good thing that Python is a rich programming language with a powerful text formatting out of the box!

Use Python’s built-in text formatting to:

  * Remove all the quotation marks and commas
  * Place each word and example sentence in a new line
  * You might also want to cut the results to 5 words and 5 example sentences to keep it compact

### Example

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:

```fr```

Type the word you want to translate:

```hello```

You chose "fr" as a language to translate "hello".

200 OK

Context examples:

French Translations:

bonjour

allô

ohé

coucou

salut

French Examples:

Well, hello, freedom fighters.:

Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...:

Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.:

Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.:

Allô, allô, allô, allô.

And began appearing hello kitty games online.:

Et a commencé à apparaître bonjour Kitty jeux en ligne.

## Stage 4/7: All of them
### Description
Good! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will add the ability to translate from/to any language in the list.

The maximum number of languages our translator can support is 13. They are:

Arabic
German
English
Spanish
French
Hebrew
Japanese
Dutch
Polish
Portuguese
Romanian
Russian
Turkish
They should be enumerated in the program. A great idea is to present them with relevant numbers, so that the user can choose the first as the original language and the second as a translation.

Tip: just place the listed languages into the URL depending on the user’s choice!

Tip-2: Try to convert the input to lower case: it may cause an error if the user's input is in upper case or mixed. You can do it with Python's built-in functionality.

### Example
```Hello, you're welcome to the translator. Translator supports: 
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
13. Turkish
Type the number of your language: 
> 3
Type the number of language you want to translate to: 
> 4
Type the word you want to translate:
> hello

Spanish Translations:
hola
buenos días
qué tal
saludo
buen día

Spanish Examples:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.

He didn't introduce us, so hello.:
No nos presentó, así que hola.

Well, hello, Prince Charming.:
Vaya, hola, Príncipe Azul.

In addition, fast delivery. hello Laura.:
Además, la entrega rápida. hola Laura.

L: Well, hello, my dear secretary.:
A: Bien, hola, mi querida secretaria.
```

## Stage 5/7: Simultaneous translation
## Description
You’ve done a great job! There is just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better.

This stage is meant to teach you how to work with files.

First, you’re going to add another cool feature to the project. Think how great it would be if you could translate to all the languages at once and save it for later!

Here's what you’ll do:

  * Add the ability to translate to all languages at once
  * Save results to the file on your computer
To make the first feature possible, there’s a way to expand the existing language list with zero, which will mean the translation to all languages listed below.

Since you will get a long output with all these translations coming one after another, it’s better to save it to the file on your computer so that you can read it later. You can name this file as the word in the input.

### Example
```
Hello, welcome to the translator. Translator supports: 
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
13. Turkish
Type the number of your language:
> 3
Type the number of a language you want to translate to or '0' to translate to all languages:
> 0
Type the word you want to translate:
> hello
This will result in a file called «hello.txt» with the following content:

Arabic Translations:
مرحبا

Arabic Example:
Well, hello, old-school racist.:
حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!


German Translations:
hallo

German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.


Spanish Translations:
hola

Spanish Example:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.


French Translations:
bonjour

French Example:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.


Hebrew Translations:
שלום

Hebrew Example:
Is "hello" too bland?:
האם "שלום" יותר מדי מנומס?


Japanese Translations:
こんにちは

Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。


Dutch Translations:
dag

Dutch Example:
That was kind of our funny hello.:
Dat vond we een grappige begroeting.


Polish Translations:
cześć

Polish Example:
I guess it's... goodbye car insurance, hello city bus.:
I domyślam się, że to jest... do widzenia ubezpieczenie samochodu, cześć autobus miejski.


Portuguese Translations:
olá

Portuguese Example:
That was my last kiss hello.:
Pois eu garanto que aquele foi o meu último beijo de olá.


Romanian Translations:
salut

Romanian Example:
Well, hello, professor Culbertson.:
Ei bine, salut, profesor universitar Culbertson.


Russian Translations:
привет

Russian Example:
Why, hello, there, Admiral.:
А, Адмирал, привет, что здесь делаешь.


Turkish Translations:
selam

Turkish Example:
So now little Sabina says hello.:
Velhasıl minik Sabina size selam söylüyor.
```

## Stage 6/7: Faster translation
### Description
There’s a faster way to translate a word without being asked by the program every time. To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.

At this stage, you should add command-line argument handling in your code. This is possible via Python sys package.

You'll see some significant changes in the usability of the app!

### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

### Example 1

```python translator.py english french hello
French Translations:
bonjour
allô
ohé
coucou
salut

French Examples:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...:
Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.:
Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.:
Allô, allô, allô, allô.

And began appearing hello kitty games online.:
Et a commencé à apparaître bonjour Kitty jeux en ligne.
```
### Example 2

Don’t forget to take a zero-argument, which means translating to all languages in the list and saving the output to a file.

```python translator.py english all hello```

## Stage 7/7: Unexpected
### Description
Okay, it seems like your program translates as expected. However, there’s a problem you should always keep in mind: something can break your program.

Up to this stage, you were thinking about things that should be in your code. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? That can break your program.

All these situations are called exceptions because you didn’t expect them to happen, and now you have to handle them.

### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

#### Example 1

Notify users that they cannot translate to or from some languages.

```python translator.py english korean hello
Sorry, the program doesn't support korean
```
#### Example 2

Check and notify if there’s a problem with the user’s internet connection.

```python translator.py english all hello
Something wrong with your internet connection
```
#### Example 3

Tell the user that you can’t translate jabberwocky.

```python translator.py english all brrrrrrrrrrr
Sorry, unable to find brrrrrrrrrrr
```
