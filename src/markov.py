
# coding: utf-8

# In[130]:

import random
import re

class markov(object):

    '''
    A class that takes in a file and returns a sentence 
    of a specified size generated using a Markov Chain
        markov contains 4 functions:
            words_from_file,
            triples,
            model,
            text_generator
    '''
    
    def __init__(self, file):
        #Empty dictionary to store word occurances
        self.collection = {}
        self.file = open(file)
        self.words = self.words_from_file()
        self.model()

        
    def words_from_file(self):
        
        '''
        Reads in a file, transforms all words to lowercase,
        removes all characters that are not a space or apostrophe,
        and splits all the words individually into a list
            Output: words, a list of words read from the file
        '''
        
        #Set the cursor to the beginning of the text
        self.file.seek(0)
        text = self.file.read().lower()
        text = re.sub(r'([^\s\w]|_)+', '', text).replace('\n', " ")
        words = text.split()
        return words
    
    def triples(self):
        
        '''
        Creates 'triples' of every single combination of 3
        consecutive words from the text
            Output: triple_word, a list of 3 consecutive words
        '''
        
        #Can't generate if text length is less than 3
        if len(self.words) < 3:
            return
        
        #Create triples lists
        for i in range(len(self.words) - 2):
            triple_word = (self.words[i], self.words[i+1], self.words[i+2])
            yield triple_word

    def model(self):
        
        '''
        Takes in generated triples and stores the first two
        words as keys and the third word as their value
        '''
        
        #Set the key as the first 2 words
        for triple_word in self.triples():
            key = (triple_word[0], triple_word[1])
            
            #Append the third word if key already exists in the collection
            if key in self.collection:
                self.collection[key].append(triple_word[2])
            #Set key and assign value if key does not already exist in the collection
            else:
                self.collection[key] = [triple_word[2]]

    def text_generator(self, size = 30):
        
        '''
        Selects 2 consecutive words at random and
        then uses the collection hash table to choose
        the next word. Repeats until desired text length
        is reached
            Input: size, an integer specifying preferred
                   text size (defaults to size = 30)
            Output: A randomly generated string
        '''
        
        #Select the first 2 consecutive words at random
        index = random.randint(0, len(self.words) - 1)
        first_word = self.words[index]
        next_word = self.words[index + 1]
        sentence = []
        #For the specified size
        for i in range(size - 1):
            #Append the first word to the sentence
            sentence.append(first_word)
            #Reassign both words based on collection dictionary
            first_word, next_word = next_word, random.choice(self.collection[(first_word, next_word)])
        sentence.append(next_word)
        #Join the list to form a sentence
        return ' '.join(sentence)

