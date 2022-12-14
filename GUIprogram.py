from tkinter import *
from tkinter import messagebox

def reset_entry():
    txt1.delete(0,'end')
    txt2.delete(0,'end')
    txt3.delete(0,'end')     # This is a function to reset all the input fields so that the user can clear the data and continue using the widget.
    #female.deselect()
    #male.deselect()
    vars.set(None)
   
    

def calculate_bmi():
    kg = float(txt2.get())
    m = float(txt3.get())
    bmi = kg/(m*m)
    bmi = round(bmi, 1)     # This is a function where bmi is being calculated.
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):                                             # Thus is a function to display the BMI ranges in a messagebox.
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')   

    

root =Tk()
root.title("BMI CALCULATOR")      # title of the widget
root.geometry('400x250')        # size of the widget
root.configure(bg='light blue')   # background color
vars = IntVar()
gender_lbl = Label(root,text='Select Gender')                        #  defining label displaying text select gender
male = Radiobutton(root,text='Male',variable=vars,value=1)
female = Radiobutton(root,text='Female',variable=vars,value=2)       # defining 2 radio buttons to select gender from ( only one can be selected at a time)
gender_lbl.grid(column= 0, row =0)
male.grid(column =1, row =0)
female.grid(column = 2, row =0)        # defining the position of the label and radio buttons on the grid


lbl = Label(root,text = "Enter Age")
lbl.grid(column = 0,row = 3,pady =10)        
txt1 =Entry(root,width =15)
txt1.grid(column =1, row =3,pady=10)
lbl1 = Label(root,text = "Enter your weight(kg)")
lbl1.grid(column = 0, row =5, pady=10)                       # defining labels of enter weight, age and height with text and position on the grid.
txt2 =Entry(root,width =15)
txt2.grid(column =1, row =5)
lbl2 = Label(root,text = "Enter your height(m)")
lbl2.grid(column = 0, row =7,pady =15)
txt3 =Entry(root,width =15)
txt3.grid(column =1, row =7)
calbutton =Button(root,text = "Calculate", command =calculate_bmi)
calbutton.grid(column=0, row = 11,pady=15)                                   # defining three buttons of reset, exit and calculate. Each is associated with their respective functions.
resetbutton =Button(root,text = "Reset",command=reset_entry)                 # When pressed, the button will call/execute their respective functions of reset, calculate bmi and exit program
resetbutton.grid(column=1, row = 11,pady=15)
exitbutton =Button(root,text = "Exit",command=lambda:root.destroy())
exitbutton.grid(column=2, row = 11,pady=15 )



root.mainloop()
