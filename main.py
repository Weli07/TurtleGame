import turtle
import time

score_puan=0
times=15
FONT_SIZE = 18
FONT = ('Arial', FONT_SIZE, 'bold')

drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Drawing")
drawing_board.title("Turtle Drawing Screen")

turtle_instance=turtle.Turtle()


turtle_instance.penup()
turtle_instance.goto(0,350)
turtle_instance.write("Score "+str(score_puan), align='center',font=FONT)
turtle_instance.penup()
turtle.setposition(0, 0)





pen_sayac=turtle.Turtle()

def sayac():
    global times
    global score_puan
    while times>0:
        time.sleep(1)
        pen_sayac.clear()
        pen_sayac.penup()
        pen_sayac.goto(0, 320)
        pen_sayac.write("Time : " + str(times), align='center', font=FONT)
        times-=1
        if times == 0:
            times = 15
            score_puan=0




def temizle():
    print("temizle")
    pen_sayac.clear()
    global times
    global score_puan
    score_puan=0
    times=15

sayac()


drawing_board.listen()

drawing_board.onkey(fun=temizle,key="space")


drawing_board.mainloop()