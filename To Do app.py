import customtkinter
from CTkListbox import *
from customtkinter import END

root = customtkinter.CTk()
root.title("To Do")
root.geometry("400x500")
root.resizable(False, False)

task_list = []


def openTaskFile():
    try:
        global task_list
        with open("TaskList.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open("TaskList.txt", "w")
        file.close()


def popup():
    global pop
    global entry1
    global button2

    pop = customtkinter.CTkToplevel(root)
    pop.attributes("-topmost", True)
    pop.title("Enter New Task")
    pop.geometry("250x150")
    entry1 = customtkinter.CTkEntry(master=pop, placeholder_text="meow")
    entry1.pack(pady=12, padx=10)
    button2 = customtkinter.CTkButton(master=pop, text=" Add Task!", command=addTask)
    button2.pack(pady=12, padx=10)


def addTask():
    task = entry1.get()
    entry1.delete(0, END)

    if task:
        with open("TaskList.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Today's To Do list!")
label.pack(pady=12, padx=10)

frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=12, padx=10)
listbox = CTkListbox(frame2)
listbox.pack()

button0 = customtkinter.CTkButton(master=frame, text="Delete Task")
button0.pack(pady=12, padx=10)
button1 = customtkinter.CTkButton(master=frame, text=" Add a new task!", command=popup)
button1.pack(pady=12, padx=10)

openTaskFile()
root.mainloop()
