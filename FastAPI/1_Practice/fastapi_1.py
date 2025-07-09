from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel

app = FastAPI(debug = True)

# 1) Query Parameter :
# @app.get(path = "/")
# def display(info:str = Query(default = "Not Given Yet", alias = "name")): # Type /?name=your_name to write value in the url path.
#     return {"name" : info} # Previously you'd use info=your_name, but with alias "name" now we can use "name" of this json.

# ---------------------------------------------------------------------------------------------------------------------------------

# 2) Path Parameter :
# student_details = {
#     1601 : {'Name' : 'Ainaa', 'Age' : 18, 'Section' : 'C'},
#     1602 : {'Name' : 'Ayase', 'Age' : 22, 'Section' : 'A'},
# }

# @app.get(path = "/")
# def get_student_details():
#     return {'Name' : 'Not Given Yet', 'Age' : 'Not Given Yet, 'Section' : 'Not Given Yet'}

# @app.get(path = "/{student_id}")
# def get_student_details(student_id:int = Path(description = "Enter your current student ID", ge = 1601, le = 1602)):
#     """
#     This function won't even be executed if student_id doesn't meet the requirements of ge = 1601, le = 1602 written inside Path.
#     Hence the below if condition is redundant in this case.
#     """
#     if student_id not in student_details:
#         return {"Unknown" : 'This student has not registered yet!'}
#     return student_details[student_id]

# ---------------------------------------------------------------------------------------------------------------------------------

# 3) Post Method : ANY PARAMETER WITH Body(..) is a Requested Body part which is from client side.
# student_details = {
#     "student_ids" : [],
# }

# @app.post(path = "/students_registration")
# def add_student(student_id: int = Body()): # description value of Body() doesn't show up in Swagger UI, so don't write it ig.
#     if student_id in student_details:
#         return {"Error" : "The student is already registered."}
    
#     student_details["student_ids"].append(student_id)
#     return {"Response" : f"The student with ID {student_id} is registered.",
#             "Total Students so far" : student_details["student_ids"].__len__()}

# ---------------------------------------------------------------------------------------------------------------------------------

# 4) Post Method with path parameter even if the path parameter is not written in path using {..}.
# student_details = {
#     1601 : {'Name' : 'Ainaa', 'Age' : 18, 'Section' : 'C'},
#     1602 : {'Name' : 'Ayase', 'Age' : 22, 'Section' : 'A'},
# }

# class Student(BaseModel): # For custom Data Structure use BaseModel to make sure data with type Student is VALID the defined below :
#     # The attributes' names can be same as any student's attributes of student_details or not.
#     name: str = "Not Given"
#     age: int # must use typehint so pydantic understands what is the type of Name and can validate easily.
#     section: str = 'A'

# @app.post(path = "/students_registration/{student_id}") # to write data from client side in Swagger UI.
# def add_student(student_id: int  = Path(description = "Enter New Student ID"), student: Student = Body()):
#     """
#     student_id = A Path and function Parameter. It must be declared in the path which we did --> {student_id}.
#     student = A parameter of type Student and it is type annotated with Body(). That means the value of student need to be manually
#               inserted in swagger UI, inside Request body.
    
#     Using student_id we can first check if that student_id already exists and if its not, then we insert the value of student inside
#     Request body. How? First insert student_id value (and by default student has default value in Request body) and hit the execute
#     button. See if its already existing or not. If its not, then insert values inside Request body for the parameter student.

#     Note : This insertion of new student in student_details is temporary until the web page is refreshed. Need database to make the
#            changes permanent. 
#     """
#     if student_id in student_details: # we access student_id after we hit execute button in swagger UI.
#         return {"Error" : "The student is already registered."}
#     elif student_id not in student_details and student.name == "Not Given":
#         return {"Error" : "Checking first if the student has registered yet? Yes he has not! Now inside Request Body."}
#     else:
#         student_details[student_id] = student
#         return {"Response" : f"The student with ID {student_id} is registered.",
#                 "Total Students so far" : student_details.__len__()}

# @app.get(path = "/{student_id}") # to access data in Swagger UI or inside URL and then display it.
# def get_student_details(student_id:int = Path(description = "Enter your current student ID")):
#     return student_details[student_id]

# 5) Put(Update) method :
# student_details = {
#     1601 : {'Name' : 'Ainaa', 'Age' : 18, 'Section' : 'C'},
#     1602 : {'Name' : 'Ayase', 'Age' : 22, 'Section' : 'A'},
# }

# class Student(BaseModel): # For custom Data Structure use BaseModel to make sure data with type Student is VALID the defined below :
#     """
#     The attributes' names of a Student must be same as any student of student_details since we're updating student_details here using
#     the Student's attributes in the def update_...().

#     If you write Name: str|None = None, you'll see "Name" : "string", not "Name" : None. Hence wrote "No change" for string values
#     and -1 for Age since Age can't be -1.

#     Note : This update of an existing student in student_details is temporary until you rerun this program because even after
#            refreshing the web page I saw the changes still there. Need database to make the changes permanent.
#     """
#     Name: str = "Skip if you don't want to change that"
#     Age: int = -1
#     Section: str = "Skip if you don't want to change that"

#     def __iter__(self): # This is so we can iterate class Student's attributes as a dictionary.
#         return iter(self.__dict__.items())

# @app.put(path = "/updating_students_info/{student_id}")
# def update_any_info_of_any_student(student_id:int = Path(description = "Enter your current student ID"),
#                                    student: Student = Body()):
#     if student_id not in student_details:
#         return {"Error" : f"No student with ID {student_id} exists."}
    
#     for attribute, value in student: # attribute is string.
#         if value not in {"Skip if you don't want to change that", -1}:
#             student_details[student_id][attribute] = value
    
#     return {"Update" : "Update is Successful"}

# @app.get(path = "/display_student_info_of/{student_id}") # to access data in Swagger UI or inside URL and then display it.
# def get_student_details(student_id:int = Path(description = "Enter your current student ID")):
#     return student_details[student_id]

# 6) Delete method :
student_details = {
    1601 : {'Name' : 'Ainaa', 'Age' : 18, 'Section' : 'C'},
    1602 : {'Name' : 'Ayase', 'Age' : 22, 'Section' : 'A'},
}

@app.delete(path = "/Delete_student_by_ID/{student_id}")
def delete_student(student_id:int = Path(description = "Enter your current student ID")):
    if student_id not in student_details:
        return {"Error" : f"No student with ID {student_id} exists."}
    
    del student_details[student_id]
    return {"Delete" : f"Deletion of the ID {student_id} is Successful"}

@app.get(path = "/display_student_info_of/{student_id}") # to access data in Swagger UI or inside URL and then display it.
def get_student_details(student_id:int = Path(description = "Enter your current student ID")):
    if student_id not in student_details:
        return {"Error" : f"No student exists with ID {student_id}."}
    
    return student_details[student_id]