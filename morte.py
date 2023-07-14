from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *
import random

def mortt(janela):

    prota_morto = Sprite("./imagens/morte.png")
    prota_morto.set_position(650,650)
    teclado = janela.get_keyboard()
    sangue = Sprite("./imagens/bloodslash2.png")
    sangue2 = Sprite("./imagens/bloodspray.png")
    sangue3 = Sprite("./imagens/bloodslash_heavy.png")
    som=Sound("musicas/morte.ogg")
    som.set_repeat(1)
    som.play()

    rand_sangue = random.randint(0,2)
    rand = random.randint(0,4)
        

    while True:
        
        janela.set_background_color((0, 0, 0))
        if (rand_sangue==0):
            sangue.draw()
        elif(rand_sangue==1):
            sangue2.draw()
        elif(rand_sangue==2):
            sangue3.draw()
        janela.draw_text("Game Over", 330,280, 150,(255,255,255), "Cambria") 
        if(rand == 0):
            janela.draw_text("Você acha que enganou a morte? A morte enganou você.", 350,500, 25,(255,255,255), "Cambria")
        elif(rand == 1) :
            janela.draw_text("Uma espada não exerce força a menos que as mãos que a seguram tenham coragem.", 350,500, 25,(255,255,255), "Cambria")
        elif(rand == 2) :
            janela.draw_text("Não importa o quão escura a noite seja,a manhã sempre vem.", 350,500, 25,(255,255,255), "Cambria")
        elif(rand == 3) :
            janela.draw_text("Um herói não é definido por suas vitórias, mas como ele se recupera após falhar.", 350,500, 25,(255,255,255), "Cambria")
        elif(rand == 4) :
            janela.draw_text("Uma jornada de mil milhas começa com um único passo", 350,500, 25,(255,255,255), "Cambria")
            

        if(teclado.key_pressed("ESC")):
            morte = False
            som.stop()
            return morte
        
        prota_morto.draw()

        janela.update()