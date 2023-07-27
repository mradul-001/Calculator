import customtkinter as ctk

window = ctk.CTk()
window.title("Calculator")
window.geometry("360x439")
window.resizable(False, False)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")


def con_one():
        
        if result.cget("text") == '0':
            result.configure(text='1')
        else :
            result.configure(text= result.cget("text") + '1')

def con_two():
    if result.cget("text") == '0':
        result.configure(text='2')
    else :
        result.configure(text= result.cget("text") + '2')

def con_three():
    if result.cget("text") == '0':
        result.configure(text='3')
    else :
        result.configure(text= result.cget("text") + '3')

def con_four():
    if result.cget("text") == '0':
        result.configure(text='4')
    else :
        result.configure(text= result.cget("text") + '4')

def con_five():
    if result.cget("text") == '0':
        result.configure(text='5')
    else :
        result.configure(text= result.cget("text") + '5')

def con_six():
    if result.cget("text") == '0':
        result.configure(text='6')
    else :
        result.configure(text= result.cget("text") + '6')

def con_seven():
    if result.cget("text") == '0':
        result.configure(text='7')
    else :
        result.configure(text= result.cget("text") + '7')

def con_eight():
    if result.cget("text") == '0':
        result.configure(text='8')
    else :
        result.configure(text= result.cget("text") + '8')

def con_nine():
    if result.cget("text") == '0':
        result.configure(text='9')
    else :
        result.configure(text= result.cget("text") + '9')

def con_zero():
    if result.cget("text") == '0':
        result.configure(text='0')
    else :
        result.configure(text= result.cget("text") + '0')

def con_plus():
        result.configure(text= result.cget("text") + '+')

def con_minus():
        result.configure(text= result.cget("text") + '-')

def con_multiply():
        result.configure(text= result.cget("text") + '*')

def con_divide():
        result.configure(text= result.cget("text") + '/')

def con_bracket_open():
    if result.cget("text") == '0':
        result.configure(text='(')
    else :
        result.configure(text= result.cget("text") + '(')

def con_bracket_close():
    if result.cget("text") == '0':
        result.configure(text='0')
    else :
        result.configure(text= result.cget("text") + ')')

def clear_everything():
    if result.cget("text") == '0':
        result.configure(text='0')
    else :
        result.configure(text= '0')

def plus_minus():
    try:
        num = int(result.cget("text"))
        result.configure(text = str(-num))
    except Exception as e:
        result.configure(text = "Error")
      

def back():
    if len(result.cget("text")) == 1:
        result.configure(text = "0") 
    else:
        lst = list(result.cget("text"))
        lst.pop()
        new_text = "".join(lst)
        result.configure(text = new_text)

def sqr():
    try:
        squared = (float(result.cget("text")))**2
        if len(str(squared)) <= 14:
            result.configure(text = str(squared))
        else:
            result.configure(text = "Number too big")    
    except Exception as e:
        result.configure(text = "Error")
      

def sqrt():
    try:
        root_squared = float((float(result.cget("text")))**0.5)
        if len(str(root_squared)) <= 14:
            result.configure(text = str(root_squared))
        else:
            root_squared = round(root_squared, 10)    
            result.configure(text = str(root_squared))

    except Exception as e:
        result.configure(text = "Error")
      

def decimal():
    if "." in result.cget("text"):
        result.configure(text = result.cget("text"))
    else:
        result.configure(text = result.cget("text") + ".")    

def cube():

    try:
        cubed = (float(result.cget("text")))**3
        if len(str(cubed)) <= 14:
            result.configure(text = str(cubed))
        else:
            result.configure(text = "Number too big")    
    except Exception as e:
        result.configure(text = "Error")
      


def evaluate():
    try:
        result.configure(text=str(eval(result.cget("text"))))
    except Exception as e:
        result.configure(text = "Error")
      


result = ctk.CTkLabel( window, 
                      text = "0", 
                      pady = 25 , 
                      font = ("courier", 25), 
                      fg_color= "transparent", 
                      width = 360,
                      )
result.grid(column = 0 , row = 0 , columnspan= 4)


