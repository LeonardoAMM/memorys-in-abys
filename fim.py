from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *


def fim(janela,var_mapa):
    uni = GameImage("./imagens/Background_space.png")
    som=Sound("musicas/ganhar.ogg")
    som.set_repeat(1)
    som.play()
    teclado = janela.get_keyboard()

    while True:
        janela.set_background_color((0,0,0))
        uni.draw()
        janela.draw_text("PARABÉNS!", 100,300, 80,(255,255,255), "Cambria")
        janela.draw_text("Essa foi uma jornada incrível!!", 100,420, 80,(255,255,255), "Cambria")
        if(teclado.key_pressed("ESC")):
            som.stop()
            
        if(teclado.key_pressed("ESC")):
            som.stop()
            ganhar = False
            var_mapa = 0
            return ganhar,var_mapa
        janela.update()

