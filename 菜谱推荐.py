# /usr/bin/python
# coding: utf-8

from tkinter import *
import math

# 按键返回函数
def call(num):
    content = display.get() + num
    display.set(content)


# 使用eval 函数计算
def calculate():
    content = display.get()
    if content == '酸':
        content3 = '鱼香肉丝 酸辣土豆丝 菠萝古老肉 糖醋排骨 ' + '\n' +\
                   '刀拍黄瓜 水煮鱼 水煮牛肉 酸汤肥牛 '
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '甜':
        content3 = '鱼香肉丝 菠萝古老肉 糖醋排骨 西红柿炒鸡蛋' + '\n' +\
                   '刀拍黄瓜 水煮鱼 水煮牛肉 酸汤肥牛 鸡蛋羹 ' + '\n' +\
                   '可乐鸡翅 芝士炒年糕 南瓜饼 拔丝地瓜 南瓜红枣汤 ' + '\n' +\
                   '红烧肉 红烧鲫鱼 红烧狮子头 糯米圆子'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣':
        content3 = '鱼香肉丝 酸辣土豆丝 麻婆豆腐 手撕包菜 辣椒炒肉 ' + '\n' +\
                   '回锅肉 宫保鸡丁 剁椒鱼头 清蒸鲈鱼 水煮鱼 香辣蟹 ' + '\n' +\
                   '水煮牛肉 干锅牛蛙 酸汤肥牛 口水鸡 毛血旺 炸鸡翅 ' + '\n' +\
                   '油泼面'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '麻':
        content3 = '麻婆豆腐 辣椒炒肉 剁椒鱼头 水煮鱼 水煮牛肉 ' + '\n' +\
                   '香辣蟹 干锅牛蛙 酸汤肥牛 口水鸡 毛血旺'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '咖喱':
        content3 = '咖喱牛腩 咖喱土豆'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '红烧':
        content3 = '鱼香肉丝 糖醋排骨 麻婆豆腐 宫保鸡丁 可乐鸡翅 ' + '\n' +\
                   '回锅肉 香辣蟹 红烧肉 红烧鲫鱼 红烧狮子头 啤酒鸭'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '炸':
        content3 = '油爆大虾 可乐鸡翅 拔丝地瓜 炸鸡翅 南瓜饼'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '蒸':
        content3 = '剁椒鱼头 清蒸鲈鱼'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '煮':
        content3 = '麻婆豆腐 鸡蛋羹 水煮鱼 水煮牛肉 酸汤肥牛 ' + '\n' +\
                   '口水鸡 毛血旺 南瓜红枣汤 糯米圆子 油泼面 馄饨'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '炒':
        content3 = '鱼香肉丝 酸辣土豆丝 菠萝古老肉 糖醋排骨 手撕包菜' + '\n' +\
                   '辣椒炒肉 回锅肉 西红柿炒鸡蛋 宫保鸡丁 ' + '\n' +\
                   '芝士炒年糕 蛋炒饭 啤酒鸭'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '酸红烧' or content == '红烧酸':
        content3 = '鱼香肉丝 糖醋排骨'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '酸煮' or content == '煮酸':
        content3 = '水煮鱼 水煮牛肉 酸汤肥牛'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '酸炒' or content == '炒酸':
        content3 = '鱼香肉丝 酸辣土豆丝 菠萝古老肉 糖醋排骨'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '甜红烧' or content == '红烧甜':
        content3 = '鱼香肉丝 糖醋排骨 可乐鸡翅 红烧肉 红烧鲫鱼 红烧狮子头'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '甜炸' or content == '炸甜':
        content3 = '可乐鸡翅 拔丝地瓜 南瓜饼'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '甜煮' or content == '煮甜':
        content3 = '鸡蛋羹 南瓜红枣汤 糯米圆子'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '甜炒' or content == '炒甜':
        content3 = '鱼香肉丝 菠萝古老肉 糖醋排骨 芝士炒年糕'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣红烧' or content == '红烧辣':
        content3 = '鱼香肉丝 麻婆豆腐 回锅肉 宫保鸡丁 香辣蟹'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣炸' or content == '炸辣':
        content3 = '炸鸡翅'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣蒸' or content == '蒸辣':
        content3 = '剁椒鱼头 清蒸鲈鱼'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣煮' or content == '煮辣':
        content3 = '麻婆豆腐 水煮鱼 水煮牛肉 酸汤肥牛 口水鸡 毛血旺 油泼面'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '辣炒' or content == '炒辣':
        content3 = '鱼香肉丝 酸辣土豆丝 手撕包菜 辣椒炒肉 回锅肉 宫保鸡丁'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '麻红烧' or content == '红烧麻':
        content3 = '麻婆豆腐 香辣蟹'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '麻蒸' or content == '蒸麻':
        content3 = '剁椒鱼头'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '麻煮' or content == '煮麻':
        content3 = '麻婆豆腐 水煮鱼 水煮牛肉 酸汤肥牛 口水鸡 毛血旺'
        display.set(content + '的推荐结果：\n' + content3)
    elif content == '麻炒' or content == '炒麻':
        content3 = '辣椒炒肉'
        display.set(content + '的推荐结果：\n' + content3)
    else:
        display.set('该口味暂时没有，可以考虑换种口味哦~')

