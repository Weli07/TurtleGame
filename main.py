import turtle
import random

# Ekran ayarları
screen = turtle.Screen()
screen.title("Rastgele Kaplumbağa,Sayaç ve Score")
screen.bgcolor("lightblue")
screen.setup(width=500, height=500)

# Kaplumbağa (ekranda gezen)
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()

# Score yazısı için turtle
score_yazici = turtle.Turtle()
score_yazici.hideturtle()
score_yazici.penup()
score_yazici.goto(0,210)
score=0


# Sayaç yazısı için turtle
sayac_yazici = turtle.Turtle()
sayac_yazici.hideturtle()
sayac_yazici.penup()
sayac_yazici.goto(0, 180)
sayac = 15

def sayac_guncelle():
    global sayac
    global score
    sayac_yazici.clear()
    sayac_yazici.write(f"Time : {sayac}", align="center", font=("Arial", 20, "bold"))

    sayac -= 1
    if sayac == 0:
        sayac=15
        score=0
        score_guncelle()

    screen.ontimer(sayac_guncelle, 1000)

def score_guncelle():
    score_yazici.clear()
    score_yazici.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

def rastgele_konum():
    x = random.randint(-230, 200)
    y = random.randint(-230, 200)
    kaplumbaga.goto(x, y)

    screen.ontimer(rastgele_konum, 500)


def tiklandi(x, y):
    global score
    score += 1
    score_guncelle()


kaplumbaga.onclick(tiklandi)


sayac_guncelle()
score_guncelle()
rastgele_konum()



turtle.done()
