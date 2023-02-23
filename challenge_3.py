class student:
    def student_(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name

    def get_rollno(self):
        return self.roll_no
    def set_rollno(self,new_rollno):
        self.roll_no = new_rollno


    def display(self):
        print(f"Name : {self.name} \nRoll no. : {self.roll_no}")


student_obj = student()
student_obj.student_(input('Enter your name : '),int(input('Enter your roll no : ')))
student_obj.display()
print(student_obj.get_name())
student_obj.set_name(input('Enter your new name : '))
student_obj.display()
print(student_obj.get_rollno())
student_obj.set_rollno(int(input('Enter your new roll no : ')))
student_obj.display()