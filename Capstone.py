from datetime import datetime 

# importing database
import sqlite3
connection = sqlite3.connect('Capstone.db')
cursor = connection.cursor()

# importing password encrypting
import bcrypt

class Assessments():
    def __init__(self,assessment_id, compentency_id, name):
        self.assessment_id = assessment_id
        self.compentency_id = compentency_id
        self.name = name
        self.date_created = datetime.now().strftime('%x')

    def save_assessment(self):
            cursor.execute('UPDATE Assessments SET compentency_id = ?, name = ?, date_created = ? WHERE assessment_id = ?', (self.compentency_id, self.name, self.date_created, self.assessment_id))
            connection.commit()
            input('''
    Your information has been updated, Thank you.''')
            
    def load_assessment(self, assessment_id = 0):
        if assessment_id == 0:
            assessment_id = int(input('''
    Provide Assessment ID here: '''))
            available_ids = cursor.execute('SELECT assessment_id FROM Assessments').fetchall()
            if (assessment_id, ) in available_ids:
                results = cursor.execute('SELECT * FROM Assessments WHERE assessment_id = ?',(assessment_id, )).fetchone() 
                self.name = results[2]
                self.assessment_id = results[0]
                self.compentency_id = results[1]
                self.date_created = results[3]
            else:
                input('''
    Please provide correct ID.''')   
                
                

    def edit_assessments(self):
        available_ids = cursor.execute('SELECT assessment_id FROM Assessments').fetchall()  
        if (self.assessment_id, ) in available_ids:
            while True:
                edit_what_info = input('''
    Select from the following below, what you would like to edit in this assessment.
        1.) Related Compentency
        2.) Name
        3.) Quit to previous menu.
        >> ''')
                if edit_what_info == '1':
                    while True:
                        edit_compentency = int(input('''
    Please Provide Compentency ID:
    >> '''))
                        available_ids = cursor.execute('SELECT compentency_id FROM Compentencies').fetchall()     
                        if (edit_compentency, ) in available_ids:
                            cursor.execute('UPDATE Assessments SET compentency_id = ? WHERE assessment_id = ?', (edit_compentency, self.assessment_id))
                            connection.commit()
                            input('''
    Your information has been saved. ''') 
                            break
                        else:
                            input('''
    This Compentency ID does not exist. Please try again.''')
                            break 
                if edit_what_info == '2':
                    edit_assessment_name = input('''
    Please provide new assessment name.
    >> ''')
                    cursor.execute('UPDATE Assessments SET name = ? WHERE assessment_id = ?', (edit_assessment_name, self.assessment_id))
                    connection.commit()
                    input('''
    Your information has been updated. ''')    
                if edit_what_info == '3':
                    break    
        

class Compentencies():
    def __init__(self, compentency_id, name):
        self.compentency_id = compentency_id
        self.name = name
        self.date_created = datetime.now().strftime('%x')

    def edit_compentency_info(self):

        # while True:
    #         edit_compentency = int(input('''
    # Please Provide Compentency ID:
    # >> '''))
        available_ids = cursor.execute('SELECT compentency_id FROM Compentencies').fetchall()  
        if (self.compentency_id, ) in available_ids:
            new_compentency_name = input('''
    Provide updated compentency name here.
    >> ''')
            cursor.execute('UPDATE Compentencies SET name = ? WHERE compentency_id = ?',(new_compentency_name, self.compentency_id)) 
            connection.commit()
            input('''
    Your information has been saved.''') 
        
        else:
            input('''
    This ID does not exist. Please try again.''')   
                 
                
    def load_compentency(self, compentency_id = 0):    
        if compentency_id == 0:
            compentency_id = int(input('Provide Compentency ID here: '))
        available_ids = cursor.execute('SELECT compentency_id FROM Compentencies').fetchall()
        if (compentency_id, ) in available_ids:            
            results = cursor.execute('SELECT * FROM Compentencies WHERE compentency_id = ?', (compentency_id, )).fetchone()
            self.compentency_id = results[0]
            self.name = results[1]
            self.date_created = results[2]


    def save_compentency(self):
        cursor.execute('UPDATE Compentencies SET name = ?, date_created = ? WHERE compentency_id = ?', (self.name, self.date_created, self.compentency_id))
        connection.commit()
        input('''
        Your information has been saved.''')
    

