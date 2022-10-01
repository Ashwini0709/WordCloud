# WordCloud

## Project goal

The goal of the project is to create a “word cloud” from a text by writing a program. This program needs to process the text, remove punctuation, count the frequencies, and ignore uninteresting or irrelevant words.

The program go through the text, clean up the text to remove any punctuation marks [1], count how many times each word appears using a dictionary and use that as a parameter for the word cloud module..

For that, we create a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the `WordCloud` class.

Then the following code generate the word cloud image:

```
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
```

Before storing words in the frequency dictionary, the program also checks and exclude irrelevant or uninteresting words when processing the text by removing certain words in our language that crop up a lot which prevents a pretty dull word cloud. Words like *a*, *the*, *to*, *two* or *if* usually appear a whole lot in text but aren't too relevant to the text's overall message. Hence the Cloud show words that are relevant to the text we're using for the input.

To split a line of text into words, the program uses the `split()` method.

### Input file

For the input, we're going to use a text file only. Choose any text file you like for your input. The text itself could be the contents of a website, a full novel or even everything that one author has ever written. You can copy and paste the contents of a website you like or you can use a site like <a href=https://www.gutenberg.org/>Project Gutenberg</a> to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen..
You just need to make sure that it's one text file, so that it can be processed by the code..

<hr>

[1]   To do this, the program go through each line of text, character-by-character, using the `isalpha()` method. This will check whether or not the character is a letter.

