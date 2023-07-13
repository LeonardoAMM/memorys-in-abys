from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sound import *
import protagonis
import soldado




def stage3(var,janela):
    
    teclado = Keyboard()
   
   
    som=Sound("musicas/3fase.ogg")
    som.set_repeat(1)
    som.play()

    prota=[]
    castelo = GameImage("imagens/stage3/castelo.png")
    #tem 2 sprites:
    #o protagonista virado para direita
    protagonista=Sprite("imagens/prota/sheet5.png",24)
    # e ele virado para a esquerda
    protagonistaIn=Sprite("imagens/prota/sheetIn2.png",24)

    Vida5=Sprite("imagens/vida/vida5.png")
    Vida4=Sprite("imagens/vida/vida4.png")
    Vida3=Sprite("imagens/vida/vida3.png")
    Vida2=Sprite("imagens/vida/vida2.png")
    Vida1=Sprite("imagens/vida/vida1.png")
    Vida0=Sprite("imagens/vida/vida0.png")
    vida=5

    brick =  Sprite("imagens/stage3/brick.png")
    brick2 = Sprite("imagens/stage3/brick.png")
    pala = Sprite("imagens/stage3/pala.png")#APPEND
    pala2 = Sprite("imagens/stage3/pala2.png")
    sponte = Sprite("imagens/stage3/plata2.png")
    plata=Sprite("imagens/stage3/plata.png")
    porta=Sprite("imagens/stage3/porta.png")



    brick.set_position(300,janela.height/2.5+brick.height)
    pala.set_position(1000,janela.height/1.8+pala.height)
    pala2.set_position(1900,janela.height/3)
    brick2.set_position(2200,janela.height/1.25)
    sponte.set_position(2900,janela.height/1.25)
    plata.set_position(4600,janela.height/1.7)
    porta.set_position(5900,plata.y-plata.height)


    vidas=[]
    vidas.append(Vida5)
    vidas.append(vida)

    chaos=[]

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
    protagonista.set_position(300,janela.height/5)
    protagonistaIn.set_position(300,janela.height/5)
    protagonista.set_total_duration(2000)
    protagonistaIn.set_total_duration(2000)

    inimigos=[]

    Ninimigos=10

    for x in range(Ninimigos):
        inimigoL=[]
        solda=Sprite("imagens/inimigos/soldado.png",24)
        solda.set_total_duration(3000)
        solda.set_initial_frame(0)
        solda.set_final_frame(4)
        solda.set_position(600+x*700,janela.height/6)
        gravisli=False
        aparece=False
        ataqueini=False
        velocidadeIn=0
        cooldown=0
        vidai=3
        coolHit=0
        inimigoL.append(solda)
        inimigoL.append(gravisli)
        inimigoL.append(aparece)
        inimigoL.append(ataqueini)
        inimigoL.append(velocidadeIn)
        inimigoL.append(cooldown)
        inimigoL.append(vidai)
        inimigoL.append(coolHit)

        inimigos.append(inimigoL)


    segundo=0
    tempo=0
    fps=0
    cont=0

    hitboxsI=[]

    hitboxsp=[]


    chaos.append(brick)
    chaos.append(pala)
    chaos.append(sponte)
    chaos.append(pala2)
    chaos.append(plata)
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
        if(vidas[1]==0):
            del vidas[0]
            vidas.insert(0,Vida0)
            som.stop()
            morte=True
            return var,morte

        hitboxsp.clear()

        protaF=protagonis.protag(prota,janela,hitboxsI,vidas,hitboxsp,renasce)
        
        prota=protaF[0]
        vidas=protaF[1]
        hitboxsp=protaF[2]

        hitboxsI.clear()

        iniF=soldado.inimi(prota,inimigos,janela,hitboxsI,hitboxsp)


        inimigos=iniF[0]
        hitboxsI=iniF[1]


        for x in inimigos:

            if((x[0].collided(brick)==False and  x[0].collided(pala2)==False  and x[0].collided(brick2)==False and x[0].collided(sponte)==False  and x[0].collided(pala)==False and x[0].collided(plata)==False) and x[1]==True):
                x[1]=False

            if( (x[1]==False) and ((x[0].collided(brick)) or (x[0].collided(pala2)) or (x[0].collided(brick2)) or (x[0].collided(sponte)) or (x[0].collided(pala)) or (x[0].collided(plata))) ):
                x[1]=True
                
            if(x[0].y>janela.height):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1
            if(x[6]==0):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1

        if((prota[0].collided(brick)==False and prota[0].collided(pala2)==False and prota[0].collided(brick2)==False and prota[0].collided(sponte)==False and prota[0].collided(pala)==False and prota[0].collided(plata)==False) and prota[8]==True):
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
        if( (prota[8]==False) and (((prota[0].collided(brick)) and (prota[0].y<=brick.y-brick.height*3))or (prota[0].collided(pala2) and (prota[0].y<=pala2.y-pala2.height*1.4)) or (prota[0].collided(brick2) and (prota[0].y<=brick2.y-brick2.height))or (prota[0].collided(pala) and (prota[0].y<=pala.y-pala.height*1.4))
        or (prota[0].collided(sponte) and (prota[0].y <= sponte.y-sponte.height*.7)) or (prota[0].collided(plata) and (prota[0].y <= plata.y-plata.height*1))) and (prota[0].get_curr_frame()!=14 or prota[1].get_curr_frame()!=14)):
            prota[5]=0
            prota[8]=True
            prota[6]=False
            prota[7]=0



        if(teclado.key_pressed('ESC')):
            som.stop()
            return var,morte

        if(prota[0].x > janela.width-(prota[0].width) and prota[4]==True):#>= janela.width-(protagonista.width)
            for x in chaos:
                x.move_x(-prota[2]*janela.delta_time())
            for x in inimigos:
                x[0].move_x(-prota[2]*janela.delta_time())
        if(prota[0].x >=janela.width-(prota[0].width)):
            prota[0].x = janela.width-(prota[0].width)
            prota[1].x = janela.width-(prota[1].width)

        if(prota[0].x<0 and prota[4]== False):
            for k in chaos:
                k.move_x(-prota[2]*janela.delta_time())
            for k in inimigos:
                k[0].move_x(-prota[2]*janela.delta_time())
                
        if(protagonista.collided(porta) and Ninimigos==0 and porta.x<janela.width*.9):
            som.stop()
            var+=1
            return var,morte


        segundo+=janela.delta_time()

        cont+=1

        tempo = int(segundo)

        if(tempo>=1):
            segundo=0
            fps=cont
            cont=0
        
        #if passou pelo portal var +=1



        castelo.draw()

        
        for x in chaos:
            x.draw()
            if(prota[0].collided(x) and prota[8]==True):
                renasce=x.x

        vidas[0].draw()
        janela.draw_text(str(fps), 0, 0, 68, (255,255,255), "Calibri")

        for y in range(Ninimigos):
            if(inimigos[y][2]==True):
                inimigos[y][0].draw()
                inimigos[y][0].update()

        for y in hitboxsI:
            y.draw()
        for y in hitboxsp:
            y.draw()
        
        protagonista.draw()
        protagonistaIn.draw()
        protagonistaIn.update()
        protagonista.update()

        janela.update()
