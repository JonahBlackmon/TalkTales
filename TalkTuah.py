import os
from openai import OpenAI
from dotenv import load_dotenv
import functions
import time
import re

azureReader = functions.SpeechToTextManager()

sample_script = {
                1 : "Doe, a deer, a female deer,",
                2 : "Ray, a drop of golden sun,",
                3 :  "Me, a name, I call myself,",
                4 : "Far, a long long way to run,",
                5 : "So, a needle pulling thread,",
                6 : "Lah a note to follow so,",
                7 : "Tea, a drink with jam and bread,",
                8 : "That will bring us back to Doe"
                }

word_mapping = {
                1 : "Do",
                2 : "Re",
                3 : "Mi",
                4 : "Fa",
                5 : "So",
                6 : "La",
                7 : "Ti"
                }

def get_word_map():
     return word_mapping



def save_new():
    sample_list = {}
    index = 1
    with open("words.txt", "r", encoding="utf-8") as text_file:
            output = ""
            print("Here")
            print(text_file.readlines())
            text = text_file.readlines()
            for line in text:
                 output = line
                 output = output[:-1]
                 words = output.split(", ")
                 words_list = words
                 sample_list[index] = words_list
                 index = index + 1
    

    # print(sample_list)
    return sample_list

default_path = functions.get_default()

def save_words():
     sample_list = {}
     index = 1
     with open(f"{default_path}/TalkTuah/words.txt", "r") as text_file:
          text = text_file.readlines()
          for line in text:
               output = line
               output = output[:output.index('!')]
               words = output.split(", ")
               words_list = words
               sample_list[index] = words_list
               index = index + 1
     return sample_list

sample_list = save_words()
print(sample_list)

def child_check(index) :
    child_input = azureReader.speechtotext_from_mic()
    cleaned_text = re.sub(r'[^\w\s]', '', child_input)
    segmented_input = cleaned_text.split()
    print(child_input) # For testing purposes
    for word in segmented_input:
        print(sample_list.get(index))
        for temp in sample_list.get(index):
            if word.lower() == temp.lower():
                return True
    return False

accuracy_map = {}
for index in word_mapping:
        accuracy_map[word_mapping.get(index)] = 0
        
def script_run(index, size):
    while (index <= size) :
        print(index)
        print(sample_script.get(index))
        if (child_check(index)) :
            print("Well Done!")
            index = index + 1
            
        else:
            print("Maybe try again?")
            accuracy_map[word_mapping.get(index)] = accuracy_map.get(word_mapping.get(index)) + 1
            script_run(index, size)
            break
        if (index > size) :
            break

temp = len(sample_list)
script_run(1, temp)
print(accuracy_map)