class Results():
    def __init__(self, result_id, assessment_id, employee_id, manager_id,date_taken,score):
        self.result_id = result_id
        self.assessment_id = assessment_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.date_taken = date_taken
        self.score = score


    def save_result(self):
        cursor.execute('UPDATE Results SET assessment_id = ?, employee_id = ?, manager_id = ?, date_taken = ? score = ? WHERE result_id = ?', (self.assessment_id, self.employee_id, self.manager_id, self.date_taken, self.score, self.result_id))   
        connection.commit()
        input('''
    Your information has been updated, Thank you.''')

    def load_result(self, result_id = 0):
            if result_id == 0:
                result_id = int(input('Provide Result ID here: '))
            available_ids = cursor.execute('SELECT result_id FROM Results').fetchall()
            if (result_id, ) in available_ids:
                results = cursor.execute('SELECT * FROM Results WHERE result_id = ?',(result_id, )).fetchone() 
                self.result_id = results[0]
                self.assessment_id_id = results[1]
                self.employee_id = results[2]
                self.manager_id = results[3]
                self.date_taken = results[4]
                self.score = results[5]

    def edit_results(self):       
        available_ids = cursor.execute('SELECT result_id FROM Results').fetchall()  
        if (self.result_id, ) in available_ids:                               
            while True:
                edit_what_result = input('''
    Select from the following below, what would you like to edit in this result.
    1.) Related Assessment
    2.) Employee ID
    3.) Assigning Manager
    4.) Date Taken
    5.) Score
    6.) Quit and return to previous menu.
    >> ''')
                if edit_what_result == '1':
                    while True:
                        edit_assessment = int(input('''
    Please Provide Assessment ID:
    >> '''))
                        available_ids = cursor.execute('SELECT assessment_id FROM Assessments').fetchall()
                   
                        if (edit_assessment, ) in available_ids:
                            cursor.execute('UPDATE Results SET assessment_id = ? WHERE result_id = ?', (edit_assessment, self.result_id))

                            input('''
    Your information has been saved. ''')
                            break
                        else:
                            input('''
    This assessment ID does not exist. Please try again.''')  
                        break  
                elif edit_what_result == '2':
                    while True:
                        edit_employee = int(input('''
    Please Provide Employee ID:
    >> '''))
                        available_ids = cursor.execute('SELECT employee_id FROM Users').fetchall()     
                        if (edit_employee, ) in available_ids:
                            cursor.execute('UPDATE Results SET employee_id = ? WHERE result_id = ?', (edit_employee, self.result_id))
                            connection.commit()
                            input('''
    Your information has been saved. ''') 
                            break
                        else:
                            input('''
    This Employee ID does not exist. Please try again.''')
                            break 
                elif edit_what_result == '3':
                    while True:
                        edit_manager = int(input('''
    Please Provide Manager ID:
    >> '''))
                        available_ids = cursor.execute('SELECT employee_id FROM Users WHERE user_type = "1"').fetchall()     
                        if (edit_manager, ) in available_ids:
                            cursor.execute('UPDATE Results SET manager_id = ? WHERE result_id = ?', (edit_manager, self.result_id))
                            connection.commit()
                            input('''
    Your information has been saved. ''') 
                            break
                        else:
                            input('''
    This Manager ID does not exist. Please try again.''')
                            break 
                
                elif edit_what_result == '4':
                    edit_date_taken = input('''
    Please Provide the date taken:
    >> ''')
                    cursor.execute('UPDATE Results SET date_taken = ? WHERE result_id = ?', (edit_date_taken, self.result_id))
                    connection.commit()
                    input('''
    Your information has been saved. ''')
                    break
                elif edit_what_result == '5':
                    edit_score = input('''
    Please Provide the Score:
    >> ''')
                    if edit_score in ['0', '1', '2', '3', '4']:
                        cursor.execute('UPDATE Results SET score = ? WHERE result_id = ?', (edit_score, self.result_id))
                        connection.commit()   
                        input('''
    Your information has been saved. ''')
                        break
                    if edit_score not in ['0', '1', '2', '3', '4']:
                        input('''
    Score must be between 0 and 4.''')
                        break
                elif edit_what_result == '6':
                    break                                                               
                else:
                    input('''
    We do not recogniize this result ID. Please try again.''')  
                    break                                                                          
            connection.commit()                        
        else:
            input('''
    This ID does not exist. Please try again.''')  
