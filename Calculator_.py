from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("360x444")
window.resizable(False, False)


def con_one():
        
        if result['text'] == '0':
            result.configure(text='1')
        else :
            result.configure(text= result['text'] + '1')

def con_two():
    if result['text'] == '0':
        result.configure(text='2')
    else :
        result.configure(text= result['text'] + '2')

def con_three():
    if result['text'] == '0':
        result.configure(text='3')
    else :
        result.configure(text= result['text'] + '3')

def con_four():
    if result['text'] == '0':
        result.configure(text='4')
    else :
        result.configure(text= result['text'] + '4')

def con_five():
    if result['text'] == '0':
        result.configure(text='5')
    else :
        result.configure(text= result['text'] + '5')

def con_six():
    if result['text'] == '0':
        result.configure(text='6')
    else :
        result.configure(text= result['text'] + '6')

def con_seven():
    if result['text'] == '0':
        result.configure(text='7')
    else :
        result.configure(text= result['text'] + '7')

def con_eight():
    if result['text'] == '0':
        result.configure(text='8')
    else :
        result.configure(text= result['text'] + '8')

def con_nine():
    if result['text'] == '0':
        result.configure(text='9')
    else :
        result.configure(text= result['text'] + '9')

def con_zero():
    if result['text'] == '0':
        result.configure(text='0')
    else :
        result.configure(text= result['text'] + '0')

def con_plus():
        result.configure(text= result['text'] + '+')

def con_minus():
        result.configure(text= result['text'] + '-')

def con_multiply():
        result.configure(text= result['text'] + '*')

def con_divide():
        result.configure(text= result['text'] + '/')

def con_bracket_open():
    if result['text'] == '0':
        result.configure(text='(')
    else :
        result.configure(text= result['text'] + '(')

def con_bracket_close():
    if result['text'] == '0':
        result.configure(text='0')
    else :
        result.configure(text= result['text'] + ')')

def clear_everything():
    if result['text'] == '0':
        result.configure(text='0')
    else :
        result.configure(text= '0')

def plus_minus():
    try:
        num = int(result['text'])
        result.configure(text = str(-num))
    except Exception as e:
        result.configure(text = "Error")
      

def back():
    if len(result['text']) == 1:
        result.configure(text = "0") 
    else:
        lst = list(result['text'])
        lst.pop()
        new_text = "".join(lst)
        result.configure(text = new_text)

def sqr():
    try:
        squared = (float(result['text']))**2
        if len(str(squared)) <= 14:
            result.configure(text = str(squared))
        else:
            result.configure(text = "Number too big")    
    except Exception as e:
        result.configure(text = "Error")
      

def sqrt():
    try:
        root_squared = float((float(result['text']))**0.5)
        if len(str(root_squared)) <= 14:
            result.configure(text = str(root_squared))
        else:
            root_squared = round(root_squared, 10)    
            result.configure(text = str(root_squared))

    except Exception as e:
        result.configure(text = "Error")
      

def decimal():
    if "." in result['text']:
        result.configure(text = result['text'])
    else:
        result.configure(text = result['text'] + ".")    

def cube():

    try:
        cubed = (float(result['text']))**2
        if len(str(cubed)) <= 14:
            result.configure(text = str(cubed))
        else:
            result.configure(text = "Number too big")    
    except Exception as e:
        result.configure(text = "Error")
      


def evaluate():
    try:
        result.configure(text=str(eval(result['text'])))
    except Exception as e:
        result.configure(text = "Error")
      


result = Label( window, text = "0", pady = 20 , font = ("courier", 25))
result.grid(column = 0 , row = 0 , columnspan= 4)


cube = Button( window , height= 3 ,width= 10 , text="x³", cursor='circle', font=("", 10))
cube.grid(column=0,row=1)

ce = Button( window , height= 3 ,width= 10 , text="CE", cursor='circle', font=("", 10), command=clear_everything)
ce.grid(column=1,row=1)

plus_minus = Button( window , height= 3 ,width= 10 , text="+/-", cursor='circle', font=("", 10), command=plus_minus)
plus_minus.grid(column=2,row=1)

back = Button( window , height= 3 ,width= 10 , text="⌫", cursor='circle', font=("", 10), command=back)
back.grid(column=3,row=1)

sqr = Button( window , height= 3 ,width= 10 , text="x²", cursor='circle' , font=("", 10), command=sqr)
sqr.grid(column=0,row=2)

sqrt = Button( window , height= 3 ,width= 10 , text="√x", cursor='circle', font=("", 10), command=sqrt)
sqrt.grid(column=1,row=2)

multiply = Button( window , height= 3 ,width= 10 , text="✱", cursor='circle', font=("", 10), command=con_multiply)
multiply.grid(column=2,row=2)

divide = Button( window , height= 3 ,width= 10 , text="/", cursor='circle', font=("", 10), command= con_divide)
divide.grid(column=3,row=2)

seven = Button( window , height= 3 ,width= 10 , text="7", cursor='circle' , font=("", 10), command=con_seven, bg="light grey")
seven.grid(column=0,row=3)

eight = Button( window , height= 3 ,width= 10 , text="8", cursor='circle', font=("", 10), command= con_eight, bg="light grey")
eight.grid(column=1,row=3)

nine = Button( window , height= 3 ,width= 10 , text="9", cursor='circle', font=("", 10), command= con_nine, bg="light grey")
nine.grid(column=2,row=3)

plus = Button( window , height= 3 ,width= 10 , text="+", cursor='circle', font=("", 10), command= con_plus)
plus.grid(column=3,row=3)

four = Button( window , height= 3 ,width= 10 , text="4", cursor='circle' , font=("", 10), command= con_four, bg="light grey")
four.grid(column=0,row=4)

five = Button( window , height= 3 ,width= 10 , text="5", cursor='circle', font=("", 10), command= con_five, bg="light grey")
five.grid(column=1,row=4)

six = Button( window , height= 3 ,width= 10 , text="6", cursor='circle', font=("", 10), command= con_six, bg="light grey")
six.grid(column=2,row=4)

minus = Button( window , height= 3 ,width= 10 , text="—", cursor='circle', font=("", 10), command= con_minus)
minus.grid(column=3,row=4)

one = Button( window , height= 3 ,width= 10 , text="1", cursor='circle' , font=("", 10), command=con_one, bg="light grey")
one.grid(column=0,row=5)

two = Button( window , height= 3 ,width= 10 , text="2", cursor='circle', font=("", 10), command= con_two, bg="light grey")
two.grid(column=1,row=5)

three = Button( window , height= 3 ,width= 10 , text="3", cursor='circle', font=("", 10), command= con_three, bg="light grey")
three.grid(column=2,row=5)

decimal = Button( window , height= 3 ,width= 10 , text="•", cursor='circle', font=("", 10), bg="light grey", command=decimal)
decimal.grid(column=2,row=6)

zero = Button( window , height= 3 ,width= 21 , text="0", cursor='circle', font=("", 10), command= con_zero, bg="light grey")
zero.grid(column=0,row=6, columnspan=2)

equal = Button( window , height= 7 ,width= 10 , text="=", cursor='circle', font=("", 10), fg = "black", bg="light green", command=evaluate)
equal.grid(column=3,row=5,rowspan=2)

window.mainloop()