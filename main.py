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
kaplumbaga.penup()   # Çizgi bırakmasın

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
sayac_yazici.goto(0, 180)  # Üst tarafa konumlandır
sayac = 15

def sayac_guncelle():
    global sayac
    global score

    """Sayaç yazısını ekranda günceller."""
    sayac_yazici.clear()
    sayac_yazici.write(f"Time : {sayac}", align="center", font=("Arial", 20, "bold"))

    # Sayaç artır ve ekranda güncelle
    sayac -= 1
    if sayac == 0:
        sayac=15
        score=0
        score_guncelle()

    screen.ontimer(sayac_guncelle, 1000)

def score_guncelle():
    """Sayaç yazısını ekranda günceller."""
    score_yazici.clear()
    score_yazici.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

def rastgele_konum():
    """Kaplumbağayı her 1 saniyede rastgele bir konuma taşır ve sayacı artırır."""
    # Ekran boyutuna göre rastgele x, y
    x = random.randint(-230, 200)
    y = random.randint(-230, 200)
    kaplumbaga.goto(x, y)

    # 1000 ms (1 saniye) sonra fonksiyonu tekrar çağır
    screen.ontimer(rastgele_konum, 500)


def tiklandi(x, y):
    """Kaplumbağaya tıklanınca skoru artırır."""
    global score
    score += 1
    score_guncelle()

# Kaplumbağaya tıklanma olayı bağlama
kaplumbaga.onclick(tiklandi)

# Başlangıçta bir kez çağır
sayac_guncelle()
score_guncelle()
rastgele_konum()


# Pencereyi açık tut
turtle.done()
