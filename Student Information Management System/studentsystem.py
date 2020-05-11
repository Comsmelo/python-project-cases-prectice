import os
import re

def menu():
    print('''
        ------------------------------------------------
        |                                               
        |           ======  功能菜单  ======             
        |                                               
        |       1. 录入学生数据                                        
        |       2. 查找学生信息                           
        |       3. 删除学生信息                           
        |       4. 修改学生信息                           
        |       5. 排序                                  
        |       6. 统计学生的总人数                        
        |       7. 显示所有学生信息                        
        |       0. 退出系统                              
        | ============================================  
        |     说明：通过数字或⬆ ⬇ 方向键选择菜单            
        -------------------------------------------------
    ''')

def insert():
    print('it is insert module')
    return True

def search():
    print('it is search module')
    return True

def delete():
    print('it is delete module')
    return True

def modify():
    print('it is modify module')
    return True

def sort():
    print('it is sort module')
    return True

def total():
    print('it is total module')
    return True

def show():
    print('it is show module')
    return True
    
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