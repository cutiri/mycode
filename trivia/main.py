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
        pprint.pprint('Select the correct answer:')
        correct_answer_position = random.randint(0, len(question.get("incorrect_answers")))
        answers = question.get("incorrect_answers")
        answers.insert(correct_answer_position, question.get("correct_answer"))
        count = 1
        for answer in answers:
            pprint.pprint(str(count) + ": " + html.unescape(answer))
            count += 1
    elif question.get("type") == 'boolean':     
        pprint.pprint('Answer T or F:')
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