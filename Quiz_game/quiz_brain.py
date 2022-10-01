from question_model import Question


class Quiz:
    def __init__(self, questionslist):
        self.score = 0
        self.questionnumber = 0
        self.quelist = questionslist

    def sufficeintQns(self):
        if self.questionnumber < len(self.quelist):
            return True
        else:
            return False

    def nextQn(self):
        current = self.quelist[self.questionnumber]
        self.questionnumber = self.questionnumber + 1
        userans = input(f"Q.{self.questionnumber} {current.qn} true/ false? : ")

        if userans.lower() == current.an.lower():
            self.score += 1
        else:
            print(f"the correct answer is {current.an}")
        print(f"Your score is {self.score}/ {len(self.quelist)}")
        print("\n")
