#This class represents a trivia question with the options and right answer(s)
#question: The question itself, just a string
#options: List of string with the possible options
#right: List of integers representing the positions in options that are right answers


class Question:
    def __init__(self, question, options, right) -> None:
        self.question = question
        self.options = options
        self.right = right        