cube = ctk.CTkButton( window , height= 60 ,width= 90 , text="x³", font=("", 20), corner_radius=0 ,fg_color= ("white","gray16") , command= cube, text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
cube.grid(column=0,row=1)

ce = ctk.CTkButton( window , height= 60 ,width= 90 , text="CE",  font=("", 15), corner_radius=0, command=clear_everything ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
ce.grid(column=1,row=1)

plus_minus = ctk.CTkButton( window , height= 60 ,width= 90 , text="+/-", font=("", 20), corner_radius=0  , command=plus_minus ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
plus_minus.grid(column=2,row=1)

back = ctk.CTkButton( window , height= 60 ,width= 90 , text="⌫", font=("", 15), corner_radius=0  , command=back ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
back.grid(column=3,row=1)

sqr = ctk.CTkButton( window , height= 60 ,width= 90 , text="x²",font=("", 20), corner_radius=0  , command=sqr ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
sqr.grid(column=0,row=2)

sqrt = ctk.CTkButton( window , height= 60 ,width= 90 , text="√x", font=("", 20), corner_radius=0  , command=sqrt ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
sqrt.grid(column=1,row=2)

multiply = ctk.CTkButton( window , height= 60 ,width= 90 , text="✕", font=("", 20), corner_radius=0  , command=con_multiply ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
multiply.grid(column=2,row=2)

divide = ctk.CTkButton( window , height= 60 ,width= 90 , text="/", font=("", 20), corner_radius=0  , command= con_divide ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
divide.grid(column=3,row=2)

seven = ctk.CTkButton( window , height= 60 ,width= 90 , text="7", font=("", 20), corner_radius=0  , command=con_seven ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
seven.grid(column=0,row=3)

eight = ctk.CTkButton( window , height= 60 ,width= 90 , text="8",  font=("", 20), corner_radius=0  , command= con_eight ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
eight.grid(column=1,row=3)

nine = ctk.CTkButton( window , height= 60 ,width= 90 , text="9",  font=("", 20), corner_radius=0  , command= con_nine ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
nine.grid(column=2,row=3)

plus = ctk.CTkButton( window , height= 60 ,width= 90 , text="+", font=("", 20), corner_radius=0  , command= con_plus ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
plus.grid(column=3,row=3)

four = ctk.CTkButton( window , height= 60 ,width= 90 , text="4", font=("", 20), corner_radius=0  , command= con_four ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
four.grid(column=0,row=4)

five = ctk.CTkButton( window , height= 60 ,width= 90 , text="5", font=("", 20), corner_radius=0  , command= con_five ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
five.grid(column=1,row=4)

six = ctk.CTkButton( window , height= 60 ,width= 90 , text="6",  font=("", 20), corner_radius=0  , command= con_six ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
six.grid(column=2,row=4)

minus = ctk.CTkButton( window , height= 60 ,width= 90 , text="-",  font=("", 20), corner_radius=0  , command= con_minus ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
minus.grid(column=3,row=4)

one = ctk.CTkButton( window , height= 60 ,width= 90 , text="1", font=("", 20), corner_radius=0  , command=con_one ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
one.grid(column=0,row=5)

two = ctk.CTkButton( window , height= 60 ,width= 90 , text="2", font=("", 20), corner_radius=0  , command= con_two ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
two.grid(column=1,row=5)

three = ctk.CTkButton( window , height= 60 ,width= 90 , text="3",  font=("", 20), corner_radius=0  , command= con_three ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
three.grid(column=2,row=5)

decimal = ctk.CTkButton( window , height= 60 ,width= 90 , text="•",  font=("", 20), corner_radius=0  , command=decimal ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
decimal.grid(column=2,row=6)

zero = ctk.CTkButton( window , height= 60 ,width= 180 , text="0",  font=("", 20), corner_radius=0  , command= con_zero ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
zero.grid(column=0,row=6, columnspan=2)

equal = ctk.CTkButton( window , height= 120 ,width= 90 , text="=",  font=("", 20), corner_radius=0  , command=evaluate ,fg_color= ("white","gray16"), text_color = ("gray20", "white"), hover_color = ("OliveDrab1", "Dodgerblue2"))
equal.grid(column=3,row=5,rowspan=2)

window.mainloop()