from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

janela = Window(1400,900)
teclado = Keyboard()

#tem 2 sprites:
#o protagonista virado para direita
protagonista=Sprite("imagens/prota/sheet1.png",17)
# e ele virado para a esquerda
protagonistaIn=Sprite("imagens/prota/sheetin.png",17)


chao1=Sprite("imagens/terra_1.png")
chao2=Sprite("imagens/terra_1.png")

chaos=[]

velocidadeX = 0
velocidadeY = 0

direita=True

gravidade=0

#variavel para ver se o player esta no chao
chao=True

#o protagonista virado para os 2 lados
protagonista.set_position(300,janela.height/3)
protagonistaIn.set_position(300,janela.height/3)
protagonista.set_total_duration(2000)
protagonistaIn.set_total_duration(2000)

chao1.set_position(300,janela.height/2+chao1.height)
chao2.set_position(900,janela.height/2+chao1.height)

chaos.append(chao1)
chaos.append(chao2)


while(True):

    #se a Var direita for verdade o sprite da esqueda fica invisivel e o da direita aparece, mas caso ela for falsa o da esquerda aparece e o da direita fica invisivel
    if(direita==True):
        protagonistaIn.hide()
        protagonista.unhide()
    else:
        protagonista.hide()
        protagonistaIn.unhide()

    #se apertar D, a VAR da direita vira Verdade, alem de mover os sprites para frente
    if(teclado.key_pressed("D")):
        direita=True
        velocidadeX = 300
        protagonista.move_x(velocidadeX*janela.delta_time())
        protagonistaIn.move_x(velocidadeX*janela.delta_time())
    #Se apertar A, a VAR da direita vira Falso, alem de mover os sprites para tras
    elif(teclado.key_pressed("A")):
        direita=False
        velocidadeX = -300
        protagonistaIn.move_x(velocidadeX*janela.delta_time())
        protagonista.move_x(velocidadeX*janela.delta_time())
    else:
        velocidadeX=0


    #Aqui muda a animação do protagonista enquanto pula, quando ele estiver no chao (VAR chao for verdade) e apertar W, ele muda para essa animação
    #a velocidadeY, ta positivo pq ele da um impulso
    if(teclado.key_pressed("W") and chao==True):
        chao=False
        protagonista.set_curr_frame(14)
        protagonista.set_initial_frame(15)
        protagonista.set_final_frame(17)
        protagonistaIn.set_curr_frame(14)
        protagonistaIn.set_initial_frame(15)
        protagonistaIn.set_final_frame(17)
        velocidadeY=1

    #Aqui muda a animação do protagonista enquanto ele cai, quando ele estava no chao (VAR chao for verdade) e não estiver tocando em mais nada (esses colides dai) ele cai direto
    #a velocidadY esta zerado, pq ele n da um impulso
    if((protagonista.collided(chao1)==False and protagonista.collided(chao2)==False) and chao==True):
        chao=False
        protagonista.set_curr_frame(15)
        protagonista.set_initial_frame(15)
        protagonista.set_final_frame(17)
        protagonistaIn.set_curr_frame(15)
        protagonistaIn.set_initial_frame(15)
        protagonistaIn.set_final_frame(17)
        velocidadeY=0
        gravidade=.6

    #aqui a movimentação do player no sentidp Vertical, se a velocidadeY for positiva, ele vai dar um impulso e cair com a gravidade, MAS se a velocidadeY for 0 só tem a gravidade atuando no protagonista
    if(chao==False):
        if(protagonista.get_curr_frame()>14 or protagonistaIn.get_curr_frame()>14):
            if(velocidadeY<=0):
                velocidadeY = 0-((gravidade-.6)*1000)
            else:
                velocidadeY = 600-(gravidade*1000)
            protagonista.move_y(-velocidadeY*janela.delta_time())
            protagonistaIn.move_y(-velocidadeY*janela.delta_time())
            gravidade+=janela.delta_time()


    #quando o protagonista tocar em algo, a VAR chao vira verdade e a gravidade zera
    if(chao==False and (protagonista.collided(chao1) or protagonista.collided(chao2)) and 
       (protagonista.y<chao1.y-chao1.height) and (protagonista.get_curr_frame()!=14 or protagonistaIn.get_curr_frame()!=14)):
        gravidade=0
        chao=True


    #aqui é a animação do player ANDANDO, quando a velocidadeX for 0, mostra a ANIM dele parado, mas se for algo diferente, vai para a anim dele andando
    if(chao==True):
        if(velocidadeX==0):
            protagonista.set_initial_frame(0)
            protagonista.set_final_frame(6)
            protagonistaIn.set_initial_frame(0)
            protagonistaIn.set_final_frame(6)
            if((protagonista.get_curr_frame() > 6 and direita==True)or(protagonistaIn.get_curr_frame() > 6 and direita==False)):
                protagonista.set_curr_frame(0)
                protagonistaIn.set_curr_frame(0)
        else:
            protagonista.set_initial_frame(6)
            protagonistaIn.set_initial_frame(6)
            protagonista.set_final_frame(14)
            protagonistaIn.set_final_frame(14)
            if((protagonista.get_curr_frame()> 14 or protagonista.get_curr_frame() < 6 and direita==True)or(protagonistaIn.get_curr_frame()> 14 or protagonistaIn.get_curr_frame() < 6 and direita==False)):
                protagonista.set_curr_frame(6)
                protagonistaIn.set_curr_frame(6)



    janela.set_background_color((0, 0, 0))

    chao1.draw()
    chao2.draw()

    protagonista.draw()
    protagonistaIn.draw()
    protagonistaIn.update()
    protagonista.update()


    janela.update()