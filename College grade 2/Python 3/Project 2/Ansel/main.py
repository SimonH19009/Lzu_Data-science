import sys
from basic_class import Person,Student,Course,CourseManagement

names=globals()
le_names = globals()
i=0
result=0
oper=["Course registration for new user","Modify user course registration","Course management",
      "Print selected course schedule","Query grades and credits","Exit"]
names[5]=Student("1","2","3","4",5,"6")
le_names["math"]=Course("001","math","technology",5,"Monday 13.00-14.00","TianShantang302")
le_names["chinese"]=Course("0012","chinese","Liberty",3,"Tuesday 13.00-14.00","TianShantang565")
Cam_list=["Add a new course","Delete a course","Find course information","Add Student","Set students’ grades","Return registrants information","Exit"]
le_list=[le_names["math"],le_names["chinese"]]

def identy():
    global dd
    dd=int(input("Please input your ID:"))
    #确认是否有这个学生
    try:
        a=names[dd].last
    except:
        print("Sorry your account was not found, please confirm the id entered.")
        return True
    else:
        return dd

def start():
    # print the beginning menu
    global oper
    print("#"*76+"\n"+"#"*13+"Welcome to our course registration system!".center(48," ")+"#"*15+"\n"+"#"*76)
    for i in range(6):
        print("#"*13+" "*6+(str(i+1)+". "+oper[i]).ljust(42," ")+"#"*15)
    print("#"*76)

#功能:学生注册
def register():
    print("\nYou will be entering the new user registration stage.")
    a=input("Please enter c to continue or another string to return:")
    if a!="c":return False
    else:
        while True:
            try:
                iD=input("\nPlease enter your student id:")
            except:
                print("Please enter the correct ID!!\n")
            else:
                first=input("Please enter your first name:")
                last=input("Please enter your surname:")
                try:
                    gender=int(input("Please enter your gender:"))
                except:
                    print("Please enter the correct gender!!\n")
                else:
                    birth=input("Please enter your birthday:")
                    depart=input("Please enter your department:")
                    global names
                    names[iD] = Student(first, last, gender, birth, iD, depart)
                    print("\n\nCongratulations, you have been successfully registered!")
                    print("\nHere is your information, please check.")
                    print("Name:".ljust(14," ")+names[iD].first+" "+names[iD].last+"\nGender:".ljust(15," ")+str(names[iD].gender))
                    print("Birthday:".ljust(14," ")+names[iD].birth+"\nID:".ljust(15," ")+str(names[iD].id)+"\nDepartment:".ljust(15," ")+names[iD].depart)
                    print("\nIf the above information is incorrect, please re-enter it by entering q. \nOtherwise, you will be returned to the initial screen.")
                    a = input("Enter:")
                    if a=="q":pass
                    else:
                        print("\n\n\n")
                        break

#打印课程列表
def pr_le_list():
    global le_list
    print("The list of courses you can choose from is as follows:")
    for i in range(len(le_list)):
        print(str(i+1)+"."+str(le_list[i].le_name))

def choose():
    pass


def Choosene():
    pr_le_list()
    a=input("Please enter the course number of your choice.")

def delete():
    pass

#实现第二个功能区：学生选课，学生删除自己的选课
def modify_Cregister():
    global names
    #获取操作的学生
    while identy():
        print("Please select the next action: \nEnter 1 to re-enter, Enter 2 to return to the main page")
        a=input("Your choice:")
        if a=="2":
            return None
    #选择功能 1.选课 2.删除选课
    print("\n\n\n")
    print("#" * 76 + "\n" + "#" * 13 + "Welcome to Course Registration".center(48, " ") + "#" * 15 + "\n" + "#" * 76)
    print("#" * 13 + " " * 6 + "1. Choose a new course".ljust(42, " ") + "#" * 15)
    print("#" * 13 + " " * 6 + "2. Delete selected courses".ljust(42, " ") + "#" * 15)
    print("#" * 13 + " " * 6 + "3. Exit".ljust(42, " ") + "#" * 15)
    print("#" * 76)
    while True:
        oper = input("\nPlease select the operation you require:")  # get the operation number
        try:
            nu = int(oper)
        except:
            print("##  Please enter the correct serial number!!!\n")
        else:
            if nu == 1:
                Choosene()
                break
            elif nu == 2:
                delete()
                break
            elif nu==3:
                break
            else:
                print("##  Please enter the correct serial number!!!\n")

    pr_le_list()
    choose()
    

    #展示可选择的课程列表

