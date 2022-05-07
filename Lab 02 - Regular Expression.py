#!/usr/bin/env python
# coding: utf-8

# # Regular Expression (RegEx)

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# 
# RegEx can be used to check if a string contains the specified search pattern.

# In[1]:


import re
import nltk

word = 'supercalifragilisticexpialidocious'  # to use the text data file in .txt

print(re.findall(r'[aeiou]', word))
print(len(re.findall(r'[aeiou]', word)))



# Search
str = 'word:cyt!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
print(match) 
if match:
  print('found') ## 'found word:cat'
else:
  print('did not find')

# Example
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[abc]{2,}', word))
print(fd.most_common(5)) # the highest frequency in the descending order
print()
print(fd.items()) # print the entire list 


# In[2]:


import re
import nltk

word = 'supercalifragilisticexpialidocious'
regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'

def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

english_udhr = nltk.corpus.udhr.words('English-Latin1')
print(nltk.tokenwrap(compress(w) for w in english_udhr[:75]))


# In[3]:


import urllib.request

url = "http://www.gutenberg.org/ebooks/2554?msg=welcome_stranger"

with urllib.request.urlopen(url) as f:
    print(f.read(300).decode('utf-8'))


# In[4]:


import nltk, re

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')

cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)

print(cfd.tabulate())


# In[5]:


import nltk, re

rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')

cv_word_pairs = [(cv, w) for w in rotokas_words
                 for cv in re.findall(r'[ptksvr][aeiou]', w)]

cv_index = nltk.Index(cv_word_pairs)

print(cv_index['su'])
print(cv_index['po'])


# ### Stemming
# 
# Importance of Stemming in Text Analytics
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stemming is used in information retrieval systems like search engines.
# It is used to determine domain vocabularies in domain analysis.
# 
# **Stemming is the process of reducing inflected words to their word stem, base or root form.**

# ![stemming.jpg](attachment:stemming.jpg)

# In[10]:


import re
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
print(stem('usually'))
print()

print(re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))

print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))

print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|ment)$', 'studies'))


# In[6]:


inputWord = input("\nEnter the word for stemming: ")
print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', inputWord))


# #### Using RegexpStemmer from NLTK

# In[2]:


from nltk.stem import RegexpStemmer
st = RegexpStemmer('ing$|s$|e$|able$|ies$')
print(st.stem('studies'))


# In[7]:


import re #Python2
from nltk.tokenize import sent_tokenize, word_tokenize

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

sampleText = """You probably worked out that a backslash means that
            the following character is deprived of its special powers
            and must literally match a specific character in the word.
            Thus, while . is special, \. only matches a period. The
            braced expressions, like {3,5}, specify the number of repeats
            of the previous item. The pipe character indicates a choice
            between the material on its left or its right. Parentheses
            indicate the scope of an operator: they can be used together
            with the pipe (or disjunction) symbol like this: «w(i|e|ai|oo)t»,
            matching wit, wet, wait, and woot. It is instructive to see what
            happens when you omit the parentheses from the last expression
            above."""

tokens = word_tokenize(sampleText)
print([stem(t) for t in tokens])


# In[8]:


import re #Python3
import nltk

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

sampleText = """You probably worked out that a backslash means that
            the following character is deprived of its special powers
            and must literally match a specific character in the word.
            Thus, while . is special, \. only matches a period. The
            braced expressions, like {3,5}, specify the number of repeats
            of the previous item. The pipe character indicates a choice
            between the material on its left or its right. Parentheses
            indicate the scope of an operator: they can be used together
            with the pipe (or disjunction) symbol like this: «w(i|e|ai|oo)t»,
            matching wit, wet, wait, and woot. It is instructive to see what
            happens when you omit the parentheses from the last expression
            above."""

tokens = nltk.tokenize.word_tokenize(sampleText)

print([stem(t) for t in tokens])


# ### Using Regular Expression package to perform split

# Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.

# https://docs.python.org/3/library/re.html

# In[2]:


import re
text = "I am a human"
tokens = re.split(' ', text)
print(tokens)


# An example of split by consecutive numbers is as follows.
s_nums = 'one1two22three333four4444five'
print(re.split('\d+', s_nums))

print(re.split('\d+', s_nums, 2))

s_marks = 'one-two+three#four$five@six'
print(re.split('[-+#$@]', s_marks))


# ### Using Python String split()  method to perform split

# The split() method splits a string into a list.
# 
# You can specify the separator, default separator is any whitespace.
# 
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

# Syntax:
# 
# string.split(separator, maxsplit)

# separator --> Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# 
# maxsplit --> Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# #### Example 1: Split the string, using comma, followed by a space, as a separator:

# In[8]:


txt = "hello, my name is Peter, I am 26 years old"
# sent tokenization
x = txt.split(",")
print(x)
# word tokenization
y = txt.split(" ")
print(y)


# #### Example 2: Use a hash character as a separator:

# In[11]:


txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)


# #### Example 3: Split the string into a list with max 2 items:

# In[12]:


txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)


# # Porter Stemmer

# ### In linguistic morphology and information retrieval, stemming is the process of reducing inflected words to their word stem, base or root form—generally a written word form

# In[13]:


import nltk

Text = input("Enter the text corpus for stemming: ")
# Split using split()
word = Text.lower().split(' ')
print(word)

porter = nltk.PorterStemmer()
for t in word:
    print(porter.stem(t))


# In[14]:


import nltk

Text = input("Enter the text corpus for stemming: ")
# Split using 
word = nltk.tokenize.word_tokenize(Text)
print(word)

porter = nltk.PorterStemmer()
for t in word:
    print(porter.stem(t))

