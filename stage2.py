from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
import protagonis
import esqueleto

caverna = GameImage("imagens/stage2/caverna.png")


prota=[]

def stage2(var):
    janela = Window(1400,900)
    teclado = Keyboard()
    mouse1 = Window.get_mouse()

    #tem 2 sprites:
    #o protagonista virado para direita
    protagonista=Sprite("imagens/prota/sheet5.png",24)
    # e ele virado para a esquerda
    protagonistaIn=Sprite("imagens/prota/sheetin2.png",24)

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
    pedra = Sprite("imagens/stage2/pedra.png")
    conjped = Sprite("imagens/stage2/conjped.png")
    estacom = Sprite("imagens/stage2/estacom.png")
    tronco2 = Sprite("imagens/stage2/tronco2.png")
    caixa = Sprite("imagens/stage2/caixa.png")
    porta=Sprite("imagens/stage2/porta.png")



    tronco.set_position(200,600)
    pedra.set_position(1100, janela.height/2.25)
    conjped.set_position(1500, janela.height/1.2)
    estacom.set_position(3000, janela.height/2)
    tronco2.set_position(4600, janela.height/1.5)
    caixa.set_position(5500, janela.height/1.8)
    porta.set_position(5500, janela.height/2.8)

    chaos=[]

    chaos.append(tronco)
    chaos.append(pedra)
    chaos.append(conjped)
    chaos.append(estacom)
    chaos.append(tronco2)
    chaos.append(caixa)
    chaos.append(porta)


    velocidadeX = 0
    velocidadeY = 0
    vel_chao_rand = 30
    direita=True

    renasce=0




    gravidade=0
    puloduplo=False
    recarga=0

    ataquep=False
    ataqrecarga=0

    invencivel=False
    invenrecarga=0
    tempoInven=0

    tempoInvenD=0

    invencivelD=False

    #variavel para ver se o player esta no chao
    chao=True

    prota.append(protagonista) #0
    prota.append(protagonistaIn) #1
    prota.append(velocidadeX) #2
    prota.append(velocidadeY) #3
    prota.append(direita) #4
    prota.append(gravidade) #5
    prota.append(puloduplo)#6
    prota.append(recarga)#7
    prota.append(chao)#8
    prota.append(ataquep)#9
    prota.append(ataqrecarga)#10
    prota.append(invencivel)#11
    prota.append(invenrecarga)#12
    prota.append(tempoInven)#13
    prota.append(tempoInvenD)#14
    prota.append(invencivelD)#15
    #o protagonista virado para os 2 lados
    prota[0].set_position(300,janela.height/3)
    prota[1].set_position(300,janela.height/3)
    prota[0].set_total_duration(2000)
    prota[1].set_total_duration(2000)

    inimigos=[]

    Ninimigos=7

    for x in range(Ninimigos):
        inimigoL=[]
        esquelet=Sprite("imagens/inimigos/esqueleto3.png",52)
        esquelet.set_total_duration(3000)
        esquelet.set_initial_frame(0)
        esquelet.set_final_frame(4)
        esquelet.set_position(300+x*700,janela.height/6)
        gravisli=False
        aparece=False
        ataqueini=False
        velocidadeIn=0
        cooldown=0
        vidai=2
        coolHit=0
        inimigoL.append(esquelet)
        inimigoL.append(gravisli)
        inimigoL.append(aparece)
        inimigoL.append(ataqueini)
        inimigoL.append(velocidadeIn)
        inimigoL.append(cooldown)
        inimigoL.append(vidai)
        inimigoL.append(coolHit)

        inimigos.append(inimigoL)



    hitboxsI=[]

    hitboxsp=[]

    segundo=0
    tempo=0
    fps=0
    cont=0

    chaos.append(tronco)
    chaos.append(pedra)


    hitboxsI=[]

    hitboxsp=[]

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
        if(vidas[1]==0):
            del vidas[0]
            vidas.insert(0,Vida0)

        hitboxsp.clear()
        
        protaF=protagonis.protag(prota,janela,hitboxsI,vidas,hitboxsp,renasce)

        prota=protaF[0]
        vidas=protaF[1]
        hitboxsp=protaF[2]


        hitboxsI.clear()

        for x in inimigos:

            if((x[0].collided(tronco)==False and  x[0].collided(pedra)==False  and x[0].collided(conjped)==False and x[0].collided(estacom)==False and x[0].collided(tronco2)==False and x[0].collided(caixa)==False) and x[1]==True):
                x[1]=False

            if( (x[1]==False) and ((x[0].collided(tronco)) or (x[0].collided(pedra)) or (x[0].collided(conjped)) or (x[0].collided(estacom)) or (x[0].collided(tronco2)) or (x[0].collided(caixa))) ):
                x[1]=True
                
            if(x[0].y>janela.height):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1
            if(x[6]==0):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1


        iniF=esqueleto.inimi(prota,inimigos,janela,hitboxsI,hitboxsp)


        inimigos=iniF[0]
        hitboxsI=iniF[1]


        if((prota[0].collided(tronco)==False and prota[0].collided(pedra)==False and prota[0].collided(conjped)==False and prota[0].collided(estacom)==False and prota[0].collided(tronco2)==False and prota[0].collided(caixa)==False) and prota[8]==True):
            prota[8]=False
            prota[0].set_curr_frame(15)
            prota[0].set_initial_frame(15)
            prota[0].set_final_frame(17)
            prota[1].set_curr_frame(15)
            prota[1].set_initial_frame(15)
            prota[1].set_final_frame(17)
            prota[3]=0
            prota[5]=.6


        #quando o protagonista tocar em algo, a VAR chao vira verdade e a gravidade zera
        if( (prota[8]==False) and (((prota[0].collided(tronco)) and (prota[0].y+protagonista.height<=tronco.y+tronco.height*.3)) or ((prota[0].collided(pedra)) and (prota[0].y+protagonista.height<=pedra.y+pedra.height*.6))
            or ((prota[0].collided(conjped)) and (prota[0].y+protagonista.height<=conjped.y+conjped.height*.2))  or ((prota[0].collided(estacom)) and (prota[0].y+protagonista.height<=estacom.y+estacom.height*.15))   or ((prota[0].collided(tronco2)) and (prota[0].y+protagonista.height<=tronco2.y+tronco2.height*.15))
            or ((prota[0].collided(caixa)) and (prota[0].y+protagonista.height<=caixa.y+caixa.height*.15))                                      ) and (prota[0].get_curr_frame()!=14 or prota[1].get_curr_frame()!=14)):
            prota[5]=0
            prota[8]=True
            prota[6]=False
            prota[7]=0



        if(teclado.key_pressed('ESC')):
            return var

                
        if(protagonista.x<=-1):
            protagonista.x = -1
            protagonistaIn.x = -1


        if(prota[0].x > janela.width-(prota[0].width) and prota[4]==True):#>= janela.width-(protagonista.width)
            for x in chaos:
                x.move_x(-prota[2]*janela.delta_time())
            for x in inimigos:
                x[0].move_x(-prota[2]*janela.delta_time())
                
        if(prota[0].x >=janela.width-(prota[0].width)):
            prota[0].x = janela.width-(prota[0].width)
            prota[1].x = janela.width-(prota[1].width)
        if(prota[0].x<=-1 and prota[4]== False):
            for k in chaos:
                k.move_x(-prota[2]*janela.delta_time())
            for k in inimigos:
                k[0].move_x(-prota[2]*janela.delta_time())

        segundo+=janela.delta_time()

        cont+=1

        tempo = int(segundo)

        if(tempo>=1):
            segundo=0
            fps=cont
            cont=0


        print(renasce)


        
        

        if(protagonista.collided(porta)):
           var+=1
           return var

        caverna.draw()

        vidas[0].draw()
        janela.draw_text(str(fps), 0, 0, 68, (255,255,255), "Calibri")

        
        for x in chaos:
            x.draw()
            if(prota[0].collided(x) and prota[8]==True):
                renasce=x.x


        protagonista.draw()
        protagonistaIn.draw()
        protagonistaIn.update()
        protagonista.update()

        
        for y in range(Ninimigos):
            if(inimigos[y][2]==True):
                inimigos[y][0].draw()
                inimigos[y][0].update()

        for y in hitboxsI:
            y.draw()
        for y in hitboxsp:
            y.draw()

        janela.update()

