# /usr/bin/python
# coding: utf-8

from tkinter import *


# 按键返回函数
def call1(num1):
    global qqcontent2
    if num1 == '的':
        qqcontent = display1.get() + num1
        display1.set(qqcontent)
    elif num1 == '父亲':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'f'
            display1.set(qqcontent)
    elif num1 == '母亲':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'm'
            display1.set(qqcontent)
    elif num1 == '丈夫':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'h'
            display1.set(qqcontent)
    elif num1 == '妻子':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'w'
            display1.set(qqcontent)
    elif num1 == '哥哥':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'g'
            display1.set(qqcontent)
    elif num1 == '弟弟':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'a'
            display1.set(qqcontent)
    elif num1 == '妹妹':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'q'
            display1.set(qqcontent)
    elif num1 == '儿子':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 's'
            display1.set(qqcontent)
    elif num1 == '女儿':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'd'
            display1.set(qqcontent)
    elif num1 == '姐姐':
            qqcontent = display1.get() + num1
            qqcontent2 = qqcontent2 + 'j'
            display1.set(qqcontent)


# 使用eval 函数计算
def calculate1():
    global qqcontent2
    if qqcontent2 == '':
        result = '我'
    elif qqcontent2 == 'f':
        result = '父亲'
    elif qqcontent2 == 'm'or qqcontent2=='fw' or qqcontent2=='gm' or qqcontent2=='am' or qqcontent2=='qm' or qqcontent2=='jm':
        result = '母亲'
    elif qqcontent2 == 'h'or qqcontent2=='mh' or qqcontent2=='gf' or qqcontent2=='af' or qqcontent2=='qf' or qqcontent2=='jf':
        result = '丈夫'
    elif qqcontent2 == 'w':
        result = '妻子'
    elif qqcontent2 == 's':
        result = '儿子'
    elif qqcontent2 == 'd':
        result = '女儿'
    elif qqcontent2 == 'g':
        result = '哥哥'
    elif qqcontent2 == 'a':
        result = '弟弟'
    elif qqcontent2 == 'ga':
        result = '兄弟/我'
    elif qqcontent2 == 'ag':
        result = '兄弟/我'
    elif qqcontent2 == 'j':
        result = '姐姐'
    elif qqcontent2 == 'q':
        result = '妹妹'
    elif qqcontent2 == 'jq':
        result = '姐妹/我'
    elif qqcontent2 == 'qj':
        result = '姐妹/我'
    elif qqcontent2 == 'ff':
        result = '爷爷'
    elif qqcontent2 == 'fm':
        result = '奶奶'
    elif qqcontent2 == 'mf':
        result = '姥爷'
    elif qqcontent2 == 'mm':
        result = '姥姥'
    elif qqcontent2 == 'ss':
        result = '孙子'
    elif qqcontent2 == 'sd':
        result = '孙女'
    elif qqcontent2 == 'ds':
        result = '外孙'
    elif qqcontent2 == 'dd':
        result = '外孙女'
    elif qqcontent2 == 'hf':
        result = '公公'
    elif qqcontent2 == 'hm':
        result = '婆婆'
    elif qqcontent2 == 'wf':
        result = '岳父'
    elif qqcontent2 == 'wm':
        result = '岳母'
    elif qqcontent2 == 'fg':
        result = '伯父'
    elif qqcontent2 == 'fa':
        result = '叔叔'
    elif qqcontent2 == 'fj':
        result = '姑妈'
    elif qqcontent2 == 'fq':
        result = '姑妈'
    elif qqcontent2 == 'fgw':
        result = '伯母'
    elif qqcontent2 == 'faw':
        result = '婶婶'
    elif qqcontent2 == 'fjh':
        result = '姑丈'
    elif qqcontent2 == 'fqw':
        result = '姑丈'
    elif qqcontent2 == 'fgs':
        result = '堂哥/堂弟'
    elif qqcontent2 == 'fas':
        result = '堂哥/堂弟'
    elif qqcontent2 == 'fgd':
        result = '堂姐/堂妹'
    elif qqcontent2 == 'fad':
        result = '堂姐/堂妹'
    elif qqcontent2 == 'fjs':
        result = '姑表哥/姑表弟'
    elif qqcontent2 == 'fqs':
        result = '姑表哥/姑表弟'
    elif qqcontent2 == 'fjd':
        result = '姑表姐/姑表妹'
    elif qqcontent2 == 'fqd':
        result = '姑表姐/姑表妹'
    elif qqcontent2 == 'gw':
        result = '嫂子'
    elif qqcontent2 == 'jh':
        result = '姐夫'
    elif qqcontent2 == 'aw':
        result = '弟妹'
    elif qqcontent2 == 'qh':
        result = '妹夫'
    elif qqcontent2 == 'gs':
        result = '侄子'
    elif qqcontent2 == 'gd':
        result = '侄女'
    elif qqcontent2 == 'as':
        result = '侄子'
    elif qqcontent2 == 'ad':
        result = '侄女'
    elif qqcontent2 == 'js':
        result = '外甥'
    elif qqcontent2 == 'jd':
        result = '外甥女'
    elif qqcontent2 == 'qs':
        result = '外甥'
    elif qqcontent2 == 'qd':
        result = '外甥女'
    elif qqcontent2 == 'mg':
        result = '大舅'
    elif qqcontent2 == 'ma':
        result = '小舅'
    elif qqcontent2 == 'mj':
        result = '大姨'
    elif qqcontent2 == 'mq':
        result = '小姨'
    elif qqcontent2 == 'mgw':
        result = '大舅妈'
    elif qqcontent2 == 'maw':
        result = '小舅妈'
    elif qqcontent2 == 'mjh':
        result = '大姨夫'
    elif qqcontent2 == 'mqh':
        result = '小姨夫'
    elif qqcontent2 == 'mgs':
        result = '舅表哥/舅表弟'
    elif qqcontent2 == 'mas':
        result = '舅表哥/舅表弟'
    elif qqcontent2 == 'mgd':
        result = '舅表姐/舅表妹'
    elif qqcontent2 == 'mad':
        result = '舅表姐/舅表妹'
    elif qqcontent2 == 'mjs':
        result = '姨表哥/姨表弟'
    elif qqcontent2 == 'mqs':
        result = '姨表哥/姨表弟'
    elif qqcontent2 == 'mgd':
        result = '姨表姐/姨表妹'
    elif qqcontent2 == 'mad':
        result = '姨表姐/姨表妹'
    elif qqcontent2 == 'sw':
        result = '儿媳妇'
    elif qqcontent2 == 'dh':
        result = '女婿'
    elif qqcontent2 == 'wg':
        result = '大舅哥'
    elif qqcontent2 == 'wa':
        result = '小舅子'
    elif qqcontent2 == 'wj':
        result = '大姨子'
    elif qqcontent2 == 'wq':
        result = '小姨子'
    elif qqcontent2 == 'hg':
        result = '大伯子'
    elif qqcontent2 == 'ha':
        result = '小叔子'
    elif qqcontent2 == 'hj':
        result = '大姑子'
    elif qqcontent2 == 'hq':
        result = '小姑子'
    else:
        result = '抱歉，关系有误或者你们不太熟哦~'

    qqcontent = display1.get()
    qqcontent2 = str(result)
    display1.set(qqcontent + '=\n' + str(result))


