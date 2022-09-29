#!pip install wordcloud


import wordcloud
import numpy as np
from matplotlib import pyplot as plt


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","in","for", "on"]

    # LEARNER CODE START HERE
    word_frequency = {}
    new_filecontent = file_contents.split()

    for words in new_filecontent:
        word = words.strip(punctuations)
        lword = word.lower()

        if lword.isalpha() == True and lword not in uninteresting_words:
            if lword not in word_frequency:
                word_frequency[lword]=0
        else:
            continue

        word_frequency[lword] += 1

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequency)
    return cloud.to_array()

#Opening a file 

file_contents = open("wordcloud_words_file.txt").read()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
