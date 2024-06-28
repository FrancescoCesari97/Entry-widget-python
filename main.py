
# * entry widget = textbox that accepts a single line of user input

# from tkinter import *

# def submit():
#     username = entry.get()
#     print(f"Welcome {username}")
#     entry.config(state=DISABLED)

# def delete():
#     entry.delete(0, END)

# def backspace():
#     entry.delete(len(entry.get()) - 1, END)

# window = Tk()

# entry = Entry(window,
#               font=("Arial", 30),
#               show="*")
# entry.insert(0, 'type here')
# entry.pack(side=LEFT)


# submit_button = Button(window, text="submit", command=submit)
# submit_button.pack(side=RIGHT)

# delete_button = Button(window, text="delete", command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button = Button(window, text="backspace", command=backspace)
# backspace_button.pack(side=RIGHT)


# window.mainloop()


# * checkbox 

# from tkinter import *


# def display():
#     if(x.get()==1):
#         print("You agree!")
#         check_buton.config(fg='green', activeforeground='green')
#     else:
#         print("You don't agree :(")
#         check_buton.config(fg='red', activeforeground='red')
        
# window = Tk()

# x = IntVar()

# check_buton = Checkbutton(window,
#                           text="I agree to something",
#                           variable=x,
#                           onvalue=1,
#                           offvalue=0,
#                           command=display,
#                           font=("Arial", 20),
#                           activebackground='black',
#                           bg='black')
# check_buton.pack()



# window.mainloop()


# * radio buttons


from tkinter import *


food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("you selcet pizza")
    elif(x.get()==1):
        print("you select hamburger")
    else:
        print("you select hotdog")

window = Tk()

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[i],  # * adds taxt to radio buttons
                            variable = x,  # * groups radiobuttons together if they share the same variable
                            value = i,      # * assigns each radiobutton a different value
                            font= ('Arial', 25),
                            # indicatoron = 0,  # * eliminate circle indicators
                            # width= 375
                            command=order  # * set command of radiobutton to function
                            )
    radiobutton.pack(anchor=W)


window.mainloop()