class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        """
        Function to print next question and take input answer from user
        """
        current_question = self.q_list[self.q_number]
        self.q_number +=1
        user_answer = input(f"Q.{self.q_number }) : {current_question.q_text} (True/False)")
        self.check_answer(user_answer, current_question.q_ans)

    def still_has_questions(self):
        """
        Function to if there are questions remaining in the list.
        return: Boolean (True if remaining otherwise false.
        """
        return self.q_number < len(self.q_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("Hooray!!! You got it right.")
            self.score += 1
        else:
            print(f"Ooopsie!!! You got it wrong.\nCorrect answer is {c_answer}")
        print(f"Your current score is : {self.score}/{self.q_number}")
