from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sound import *



def protag(prota,janela,hitboxs,vidas,hitboxp,renasce):
    teclado = Keyboard()

    while(True):

        #se a Var direita for verdade o sprite da esqueda fica invisivel e o da direita aparece, mas caso ela for falsa o da esquerda aparece e o da direita fica invisivel
        if(prota[4]==True):
            prota[1].hide()
            prota[0].unhide()
        else:
            prota[0].hide()
            prota[1].unhide()

        #se apertar D, a VAR da direita vira Verdade, alem de mover os sprites para frente
        if(teclado.key_pressed("RIGHT") and prota[11]==False):
            prota[4]=True
            prota[2] = 300
            prota[0].move_x(prota[2]*janela.delta_time())
            prota[1].move_x(prota[2]*janela.delta_time())
        #Se apertar A, a VAR da direita vira Falso, alem de mover os sprites para tras
        elif(teclado.key_pressed("LEFT") and prota[11]==False):
            prota[4]=False
            prota[2] = -300
            prota[0].move_x(prota[2]*janela.delta_time())
            prota[1].move_x(prota[2]*janela.delta_time())
        else:
            prota[2]=0

        prota[10]+=janela.delta_time()

        if(teclado.key_pressed("Z") and prota[10]>.7 and prota[11]==False):
            prota[9]=True
            prota[10]=0
        if(prota[9]==True and prota[8]==True):
            prota[0].set_initial_frame(20)
            prota[0].set_final_frame(24)
            prota[1].set_initial_frame(20)
            prota[1].set_final_frame(24)
            if((prota[0].get_curr_frame() == 22)):
                hitb=Sprite("imagens/HitboxP.png")
                if(prota[4]==True):
                    hitb.set_position(prota[0].x+60,prota[0].y)
                else:
                    hitb.set_position(prota[0].x-60,prota[0].y)
                hitboxp.append(hitb)
            if((prota[0].get_curr_frame() >= 23 and prota[4]==True) or (prota[1].get_curr_frame() >= 23 and prota[4]==False)):
                prota[9]=False
            if((prota[0].get_curr_frame() < 20 and prota[4]==True)or(prota[1].get_curr_frame() < 20 and prota[4]==False)):
                prota[0].set_curr_frame(20)
                prota[1].set_curr_frame(20)

        for x in hitboxs:
            if(prota[0].collided(x) and prota[11]==False and prota[15]==False):
                vidas[1]-=.5
                prota[15]=True

        prota[14]+=janela.delta_time()

        if(prota[15]==True and prota[14]>1):
            prota[14]=0
            prota[15]=False

        prota[12]+=janela.delta_time()

        if(teclado.key_pressed("C") and prota[12]>.3 and prota[9]==False):
            prota[11]=True
        if(prota[11]==True and prota[8]==True):
            prota[0].set_initial_frame(17)
            prota[0].set_final_frame(19)
            prota[1].set_initial_frame(17)
            prota[1].set_final_frame(19)
            prota[13]+=janela.delta_time()
            if(prota[4]==True):
                prota[0].move_x(400*janela.delta_time())
                prota[1].move_x(400*janela.delta_time())
            else:
                prota[0].move_x(-400*janela.delta_time())
                prota[1].move_x(-400*janela.delta_time())
            if(((prota[0].get_curr_frame() < 17 or prota[0].get_curr_frame() > 19)  and prota[4]==True)or((prota[0].get_curr_frame() < 17 or prota[0].get_curr_frame() > 19) and prota[4]==False)):
                prota[0].set_curr_frame(17)
                prota[1].set_curr_frame(17)
            if(prota[13]>.3):
                prota[13]=0
                prota[11]=False


        #Aqui muda a animação do protagonista enquanto pula, quando ele estiver no chao (VAR chao for verdade) e apertar W, ele muda para essa animação
        #a velocidadeY, ta positivo pq ele da um impulso
        if(teclado.key_pressed("UP") and prota[6]==False and prota[7]>.3):
            if(prota[8]==True):
                prota[6]=False
                prota[7]=0
            elif(prota[8]==False and prota[7]>.5):
                prota[6]=True
            prota[8]=False
            prota[0].set_curr_frame(14)
            prota[0].set_initial_frame(15)
            prota[0].set_final_frame(17)
            prota[1].set_curr_frame(14)
            prota[1].set_initial_frame(15)
            prota[1].set_final_frame(17)
            prota[3]=1
            prota[5]=0

        prota[7]+=janela.delta_time()

        #Aqui muda a animação do protagonista enquanto ele cai, quando ele estava no chao (VAR chao for verdade) e não estiver tocando em mais nada (esses colides dai) ele cai direto
        #a velocidadY esta zerado, pq ele n da um impulso
        if(prota[8]==False):
            if(prota[0].get_curr_frame()>14 or prota[1].get_curr_frame()>14):
                if(prota[3]<=0):
                    prota[3] = 0-((prota[5]-.6)*1000)
                else:
                    prota[3] = 600-(prota[5]*1000)
                prota[0].move_y(-prota[3]*janela.delta_time())
                prota[1].move_y(-prota[3]*janela.delta_time())
                prota[5]+=janela.delta_time()
                prota[11]=False

        if(prota[8]==True and prota[9]==False and prota[11]==False):
            if(prota[2]==0):
                prota[0].set_initial_frame(0)
                prota[0].set_final_frame(6)
                prota[1].set_initial_frame(0)
                prota[1].set_final_frame(6)
                if((prota[0].get_curr_frame() > 6 and prota[4]==True)or(prota[1].get_curr_frame() > 6 and prota[4]==False)):
                    prota[0].set_curr_frame(0)
                    prota[1].set_curr_frame(0)
            else:
                prota[0].set_initial_frame(6)
                prota[1].set_initial_frame(6)
                prota[0].set_final_frame(14)
                prota[1].set_final_frame(14)
                if((prota[0].get_curr_frame()> 14 or prota[0].get_curr_frame() < 6 and prota[4]==True)or(prota[1].get_curr_frame()> 14 or prota[1].get_curr_frame() < 6 and prota[4]==False)):
                    prota[0].set_curr_frame(6)
                    prota[1].set_curr_frame(6)

        if(prota[0].x<=-1):
            prota[0].x = -1
            prota[1].x = -1

   
        if(prota[0].y > janela.height):
            prota[0].set_position(renasce,0)
            prota[1].set_position(renasce,0)

        return prota,vidas,hitboxp