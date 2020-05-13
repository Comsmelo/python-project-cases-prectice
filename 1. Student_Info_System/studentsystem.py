import os
import re

def menu():
    print('''
        =================================================                                                     
                    ------  功能菜单  ------                                                         
               1. 录入学生数据                                        
               2. 查找学生信息                           
               3. 删除学生信息                           
               4. 修改学生信息                           
               5. 排序                                  
               6. 统计学生的总人数                        
               7. 显示所有学生信息                        
               0. 退出系统                              
            -----------------------------------------      
             说明：通过数字或⬆ ⬇ 方向键选择菜单            
        =================================================                   
    ''')

# 保存学生信息
def save(student):
    try: 
        students_text = open('student.txt', 'a')
    except Exception as e:
        # 如果没有这个文件就创建文件并打开，也体现了 w 和 a 的区别
        students_text = open('student.txt', 'w')
    # student 为 list
    for info in student:
        students_text.write(str(info) + '\n')
    students_text.close()


# 插入学生信息
def insert():
    studentList = []    # 保存学生信息列表
    mark = True         # 表示是否继续添加
    while(mark):
        id = input("请输入ID如(1001): ")
        if not id:
            break 
        name = input('请输入名字:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩: '))
            python = int(input('请输入Python成绩: '))
            c = int(input('请输入C语言成绩: '))
        except:
            print('输入无效，请重新输入')
            continue 
        # 将输入的学生信息保存到词典
        student = {
            'id' : id,
            'name' : name,
            'english' : english,
            'python' : python,
            'c': c
        }
        studentList.append(student)
        input_mark = input('是否继续添加？(y/n)')
        if input_mark == 'y' or input_mark == 'Y':
            mark = True 
        else:
            mark = False
    save(studentList)
    print('学生信息录入完毕')

    return True

def search():
    #print('it is search module')
    student_query = []
    mark = True 
    while(mark):
        id = ''
        name = ''
        if os.path.exists('student.txt'):
            mode = input('按ID查输入1;按姓名查输入2;\n')
            mark2 = True 
            while(mark2):
                if mode == '1':
                    id = input('请输入学生id: ')
                    mark2 = False
                elif mode == '2':
                    name = input('请输入学生姓名:')
                    mark2 = False
                else:
                    print('输入有误请重新输入')
            with open('student.txt', 'r') as rfile:
                student = rfile.readlines()
                for list_ in student:
                    d = dict(eval(list_))
                    if id is not '':
                        if d['id'] == id :
                            student_query.append(d)
                    elif name is not '':
                        if d['name'] ==  name:
                            student_query.append(d)
                    show_student(student_query)
                    student_query.clear() # 清空列表
        
                input_mark = input('是否继续查询？(y/n)')
                if input_mark == 'y' or input_mark == 'Y':
                    mark = True 
                else:
                    mark = False
        else:
            print('未找到文件')


    return True

