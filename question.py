"""
question

quiz


"""

class Question:
    adress:"Soru"
    def __init__(self,question,answer,number,choose):
        self.question=question
        self.answer=answer
        self.number=number
        self.choose=choose
    def Soru(self):
        print(f"{self.question}")
        

class Quiz(Question):
    def __init__(self,number):
        self.number=number
        Question.__init__(self,question,answer,number,choose):
        



    
        
