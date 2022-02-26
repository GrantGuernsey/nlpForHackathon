#!/usr/bin/env python
# coding: utf-8

# In[86]:


from textblob.blob import BaseBlob
from textblob import TextBlob
import random


inputStatement = """This code seeks to find the nouns in a sentence. 
        The goal of this is to work with the story that is 
        being created in our hackathon project.""" #gotten from parsing the questions


blob = TextBlob(inputStatement)


nounList = ["air", "arm", "leg"] #put story list of words
nounListPlural = ["airs", "arms", "legs"]
properNounList = ["Grant", "Anjali", "Rohit", "Saumick"]


newblob = TextBlob("")
for word,noun in blob.tags:
    if noun in ['NN','NNS','PRP']: #finds nounage
        if noun in ['NN']:
            newblob += random.choice(nounList) + " "
        elif noun in ['PRP']:
            newblob += random.choice(properNounList) + " "
        else:
            newblob += random.choice(nounListPlural) + " "
    else:
        newblob += word + " "
#biggest issue is that it does not keep punctuation
#using blob, it ignores the puncation with all of
#its functions that i could find so im not sure


print(newblob)




