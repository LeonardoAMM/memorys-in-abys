from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

def inimi(prota,inimigos,janela,hitboxs,hitboxsp):

    for x in inimigos:
        if(x[1]==False):
            x[0].move_y(400*janela.delta_time())
        else:
            x[0].move_y(0)

        x[5]+=janela.delta_time()

        if(((x[0].x-prota[0].x)<100) and ((x[0].x-prota[0].x)>-100) and x[5]>.5 and x[4]==0):
            x[3]=True
        else:
            x[3]=False

        if(x[3]==True and x[4]==0 and x[5]>=.8):
            if((x[0].get_curr_frame()>=13 and x[0].get_curr_frame()<14)  or (x[0].get_curr_frame()>24)):
                x[5]=0
            if((x[0].get_curr_frame()==11) or (x[0].get_curr_frame()==23)):
                hitb=Sprite("imagens/Hitbox.png")
                if(x[0].x>=prota[0].x):
                    hitb.set_position(x[0].x-60,x[0].y)
                else:
                    hitb.set_position(x[0].x+60,x[0].y)
                hitboxs.append(hitb)
            if(x[0].x>=prota[0].x):
                x[0].set_initial_frame(8)
                x[0].set_final_frame(14)
                if(x[0].get_curr_frame() > 14 or x[0].get_curr_frame()<8):
                    x[0].set_curr_frame(8)
            else:
                x[0].set_initial_frame(21)
                x[0].set_final_frame(26)
                if(x[0].get_curr_frame() < 21):
                    x[0].set_curr_frame(21)

        x[7]+=janela.delta_time()

        for z in hitboxsp:
            if(x[0].collided(z) and x[7]>.6):
                x[6]-=1
                x[7]=0

        if( ((x[0].x-prota[0].x)<-100) and (x[1]==True) and ((x[0].x-prota[0].x)>-200)):
            x[4]=200
            x[0].move_x(x[4]*janela.delta_time())
        elif(((x[0].x-prota[0].x)>100) and ((x[0].x-prota[0].x)<300) and (x[1]==True)):
            x[4]=-200
            x[0].move_x(x[4]*janela.delta_time())
        else:
            x[4]=0

        if(x[0].get_curr_frame()>=26):
            x[0].set_curr_frame(0)
        

        if(((x[0].x-prota[0].x) < janela.width) and ((x[0].x-prota[0].x) > -janela.width)):
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
            if(x[0].get_curr_frame() > 8):
                x[0].set_initial_frame(5)

    return inimigos,hitboxs