class Users:
    def __init__(self, employee_id, first_name, last_name, email, password, phone, date_hired, user_type, user_active):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) 
        self.phone = phone
        self.date_hired = date_hired
        self.user_created_date = datetime.now().strftime('%x')
        self.user_type = user_type
        self.user_active = user_active

    def change_password(self):
        while True:
            
            old_password = input('''
    Current Password:
    ''')
            if old_password == bcrypt.checkpw(old_password.encode('utf-8'), self.password):
                new_password = input('New Password:\n\n>> ')
                self.password =  bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                input('''
    New password has been successfully entered.
    ''')
            else:
                input('''
    This password is incorrect.
        Please provide the correct password:''')    
                break

    def edit_own_information(self):
            email_verify = input('''
    Please enter your email below:
    >> ''')
                                          
            user_id = cursor.execute('SELECT employee_id FROM Users WHERE email = ?', (email_verify,)).fetchone()
            if user_id:
                self.load_user(user_id[0])
                verify_self = input('''
    Please verify identity by providing password below:
    >> ''')
                
                if verify_self == bcrypt.checkpw(verify_self.encode('utf-8'), self.password):              
                        choose_employee_update = input('''
    Select from the following to update employee information.
        1.) First name
        2.) Last name
        3.) Email
        4.) Phone
        5.) Quit and return to previous menu''')
                        
                        if choose_employee_update == '1':
                            new_first_name = input('''
    Provide First Name here.
        >> ''')
                            cursor.execute('UPDATE Users SET first_name = ? WHERE employee_id = ?',(new_first_name, self.employee_id))
                        if choose_employee_update == '2':
                            new_last_name = input('''
    Provide Last Name here.
        >> ''')
                            cursor.execute('UPDATE Users SET last_name = ? WHERE employee_id = ?',(new_last_name, self.employee_id))
                        if choose_employee_update == '3':
                            new_email = input('''
    Provide Email here.
        >> ''')
                            cursor.execute('UPDATE Users SET email = ? WHERE employee_id = ?',(new_email, self.employee_id))        
                        if choose_employee_update == '4':
                            new_phone = input('''
    Provide Phone Number here.
        >> ''')
                            cursor.execute('UPDATE Users SET phone = ? WHERE employee_id = ?',(new_phone, self.employee_id))            

                              
            else:
                 input('''
    We coud not find an account with this email and password.
        Please try again.''')
             
    def edit_employee_info(self):
        which_employee = int(input('''
    Please enter the ID for the selected Employee.
    >> '''))
        available_ids = cursor.execute('SELECT employee_id FROM Users').fetchall()  
        if (which_employee, ) in available_ids:   
            while True:
                choose_employee_update = input('''
    Select from the following to update employee information.
        1.) First name
        2.) Last name
        3.) Email
        4.) Phone
        5.) Hire date
        6.) Employee type
            1 = Manager
            0 = Employee

        7.) Quit and return to previous menu.    
        >>    ''')    
                if choose_employee_update == '1':
                    new_first_name = input('''
    Provide First Name here.
        >> ''')
                    cursor.execute('UPDATE Users SET first_name = ? WHERE employee_id = ?',(new_first_name, self.employee_id))

                    connection.commit()
                    input('''
    Entry has been saved.''')                    
                if choose_employee_update == '2':
                    new_last_name = input('''
    Provide Last Name here.
        >> ''')
                    cursor.execute('UPDATE Users SET last_name = ? WHERE employee_id = ?',(new_last_name, self.employee_id))

                    connection.commit()
                    input('''
    Entry has been saved.''')                    
                if choose_employee_update == '3':
                    new_email = input('''
    Provide Email here.
        >> ''')
                    cursor.execute('UPDATE Users SET email = ? WHERE employee_id = ?',(new_email, self.employee_id))

                    connection.commit()
                    input('''
    Entry has been saved.''')                            
                if choose_employee_update == '4':
                    new_phone = input('''
    Provide Phone Number here.
        >> ''')
                    cursor.execute('UPDATE Users SET phone = ? WHERE employee_id = ?',(new_phone, self.employee_id))   

                    connection.commit()
                    input('''
    Entry has been saved.''')
                if choose_employee_update == '5':
                    new_hire_date = input('''
    Provide Hire Date here.
        >> ''')
                    cursor.execute('UPDATE Users SET hire_date = ? WHERE employee_id = ?',(new_hire_date, self.employee_id))

                    connection.commit()
                    input('''
    Entry has been saved.''')                           
                if choose_employee_update == '6':
                    hire_type = input('''
    Provide Employee type.
        1 for manager, 0 for employee.
        >> ''')
                    if hire_type in ['0', '1']:
                        cursor.execute('UPDATE Users SET user_type = ? WHERE employee_id = ?',(hire_type, self.employee_id))   
            

                        connection.commit()
                        input('''
    Entry has been saved.''')
                        break
                    else:
                        input('''
    Entry must be 1 for Manager or 0 for employee. Please try again.''')
                        break
                if choose_employee_update == '7':
                    break
           


    def update_email(self):
        while True:
            old_email = input('Current E-mail:\n\n>> ')
            if old_email == self.email:
                new_email = input('New E-mail:\n\n>> ')
                self.email = new_email 
            else:
                input('''
    Please provide the correct current email address.''')    
                break            

