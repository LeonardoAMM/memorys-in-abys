from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

caverna = GameImage("imagens/stage2/caverna.png")

#def stage1(var):
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



tronco = Sprite("imagens/stage2/tronco.png")
tronco1 = Sprite("imagens/stage2/tronco.png")
tronco2 = Sprite("imagens/stage2/tronco2.png")
pedra = Sprite("imagens/stage2/pedra.png")
bloco = Sprite("imagens/stage2/bloco_pedra.png")
bloco_pedra = Sprite("imagens/stage2/bloco_pedra.png")
est = Sprite("imagens/stage2/est.png")
estc = Sprite("imagens/stage2/estc.png")
porta = Sprite("imagens/stage2/Porta.PNG")
caixa = Sprite("imagens/stage2/caixa.png")

tronco.set_position(200,janela.height/1.5)
pedra.set_position(1100, janela.height/2.25)
est.set_position(190,janela.height/1.25)
estc.set_position(1600,janela.height/1.25)
tronco2.set_position(3200,janela.height/1.5)
bloco.set_position(2700,janela.height/2)
porta.set_position(3200+3*porta.width,janela.height/2.8+porta.height/2)


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
chaos.append(est)
chaos.append(tronco)
chaos.append(pedra)
chaos.append(tronco1)
chaos.append(tronco2)
chaos.append(bloco)
chaos.append(estc)
chaos.append(porta)

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

        if((x[0].collided(tronco)==False and x[0].collided(tronco2)==False and x[0].collided(estc)==False and x[0].collided(pedra)==False  and x[0].collided(est)==False and x[0].collided(bloco_pedra)==False and x[0].collided(bloco)==False) and x[1]==True):
            x[1]=False

        if( (x[1]==False) and ((x[0].collided(tronco)) or (x[0].collided(tronco2))or (x[0].collided(estc)) or (x[0].collided(pedra)) or (x[0].collided(est)) or (x[0].collided(bloco_pedra)) or (x[0].collided(bloco))) ):
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

    if((protagonista.collided(tronco)==False and protagonista.collided(pedra)==False and protagonista.collided(estc)==False and protagonista.collided(est)==False and protagonista.collided(bloco_pedra)==False and protagonista.collided(bloco)==False and protagonista.collided(tronco2)==False) and chao==True):
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
    if( (chao==False) and (((protagonista.collided(tronco)) and (protagonista.y<=tronco.y-tronco.height))or (protagonista.collided(pedra) and (protagonista.y<=pedra.y-pedra.height)) or (protagonista.collided(est) and (protagonista.y<=est.y-est.height))or (protagonista.collided(tronco2) and (protagonista.y<=tronco2.y-tronco2.height))
     or (protagonista.collided(bloco_pedra) and (protagonista.y <= bloco_pedra.y-bloco_pedra.height*.7))or (protagonista.collided(estc) and (protagonista.y <= estc.y-estc.height*.7)) or (protagonista.collided(bloco) and (protagonista.y<=bloco.y-bloco.height))) and (protagonista.get_curr_frame()!=14 or protagonistaIn.get_curr_frame()!=14)):
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
        #if (len(vidas))!= 0:
            #vidas.pop()


    segundo+=janela.delta_time()

    cont+=1

    tempo = int(segundo)

    if(tempo>=1):
        segundo=0
        fps=cont
        cont=0
    
    #if passou pelo portal var +=1

    if(protagonista.collided(porta)):
        var = 2
        #break#isso depois de botar se ele quer continuar ou não, botar um janeladrawtext

    caverna.draw()

    vidas[0].draw()
    janela.draw_text(str(fps), 0, 0, 68, (255,255,255), "Calibri")

    
    tronco.draw()
    pedra.draw()
    est.draw()
    estc.draw()
    tronco2.draw()
    bloco.draw()
    porta.draw()

    protagonista.draw()
    protagonistaIn.draw()
    protagonistaIn.update()
    protagonista.update()

    janela.update()

        #return var