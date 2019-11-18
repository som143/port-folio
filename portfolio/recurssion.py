class student:
    name = "telusko"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return (self.name,self.age)
    @classmethod    
    def getname(cls):
        return cls.name
    @staticmethod
    def info():
        print("this is a student class")





c1 = student("raja",7)

print(c1.name,student.name,student.getname())
student.info()
print(c1.show())