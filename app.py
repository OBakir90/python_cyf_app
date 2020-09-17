
order = False

entrance = input('''
    Hello, 
    This app shows CYF Manchester Class Students names and grades
    You can see all students by ordering 'show_all'
    You can see a student by ordering 'show_one'
    You can add a new student by ordering 'add_student'
    You can update a student' grade by ordering 'update'
    You can get the average of class by 'average_grade'
    You can close the app by ordering 'finish'
    Would you like to go on ? Yes or No : 
''')

if entrance.lower() == 'yes':
    order = True
elif entrance.lower() == 'no':
    print('Thank you, see you next time...')
else:
    input('Your request is not recognised')


students = {
    "Halit": 9,
    "Fatma": 7,
    "Tas": 8,
    "Osman": 8,
    "Altom": 7,
    "Laetitia": 7,
    "Nawal": 9,
    "Tinta": 8,
    "Erol": 6,
    "Orhan": 5
}

def show_all():
    print(students)


def show_one(name):
    print(students.get(name))


def add_student(name,grade):
    if name in students:
        print('We already have a student with this name')
        return

    if grade not in [1-10]:
        print('Level must be between 1-10')
        return

    try:
        students[name] = int(grade)
        print(f"{name} is added with grade {students.get(name)}")
    except ValueError:
        print('Please type a number as a level')

def update (name, grade):

    if grade not in [1 - 10]:
        print('Level must be between 1-10')
        return
    try:
        students[name] = int(grade)
        print(f"{name}'s grade is updated as {students.get(name)}")
    except ValueError:
        print('Please type a number as a level')


def get_avg ():
    avg = sum(students.values())/len(students)
    print(f'Average grade of class is {avg}')

def finish ():
    global order
    order = False
    print("Thank You, See you next time")

reducer = {
    'show_all': show_all,
    'show_one': show_one,
    'add_student':add_student,
    'update': update,
    'average_grade': get_avg,
    'finish': finish
}

while order:
    msg = input('request:  ')
    my_function = reducer.get(msg, 'error')
    if msg == 'show_one':
        name = input('name:  ')
        my_function(name)
    elif msg in {'update', 'add_student'}:
        name = input('name:  ')
        grade = input('grade:  ')
        my_function(name, grade)
    elif msg in {'show_all', 'finish', 'average_grade'}:
        my_function()
    else : print ('Request is not recognised')
