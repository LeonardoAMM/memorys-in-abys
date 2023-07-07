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
Vida4=Sprite("imagens/vida/vida4.png")
Vida3=Sprite("imagens/vida/vida3.png")
Vida2=Sprite("imagens/vida/vida2.png")
Vida1=Sprite("imagens/vida/vida1.png")
Vida0=Sprite("imagens/vida/vida0.png")
vida=5

vidas=[]
vidas.append(Vida5)
vidas.append(vida)


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

inimigos=[]

Ninimigos=3

for x in range(Ninimigos):
    inimigoL=[]
    Slime=Sprite("imagens/inimigos/slime.png",21)
    Slime.set_total_duration(3000)
    Slime.set_initial_frame(0)
    Slime.set_final_frame(4)
    Slime.set_position(300+x*700,janela.height/6)
    gravisli=False
    aparece=False
    ataqueini=False
    velocidadeIn=0
    cooldown=0
    inimigoL.append(Slime)
    inimigoL.append(gravisli)
    inimigoL.append(aparece)
    inimigoL.append(ataqueini)
    inimigoL.append(velocidadeIn)
    inimigoL.append(cooldown)
    inimigos.append(inimigoL)

segundo=0
tempo=0
fps=0
cont=0




chao1.set_position(300,janela.height/2.5+chao1.height)
chao2.set_position(1000,janela.height/2.5+chao2.height)
chao3.set_position(1600,1.5*janela.height/2+chao3.height)
chao_ponte.set_position(2400,janela.height/2.8+chao_ponte.height)


chaos.append(chao1)
chaos.append(chao2)
chaos.append(chao3)
chaos.append(chao_ponte)


janela.set_title("Memories In Abyss")

while(True):

    if(vidas[1]==5):
        del vidas[0]
        vidas.insert(0,Vida5)
    if(vidas[1]==4):
        del vidas[0]
        vidas.insert(0,Vida4)
    if(vidas[1]==3):
        del vidas[0]
        vidas.insert(0,Vida3)
    if(vidas[1]==2):
        del vidas[0]
        vidas.insert(0,Vida2)
    if(vidas[1]==1):
        del vidas[0]
        vidas.insert(0,Vida1)


    for x in inimigos:
        if(x[1]==False):
            x[0].move_y(400*janela.delta_time())
        else:
            x[0].move_y(0)

        if((x[0].collided(chao1)==False and x[0].collided(chao2)==False  and x[0].collided(chao3)==False and x[0].collided(chao_ponte)==False) and x[1]==True):
            x[1]=False

        if( (x[1]==False) and ((x[0].collided(chao1)) or (x[0].collided(chao2)) or (x[0].collided(chao3) or (x[0].collided(chao_ponte)))) ):
            x[1]=True

        x[5]+=janela.delta_time()

        if(((x[0].x-protagonista.x)<100) and ((x[0].x-protagonista.x)>-100) and x[5]>.5 and x[4]==0):
            x[3]=True
        else:
            x[3]=False

        if(x[3]==True):
            if(x[0].get_curr_frame()>=13):
                x[5]=0
            x[0].set_initial_frame(8)
            x[0].set_final_frame(14)
            if(x[0].get_curr_frame() >13 or x[0].get_curr_frame()<8):
                x[0].set_curr_frame(8)

        if( ((x[0].x-protagonista.x)<-100) and (x[1]==True) and ((x[0].x-protagonista.x)>-200)):
            x[4]=200
            x[0].move_x(x[4]*janela.delta_time())
        elif(((x[0].x-protagonista.x)>100) and ((x[0].x-protagonista.x)<300) and (x[1]==True)):
            x[4]=-200
            x[0].move_x(x[4]*janela.delta_time())
        else:
            x[4]=0
        
        if(x[0].y>janela.height):
            inimigos.remove(x)
            Ninimigos=Ninimigos-1

        if(((x[0].x-protagonista.x) < janela.width) and ((x[0].x-protagonista.x) > -janela.width)):
            x[2]=True
        else:
            x[2]=False

        if(x[4]==0 and x[3]==False):
            x[0].set_initial_frame(0)
            x[0].set_final_frame(4)
            if((x[0].get_curr_frame() > 4)):
                x[0].set_curr_frame(0)
        if(x[4]!=0):
            x[0].set_initial_frame(5)
            x[0].set_final_frame(8)
            if(x[0].get_curr_frame() > 8 or x[0].get_curr_frame() < 5):
                x[0].set_initial_frame(5)

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
        elif(chao==False and recarga>.5):
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
    if( (chao==False) and (((protagonista.collided(chao1) or protagonista.collided(chao2)) and (protagonista.y<=chao1.y-chao1.height)) or (protagonista.collided(chao3) and (protagonista.y<=chao3.y-chao3.height))
     or (protagonista.collided(chao_ponte) and (protagonista.y <= chao_ponte.y-chao_ponte.height*.7))  ) and (protagonista.get_curr_frame()!=14 or protagonistaIn.get_curr_frame()!=14)):
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

    if(protagonista.x > janela.width-(protagonista.width) and direita==True):#>= janela.width-(protagonista.width)
        for x in chaos:
            x.move_x(-velocidadeX*janela.delta_time())
        for x in inimigos:
            x[0].move_x(-velocidadeX*janela.delta_time())
    if(protagonista.x >=janela.width-(protagonista.width)):
        protagonista.x = janela.width-(protagonista.width)
        protagonistaIn.x = janela.width-(protagonista.width)

    if(protagonista.x<-1 and direita== False):
        for k in chaos:
            k.move_x(-velocidadeX*janela.delta_time())
        for k in inimigos:
            k[0].move_x(-velocidadeX*janela.delta_time())
            
    if(protagonista.x<=-1):
        protagonista.x = -1
        protagonistaIn.x = -1

   
    if(protagonista.y > janela.height):
        protagonista.set_position(300,janela.height/3)
        protagonistaIn.set_position(300,janela.height/3)


    segundo+=janela.delta_time()

    cont+=1

    tempo = int(segundo)

    if(tempo>=1):
        segundo=0
        fps=cont
        cont=0


    ceu.draw()

    vidas[0].draw()
    janela.draw_text(str(fps), 0, 0, 68, (255,255,255), "Calibri")

    chao1.draw()
    chao2.draw()
    chao3.draw()
    chao_ponte.draw()

    protagonista.draw()
    protagonistaIn.draw()
    protagonistaIn.update()
    protagonista.update()

    print(inimigos)

    for y in range(Ninimigos):
        if(inimigos[y][2]==True):
            inimigos[y][0].draw()
            inimigos[y][0].update()


    janela.update()