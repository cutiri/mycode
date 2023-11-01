import random, starcraft, question

questions = starcraft.trivia_pool()

right_answers = 0
total_answers = 0
total_questions = len(questions)


print("Welcome to Trivia")


while True:
    print("Questions left: ", len(questions))
    print("Right answers: ", right_answers)
    question_number = random.randint(0, len(questions) - 1)
    question = questions[question_number]

    while True:
        print(question.question)

        count = 1
        for option in question.options:
            print(count, ": ", option)
            count += 1

        user_input = input("Enter your answer: ")

        if int(user_input) - 1 in question.right:
            print("Right answer!")
            right_answers += 1
        else:
            print("Wrong, you silly goose!")

        total_answers += 1
        break


    del questions[question_number]
    if len(questions) == 0:
        print("Congratulations, you completed the trivia.")
        print("Total number of right answers: ", right_answers, ", of a total of: ", total_questions, ". For a success rate of: ", right_answers / total_questions * 100, "%")
        print("Bye!")
        break