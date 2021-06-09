class Student: 
    class_="student"
    def __init__(self, name, age, class_, score1, score2, score3):
        self.name = name 
        self.age = age 
        self.class_ = class_
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def calcAverage(self):
        return int(self.score1 + self.score2 + self.score3)/3

Fopé = Student("Fopé", "28", "Class O", 69.0, 76.0, 82.0)
Nakia = Student("Nakia", "26", "Class S", 74.0, 91.0, 88.0)


print(getattr(Fopé, "name") + ", " + getattr(Fopé, "age") + ", " + getattr(Fopé, "class_"))
print(Fopé.calcAverage())


print(getattr(Nakia, "name") + ", " + getattr(Nakia, "age") + ", " + getattr(Nakia, "class_"))
print(Nakia.calcAverage())
