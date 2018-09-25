print(".")
print(".")
print("Hello!, I am your task manager!")
print("--------------------------------")
print("You may enter '--QUIT' at anytime to exit the program")




class User:
    def __init__(self, first_name, last_name, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name


class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.indv_task = []
        self.task_list = []

    def task(self, title, priority):
        self.indv_task.append(title)
        self.indv_task.append(priority)
        self.add_task()
        print(self.indv_task)

    def add_task(self):
        self.task_list.append(self.task)
        print(self.task_list)



def print_list():
    print(task_list)


def remove_task():
    print(task_list)
    item_number = int(input("choose item place in list by number. First task equals number 1: "))
    task_list.remove(task_list[item_number-1])

    i = 0
    for item in task_list:
        if (i == task_list[i]):
            i = item_number
            task_list.remove(i)
            break
        i += 1



def begin():
    start = input("Enter '--BEGIN' to begin, or '--HELP' for more options: ")
    if (start.lower() == '--quit'):
        print("OK, see you soon!")
    elif (start.lower() == '--begin'):
        enter_task()
    elif (start.lower() == '--help'):
        user_options()
    else:
        print("oops, that was an invalid letter.")
        return begin()

def user_profile():
    first_name = ("Enter your first name: ")
    last_name = ("Enter your last name: ")
    user_name = ("Enter your preffered user name: ")


def new_task(title, priority):
    indv_task = []
    indv_task.append(title)
    indv_task.append(priority)
    return indv_task


def user_options():
    print("USER OPTIONS")
    print("--USER (shows user menu)")
    print("--CURRENT (shows current list)")
    print("--REMOVE (removes a task)")
    print("--ADD (adds a task)")
    print("--MODIFY (modifies a task)")
    print("--PRIORITIZE (rearranges task list based on priority)")
    print("--QUIT (exits the program)")
    choice = input("Please enter one of the options above: ")
    if (choice.lower() == "--user"):
        pass
    if (choice.lower() == "--remove"):
        remove_task()
    if (choice.lower() == "--current"):
        print_list()
    if (choice.lower() == "--add"):
        enter_task()
    if (choice.lower() == "--modify"):
        pass
    if (choice.lower() == "--prioritize"):
        pass
    if (choice.lower() == "--quit"):
        return task_list
        quit
    else:
        print("That is not a valid option, please choose again")
        user_options()


#def priority_options():




#def modify():





task_list = []


def enter_task():
    while True:
        try:
            
            #Task Title
            print("Enter your task and priority. Enter '--QUIT' at anytime to end the program.")
            print("---Task Title---")
            title = input("Enter task title: ")
            if (title.lower() == '--quit'):
                print(task_list)
                break
            if (title.lower() == "--help"):
                user_options()
                break


            #task priority
            print("---Priority levels---")
            print("1 = HIGH")
            print("2 = MODERATE")
            print("3 = LOW")
            priority = input("Enter priority of task: ")
            
            if (priority.lower() == '--quit'):
                print(task_list)
                break
            if (priority.lower() == "--help"):
                user_options()
                break

            new_task(title, priority)

            new = new_task(title, priority)

            task_list.append(new)

            print(task_list)

            end_list = input("Enter '--CONTINUE' to continue entering tasks. Type '--FINISH' to finish entering tasks: ")
            if (end_list.lower() == '--quit'):
                print(task_list)
                break
            if (end_list.lower() == "--help"):
                user_options()
                break
            if (end_list.lower() == "--finish"):
                print(task_list)
                
                return task_list
                #modify()
                break
            if (end_list.lower() == '--continue'):
                print(task_list)
            else:
                print("Rewrite task")
                enter_task()
        except:
            print("Oops, start over")
            enter_task()

begin()

user_options()
print_list()