# you have to load before saving, remember that
    def load_user(self, employee_id = 0):
            if employee_id == 0:
                employee_id = int(input('''
    Provide Employee ID here: '''))
            available_ids = cursor.execute('SELECT employee_id FROM Users').fetchall()
            if (employee_id, ) in available_ids:               
                results = cursor.execute('SELECT * FROM Users WHERE employee_id = ?',(employee_id, )).fetchone() 
                self.employee_id = results[0]
                self.first_name = results[1]
                self.last_name = results[2]
                self.email = results[3]
                self.password = results[4]
                self.phone = results[5]     
                self.date_hired = results[6]       
                self.user_created_date = results[7]
                self.user_type = results[8]
                self.user_active = results[9]


    def load_own_results(self):
        while True:
            query = cursor.execute('''SELECT
    u.first_name,
    u.last_name,
    c.name,
    a.name,
    uar.score,
    uar.date_taken
FROM Compentencies c
CROSS JOIN Users u
LEFT JOIN Assessments a
    ON a.compentency_id = c.compentency_id
LEFT JOIN Results uar
    ON uar.assessment_id = a.assessment_id
   AND uar.employee_id = u.employee_id
WHERE u.employee_id = ?
  AND (
        uar.date_taken IS NULL
        OR uar.date_taken = (
            SELECT MAX(uar2.date_taken)
            FROM Results uar2
            JOIN Assessments a2
                ON uar2.assessment_id = a2.assessment_id
            WHERE uar2.employee_id = u.employee_id
              AND a2.compentency_id = c.compentency_id
        )
      )
ORDER BY c.compentency_id;''', (self.employee_id, )).fetchall()
            print(f'''
                        {len(query)} Results Found
                    ------------------------------------''')
            for row in query:
                print(f'''
            
    Employee:    {row[1]}, {row[0]}
    Assessment:  {row[3]} 
    Compentency: {row[2]}       Score: {row[4]}
    Date Taken:  {row[5]}
            ''')
                        
            input('Returning to menu.')
            break


    def save_user(self):
        cursor.execute('UPDATE Users SET first_name = ?, last_name = ?, email = ?, password = ?, phone = ?, date_hired = ?, user_created_date = ?, user_type = ?, user_active = ? WHERE employee_id = ?', (self.first_name, self.last_name, self.email, self.password, self.phone, self.date_hired, self.user_created_date, self.user_type, self.user_active, self.id))
        connection.commit()
        input('''
    Your information has been saved.''')

   

#  Will need save method for assessments, compentencies, and results   # 



    def login_screen(self):
        while True:
            login = input('''
    Employee Aptitude Login:
          Please enter your email below:
          >>  ''')
            user_id = cursor.execute('SELECT employee_id FROM Users WHERE email = ?', (login,)).fetchone()
            if user_id:
                self.load_user(user_id[0])
                enter_pwd = input(''' 
          Please enter your password below:
          >>  ''')
                if bcrypt.checkpw(enter_pwd.encode('utf-8'), self.password):
                    print('woo youre in')
                    self.check_role()
            else:
                input('''
    We could not find an account with this email.
          Please try again.
         
     ''')