def delete():
    #print('it is delete module')
    mark = True
    while mark:
        studentId = input('请输入要删除的学生ID:')
        if studentId is not '':
            # 路径是否存在
            if os.path.exists('student.txt'):
                with open('student.txt', 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            
            ifdel = False # 判断是否已经删除
            # 判断数组里没东西
            if student_old:
                with open('student.txt', 'w') as wfile:
                    d = {}
                    for list_ in student_old:
                        # 学习操作 用eval处理字符串后不会有异常
                        d = dict(eval(list_))
                        if d['id'] != studentId:
                            wfile.write(str(d) + '\n')
                        else:
                            ifdel = True
                if ifdel:
                    print('ID 为%s的学生信息已经被删除' % studentId)
                else:
                    print('未找到ID为%s的学生信息' % studentId)
        else:
            print('未找到学生信息')
            break
        show()
        input_mark = input('是否继续添加？(y/n)')
        if input_mark == 'y' or input_mark == 'Y':
            mark = True 
        else:
            mark = False
            
    return True

# 修改学生信息
def modify():
    #print('it is modify module')
    show()
    if os.path.exists('student.txt'):
        with open('student.txt', 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentid = input('请输入查询学生的id: ')
    with open('student.txt', 'w') as wfile:
        for student in student_old:
            d = dict(eval(student))
            if d['id'] == studentid:
                print('找到这名学生，可以修改其信息！')
                while True:
                    # 这个条件用法不错
                    try:
                        d['name'] = input('请输入姓名: ')
                        d['english'] = int(input('请输入英语成绩: '))
                        d['python'] = int(input('请输入python语言成绩: '))
                        d['c'] = int(input('请输入c语言成绩: '))
                    except:
                        print('输入有误，请重试')
                    else:
                        break
                student = str(d)
                wfile.write(student + '\n')
                print('修改成功！')
            else:
                wfile.write(student)
    return True

# 学生排序模块
def sort():
    print('it is sort module')
    show()
    if os.path.exists('student.txt'):
        with open('student.txt', 'r') as rfile:
            student_old = rfile.readlines()
            student_new = []
        for list_ in student_old:
            d = dict(eval(list_))
            student_new.append(d)
    else:
        return
    ascORdesc = input('请选择（0升序；1降序）：')
    if ascORdesc == '0':
        ascORdesc = False   # 升序排列
    elif ascORdesc == '1':
        ascORdesc = True
    else:
        print('输入有误，请重新输入')
    mode = input('请选择输入方式（1按英语成绩排序；2按python成绩排序；3按C语言成绩排序；0按总成绩进行排序')
    if mode == '1':
        student_new.sort(key=lambda x:x['english'], reverse = ascORdesc)    
    elif mode == '2':
        student_new.sort(key = lambda x:x['python'], reverse = ascORdesc)
    elif mode == '3':
        student_new.sort(key = lambda x:x['c'], reverse = ascORdesc)
    elif mode == '0':
        student_new.sort(key = lambda x:x['english'] + x['python'] +x['c'], reverse = ascORdesc)
    else:
        print('输入有错误 请重新输入')
        sort()
    show_student(student_new)
    return True

# 统计学生总人数
def total():
    #print('it is total module')
    if os.path.exists('student.txt'):
        with open('student.txt', 'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                print('一共有%d个学生'%len(student_old))
            else:
                print('还未录入学生信息')
    else:
        print('未找到录入学生信息')

    return True

# 显示所有学生信息
def show():
    #print('it is show module')
    student_new = []
    if os.path.exists('student.txt'):
        with open('student.txt', 'r') as rfile:
            student_old = rfile.readlines()
        for list_ in student_old:
            student_new.append(eval(list_))
        if student_new:
            show_student(student_new)
    else:
        print('未找到数据')

    return True

# 格式化显示学生信息，参数为列表
def show_student(student_list):
    if not student_list:
        print('show_student module input error')
        return 
    # 格式化输出
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format('ID', '名字', '英语成绩', 'python成绩', 'C语言成绩', '总成绩'))
    # 内容显示格式
    format_data = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    for info in student_list:
        print(format_data.format(info.get('id'),
            info.get('name'), str(info.get('english')), str(info.get('python')),
            str(info.get('c')),
            str(info.get('english') + info.get('python') + info.get('c')).center(12))) # 居中与填充

def main():
    ctrl = True 
    while(ctrl): # watch whether exit
        menu()
        option = input("Please select: ")
        option_str  = re.sub('/D', '', option)
        #option_int = int(re.sub("\D", "", option))  # replace \D
        try:
            option_str  = re.sub('/D', '', option)
            option_int = int(option_str)
            if option_int<0 or option_int>7:
                print('输入数字有误')
                continue
        except Exception as e:
            print(e)

        if option_int == 0:
            print('退出学生信息管理系统')
            ctrl = False
        elif option_int == 1:
            insert()
        elif option_int == 2:
            search()
        elif option_int == 3:
            delete()
        elif option_int == 4:
            modify()
        elif option_int == 5:
            sort()
        elif option_int == 6:
            total()
        elif option_int == 7:
            show()


if __name__ == '__main__':
    main()