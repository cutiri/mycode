#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html
import pprint
import random

categories= {
9:  "General Knowledge", 
10: "Entertainment- Books", 
11: "Entertainment- Film", 
12: "Entertainment- Music", 
13: "Entertainment- Musicals & Theater", 
14: "Entertainment- Television", 
15: "Entertainment- Video Games", 
16: "Entertainment- Board Games", 
17: "Science- Nature", 
18: "Science- Computers", 
19: "Science- Mathematics", 
20: "Mythology", 
21: "Sports", 
22: "Geography", 
23: "History", 
24: "Politics", 
25: "Art", 
26: "Celebrities", 
27: "Animals", 
28: "Vehicles", 
29: "Entertainment- Comics", 
30: "Science- Gadgets", 
31: "Entertainment- - Japanese Anime & Manga", 
32: "Entertainment- - Cartoon Animations"
}

URL= "https://opentdb.com/api.php?amount=10&category="

def display_question(question):
    pprint.pprint(html.unescape(question.get('question')))
    if question.get("type") == 'multiple':
        correct_answer_position = random.randint(0, len(question.get("incorrect_answers")))
        answers = question.get("incorrect_answers")
        answers.insert(correct_answer_position, question.get("correct_answer"))
        count = 1
        for answer in answers:
            pprint.pprint(str(count) + ": " + html.unescape(answer))
            count += 1
        answer = int(input('Select the correct answer:'))
        if answers[answer - 1] == question.get('correct_answer'):
            print("The answer is correct!!!")
        else:
            print("The answer is incorrect.", "Correct answer is: ", question.get('correct_answer'))
    elif question.get("type") == 'boolean':     
        response = input('Answer T or F:').upper()
        if (response == 'F' and question.get('correct_answer') == 'False') or (response == 'T' and question.get('correct_answer') == 'True'):
            print("The answer is correct!!!")
        else:
            print("The answer is incorrect.")
        #pprint.pprint(html.unescape(question.get('question')))

def main():
    pprint.pprint(categories)
    category = input("Select a category: ")
    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL + category).json()

    results = data.get('results')
    for question in results:
        display_question(question)
        print('-------------------------------------------------------------------------------------------')


if __name__ == "__main__":
    main()