# checks if employee is a manager or not
    def check_role(self):
        if self.user_type == 1:
            print('Youre a manager')
            manager_menu()
        elif self.user_type == 0:
            print('youre an employee')
            self.employee_menu()    

    def employee_menu(self):  
        print(f"""
            You have been successfully logged into your Employee Account.""")
        while True:
        
            search_input = input("""
            Select from the following actions below:
                V: View scores by Compentencies.
                E: Edit personal information.
                P: Change Password.
                Q: Quit
                >>  """).upper()   
            if search_input == 'V':
                self.load_own_results()
            if search_input == 'E':  
                self.edit_own_information() 
            if search_input == 'P':
                self.change_password()
               
# Menu that appears for non-management employees.


             
# # add employee menu screen 
# menu will include viewing all user information
# editing user information. 
#     password,,, email,,, phone,, 
# view personal compentencies and results from tests taken.

# Menu that appears for management.



# menu after manager selects to search on database.---------------------------------------------------------
                

# menu after manager selects to add to database------------------------------------------------------------



# with viewing employees after menu, ask yes or no to also viewing their compentencies
    


        # create 4 menu screens for searching, viewing, editting, adding


    
    def add_user(self):
        query = 'INSERT INTO Users (first_name, last_name, email, password, phone, date_hired, user_created_date, user_type, user_active) VALUES (?,?,?,?,?,?,?,?,?)'
        values = (self.first_name, self.last_name, self.email, self.password, self.phone, self.date_hired, self.user_created_date, self.user_type, self.user_active)
        self.employee_id = cursor.lastrowid
        cursor.execute(query, values)
        connection.commit()





def add_result():
    available_ids = cursor.execute('SELECT assessment_id FROM Assessments').fetchall() 
    while True:
        input_assessment_id = int(input('''
To add a result to the database, please provide the following information.
    Assessment ID: '''))
        print(f'{available_ids}')
        print(f'{input_assessment_id, }')
        if (input_assessment_id, ) in available_ids:
            available_ids = cursor.execute('SELECT employee_id FROM Users').fetchall() 
            input_employee_id = int(input('''
    Employee ID: '''))
            if (input_employee_id, ) in available_ids:
                available_ids = cursor.execute('SELECT employee_id FROM Users WHERE user_type = "1" ').fetchall() 
                input_manager_id = int(input('''
    Assigning Manager ID:  '''))
                if (input_manager_id, ) in available_ids:
                    input_date_taken =  input('''
    Date Assessment Was Taken: ''')
                    input_score = input('''
    Score of Assessment:

      *Please note score must be from 0 to 4, 0 being No Compentency and 4 being Mastery.*
       >> ''')
                    if input_score in ['0', '1', '2', '3', '4']:
                        new_result = 'INSERT INTO Results(assessment_id, employee_id, manager_id, date_taken, score ) VALUES (?,?,?,?,?)'
                        update_values = (input_assessment_id, input_employee_id, input_manager_id, input_date_taken, input_score)
                        cursor.execute(new_result, update_values)
                        input('''
This entry has been saved.''')
                        connection.commit()
                        break
                    else:
                        print('''
    Score must be between 0 to 4.''')    
                else:
                    print('''
    Please provide the correct manager ID.''')
                    
            else:
                print('''
    Please provide the correct employee ID.''')  
                 
        else:
            print('''
Please provide correct assessment ID''')  
            

def manager_menu():

    print(f"""
    You have been successfully logged into your Employee Management Account.""")
    while True:

        search_input = input("""
    Select from the following actions below:
        S: Search for files from database.
        A: Add to database.
        V: View files from database.
        E: Edit files from database.
        Q: Quit
        >>  """).upper()
        if search_input == 'S':
            manager_search_files_menu()  
        if search_input == 'A':
            add_to_database_menu()
        if search_input == 'V':
            view_files_menu()
        if search_input == 'E':
            edit_files_menu()    
        if search_input == 'Q':
            input('You have been logged out.')   
            break     
                
             
