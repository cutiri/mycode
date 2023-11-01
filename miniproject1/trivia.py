import random, starcraft, question

questions = starcraft.trivia_pool()
#rightanswers = 0
correctanswers = 0
totalanswers = 0
totalquestions = len(questions)

def final_results():
    percent = correctanswers / totalquestions * 100
    final_comment = "Good job!!!" if (percent > 80) else "Try harder Dummy!!!"
    print("-----------------------------------------------------------------------")
    print("Congratulations, you completed the trivia.")
    print("Correct answers:", correctanswers, ", out of", totalquestions)
    print("Your success rate was: ", percent, "%. ", final_comment)
    print("Bye!")
    print("-----------------------------------------------------------------------")

def print_question(question):
    print("-----------------------------------------------------------------------")
    print(question.question)
    count = 1
    for option in question.options:
        print(count, ": ", option)
        count += 1
    print("-----------------------------------------------------------------------")

def main():
    global correctanswers
    global totalanswers
    global totalquestions
    print("Welcome to Trivia")

    while True:
        print("Questions left: ", len(questions))
        print("Right answers: ", correctanswers)
        question_number = random.randint(0, len(questions) - 1)
        question = questions[question_number]

        while True:
            print_question(question)

            try:
                user_input = int(input("Enter your answer: "))
                if not user_input in range(1, len(question.options) + 1):
                    raise Exception()
                if int(user_input) - 1 in question.right:
                    print("Right answer!")
                    correctanswers += 1
                else:
                    print("Wrong, you silly goose!")

                totalanswers += 1
                break
            except Exception as e:
                print("I see you can't follow instructions, try again.")


        del questions[question_number]
        if len(questions) == 0:
            final_results()
            break


if __name__ == "__main__":
    main()
