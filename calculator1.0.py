from tkinter import *     #导入tkinter模块

root = Tk()         #建立窗体实例
root.title('Caculator')     #设置窗体标题属性
root.geometry('350x300')    #设置窗体物理大小（长×高）
root.resizable(0, 0)     #设置窗体大小不可变

global display
display = StringVar()

label = Label(root,relief='sunken',borderwidth=3, anchor=SE)#显示窗口
label['textvariable'] = display
label.config(bg='white', width=48, height=7)
label.grid(row=0, column=0, columnspan=5,pady=10)
positions=[(x,y) for x in range(1,6) for y in range(5)]

tests=['AC','DEL','^','/',
        '','7','8','9',
        '*','','4','5',
        '6','-','','1',
        '2','3','+','',
        '0','.','(',')'
        '','=','','']

for i in zip(tests,positions): #将两个列表并列
    text=i[0]
    row=i[1][0]
    column=i[1][1]
    if text=='AC':
        Button(root, text=text, bg='red', width=8, command=lambda text=text: clear()).grid(row=row, column=column)
    elif text=='DEL':
        Button(root, text=text, width=8, command=lambda text=text: dell()).grid(row=row, column=column)
    elif text=='=':
        Button(root, text=text, bg='orange', width=8, command=lambda text=text: calculate()).grid(row=row, column=column)
    elif text=='^':
        Button(root, text=text, width=8, command=lambda text=text: pow(text)).grid(row=row, column=column)
    elif text=='(':
        Button(root, text=text, width=8, command=lambda text=text: zuokuohao()).grid(row=row, column=column)
    elif text==')':
        Button(root, text=text, width=8, command=lambda text=text: youkuohao()).grid(row=row, column=column)
    else:
        Button(root, text=text, width=8, command=lambda text=text: userinput(text)).grid(row=row, column=column)

def userinput(text):    #按键返回函数
    content = display.get() + text
    display.set(content)

def pow(text):     #乘方函数
    display.set(text**1)

def zuokuohao():    #左括号函数
    display.set('(')

def youkuohao():    #右括号函数
    display.set(')')

def clear():   #清空函数
    display.set('')

def dell():     #删除一字符函数
    display.set(str(display.get()[:-1]))

def calculate():   #调用eval计算表达式
        num=display.get()
        res=eval(num)
        display.set(num+'\n='+str(res))

root.mainloop()     #启动窗体运行，并等待接收各种事件信息
