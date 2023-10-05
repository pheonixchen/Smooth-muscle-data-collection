import keyboard
import pyautogui
waiting_for_calculation=0
Y1up=0
Y1down=0
Y2up=0
Y2down=0
flag=0
middle=0
artificial_size = float(input('输入人工计算的大小'))

def get_cursor_position1():
    global Y1up
    input('按下空格键继续...')
    x, y = pyautogui.position()
    print(f'当前光标位置：X={x}, Y1up={y}')
    Y1up=y

def get_cursor_position2():
    global Y1down
    input('按下空格键继续...')
    x, y = pyautogui.position()
    print(f'当前光标位置：X={x}, Y1down={y}')
    Y1down=y

def get_cursor_position():
    global middle
    input('按下空格键继续...')
    x, y = pyautogui.position()
    print(f'当前光标位置：X={x}, Y={y}')
    middle=y

get_cursor_position1()
print(Y1up)
get_cursor_position2()
print(Y1down)
for number in range(1, 60):  # 从1到59
    get_cursor_position()
    if flag == 0:
        Y2up = middle
        flag =1
        print(Y2up)

    else:
        Y2down = middle
        flag = 0
        print(Y2down)
        waiting_for_calculation=(Y2up-Y2down)*(artificial_size/(Y1up-Y1down))
        print('这个待测峰的大小是'+str(waiting_for_calculation))

