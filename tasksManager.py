def getUserInput():
  optionSelected =  input(f"===To Do List===\n1.Add Tasks\n2.Show Tasks\n3.Mark As Done\n4.Exit\n")
  return optionSelected
def isValidOptionSelected(formattedUserSelection):
  if(formattedUserSelection==None or formattedUserSelection>=5 or formattedUserSelection<1):
      return False
  else:
      return True
def formatInputToInteger(input):
    try:
       return int(input)
    except ValueError:
        return None
def addNewTasks():
    taskToAdd = input("Enter the new task to be added:")
    task_list.append(taskToAdd)
def displayTasks():
    if(len(task_list)==0):
        print("No tasks to be displayed.Add a task to display")
        return
    print("Displaying task list:")
    counter =1
    for task in task_list:
        print(f"{counter}: {task}")
        counter+=1
def markTasksAsDone():
    if(len(task_list)==0):
        print("No tasks to be processed. Add a task")
        return   
    taskToBeMarked = input("Enter the task number to be marked as done:")
    optionSelected = formatInputToInteger(taskToBeMarked)
    if(optionSelected==None or optionSelected>len(task_list)):
        print("Enter valid task number")
    elif(task_list[optionSelected-1].endswith("-Done")):
        print("Task is already completed")
    else:
        task_list[optionSelected-1]= task_list[optionSelected-1] + "-Done"
        displayTasks()
task_list = []
while(True):
        userSelection = getUserInput()
        formattedUserSelection= formatInputToInteger(userSelection)
        if(isValidOptionSelected(formattedUserSelection) == False):
            print("Invalid Input option entered. Choose a valid option")
            continue
        else:
           if(formattedUserSelection == 1):
               addNewTasks()
           elif(formattedUserSelection == 2):
                displayTasks()
           elif(formattedUserSelection == 3):
                markTasksAsDone()
           else:
                break
   




