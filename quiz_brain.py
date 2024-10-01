class QuizBrain:
    def __init__(self,question_list):
        self.number = 0
        self.score = 0
        self.list = question_list

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        while True:
            try:
                user_answer = input(f"\n{self.number}: {current_question.text} (True/False): ").lower()
                if user_answer[:1] == "t":
                    user_answer = "true"
                    break
                elif user_answer[:1] == "f":
                    user_answer = "false"
                    break
            except:
                continue
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        length_of_list = len(self.list)
        return self.number < length_of_list
        
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong!")
        print(f"The answer was: {correct_answer}!\nCurrent score:{self.score}/{self.number}")