def add_to_database_menu():
    while True:
        user_add = input('''
    You have been redirected.

    What would you like to add to today?
        Select from the options below:
        C: Add to current list of Compentency skills.
        A: Add a new assessment.
        R: Add a result to a completed assessment to employee file.
        E: Add an Employee.
        Q: Quit to Main Menu.
    >>  ''').upper()
        if user_add == "C":
            add_compentency()
        if user_add == 'A':
            add_assessment()
        if user_add == 'R':
            add_result() 
        if user_add == 'E':
            add_employee()      
        if user_add == 'Q':
            break    

def manager_search_files_menu():
    while True:
        search_files = input('''
    You have been redirected to the search engine.
    Select from the options below:
        A: Search for Assessments. 
        C: Search for Compentency skills.
        E: Search for Employees by name.
        R: Search for Assessment Results by Employee.
        S: Search for Assessment Results by Compentencies.
        Q: Quit to Main Menu.
    >>  ''').upper()
        if search_files == 'A':
            search_assessments()
        if search_files == 'C':
            search_compentencies()
        if search_files == 'E':
            search_employees()
        if search_files == 'R':
            search_one_set_results()   
        if search_files == 'S':
            search_results_by_compentency()    
        if search_files == 'Q':
            break     

def view_files_menu():
    while True:
        user_view = input('''
Select from below to view:
    C: View Compentencies available.
    A: View Assessments available.
    S: View Select employees.
    E: View all Employees.
    R: View results from an Employee.
    RS: View summary of results.
    Q: Quit to Main Menu.
    >>  ''').upper()
        if user_view == 'C':
            view_all_compentencies()
        if user_view == 'A':
            view_all_assessments()
        if user_view == 'S':
            search_employees()
        if user_view == 'E':
            view_all_employees()
        if user_view == 'R':
            search_one_set_results()
        if user_view == 'CRS':
            view_all_results()  
        if user_view == 'Q':
            break     
def add_employee():
    input_first_name = input('''
To add Employee to database, please provide the following information.

    First Name: ''')
    input_last_name = input('''
    Last Name: ''')
    input_email = input('''
    Email: ''')
    input_password = input(''' 
    Password: ''')
    input_phone = input('''
    Phone Number: ''')
    input_date_hired = input('''
    Hire Date: ''')
    input_user_type = input('''
    Is this Employee a manager?
        0: Employee
        1: Manager  
        ''')
    while True:
        if input_user_type in ['0', '1']:
            new_password = bcrypt.hashpw(input_password.encode('utf-8'), bcrypt.gensalt())
            input_date_created = datetime.now().strftime('%x')
            new_user = 'INSERT INTO Users(first_name, last_name, email, password, phone, date_hired, user_created_date, user_type) VALUES (?,?,?,?,?,?,?,?)'
            new_values = (input_first_name, input_last_name, input_email, new_password, input_phone,input_date_hired, input_date_created, input_user_type)
            cursor.execute(new_user, new_values)
            connection.commit()
            input('''
Entry has been saved.''')
        if input_user_type not in ['0', '1']:
            input('''
    Must be 0 for employee or 1 for Manager.''')
            break
        continue        


def add_compentency():
    input_name_compentency = input('''
To add a new compentency, please provide the following information. 

    Compentency Name: ''')
    date_created = datetime.now().strftime('%x')
    new_compentency = 'INSERT INTO Compentencies(name, date_created) VALUES (?,?)'
    new_values = (input_name_compentency, date_created)
    cursor.execute(new_compentency, new_values)
    input('''
Entry has been saved.''')
    connection.commit()

def add_assessment():   
    available_ids = cursor.execute('SELECT compentency_id FROM Compentencies').fetchall() 
    while True:
        input_compentency_id = int(input('''
To add an assessment to the database, please provide the following information.
    Compentency ID: '''))
        if (input_compentency_id, ) in available_ids: 
            input_name_assessment =input('''
    Name of Assessment: ''')
            input_date_created = datetime.now().strftime('%x')
            new_assessment = "INSERT INTO Assessments(compentency_id, name, date_created) VALUES (?,?,?)"    
            new_values = (input_compentency_id, input_name_assessment, input_date_created)
            cursor.execute(new_assessment, new_values)
            input('''
Entry has been saved. ''')
            break
        if (input_compentency_id, ) not in available_ids:
            input('''
    This ID is not recognized.''')
            break    
    connection.commit()

# creates tables in database


