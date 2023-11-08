#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html
import pprint
import random

URL= "https://opentdb.com/api.php?amount=10&category=15"

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
    # data will be a python dictionary rendered from your API link's JSON!
    data = requests.get(URL).json()

    results = data.get('results')
    for question in results:
        display_question(question)
        print('-------------------------------------------------------------------------------------------')


if __name__ == "__main__":
    main()