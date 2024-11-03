import os
from openai import OpenAI
from dotenv import load_dotenv
import functions
import time
import re

azureReader = functions.SpeechToTextManager()
default_path = functions.get_default()
accuracy_map = {}

sample_script = {
                1 : "The mighty lion prowls with a regal, golden mane.",
                2 : "The sly little fox is quick on his feet.",
                3 :  "The gentle panda munches on bamboo all day,",
                4 : "The tall giraffe stretches high to the trees.",
                5 : "The playful, little monkey swings from vine to vine.",
                }

word_mapping = {
                1 : "Mane",
                2 : "Feet",
                3 : "Day",
                4 : "Trees",
                5 : "Vine",
                }

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


if __name__ == __main__:
    sample_list = save_words()
    for index in word_mapping:
            accuracy_map[word_mapping.get(index)] = 0
    temp = len(sample_list)
    script_run(1, temp)
    print(accuracy_map)


