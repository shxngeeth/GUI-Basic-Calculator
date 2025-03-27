import tkinter as tk
from tkinter import messagebox as msg, Label

calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol) #it will type caste into string even if its integer or in any other data types then it will append whichever we do button click
    text_result.delete(1.0,"end") # to delete everything in the text field and indexation 1.0 to end is for deleting the whole content(end ensures everything is deleted)
    text_result.insert(1.0,calculation)  #this will insert the updated calculation to the calculator display

def evaluate_calculation():
    global calculation         # declared calculation as global variable to manipulate outside of function
    if calculation.startswith("+") or calculation.startswith("-") or calculation.startswith("/") or calculation.startswith("*") or calculation.startswith("="):
        msg.showerror("Operator error","Equation cannot starts with operator")
        calculation=''
        text_result.delete(1.0,'end')
    else:
        try:
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except ZeroDivisionError:
            clear_field()  # if any error happen it will clear all
            msg.showerror('zero div error','can not divide by zero')
            text_result.insert(1.0, "Error!")  # after erasing it will display Error!

def clear_field():
    global calculation  #this function will delete everything and reset whatever in display why user press CE key
    calculation=""
    text_result.delete(1.0,"end")

root=tk.Tk()    #created the object
root.title("15139531_Shangeeth_GUIBasicCalculator")  #this will give calculator window name
root.configure(bg='#DFFFD6')  #This will give a background color #E3F2FD
root.geometry("300x305")   #this will create the size of window
text_result=tk.Text(root,height=2,width=16,font=("Arial",24)) # part of it(root) and declared it sizes and font
text_result.grid(columnspan=5) # used this to have a grid structure of 5 columns

# down below we put root cuz part of window, or we are adding the button to root
#command lambda expression is without immediately calling function it will refer to function
btn_1=tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14))
btn_1.grid(row=2, column=1) # we specified this in 2nd row cuz we have text box in first row
btn_2=tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial",14))
btn_2.grid(row=2, column=2)
btn_3=tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial",14))
btn_3.grid(row=2, column=3)

#buttons in 3rd row
btn_4=tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial",14))
btn_4.grid(row=3, column=1)
btn_5=tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial",14))
btn_5.grid(row=3, column=2)
btn_6=tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial",14))
btn_6.grid(row=3, column=3)

#buttons in 4th row
btn_7=tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial",14))
btn_7.grid(row=4, column=1)
btn_8=tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial",14))
btn_8.grid(row=4, column=2)
btn_9=tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial",14))
btn_9.grid(row=4, column=3)

btn_0=tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial",14))
btn_0.grid(row=5, column=2)
btn_openbra=tk.Button(root, text="(", command=lambda: add_to_calculation('('), width=5, font=("Arial",14))
btn_openbra.grid(row=5, column=1)
btn_closebra=tk.Button(root, text=")", command=lambda: add_to_calculation(')'), width=5, font=("Arial",14))
btn_closebra.grid(row=5, column=3)

#Symbol buttons in column 4
btn_plus=tk.Button(root, text="+", command=lambda: add_to_calculation('+'), width=5, font=("Arial",14))
btn_plus.grid(row=2, column=4)
btn_minus=tk.Button(root, text="-", command=lambda: add_to_calculation('-'), width=5, font=("Arial",14))
btn_minus.grid(row=3, column=4)
btn_div=tk.Button(root, text="/", command=lambda: add_to_calculation('/'), width=5, font=("Arial",14))
btn_div.grid(row=4, column=4)
btn_mul=tk.Button(root, text="x", command=lambda: add_to_calculation('*'), width=5, font=("Arial",14))
btn_mul.grid(row=5, column=4)

btn_equals=tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial",14), bg="#FF4C4C")
btn_equals.grid(row=6, column=3, columnspan=2) # increased the width to 11 and used columnspan for balanced and better User Interface(UI)
btn_dot=tk.Button(root, text=".", command=lambda: add_to_calculation('.'), width=5, font=("Arial",14))
btn_dot.grid(row=6, column=2)
btn_clear=tk.Button(root, text="CE", command=clear_field , width=5, font=("Arial",14), bg="#32CD32")
btn_clear.grid(row=6, column=1)

lblStyle=Label(root,text='Basic Calculator ©Shangeeth', bg='#DFFFD6', fg='#555555', font=("Arial", 10, "italic"))
lblStyle.grid(row=7, column=0, columnspan=5, pady=10)
root.mainloop()  #run mainloop