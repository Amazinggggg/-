# /usr/bin/python
# coding: utf-8
from 亲戚关系 import relation
from tkinter import *
import math
import os


# 按键返回函数
def call(num):
    global content2
    if num == 'sin(':
        content = display.get() + num
        content2 = content2 + 'math.sin('
        display.set(content)
    elif num == 'cos(':
            content = display.get() + num
            content2 = content2 + 'math.cos('
            display.set(content)
    elif num == 'tan(':
            content = display.get() + num
            content2 = content2 + 'math.tan('
            display.set(content)
    elif num == '^':
            content = display.get() + num
            content2 = content2 + '**'
            display.set(content)
    elif num == 'log2(':
            content = display.get() + num
            content2 = content2 + 'math.log2('
            display.set(content)
    elif num == 'log10(':
            content = display.get() + num
            content2 = content2 + 'math.log10('
            display.set(content)
    elif num == 'exp(':
            content = display.get() + num
            content2 = content2 + 'math.exp('
            display.set(content)
    elif num == 'atan(':
            content = display.get() + num
            content2 = content2 + 'math.atan('
            display.set(content)
    else:
        content = display.get() + num
        content2 = content2 + num
        display.set(content)


# 使用eval 函数计算
def calculate():
    global content2
    try:
        content = display.get()
        result = eval(content2)
        content2 = str(result)
        display.set(content + '=\n' + str(result))
    except:
        display.set('Error')

# 清空内容栏
def clear():
    display.set('')
    global content2
    content2 = ''

# 删除前一个字符
def backspace():
    display.set(str(display.get()[:-1]))
    global content2
    content2 = str(content2[:-1])

def main():
    # 定义主窗口
    global content2
    content2 = ''
    root = Tk()
    menu = Menu(root)
    menu.add_command(label='亲戚关系',command=lambda :os.system('亲戚关系.exe'))
    menu.add_command(label='性格分析',command=lambda :os.system('性格分析.exe'))
    menu.add_command(label='菜谱推荐',command=lambda :os.system('菜谱推荐.exe'))
    root.config(menu=menu)
    root.title('Calculator')
    root.geometry('400x300+300+300')
    # 将display定义成global，main() 函数外的call, calculate等可以调用
    global display
    display = StringVar()
    # 　设置内容显示栏，使用label，anchor是靠右，默认居中
    label = Label(root, relief='sunken', borderwidth=3, anchor=SE)
    label.config(bg='grey', width=55, height=3)
    label['textvariable'] = display
    label.grid(row=0, column=0, columnspan=6)

    #	text = Text(root, relief = 'sunken', borderwidth = 3)
    #	text.insert(INSERT, str(display))
    #	text.grid(row = 0, column = 0, columnspan = 4)
    # 添加各个按钮，并绑定行为,使用lambda很方便，是用的是grid布局
    Button(root, text='C', fg='#EF7321', width=3, padx=10, pady=10, command=lambda: clear()).grid(row=1, column=0)
    Button(root, text='DEL', width=3, padx=10, pady=10, command=lambda: backspace()).grid(row=1, column=1)
    Button(root, text='/', width=3, padx=10, pady=10, command=lambda: call('/')).grid(row=1, column=2)
    Button(root, text='*', width=3, padx=10, pady=10, command=lambda: call('*')).grid(row=1, column=3)
    Button(root, text='7', width=3, padx=10, pady=10, command=lambda: call('7')).grid(row=2, column=0)
    Button(root, text='8', width=3, padx=10, pady=10, command=lambda: call('8')).grid(row=2, column=1)
    Button(root, text='9', width=3, padx=10, pady=10, command=lambda: call('9')).grid(row=2, column=2)
    Button(root, text='-', width=3, padx=10, pady=10, command=lambda: call('-')).grid(row=2, column=3)
    Button(root, text='4', width=3, padx=10, pady=10, command=lambda: call('4')).grid(row=3, column=0)
    Button(root, text='5', width=3, padx=10, pady=10, command=lambda: call('5')).grid(row=3, column=1)
    Button(root, text='6', width=3, padx=10, pady=10, command=lambda: call('6')).grid(row=3, column=2)
    Button(root, text='+', width=3, padx=10, pady=10, command=lambda: call('+')).grid(row=3, column=3)
    Button(root, text='1', width=3, padx=10, pady=10, command=lambda: call('1')).grid(row=4, column=0)
    Button(root, text='2', width=3, padx=10, pady=10, command=lambda: call('2')).grid(row=4, column=1)
    Button(root, text='3', width=3, padx=10, pady=10, command=lambda: call('3')).grid(row=4, column=2)
    Button(root, text='sin(', width=3, padx=10, pady=10, command=lambda: call('sin(')).grid(row=4, column=3)
    Button(root, text='cos(', width=3, padx=10, pady=10, command=lambda: call('cos(')).grid(row=5, column=3)
    Button(root, text='tan(', width=3, padx=10, pady=10, command=lambda: call('tan(')).grid(row=5, column=4)
    Button(root, text='^', width=3, padx=10, pady=10, command=lambda: call('^')).grid(row=2, column=4)
    Button(root, text='log2(', width=3, padx=10, pady=10, command=lambda: call('log2(')).grid(row=3, column=4)
    Button(root, text='log10(', width=3, padx=10, pady=10, command=lambda: call('log10(')).grid(row=4, column=4)
    Button(root, text='(', width=3, padx=10, pady=10, command=lambda: call('(')).grid(row=1, column=4)
    Button(root, text=')', width=3, padx=10, pady=10, command=lambda: call(')')).grid(row=1, column=5)
    Button(root, text='atan(', width=3, padx=10, pady=10, command=lambda: call('atan(')).grid(row=2, column=5)
    Button(root, text='exp(', width=3, padx=10, pady=10, command=lambda: call('exp(')).grid(row=3, column=5)
    Button(root, text='=', width=3, bg='#EF7321', height=3, padx=10, pady=10, command=lambda: calculate()).grid(row=4, column=5, rowspan=2)
    Button(root, text='0', width=10, padx=10, pady=10, command=lambda: call('0')).grid(row=5, column=0, columnspan=2)
    Button(root, text='.', width=3, padx=10, pady=10, command=lambda: call('.')).grid(row=5, column=2)

    root.mainloop()

if __name__ == '__main__':
    main()

