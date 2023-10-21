import tkinter as tk
equation = ''
global equation_result

def add_to_equation(symbol):
    global equation             #allows us to modify the variable outside the current scope
    if equation == 'ERROR':
        equation = ''              #At first without this equation is added to the string "ERROR"
        equation += str(symbol)  #It just got cleared by now😁
    else:
        equation += str(symbol)
    equation_result.config(text=equation)
        
def clear_field():
    global equation
    equation = ""
    equation_result.config(text=equation)

def evaluate_equation():
    global equation
    result = ''
    if equation != "":
        try:
            result=eval(equation)
        except:
            result = 'ERROR'
            equation = ''
        equation_result.configure(text=result)
        equation = str(result)

def delete():
    global equation
    x = equation[-1]
    equation = str(equation.replace(x,''))
    equation_result.config(text=equation)
    print(x)
    
calculator = tk.Tk()
calculator.geometry('300x350')
calculator.resizable()
equation_result=tk.Label(calculator,text='',height=2,width=18,font='Arial 24 bold',bg='black',fg='white')
equation_result.grid(columnspan=5,sticky=tk.NE)

buttons = {7:(3,0),8:(3,1),9:(3,2),'+':(3,3),
         4:(4,0),5:(4,1),6:(4,2),'-':(4,3),
         1:(5,0),2:(5,1),3:(5,2),'*':(5,3),
         '(':(6,0),0:(6,1),')':(6,2),'/':(6,3),
         '.':(7,0),'00':(7,1)
         }

for i in buttons.keys():
    j = buttons[i]
    button = tk.Button(calculator,text=str(i),width=5,font='Arial 14',command=lambda x=i: add_to_equation(x))
    button.grid(row=j[0],column=j[1])
btn_clr=button=tk.Button(calculator,text='Clr',width=12,font='Arial 14',command=clear_field)
btn_clr.grid(row=2,column=0,columnspan=2)
btn_eqls=button=tk.Button(calculator,text='=',width=12,font='Arial 14',command=evaluate_equation)
btn_eqls.grid(row=7,column=2,columnspan=2)
btn_del=button=tk.Button(calculator,text='del',width=12,font='Arial 14',command=delete)
btn_del.grid(row=2,column=2,columnspan=2)
calculator.mainloop()