class Students():
    def __init__(self):
        print("I am special method")

    def studentReg(self,name,mob,sub,city):
        print("Student name is ",name)
        print("Student mobile number is ", mob)
        print("Student has opted for ", sub)
        print("Student is from",city)

    @classmethod
    def studentAdmin(cls,name):
        print("Student name is", name)

    @staticmethod
    def studentTrip(place):
        print("Student are travelling to", place)


s=Students
s.studentReg("Neel",545456,"Python","Bangalore")
s.studentAdmin("Neel")
s.studentTrip("Pune")
