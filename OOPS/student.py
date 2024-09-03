class student:
    name:str
    id:int
    gender:str
    course:str

    def set_student(self,name,id,gender,course):
        self.name=name
        self.id=id
        self.gender=gender
        self.course=course

    def display_student(self):
        print(self.name,self.id,self.gender,self.course)

student_instance=student()

student_instance.set_student("hari",233,"male","python")

student_instance.display_student()