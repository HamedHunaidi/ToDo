import customtkinter


root = customtkinter.CTk()
root.title("To Do")
root.geometry("400x400")
root.resizable(False, False)


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
    global checkbox1
    checkbox1 = customtkinter.CTkCheckBox(frame2, text=" Wash yo car")
    checkbox1.pack()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Today's To Do list!")
label.pack(pady=12, padx=10)

frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=12, padx=10)


button1 = customtkinter.CTkButton(master=frame, text=" Add a new task!", command=popup)
button1.pack(pady=12, padx=10)


root.mainloop()
