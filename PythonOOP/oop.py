class Dog:
     def __init__(self,nbLegs,eyeColor):
        self.nbLegs = nbLegs
        self.eyeColor = eyeColor
 
tomita = Dog(4,"brown")
#tomita.nbLegs = 4
#tomita.eyeColor = "brown"
 
##print(tomita.eyeColor)
print("This dog has",tomita.nbLegs,"legs and",tomita.eyeColor,"eyes.")