#添加课程信息,并实现把课程对象加入列表
def Add_le():
    while True:
        le_id=input("Please input the Course ID:")
        le_name=input("Please input the Course name:")
        le_depart=input("Please input the Course depart:")
        le_credits=input("Please input the Course credits:")
        le_time=input("Please input the Course time:")
        le_location=input("Please input the Course locations:")
        global le_names
        le_names[le_name] = Course(le_id,le_name,le_depart,le_credits,le_time,le_location)
        print("\n\nCongratulations, the lesson has been successfully registered!")
        print("\nHere is your information, please check.")
        print("Name:".ljust(14, " ") + le_names[le_name].le_name+ "\nID:".ljust(15, " ") + str(
            le_names[le_name].le_id))
        print("Credit:".ljust(14, " ") + le_names[le_name].le_credits + "\nTime:".ljust(15, " ") + str(
            le_names[le_name].le_time) + "\nDepartment:".ljust(15, " ") + le_names[le_name].le_depart+"\nLocation:".ljust(15, " ")+le_names[le_name].le_location)
        print("\nIf the above information is incorrect, please re-enter it by entering q. \nOtherwise, you will be returned to the initial screen.")
        a = input("Enter:")
        if a == "q":
            pass
        else:
            le_list.append(le_names[le_name])
            print("\n\n\n")
            break

def Find_le_info():
    pass

def Add_stu():
    pass

def Set_Grade():
    pass

def Find_stu_info():
    pass

#删除课程
def delete_le():
    global le_names
    if le_names:
        while True:
            try:
                le_name = input("Please input the Course ID:")
                print("The course information you wish to delete is as follows.")
                le_names[le_name].pr()
                a=input("Please enter c to confirm or otherwise cancel:")
                if a=="c":
                    try:
                        le_list.remove(le_names[le_name])
                        del le_names[le_name]
                        break
                    except:
                        print("Please enter the correct course name!!")
            except:
                print("Please enter the correct course name!!")
    else:print("There are no courses that can be deleted!!!")

#实现第三个功能区，打印Cmanage菜单并提供函数入口
def Cmanage():
    global Cam_list
    print("\n\n\n")
    print("#" * 76 + "\n" + "#" * 13 + "Welcome to Course Management".center(48," ") + "#" * 15 + "\n" + "#" * 76)
    for i in range(7):
        print("#"*13+" "*6+(str(i+1)+". "+Cam_list[i]).ljust(42," ")+"#"*15)
    print("#"*76)
    while True:
        oper = input("\nPlease select the operation you require:")  # get the operation number
        try:
            nu = int(oper)
        except:
            print("##  Please enter the correct serial number!!!\n")
        else:
            if nu == 1:
                Add_le()
                break
            elif nu == 2:
                delete_le()
                break
            elif nu == 3:
                Find_le_info()
                break
            elif nu == 4:
                Add_stu()
                break
            elif nu == 5:
                Set_Grade()
                break
            elif nu == 6:
                Find_stu_info()
                break
            elif nu == 7:
                sys.exit()
            else:
                print("Please enter the correct serial number")

def schedule():
    pass

def quert():
    pass

def main():
    start()                                                   # print the beginning menu
    while True:
        oper=input("\nPlease select the operation you require:")     # get the operation number
        try:nu=int(oper)
        except:print("##  Please enter the correct serial number!!!\n")
        else:
            if nu==1:
                register()
                break
            elif nu==2:
                modify_Cregister()
                break
            elif nu==3:
                Cmanage()
                break
            elif nu==4:
                schedule()
                break
            elif nu==5:
                quert()
                break
            elif nu==6:
                sys.exit()
            else:
                print("Please enter the correct serial number")

while True:
    main()
    print(le_list)








