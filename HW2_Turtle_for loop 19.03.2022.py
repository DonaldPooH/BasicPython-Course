import turtle
tao = turtle.Pen()  #ดึงความสามารถการใช้ปากกา 
tao.shape('turtle') #แปลงร่างเป็นเต๋า

def triangle():
    '''ฟังก์ชั่นเอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(9):
        tao.forward(100)
        tao.left(135)

def circle():
    for i in range(12):
        tao.circle(100)
        tao.left(30)
   
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(100,100)
triangle()
Go(-150,-150)
triangle()
Go(130,-85)
triangle()
Go(-220,70)
triangle()
Go(-25,-5)
circle()









        

        