# 清空内容栏
def clear1():
    display1.set('')
    global qqcontent2
    qqcontent2 = ''

# 删除前一个字符
def backspace1():
    display1.set(str(display1.get()[:-3]))
    global qqcontent2
    qqcontent2 = str(qqcontent2[:-1])

def relation():
    # 定义主窗口
    global qqcontent2
    qqcontent2 = ''
    root1 = Tk()
    root1.title('亲戚关系计算器')
    root1.geometry('300x400+300+300')
    # 将display1定义成global，main() 函数外的call1, calculate1等可以调用
    global display1
    display1 = StringVar()
    # 　设置内容显示栏，使用label，anchor是靠右，默认居中
    label = Label(root1, relief='sunken', borderwidth=4, anchor=SE)
    label.config(bg='grey', width=42, height=3)
    label['textvariable'] = display1
    label.grid(row=0, column=0, columnspan=3)

    #	text = Text(root1, relief = 'sunken', borderwidth = 3)
    #	text.insert(INSERT, str(display1))
    #	text.grid(row = 0, column = 0, columnspan = 4)
    # 添加各个按钮，并绑定行为,使用lambda很方便，是用的是grid布局
    Button(root1, text='C', width=3, padx=18, pady=18, command=lambda: clear1()).grid(row=1, column=2)
    Button(root1, text='DEL', width=3, padx=18, pady=18, command=lambda: backspace1()).grid(row=2, column=2)
    Button(root1, text='的', fg='#EF7321', width=3, padx=18, pady=18, command=lambda: call1('的')).grid(row=3, column=2)
    Button(root1, text='父', width=3, padx=18, pady=18, command=lambda: call1('父亲')).grid(row=1, column=0)
    Button(root1, text='母', width=3, padx=18, pady=18, command=lambda: call1('母亲')).grid(row=1, column=1)
    Button(root1, text='夫', width=3, padx=18, pady=18, command=lambda: call1('丈夫')).grid(row=2, column=0)
    Button(root1, text='妻', width=3, padx=18, pady=18, command=lambda: call1('妻子')).grid(row=2, column=1)
    Button(root1, text='兄', width=3, padx=18, pady=18, command=lambda: call1('哥哥')).grid(row=3, column=0)
    Button(root1, text='弟', width=3, padx=18, pady=18, command=lambda: call1('弟弟')).grid(row=3, column=1)
    Button(root1, text='姐', width=3, padx=18, pady=18, command=lambda: call1('姐姐')).grid(row=4, column=0)
    Button(root1, text='妹', width=3, padx=18, pady=18, command=lambda: call1('妹妹')).grid(row=4, column=1)
    Button(root1, text='儿', width=3, padx=18, pady=18, command=lambda: call1('儿子')).grid(row=5, column=0)
    Button(root1, text='女', width=3, padx=18, pady=18, command=lambda: call1('女儿')).grid(row=5, column=1)
    Button(root1, text='=', width=3, height=5, bg='#EF7321', padx=18, pady=18, command=lambda: calculate1()).grid(row=4, column=2,rowspan=2)

    root1.mainloop()

if __name__ == '__main__':
    relation()

