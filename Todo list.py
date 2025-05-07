
print("Hello Alston!")
tasks=[ ]
def todo():

 app=["Add Task or 1","View Tasks or 2","Remove Tasks or 3"]
 print(app)
 chose=input("Choose one which you want to do either words or numbers: ")
 if chose == "Add Task"or "1":
    t=input("What do you want to do? ")
    tasks.append(t)
    dec=input("Do you want to add more task? ")
    if dec== "Yes":
      t=input("What do you want to do? ")
      tasks.append(t)
    while dec=="Yes":
      dec=input("Do you want to add more task? ")
      if dec== "Yes":
       t=input("What do you want to do? ")
       tasks.append(t)
    else:
     print(tasks)   
     exit()
 elif chose== "View Tasks" or "2":
    print(tasks)
 elif chose =="Remove Tasks" or "3":
    print(tasks)
    rem= input("Select the task you want to remove: ")
    tasks.remove(rem)
print(todo())
de= input("Do you want anything else? ")
if(de=="Yes"):
  todo()
elif de=="No":
  exit()
   