from tkinter import *


window = Tk()

window.title("Calculator")
window.geometry("412x336")
window.resizable(False,False)



def con_one():
    if answer['text'] == '0':
        answer.configure(text='1')
    else :
        answer.configure(text= answer['text'] + '1')




def con_two():
    if answer['text'] == '0':
        answer.configure(text='2')
    else :
        answer.configure(text= answer['text'] + '2')




def con_three():
    if answer['text'] == '0':
        answer.configure(text='3')
    else :
        answer.configure(text= answer['text'] + '3')




def con_four():
    if answer['text'] == '0':
        answer.configure(text='4')
    else :
        answer.configure(text= answer['text'] + '4')



def con_five():
    if answer['text'] == '0':
        answer.configure(text='5')
    else :
        answer.configure(text= answer['text'] + '5')



def con_six():
    if answer['text'] == '0':
        answer.configure(text='6')
    else :
        answer.configure(text= answer['text'] + '6')



def con_seven():
    if answer['text'] == '0':
        answer.configure(text='7')
    else :
        answer.configure(text= answer['text'] + '7')



def con_eight():
    if answer['text'] == '0':
        answer.configure(text='8')
    else :
        answer.configure(text= answer['text'] + '8')




def con_nine():
    if answer['text'] == '0':
        answer.configure(text='9')
    else :
        answer.configure(text= answer['text'] + '9')




def con_zero():
    if answer['text'] == '0':
        answer.configure(text='0')
    else :
        answer.configure(text= answer['text'] + '0')



def con_plus():
    # if answer['text'] == '0':
    #     answer.configure(text='+')
    # else :
        answer.configure(text= answer['text'] + '+')


def con_minus():
    # if answer['text'] == '0':
    #     answer.configure(text='9')
    # else :
        answer.configure(text= answer['text'] + '-')



def con_multiply():
    # if answer['text'] == '0':
    #     answer.configure(text='9')
    # else :
        answer.configure(text= answer['text'] + '*')



def con_divide():
    # if answer['text'] == '0':
    #     answer.configure(text='9')
    # else :
        answer.configure(text= answer['text'] + '/')




def con_bracket_open():
    if answer['text'] == '0':
        answer.configure(text='(')
    else :
        answer.configure(text= answer['text'] + '(')



def con_bracket_close():
    if answer['text'] == '0':
        answer.configure(text='0')
    else :
        answer.configure(text= answer['text'] + ')')




def con_all_clear():
    if answer['text'] == '0':
        answer.configure(text='0')
    else :
        answer.configure(text= '0')



def evaluate():
    answer.configure(text=str(eval(answer['text'])))




answer = Label( window , font = ('courier', 15) , text = "0" , pady = 15)
answer.pack(side = TOP)
answer.grid(column=0 , row=0 , columnspan=4)





all_clear = Button( window , height = 3 , width = 29 , text="AC" , cursor='circle' , command=con_all_clear)
all_clear.grid(column = 0 , row = 1 , columnspan= 2)

equal = Button( window , height = 3 , width = 27 , text="=", cursor='circle' , command= evaluate)
equal.grid(column = 2 , row = 1 , columnspan= 2)





nine = Button( window , height= 3 ,width= 14 , text="9", cursor='circle' , command=con_nine)
nine.grid(column=0,row=2)

eight = Button( window , height= 3 ,width= 13 , text="8", cursor='circle' , command=con_eight)
eight.grid(column=1,row=2)

seven = Button( window , height= 3 ,width= 13 , text="7", cursor='circle' , command=con_seven)
seven.grid(column=2,row=2)

divide = Button( window , height= 3 ,width= 13 , text="/", cursor='circle', command=con_divide)
divide.grid(column=3,row=2)






six = Button( window , height= 3 ,width= 14 , text="6", cursor='circle' , command=con_six)
six.grid(column=0,row=3)

five = Button( window , height= 3 ,width= 13 , text="5", cursor='circle' , command=con_five)
five.grid(column=1,row=3)

four = Button( window , height= 3 ,width= 13 , text="4", cursor='circle' , command= con_four)
four.grid(column=2,row=3)

multiply = Button( window , height= 3 ,width= 13 , text="*", cursor='circle' , command= con_multiply) 
multiply.grid(column=3,row=3)







three = Button( window , height= 3 ,width= 14 , text="3", cursor='circle' ,command= con_three)
three.grid(column=0,row=4)

two = Button( window , height= 3 ,width= 13 , text="2", cursor='circle' , command= con_two)
two.grid(column=1,row=4)

one = Button( window , height= 3 ,width= 13 , text="1", cursor='circle' , command= con_one)
one.grid(column=2,row=4)

plus = Button( window , height= 3 ,width= 13 , text="+", cursor='circle' , command=con_plus)
plus.grid(column=3,row=4)






zero = Button( window , height= 3 ,width= 14 , text="0", cursor='circle' , command= con_zero)
zero.grid(column=0,row=5)

bracket_open = Button( window , height= 3 ,width= 13 , text="(", cursor='circle' , command= con_bracket_open)
bracket_open.grid(column=1,row=5)

bracket_close = Button( window , height= 3 ,width= 13 , text=")", cursor='circle' , command=con_bracket_close)
bracket_close.grid(column=2,row=5)

minus = Button( window , height= 3 ,width= 13 , text="-", cursor='circle' , command= con_minus)
minus.grid(column=3,row=5)






window.mainloop()


