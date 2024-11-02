import os
from openai import OpenAI
from dotenv import load_dotenv
import functions


default_path = functions.get_default()

def phoneticGenerator(word):
    #Loads and sets OpenAI API Key
    load_dotenv()
    api_key = os.getenv('OPENAI_KEY')

    client = OpenAI(api_key=api_key)

    #Phonetic Word
    phonetic_word = word

    #Sets settings for OpenAI, we are using gpt-4o-mini, with a temp of 1.0
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
        {"role": "system", "content": '''
         You will generate every possible word that could be phonetically similar with similar starting sounds to each word
         in the user input, for each word you generate separate each element by a comma do not write any additional  
         information other than possible words separated by a comma and an exclamation point '!' at the end of groupings.
         MOST IMPORTANT STEP:
         MAKE SURE AFTER EACH GROUP OF WORDS TO ADD AN EXCLAMATION POINT '!'
         '''},
        {"role": "user", "content": f"Words you're generating: {phonetic_word}"}
    ],
    temperature = 0.1
    )

    #Saves ChatGPTs response to a variable
    AIresponse = completion.choices[0].message.content
    return AIresponse


word_mapping = {
                1 : "Do",
                2 : "Re",
                3 : "Mi",
                4 : "Far",
                5 : "So",
                6 : "La",
                7 : "Ti"
                }

def establish_words():
    words = ""
    for word in word_mapping:
        words += word_mapping.get(word) + " "
    print(words)
    output = phoneticGenerator(words)
    with open(f"{default_path}/TalkTuah/words.txt", "w") as text_file:
        text_file.write(output)

establish_words()