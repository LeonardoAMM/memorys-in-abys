from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *


def fim(janela):
    som=Sound("musicas/ganhar.ogg")
    som.set_repeat(1)
    som.play()
    teclado = janela.get_keyboard()

    while True:
        janela.set_background_color((0,0,0))
        janela.draw_text("PARABÉNS!\nEssa foi uma jornada incrível!", 100,300, 80,(255,255,255), "Cambria")

        if(teclado.key_pressed("ESC")):
            som.stop()
            

        janela.update()