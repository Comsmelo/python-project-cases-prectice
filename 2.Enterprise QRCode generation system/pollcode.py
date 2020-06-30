import os 

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
                    print('\033[1;31;47m 必须输入，'+str(length)+'个字母，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print('\033[1;31;47m 输入非法，清重新输入！！\033[0m')
                return '0'
    else:
        print('\033[1;31;47m 输入为空，清重新输入！！\033[0m')
                return '0'


# 读取已生成对防伪信息


if __name__ == "__main__":
    #inputbox('test：', 1, 5)
    print(str.isalpha('aaa'))