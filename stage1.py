from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
import protagonis
import slime

var=0

def stage1(var):
    janela = Window(1400,900)
    teclado = Keyboard()
    mouse1 = Window.get_mouse()

    prota=[]

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


    ceu = GameImage("imagens/stage1/ceu.jpg")

    chao1=Sprite("imagens/stage1/terra_1.png")
    chao2=Sprite("imagens/stage1/terra_1.png")
    chao3=Sprite("imagens/stage1/terra_1.png")
    chao_ponte=Sprite("imagens/stage1/ponte.png")

    portal = Sprite("imagens/stage1/portal1.png")


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
    prota[0].set_position(300,janela.height/3)
    prota[1].set_position(300,janela.height/3)
    prota[0].set_total_duration(2000)
    prota[1].set_total_duration(2000)

    inimigos=[]

    Ninimigos=20

    for x in range(Ninimigos):
        inimigoL=[]
        Slime=Sprite("imagens/inimigos/slime.png",27)
        Slime.set_total_duration(3000)
        Slime.set_initial_frame(0)
        Slime.set_final_frame(4)
        Slime.set_position(300+x*700,janela.height/6)
        gravisli=False
        aparece=False
        ataqueini=False
        velocidadeIn=0
        cooldown=0
        vidai=1
        coolHit=0
        inimigoL.append(Slime)
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

    chao1.set_position(300,janela.height/2.5+chao1.height)
    chao2.set_position(2500,janela.height/2.5+chao2.height)
    chao3.set_position(1600,1.5*janela.height/2+chao3.height)
    chao_ponte.set_position(4000,janela.height/2.8+chao_ponte.height)

    portal.set_position(4700+3*portal.width,janela.height/2.8+chao_ponte.height-portal.height)


    chaos.append(chao1)
    chaos.append(chao2)
    chaos.append(chao3)
    chaos.append(chao_ponte)

    chaos.append(portal)

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

            if((x[0].collided(chao1)==False and  x[0].collided(chao2)==False  and x[0].collided(chao3)==False and x[0].collided(chao_ponte)==False) and x[1]==True):
                x[1]=False

            if( (x[1]==False) and ((x[0].collided(chao1)) or (x[0].collided(chao2)) or (x[0].collided(chao3)) or (x[0].collided(chao_ponte))) ):
                x[1]=True
                
            if(x[0].y>janela.height):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1
            if(x[6]==0):
                inimigos.remove(x)
                Ninimigos=Ninimigos-1


        iniF=slime.inimi(prota,inimigos,janela,hitboxsI,hitboxsp)


        inimigos=iniF[0]
        hitboxsI=iniF[1]

        if((prota[0].collided(chao1)==False and prota[0].collided(chao2)==False  and prota[0].collided(chao3)==False and prota[0].collided(chao_ponte)==False) and prota[8]==True):
            prota[8]=False
            prota[0].set_curr_frame(15)
            prota[0].set_initial_frame(15)
            prota[0].set_final_frame(17)
            prota[1].set_curr_frame(15)
            prota[1].set_initial_frame(15)
            prota[1].set_final_frame(17)
            prota[3]=0
            prota[5]=.6

        #aqui a movimentação do player no sentidp Vertical, se a velocidadeY for positiva, ele vai dar um impulso e cair com a gravidade, MAS se a velocidadeY for 0 só tem a gravidade atuando no protagonista



        #quando o protagonista tocar em algo, a VAR chao vira verdade e a gravidade zera
        if( (prota[8]==False) and (((prota[0].collided(chao1) or prota[0].collided(chao2)) and (prota[0].y<=chao1.y-chao1.height)) or (prota[0].collided(chao3) and (prota[0].y<=chao3.y-chao3.height))
        or (prota[0].collided(chao_ponte) and (prota[0].y <= chao_ponte.y-chao_ponte.height*.7))  ) and (prota[0].get_curr_frame()!=14 or prota[1].get_curr_frame()!=14)):
            prota[5]=0
            prota[8]=True
            prota[6]=False
            prota[7]=0

        #aqui é a animação do player ANDANDO, quando a velocidadeX for 0, mostra a ANIM dele parado, mas se for algo diferente, vai para a anim dele andando


        if(teclado.key_pressed('ESC')):
            return var

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
                
        if(protagonista.x<=-1):
            protagonista.x = -1
            protagonistaIn.x = -1

    
        segundo+=janela.delta_time()

        cont+=1

        tempo = int(segundo)

        if(tempo>=1):
            segundo=0
            fps=cont
            cont=0
        
        
        if(protagonista.collided(portal)):
           var+=1
           return var


        ceu.draw()

        vidas[0].draw()
        janela.draw_text(str(fps), 0, 0, 68, (255,255,255), "Calibri")


        for x in chaos:
            x.draw()
            if(prota[0].collided(x) and prota[8]==True):
                renasce=x.x

        prota[0].draw()
        prota[1].draw()
        prota[1].update()
        prota[0].update()

        for y in hitboxsI:
            y.draw()
        for y in hitboxsp:
            y.draw()

        for y in range(Ninimigos):
            if(inimigos[y][2]==True):
                inimigos[y][0].draw()
                inimigos[y][0].update()


        janela.update()
stage1(var)