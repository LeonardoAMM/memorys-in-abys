from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from stage1 import *
from stage2 import *
from stage3 import *
from morte import *
from PPlay.sound import *

janela = Window(1400,900)
var_mapa = 0

som=Sound("musicas/menu.ogg")
som.set_repeat(1)
som.play()

mortee=False
ganhar = False

menu = GameImage("./imagens/menu/back.png")
option1 = Sprite("./imagens/menu/start.png")
option2 = Sprite("./imagens/menu/sair.png")
aceso_option1 = Sprite("./imagens/menu/acesostart.png")
aceso_option2 = Sprite("./imagens/menu/acesoquit.png")
option1.set_position(janela.width/2 - option1.width/2,janela.height/2 - 1.1*option1.height)
option2.set_position(janela.width/2 -0.99* option2.width/2, janela.height/1.5 - 0.7*option2.height)
aceso_option1.set_position(janela.width/2 - option1.width/2,janela.height/2 - 1.1*option1.height)
aceso_option2.set_position(janela.width/2 -0.99* option2.width/2, janela.height/1.5 - 0.7*option2.height)
mouse = janela.get_mouse()

while True:
    if(som.is_playing()==False):
        som=Sound("musicas/menu.ogg")
        som.set_repeat(1)
        som.play()

    if(mortee==True):
        som.stop()
        mortee = mortt(janela)
    

    aceso_option1.hide()
    aceso_option2.hide()
    if mouse.is_over_area((option1.x,option1.y), (option1.x+option1.width,option1.y+option1.height)): 
        aceso_option1.unhide()
        option1.hide()
        if (mouse.is_button_pressed(1)):
            if(var_mapa == 0):
                aux = stage1(var_mapa,janela,mortee)
                mortee = aux[1]
                var_mapa = aux[0]
                
            elif(var_mapa == 1):
                aux = stage2(var_mapa,janela,mortee)
                mortee = aux[1]
                var_mapa = aux[0]
            
            elif(var_mapa == 2):
                aux = stage3(var_mapa,janela,mortee,ganhar)
                mortee = aux[1]
                var_mapa = aux[0]
                ganhar = aux[2]

    if(ganhar == True):
        som.stop()
        aux1 = fim(janela,var_mapa)
        ganhar = aux1[0]
        var_mapa = aux[1]




    elif mouse.is_over_area((option2.x,option2.y),(option2.x+option2.width,option2.y+option2.height)):
        aceso_option2.unhide()
        option2.hide()
        if (mouse.is_button_pressed(1)):
            break

    option1.unhide()
    option2.unhide()

    menu.draw()
    option1.draw()
    option2.draw()
    aceso_option1.draw()
    aceso_option2.draw()        
    janela.update()
    