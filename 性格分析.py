# /usr/bin/python
# coding: utf-8

from tkinter import *
import math

# 按键返回函数
def call(num):
    global content2
    if num == 'A型':
        content = display.get() + num
        content2 = content2 + '+3'
        display.set(content)
    elif num == 'B型':
            content = display.get() + num
            content2 = content2 + '+5'
            display.set(content)
    elif num == 'AB型':
            content = display.get() + num
            content2 = content2 + '+7'
            display.set(content)
    elif num == 'O型':
            content = display.get() + num
            content2 = content2 + '+11'
            display.set(content)
    elif num == '1':
            content = display.get() + num
            content2 = content2 + '1'
            display.set(content)
    elif num == '2':
            content = display.get() + num
            content2 = content2 + '2'
            display.set(content)
    else:
        content = display.get() + num
        content2 = content2 + '+'+ num
        display.set(content)


# 使用eval 函数计算
def calculate():
    global content2
    content = display.get()
    result = eval(content2)
    n = result % 9
    if n == 0:
        content3 = '坚持原则。做事有自己的一套方式，不轻易受人影响，' + '\n' +\
                   '不会随波逐流。有个人风格是件好事，尤其是懂得择善' + '\n' +\
                   '固执更能减少出错，不过适当时候选一些适当的事情与' + '\n' +\
                   '人协调，增进一下人际关系也无妨呀！'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 1:
        content3 = '重情重义。你价值观通常以人为先，认为人与人之间的' + '\n' +\
                   '和谐关系和感情是最重要的，平日也乐于助人，许多事' + '\n' +\
                   '都没所谓，给人随和易相处的感觉。要小心别感情用事' + '\n' +\
                   '否则就会令处事上有不公正的盲点。'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 2:
        content3 = '决断洒脱。做事话一就一，拖泥带水犹豫不决不是你的' + '\n' +\
                   '作风，面对工作或感情事的时候都一样。你自己决断的' + '\n' +\
                   '同时，也难忍受别人拖拉，看见别人迟疑不决，你会忍' + '\n' +\
                   '不住爽快地替他作决定。'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 3:
        content3 = '随和顺人。由于你甚么都没所谓，所以很少会与人起冲' + '\n' +\
                   '突，而随和的个性亦为你带来许多好朋友，并且深得他' + '\n' +\
                   '们喜爱。不过有时过分迁就他人可能会失去自己个性，' + '\n' +\
                   '如果能够适当地保留一点自我就更完美啦！'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 4:
        content3 = '喜当领导。你工作无疑会很努力，但待人处世则少不免' + '\n' +\
                   '带点支配欲，有时更可能为了一份凌驾他人的优越感而' + '\n' +\
                   '好胜逞强。事业上的攀升固然重要，但与人相处之道亦' + '\n' +\
                   '不可忽略，尝试在个人提升及人际关系间稍作平衡吧。'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 5:
        content3 = '心坚志毅。你意志坚定不移，做事一旦确立了目标，从' + '\n' +\
                   '不会因小阻滞而半途而废，不达终点不会放弃。每次忘' + '\n' +\
                   '我地完成手上工作后，不妨找些乐事让自己轻松一下，' + '\n' +\
                   '不要待薄自己呀！'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 6:
        content3 = '自强不息。你是个很低调、默默耕耘的人。别人眼中可' + '\n' +\
                   '能看不见你的成功，但成就不是为他人而干亦不是做给' + '\n' +\
                   '人看，即使无高职要位和金钱权力，充实的生活和自强' + '\n' +\
                   '不息就是你最好的财富和最大的成功。'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 7:
        content3 = '乐天知命。你可说是进取心不太强的人，凡事抱平常心' + '\n' +\
                   '看待，很少强求些甚么，对许多事情都不会执着。随遇' + '\n' +\
                   '而安是你的生活态度你大部分时间生活得颇开心。乐天' + '\n' +\
                   '知命当然令人活得轻松，但也不要容许自己太散漫呀！'
        display.set(content + '的分析结果：\n' + content3)
    elif n == 8:
        content3 = '吊儿郎当。不过因为你个性比较「坐唔定」，三分钟热' + '\n' +\
                   '度经常要转换口味，所以所涉猎的知识虽广却不精。做' + '\n' +\
                   '事如果能够对某个项目专心发展，成绩或许会更好，不' + '\n' +\
                   '过知识广博始终对工作及生活方面有很大帮'
        display.set(content + '的分析结果：\n' + content3)
    else:
        display.set('输入有错！请重新输入')

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
    root.title('性格分析器')
    root.geometry('400x300+300+300')
    # 将display定义成global，main() 函数外的call, calculate等可以调用
    global display
    display = StringVar()
    # 　设置内容显示栏，使用label，anchor是靠右，默认居中
    label = Label(root, relief='sunken', borderwidth=3, anchor=SW)
    label.config(font=14,bg='white', width=49, height=5)
    label['textvariable'] = display
    label.grid(row=1, column=0, columnspan=6)
    label1 = Label(root, text='请按 年月日血型 输入，如 19970101A型 ')
    label1.config(font=16,bg='grey', width=50, height=1)
    label1.grid(row=0, column=0, columnspan=6)
    #	text = Text(root, relief = 'sunken', borderwidth = 3)
    #	text.insert(INSERT, str(display))
    #	text.grid(row = 0, column = 0, columnspan = 4)
    # 添加各个按钮，并绑定行为,使用lambda很方便，是用的是grid布局
    Button(root, text='C', fg='#EF7321', width=3, padx=16, pady=16, command=lambda: clear()).grid(row=2, column=5)
    Button(root, text='DEL', width=3, padx=16, pady=16, command=lambda: backspace()).grid(row=3, column=5)
    Button(root, text='7', width=3, padx=16, pady=16, command=lambda: call('7')).grid(row=3, column=1)
    Button(root, text='8', width=3, padx=16, pady=16, command=lambda: call('8')).grid(row=3, column=2)
    Button(root, text='9', width=3, padx=16, pady=16, command=lambda: call('9')).grid(row=3, column=3)
    Button(root, text='4', width=3, padx=16, pady=16, command=lambda: call('4')).grid(row=2, column=3)
    Button(root, text='5', width=3, padx=16, pady=16, command=lambda: call('5')).grid(row=2, column=4)
    Button(root, text='6', width=3, padx=16, pady=16, command=lambda: call('6')).grid(row=3, column=0)
    Button(root, text='1', width=3, padx=16, pady=16, command=lambda: call('1')).grid(row=2, column=0)
    Button(root, text='2', width=3, padx=16, pady=16, command=lambda: call('2')).grid(row=2, column=1)
    Button(root, text='3', width=3, padx=16, pady=16, command=lambda: call('3')).grid(row=2, column=2)
    Button(root, text='A型', width=3, padx=16, pady=16, command=lambda: call('A型')).grid(row=4, column=0)
    Button(root, text='B型', width=3, padx=16, pady=16, command=lambda: call('B型')).grid(row=4, column=1)
    Button(root, text='AB型', width=3, padx=16, pady=16, command=lambda: call('AB型')).grid(row=4, column=2)
    Button(root, text='O型', width=3, padx=16, pady=16, command=lambda: call('O型')).grid(row=4, column=3)
    Button(root, text='=', width=12, bg='#EF7321', padx=16, pady=16, command=lambda: calculate()).grid(row=4, column=4, columnspan=2)
    Button(root, text='0', width=3, padx=16, pady=16, command=lambda: call('0')).grid(row=3, column=4)

    root.mainloop()

if __name__ == '__main__':
    main()

