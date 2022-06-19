class Person:
    def __init__(self,first,last,gender,birth):
        self.first=first
        self.last=last
        self.gender=gender
        self.birth=birth

class Student(Person):
    def __init__(self,first,last,gender,birth,id,depart,courses=None,sche=None):
        Person.__init__(self, first,last,gender,birth)
        self.id=id
        self.depart=depart
        self.courses=courses
        self.sche=sche

    def choose_course(self, course,goal=None):
        if self.courses is None:
            self.courses = []
        self.courses.append([course.le_name[goal,course.le_credits]])
        #第一个字典:学生端,带课程名与成绩
    def sche(self):
        pass
    def del_course(self,course):
        try:del self.courses[course]
        except:print("The course you want to delete does not exist")
    def getinfo(self):
        pass
    def getgoal(self):
        pass
    def getGPA(self):
        pass


class Course:
    "lesson list"
    def __init__(self,le_id,le_name,le_depart,le_credits,le_time,le_location):
        self.le_id=le_id
        self.le_name=le_name
        self.le_depart=le_depart
        self.le_credits=le_credits
        self.le_time=le_time
        self.le_location=le_location
    def pr(self):
        print("ClassName:".ljust(14," ")+self.le_name+"\nClass ID:".ljust(15," ")+str(self.le_id)+"\nDepartment".ljust(15," ")+str(self.le_depart))
        print("Credits:".ljust(14," ")+str(self.le_credits)+"\nTime:".ljust(15," ")+str(self.le_time)+"\nLocation:".ljust(15," ")+str(self.le_location))


class CourseManagement:
    def __init__(self,Course):#这里的Course是一个类

        pass




