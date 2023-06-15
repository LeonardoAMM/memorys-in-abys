from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *


janela = Window(1400,900)
teclado = Keyboard()
mouse1 = Window.get_mouse()

#tem 2 sprites:
#o protagonista virado para direita
protagonista=Sprite("imagens/prota/sheet1.png",17)
# e ele virado para a esquerda
protagonistaIn=Sprite("imagens/prota/sheetin.png",17)

Vida5=Sprite("imagens/vida/vida5.png")

ceu = GameImage("./imagens/ceu.jpg")

chao1=Sprite("imagens/terra_1.png")
chao2=Sprite("imagens/terra_1.png")
chao3=Sprite("imagens/terra_1.png")
chao_ponte=Sprite("imagens/ponte.png")

chaos=[]

velocidadeX = 0
velocidadeY = 0
vel_chao_rand = 30
direita=True

gravidade=0
puloduplo=False
recarga=0

#variavel para ver se o player esta no chao
chao=True

#o protagonista virado para os 2 lados
protagonista.set_position(300,janela.height/3)
protagonistaIn.set_position(300,janela.height/3)
protagonista.set_total_duration(2000)
protagonistaIn.set_total_duration(2000)

chao1.set_position(300,janela.height/2.5+chao1.height)
chao2.set_position(1000,janela.height/2.5+chao1.height)
chao3.set_position(1600,1.5*janela.height/2+chao1.height)
chao_ponte.set_position(2400,janela.height/2.8+chao1.height)


chaos.append(chao1)
chaos.append(chao2)
chaos.append(chao3)
chaos.append(chao_ponte)


janela.set_title("Memories In Abyss")

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
    if(teclado.key_pressed("W") and puloduplo==False and recarga>.3):
        if(chao==True):
            puloduplo=False
            recarga=0
        elif(chao==False and recarga>.9):
            puloduplo=True
        chao=False
        protagonista.set_curr_frame(14)
        protagonista.set_initial_frame(15)
        protagonista.set_final_frame(17)
        protagonistaIn.set_curr_frame(14)
        protagonistaIn.set_initial_frame(15)
        protagonistaIn.set_final_frame(17)
        velocidadeY=1
        gravidade=0

    recarga+=janela.delta_time()

    #Aqui muda a animação do protagonista enquanto ele cai, quando ele estava no chao (VAR chao for verdade) e não estiver tocando em mais nada (esses colides dai) ele cai direto
    #a velocidadY esta zerado, pq ele n da um impulso
    if((protagonista.collided(chao1)==False and protagonista.collided(chao2)==False  and protagonista.collided(chao3)==False and protagonista.collided(chao_ponte)==False) and chao==True):
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
    if(chao==False and (protagonista.collided(chao1) or protagonista.collided(chao2) or protagonista.collided(chao3) or protagonista.collided(chao_ponte)) and 
       ((protagonista.y<chao1.y-chao1.height)or (protagonista.y>chao3.y-chao3.height) ) and (protagonista.get_curr_frame()!=14 or protagonistaIn.get_curr_frame()!=14)):
        gravidade=0
        chao=True
        puloduplo=False
        recarga=0

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

    if(teclado.key_pressed('ESC')):
        break

    if(protagonista.x > 8.5*janela.width/10 and direita==True):#>= janela.width-(protagonista.width)
        for x in chaos:
            x.move_x(-velocidadeX*janela.delta_time())
    if(protagonista.x >=janela.width-(protagonista.width)):
        protagonista.x = janela.width-(protagonista.width)
        protagonistaIn.x = janela.width-(protagonista.width)

    if(protagonista.x<-1 and direita== False):
        for k in chaos:
            k.move_x(-2*velocidadeX*janela.delta_time())
    if(protagonista.x<=-1):
        protagonista.x = -1
        protagonistaIn.x = -1

   
    if(protagonista.y > janela.height):
        protagonista.set_position(300,janela.height/3)
        protagonistaIn.set_position(300,janela.height/3)

    
    janela.set_background_color((0, 0, 0))

    ceu.draw()

    Vida5.draw()

    chao1.draw()
    chao2.draw()
    chao3.draw()
    chao_ponte.draw()

    protagonista.draw()
    protagonistaIn.draw()
    protagonistaIn.update()
    protagonista.update()


    janela.update()