def create_schema():
    with open('Capstone.sql' , 'r') as assignment_file:
        sql_command = assignment_file.read()
        cursor.executescript(sql_command)        

def search_assessments():
    while True:
        manager_input = input('''
Enter name of assessment needed:
    >>  ''')
        query = cursor.execute('SELECT * FROM Assessments WHERE name LIKE ?', ('%' + manager_input + '%', )).fetchall()
        print(f'''
    {len(query)} Assessments Found
    -------------------------------''')
        if not query:
            input('Assessment not found.')
            break
        for row in query:
            print(f'''

    Name:           {row[2]}
    Assessment ID:  {row[0]}
    Compentency ID: {row[1]}
    Date Created:   {row[3]}
''')
        break 

def search_employees():
    while True:
        manager_input = input('''
Enter name of employee needed:
    >>  ''')
        query = cursor.execute('SELECT * FROM Users WHERE first_name ||" " || last_name LIKE ? ORDER BY last_name', ('%' + manager_input + '%', )).fetchall();
        print(f'''
    {len(query)} Employees Found
    ---------------------------------------''')
        if not query:
            input('Employee not found.')
            break
        for row in query:
            print(f'''
    
    Name:           {row[2]}, {row[1]}
    Employee ID:    {row[0]}
    Email:          {row[3]}
    phone:          {row[5]}
    Hire Date:      {row[6]}

''')
        input('Returning to Menu.')
        break

def search_compentencies():
    while True:
        search_input = input('''
    Enter name of Compentency needed:
    >>  ''')
        query = cursor.execute('SELECT * FROM  Compentencies WHERE name LIKE ? ORDER BY name', ('%' + search_input + '%', )).fetchall()
        print(f'''
        {len(query)} Compentencies Found
        -----------------------------------''')
        if not query:
            input('Compentency not found.')
            break
        for row in query:
            print(f'''

        Name:              {row[1]}
        Compentency ID:    {row[0]}
        Date Created:      {row[2]}
''')
        input('''
    Returning to menu.''')
        break


# 
        
def search_results_by_compentency():
    while True:
            search_input = input('''
    What compentency results are you looking for?
        Compentency Name: ''')
            query = cursor.execute('''SELECT c.name, a.name, r.score, r.result_id, e.last_name, e.first_name FROM Users e 
            JOIN Results r ON e.employee_id = r.employee_id 
            JOIN  Assessments a ON r.assessment_id = a.assessment_id
            JOIN Compentencies c ON a.compentency_id = c.compentency_id
            WHERE c.name LIKE  ?
            ORDER BY c.name''', (f'%{search_input}%',)).fetchall()
            print(f'''
        {len(query)} Results Found
        --------------------------------''')
            if not query:
                input('Results not found.')
                break
            for row in query:
                print(f'''

        Compentency:  {row[0]}   
        Assessment:   {row[1]}  Score:  {row[2]}
        Taken By:     {row[4]}, {row[5]}
        Result ID:    {row[3]}
    ''')
            input('''
    Returning to menu.''')
            break 



def search_one_set_results():
    while True:
        search_result = input(f'''
        Enter Employee ID Below:
        >> ''')
        query = cursor.execute('''SELECT
    u.first_name,
    u.last_name,
    c.name,
    a.name,
    uar.score,
    uar.date_taken
FROM Compentencies c
CROSS JOIN Users u
LEFT JOIN Assessments a
    ON a.compentency_id = c.compentency_id
LEFT JOIN Results uar
    ON uar.assessment_id = a.assessment_id
   AND uar.employee_id = u.employee_id
WHERE u.employee_id = ?
  AND (
        uar.date_taken IS NULL
        OR uar.date_taken = (
            SELECT MAX(uar2.date_taken)
            FROM Results uar2
            JOIN Assessments a2
                ON uar2.assessment_id = a2.assessment_id
            WHERE uar2.employee_id = u.employee_id
              AND a2.compentency_id = c.compentency_id
        )
      )
ORDER BY c.compentency_id;''', (search_result, )).fetchall()

        print(f'''
            {len(query)} Results Found
        ------------------------------------''')
        for row in query:
            print(f'''

        Employee:    {row[1]}, {row[0]}
        Assessment:  {row[3]} 
        Compentency: {row[2]}       Score: {row[4]}
        Date Taken:  {row[5]}
                ''')
            
        input('Returning to menu.')
        break

