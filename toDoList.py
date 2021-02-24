#toDoList
#allows user to add, remove, and view tasks

#variables and lists
taskList = []
loop = 1
add = 'x'

#functions
def menu():
    print('Choose a mode by entering a number:')
    print('1. Add a task')
    print('2. View list')
    print('3. Remove a task')
    print('4. Exit')

#def addTask():
    #add = input('Enter a task or type "done" to return to menu: ').lower()
    #if add == 'done':

    #else:
        #taskList.append(add)

def listDisplay():
    print("Here is your To Do List:")
    print(taskList)

#main routine
while True:
    menu()
    options = input()
    if options == '1':
        while add != 'done':
            add = input('Enter a task or type "done" to return to menu: ').lower()
            if add == 'done':
                continue
            else:
                taskList.append(add)
    elif options == '2':
        listDisplay()
    elif options == '3':
        print("This option isn't implemented yet!")
    elif options == '4':
        print('Goodbye!')
        exit()
    else:
        print('Please enter a number from the options.')