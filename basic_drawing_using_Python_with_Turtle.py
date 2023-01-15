# UncleEngineer (UncleLabMember # 2023) 
# Course : Basic Python Ep.1
# HW  : วาดรูปอะไรก็ได้โดยประยุกต์ใช้เครื่องมือจาก Turtle Library

# รูปที่ต้องการวาด : ดอกไม้

#  Import Turtle Library  and some setting
import turtle
window = turtle.Screen()
window.bgcolor('lightblue')
tao = turtle.Pen()
tao.shape('turtle')

# วาดนส่วนกลีบดอก
tao.pencolor('red')
for j in range(32) :
    for i in range(4):
        tao.forward(100)
        tao.left(90)
    tao.right(11.25)

# วาดในส่วนก้าน
tao.pencolor('green')
tao.right(90)
tao.forward(200)
tao.left(90)

# วาดในส่วนใบ
tao.forward(50)
tao.left(45)
tao.forward(50)

for i in range(3) :
    tao.right(90)
    tao.forward(50)

tao.left(45)
tao.forward(100)

tao.left(45)
tao.forward(50)

for i in range(3) :
    tao.right(90)
    tao.forward(50)

tao.left(45)
tao.forward(50)
tao.right(90)
tao.forward(50)

# To prevent Closing window automatically after finish drawing
turtle.done()