def view_all_compentencies():
    while True:
        input('''
    To view all compentencies press Enter:
      ''')
        query = cursor.execute('SELECT * From Compentencies ORDER BY name').fetchall()
        print(f'''
        {len(query)} Compentencies Found
    -------------------------------''')
        for row in query:
            print(f'''
    
    Name:           {row[1]}     
    Compentency ID: {row[0]}               
    Date Created:   {row[2]}
    -''')
        input('''
    Returning to Menu''')
        break    


def view_all_employees():
    while True:
            input('''
        To view all Employees press Enter:
          ''')
            query = cursor.execute('SELECT * From Users ORDER BY last_name').fetchall()
            print(f'''
            {len(query)} Employees Found
            ---------------------------------''')
            
            for row in query:
                print(f'''
               
               Name:           {row[2]}, {row[1]}
               Employee ID:    {row[0]}
               Email:          {row[3]}
               phone:          {row[5]}
               Hire Date:      {row[6]}''')
            input('''
        Returning to Menu''')
            break    

def view_all_results():
    while True:
        select_compentency = input('''
    To View Results Summary Enter Compentency ID:

    ''')
        query = cursor.execute('''SELECT
            c.name,
            u.first_name,
            u.last_name,
            a.name,
            uar.score,
            uar.date_taken
        FROM Users u
        CROSS JOIN Compentencies c
        LEFT JOIN Results uar
            ON uar.result_id = 
            (SELECT uar2.result_id
            FROM Results uar2
            JOIN Assessments a2
                ON a2.assessment_id = uar2.assessment_id
            WHERE uar2.employee_id = u.employee_id
                AND a2.compentency_id = c.compentency_id ORDER BY uar2.date_taken DESC limit 1)
        LEFT JOIN Assessments a
            ON a.assessment_id = uar.assessment_id
        WHERE c.compentency_id = ?
        ORDER BY u.last_name, u.first_name;
        ''', (select_compentency, )).fetchall()

        print(f'''
        {len(query)} Results Found
        ------------------------------------''')
        for row in query:
            print(f'''

        Compentency:{row[0]}       Score: {row[4]}
        Assessment: {row[3]} 
        Taken By: {row[2]}, {row[1]}
        Date Taken: {row[5]}
        ''')
        break


def view_all_assessments():
    while True:
        query = cursor.execute('SELECT * FROM Assessments ORDER BY name').fetchall()
        print(f'''
        {len(query)} Results Found
        -------------------------------''')
        for row in query:
            print(f'''

        Assessment Name:    {row[2]}
            Date Created:   {row[3]}
            Assessment ID:  {row[0]}
            Compentency ID: {row[1]}''')   
        input('''
        Returning to Menu.''')     
        break

def edit_files_menu():
    while True:
        edit_input = input('''
Select from below to edit:
    C: Edit from available Compentencies.
    A: Edit available Assessments.
    R: Edit Results from employees.
    E: Edit employee information.
    Q: Quit 
    >>  ''').upper()
        if edit_input == 'C':
            compentency_to_edit = Compentencies('', '')
            compentency_to_edit.load_compentency()
            compentency_to_edit.edit_compentency_info()
        if edit_input == 'A':
            assessment_to_edit = Assessments('', '', '')
            assessment_to_edit.load_assessment()
            assessment_to_edit.edit_assessments()   
        if edit_input == 'R':
            result_to_edit = Results('', '','', '', '', '' )
            result_to_edit.load_result()
            result_to_edit.edit_results()    
        if edit_input == 'E':
            employee_to_edit = Users('', '', '', '', '', '', '', '', '')
            employee_to_edit.load_user()
            employee_to_edit.edit_employee_info()
        if edit_input == 'Q':
            input('''
    Returning to menu.''')
            break






# create_schema()
# user3 = Users('','Joeseph', 'James', 'jonesjamenson@gmail.com', 'Pongoboiii', '555-465-2346', '05-22-25', 1, 1)
# user3.add_user()
# user3.save_user()
new_user = Users('','','','','','','','','')
# Users.load_user(new_user)

new_user.login_screen()

# (((USE JOIN)))


# select all from Results where user_id = blah

# select name From users where 





