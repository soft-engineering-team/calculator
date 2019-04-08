import tkinter             #导入tkinter模块

root  = tkinter.Tk()        #建立窗体实例
root.minsize(280,384)       #设置窗体最小物理大小（长×高）
root.resizable(0, 0)        #设置窗体大小不可变
root.title('计算器')        #设置窗体标题属性

result = tkinter.StringVar()
result.set(0)                           #显示面板1，用于显示默认数字0
result2 = tkinter.StringVar()
result2.set('')                         #显示面板2，用于显示计算过程

label = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)       #结果显示面板1
label.place(y = 50,width = 280,height = 60)
label2 = tkinter.Label(root,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)   #结果显示面板2
label2.place(width = 280,height = 50)

#数字按钮7、8、9
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('7'))
btn7.place(x = 0,y = 165,width = 70,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('8'))
btn8.place(x = 70,y = 165,width = 70,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('9'))
btn9.place(x = 140,y = 165,width = 70,height = 55)

#数字按钮4、5、6
btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('4'))
btn4.place(x = 0,y = 220,width = 70,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('5'))
btn5.place(x = 70,y = 220,width = 70,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('6'))
btn6.place(x = 140,y = 220,width = 70,height = 55)

#数字按钮1、2、3
btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('1'))
btn1.place(x = 0,y = 275,width = 70,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('2'))
btn2.place(x = 70,y = 275,width = 70,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('3'))
btn3.place(x = 140,y = 275,width = 70,height = 55)

#数字按钮0
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : pressNum('0'))
btn0.place(x = 0,y = 330,width = 70,height = 55)

#运算符按钮AC、←、^、/、*、-、+、=、.、(、)
btnac = tkinter.Button(root,text = 'AC',font = ('微软雅黑',20),fg = 'orange',bd = 0.5,command = lambda :pressCompute('AC'))
btnac.place(x = 0,y = 110,width = 70,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda :pressCompute('B'))
btnback.place(x = 70,y = 110,width = 70,height = 55)
btndivi = tkinter.Button(root,text = '^',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda :pressCompute('**'))
btndivi.place(x = 140,y = 110,width = 70,height = 55)
btnmul = tkinter.Button(root,text ='÷',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda :pressCompute('/'))
btnmul.place(x = 210,y = 110,width = 70,height = 55)
btnsub = tkinter.Button(root,text = '×',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute('*'))
btnsub.place(x = 210,y = 165,width = 70,height = 55)
btnadd = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute('-'))
btnadd.place(x = 210,y = 220,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute('+'))
btnequ.place(x = 210,y = 275,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '=',font = ('微软雅黑',20),fg = ('white'),bd = 0.5,command = lambda :pressEqual(),bg = 'orange')
btnequ.place(x = 210,y = 330,width = 70,height = 55)
btnper = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute('.'))
btnper.place(x = 70,y = 330,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '(',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute('('))
btnpoint.place(x = 140,y = 330,width = 35,height = 55)
btnpoint = tkinter.Button(root,text = ')',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressCompute(')'))
btnpoint.place(x = 175,y = 330,width = 35,height = 55)

#设置参数
lists = []                            #设置一个变量，保存运算数字和符号的列表
isPressSign = False                  #添加一个判断是否按下运算符的标志,假设默认没有按下按钮

#数字函数
def pressNum(num):                   #设置一个数字函数，判断是否按下数字，并获取数字将数字写在结果显示面板上
    global lists                     #全局化lists和按钮状态isPressSign
    global isPressSign
    if isPressSign == False:
        pass
    else:                            #重新将运算符号状态设置为否
        result.set(0)
        isPressSign = False

    #判断界面的数字是否为0
    oldnum = result.get()              #获取数字
    if oldnum =='0':                  #如果界面上的数字是0，则获取按下的数字
        result.set(num)
    else:                             #如果界面上的数字不是0，则链接上新按下的数字
        newnum = oldnum + num
        result.set(newnum)            #将按下的数字写到面板中

#运算函数
def pressCompute(sign):
    global lists
    global isPressSign
    lists.append(result.get())         # 保存界面数字到列表中
    result.set('')
    lists.append(sign)                 # 将按下的运算符号保存到列表中
    isPressSign = True
    if sign =='AC':                     #如果按下的是‘AC’按键，则清空列表内容，讲屏幕上的数字键设置为默认数字0
        result.set(0)
        result2.set('')
        lists.clear()
    if sign =='B':                      #如果按下的是退格‘Backspace’，则选取当前数字第一位到倒数第二位
        result.set(str(result.get()[:-1]))

#获取运算结果函数
def pressEqual():
    global lists
    global isPressSign
    try:
        curnum = result.get()           #设置当前数字变量，并获取添加到列表
        lists.append(curnum)
        computrStr = ''.join(lists)     #将列表内容用join命令将字符串链接起来
        endNum = eval(computrStr)       #用eval命令运算字符串中的内容
        a = str(endNum)
#       b = '='+a                       #在运算结果前添加一个‘=’，但是这样会出现BUG，不能进行连续运算，所以这里注释掉，不要‘=’
        c = a[0:12]                     #所有的运算结果取10位数
        result.set(c)                   #讲运算结果显示到屏幕1
        result2.set(computrStr)         #将运算过程显示到屏幕2
        lists.clear()                   #清空列表内容
    except ZeroDivisionError:           #除零异常
        result2.set(lists)
        result.set('VALUE ERROR')
    except SyntaxError:                 #格式异常
        result2.set(lists)
        result.set('FORMAT ERROR')
    except IndexError:                  #参数异常
        result2.set(lists)
        result.set('INDEX ERROR')
    except :                            #异常
        result2.set(lists)
        result.set('ERROR')

root.mainloop()                          #启动窗体运行，并等待接收各种事件信息
