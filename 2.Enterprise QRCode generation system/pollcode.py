import os, time, string, random, tkinter, qrcode
from tkinter import *
import tkinter
import tkinter.messagebox 
import tkinter.filedialog
from string import digits

root = tkinter.Tk()
root.attributes('-alpha', 0)    # 透明度设置
# 初始化数据
number = '123456789'
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
allis = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
i = 0
randstr = []
randsec = []
randfir = ''
fourth = []
fifth = []
randfir = ''
randsec = ''
randthr = ''
str_one = ''
strone = ''
strtwo = ''
nextcard = ''
userput = ''
nres_letter =''


# 创建文件夹
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
    

def openfile(filename):
    f = open(filename)
    fllist = f.read()
    f.close()
    return fllist


# 对输入进行验证
def inputbox(showstr, showorder, length):
    instr = input(showstr)      # showstr为提示的字符串
    if len(instr) != 0:
        # 分成三种验证方式  1:数字 不限字数；2:字母；3:数字且设置位数；
        if showorder == 1:
            if str.isdigit(instr):
                if instr == '0':
                    print('\033[1;31;47m 输入为0，请重新输入！！\033[0m')   # 命令行高亮显示
                    return '0'
                else:
                    return instr 
            else:
                print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
                return '0'
        if showorder == 2:
            if str.isalpha(instr):  # 整个串是字符构成的就行
                if len(instr) != length:
                    print('\033[1;31;47m 必须输入，'+str(length)+'个字母，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
                return '0'
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print('\033[1;31;47m 必须输入，'+str(length)+'个数字，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
                return '0'
    else:
        print('\033[1;31;47m 输入为空，清重新输入！！\033[0m')
        return '0'


# 将生成的防伪码写入文件/屏幕   s--savfe
def wfile(sstr, sfile, typeis, smsg, datapath):
    mkdir(datapath)
    datafile = datapath + '/' + sfile
    file_ = open(datafile, 'w')
    wrlist = sstr
    pdata = ''      # 屏幕输出的防伪码信息
    wdata = ''      # 保存到文本的防伪码信息
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']', '')
        wdata = wdata.replace('"', '').replace('"', '')
        file_.write(str(wdata))
        pdata = pdata + wdata 
    file_.close()
    print('\033[1;31;47m' + str(len(wrlist)) +'\033[0m')   # 屏幕输出生成的防伪信息
    if typeis != 'no':
        # 显示输出完成
        tkinter.messagebox.showinfo('提示：', smsg + str(len(randstr)) + '\n 防伪码文件存放位置' + datafile ) 
        root.withdraw()     # 关闭辅助窗口


def input_validation(insel):
    if str.isdigit(insel):
        if insel == 0:
            print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
            return 0
        else:
            return insel 
    else:
        print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
        return 0


def mainmenu():
    print('''
            \033[1;31;47m
            **********************************************************
                                企业编码生成系统
            **********************************************************
                    1.生成6位数字防伪编码（21536型)
                    2.生成9位系列产品数字防伪编码（879-335439型)
                    3.生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE)
                    4.生成含数据分析功能的防伪编码(5A61M0583D2)
                    5.智能批量生成带数据分析功能的防伪码
                    6.后续补加生成防伪码(5A61M0583D2)
                    7.EAN-13条形码批量生成
                    8.二维码批量输出
                    9.企业粉丝防伪码抽奖
            **********************************************************
                说明：通过数字键选择菜单
            **********************************************************
            \033[0m''')


# 生成六位防伪编码
def scode1(schoice):
    incount = inputbox('\033[1;31;47m 请输入想生成的伪码数量！！\033[0m', 1, 0)
    # 获得0结果表示重来
    while int(incount) == 0:
        incount = inputbox('\033[1;31;47m 请输入想生成的伪码数量！！\033[0m', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        randfir = ""    # 存储单条防伪变量
        for i in range(6):
            randfir = randfir + random.choice(number)
        randfir = randfir + '\n'
        randstr.append(randfir)
    # 调用函数写入文件屏幕输入
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成6位防伪编码共计：', 'codepath')


# 生成九位系列产品的防伪编码
def scode2(schoice):
    # 起始位数
    ordstart = inputbox('\033[1;31;47m 请输入序列产品的数字起始号（三位）！！\033[0m', 3, 3)
    while int(ordstart) == 0:
        ordstart = inputbox('\033[1;31;47m 请输入序列产品的数字起始号！！\033[0m', 3, 3)
    # 系列数量
    ordcount = inputbox('\033[1;31;47m 请输入序列产品的数量！！\033[0m', 1, 0)
    while int(ordcount) <1 or int(ordcount)>999:
        ordstart = inputbox('\033[1;31;47m 请输入序列产品的数量！！\033[0m', 1, 0)
    # 每个产品的数量
    incount = inputbox('\033[1;31;47m 生成每个系列产品的防伪码数量！！\033[0m', 1, 0)
    while incount == 0:
        incount = inputbox('\033[1;31;47m 生成每个系列产品的防伪码数量！！\033[0m', 1, 0)

    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            while str(int(ordstart) + m) + randfir + '\n' in randstr:
                randfir = ''
                for i in range(6):
                    randfir = randfir + random.choice(number)
            # 生成单条防伪码的信息
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr, 'scode'+str(schoice)+'.txt','', '已生成九位防伪码共计：', 'codepath')


# 生成25位防伪码
def scode3(schoice):
    # 生成防伪码的数量
    incount = inputbox('\033[1;31;47m 请输入要生成的防伪码数量！！ \033[0m', 1, 0)
    while int(incount) == 0:
        incount = inputbox('\033[1;31;47m 请输入要生成的防伪码数量！！ \033[0m', 1, 0)
    randstr.clear()
    for j in range(int(incount)):
        strone = ''
        for i in range(25):
            strone = strone + random.choice(letter)
            # 生成的下划线每隔五位加一个下划线
            strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + '-' + strone[15:20] + '-' + strone[20:25] + '\n'
        # 防止编码重复
        while strtwo in randstr:
            strone = ''
            for i in range(25):
                strone = strone + random.choice(letter)
                # 生成的下划线每隔五位加一个下划线
                strtwo = strone[:5] + '-' + strone[5:10] + '-' + strone[10:15] + '-' + strone[15:20] + '-' + strone[20:25] + '\n'
        randstr.append(strtwo)
    wfile(randstr, 'scode' + str(schoice) + '.txt', '', '已生成25位防伪编码: ', 'codepath')


# 生成带数据分析的防伪码
def scode4(schoice):
    intype = inputbox('\033[1;31;47m 请输入数据分析编号（三位字母）！！ \033[0m', 2, 3)
    # 验证
    while not str.isalpha(intype) or len(intype) != 3:
        intype = inputbox('\033[1;31;47m 请输入数据分析编号（三位字母）！！ \033[0m', 2, 3)
    incount = inputbox('\033[1;31;47m 请输入生成带数据分析的伪码的数量！！ \033[0m', 1, 0)
    # 验证
    while int(incount) == 0:
        incount = inputbox('\033[1;31;47m 请输入生成带数据分析的伪码的数量！！ \033[0m', 1, 0)
    ffcode(incount, intype, '', schoice)


# 将数据分析的字母随机插入生成的六位数字中
def ffcode(scount, typestr, ismessage, schoice):
    randstr.clear()
    for j in range(int(scount)):
        strpro = typestr[0].upper()         # 区域分析
        strtype = typestr[1].upper()        # 颜色分析
        strclass = typestr[2].upper()       # 版本分析
        randfir = random.sample(number, 3)  # 随机l采样三个位置，返回数组
        randsec = sorted(randfir)
        letterone = ''                      # 单条防伪码的变量
        for i in range(9):
            letterone = letterone + random.choice(number)
        # 将三个字母按randsec顺讯插入单条数字防伪码 存储之sim变量
        sim = str(letterone[0:int(randsec[0])]) + strpro +  \
            str(letterone[int(randsec[0]):int(randsec[1])]) + strtype +     \
            str(letterone[int(randsec[1]):int(randsec[2])]) + strclass +    \
            str(letterone[int(randsec[2]):9]) + '\n'
        while sim in randstr:
            letterone = ''                      # 单条防伪码的变量
            for i in range(9):
                letterone = letterone + random.choice(number)
            # 将三个字母按randsec顺讯插入单条数字防伪码 存储之sim变量
            sim = str(letterone[0:int(randsec[0])]) + strpro + str(letterone[int(randsec[0]):int(randsec[1])]) + strtype +     \
                str(letterone[int(randsec[1]):int(randsec[2])]) + strclass +    \
                str(letterone[int(randsec[2]):9]) + '\n'
        randstr.append(sim)
    wfile(randstr, typestr+'scode' + str(schoice) + '.txt', ismessage, '生产含数据分析的编码共计', 'codepath')


# 智能批量生成带数据分析功能的防伪码
def scode5(schoice):
    pass


if __name__ == "__main__":
    while i<9:
        # 调入程序主界面菜单
        mainmenu()
        # 操作
        choice = input('\033[1;31;47m 请输入您要操作的菜单选项！！\033[0m')
        if len(choice) != 0:
            choice = input_validation(choice)
            choice = int(choice)    # 对书本的更正
            # 根据序号选菜单
            if choice == 1:
                scode1(str(choice))
            if choice == 2:
                scode2(choice)
            if choice == 3:
                scode3(choice)
            if choice == 4:
                scode4(choice)
            if choice == 5:
                scode5(choice)
            if choice == 6:
                scode6(choice)
            if choice == 7:
                scode7(choice)
            if choice == 8:
                scode8(choice)
            if choice == 9:
                scode9(choice)
            if choice == 0:
                i = 0
                print('正在推出系统...')
        else:
            print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
            