# 清空内容栏
def clear():
    display.set('')
    global content2
    content2 = ''


def main():
    # 定义主窗口
    global content2
    content2 = ''
    root = Tk()
    root.title('菜谱推荐器')
    root.geometry('500x260+300+300')
    # 将display定义成global，main() 函数外的call, calculate等可以调用
    global display
    display = StringVar()
    # 　设置内容显示栏，使用label，anchor是靠右，默认居中
    label = Label(root, relief='sunken', borderwidth=3)
    label.config(font=15, bg='#EEE8CD', width=61, height=5)
    label['textvariable'] = display
    label.grid(row=0, column=0, columnspan=6)
    #	text = Text(root, relief = 'sunken', borderwidth = 3)
    #	text.insert(INSERT, str(display))
    #	text.grid(row = 0, column = 0, columnspan = 4)
    # 添加各个按钮，并绑定行为,使用lambda很方便，是用的是grid布局
    Button(root, text='C', fg='#EF7321', width=3, padx=24, pady=24, command=lambda: clear()).grid(row=2, column=4)
    Button(root, text='酸', fg='#965617', width=3, padx=24, pady=24, command=lambda: call('酸')).grid(row=1, column=0)
    Button(root, text='甜', fg='#965617', width=3, padx=24, pady=24, command=lambda: call('甜')).grid(row=1, column=1)
    Button(root, text='辣', fg='#965617', width=3, padx=24, pady=24, command=lambda: call('辣')).grid(row=2, column=0)
    Button(root, text='麻', fg='#965617', width=3, padx=24, pady=24, command=lambda: call('麻')).grid(row=2, column=1)
    Button(root, text='咖喱', width=3, padx=24, pady=24, command=lambda: call('咖喱')).grid(row=1, column=2)
    Button(root, text='红烧', width=3, padx=24, pady=24, command=lambda: call('红烧')).grid(row=1, column=3)
    Button(root, text='炸', width=3, padx=24, pady=24, command=lambda: call('炸')).grid(row=1, column=4)
    Button(root, text='蒸', width=3, padx=24, pady=24, command=lambda: call('蒸')).grid(row=1, column=5)
    Button(root, text='煮', width=3, padx=24, pady=24, command=lambda: call('煮')).grid(row=2, column=2)
    Button(root, text='炒', width=3, padx=24, pady=24, command=lambda: call('炒')).grid(row=2, column=3)
    Button(root, text='=', width=3, bg='#EF7321', padx=24, pady=24, command=lambda: calculate()).grid(row=2, column=5)

    root.mainloop()

if __name__ == '__main__':
    main()

