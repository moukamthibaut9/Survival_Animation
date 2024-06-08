import pygame, sys
import random

pygame.init()
ecran=(L_ecran,H_ecran)=(1350,500)
(nbr_cell_x,nbr_cell_y)=(150,75)
(dim_cell_x,dim_cell_y)=(L_ecran/nbr_cell_x,H_ecran/nbr_cell_y)
fenetre=(L_fenetre,H_fenetre)=(nbr_cell_x*dim_cell_x,nbr_cell_y*dim_cell_y)
normal_dog_speed=5
normal_proie_speed=3
dog_stop_time=5
ticks_per_sec=1000 # permet une conversion des micro-secondes en secondes.

# Chargement des images
image_chien=pygame.image.load("animal_de_compagnie1.png")
image_proie=pygame.image.load("Oiseau1.png")


fenetre_jeu=pygame.display.set_mode(fenetre)
pygame.display.set_caption("Appretissage_Pygame3")


class Sous_Images:
    def __init__(self):
        self.dico_chien={}
        self.rects_chien_assis=[pygame.Rect(8,17,38,33),pygame.Rect(47,19,38,33),pygame.Rect(48,20,38,33),
                pygame.Rect(126,20,33,35),pygame.Rect(160,16,32,37),pygame.Rect(193,17,31,36),
                pygame.Rect(224,17,31,36),pygame.Rect(258,18,27,35),pygame.Rect(286,18,28,35)
            ]
        self.rects_chien_cours=[pygame.Rect(4,298,55,28),pygame.Rect(59,298,55,28),pygame.Rect(114,298,55,28),
                        pygame.Rect(168,297,55,28),pygame.Rect(223,298,55,28),pygame.Rect(281,298,55,28),
                        pygame.Rect(334,298,55,28),pygame.Rect(388,297,53,28)
                        ]
        self.rects_chien_marche_abs=[pygame.Rect(0,142,48,33),pygame.Rect(47,142,48,33),pygame.Rect(92,142,48,33),
                                pygame.Rect(139,142,45,33),pygame.Rect(185,142,45,33),pygame.Rect(233,142,45,33),
                                pygame.Rect(280,142,45,33),pygame.Rect(327,142,45,33),pygame.Rect(373,142,45,33),
                                pygame.Rect(419,142,48,33)
                            ]
        self.rects_chien_marche_ord=[pygame.Rect(302,341,20,53),pygame.Rect(330,341,20,53),
                                pygame.Rect(353,341,22,53),pygame.Rect(381,341,20,53)
                            ]
        self.dico_proie={}
        self.rects_proie_marche=[pygame.Rect(26,13,94,116),pygame.Rect(164,13,94,116),pygame.Rect(298,13,94,116),
                                 pygame.Rect(436,13,94,116),pygame.Rect(24,148,94,116),pygame.Rect(162,148,94,116)
                                 ,pygame.Rect(296,148,94,116),pygame.Rect(434,148,94,116),pygame.Rect(26,282,94,116)
                                 ,pygame.Rect(165,282,94,116),pygame.Rect(296,282,94,116),pygame.Rect(433,282,94,116)
                                ]
    def obtention_sous_images_chien(self,rect1,dir1,rect2,dir2):
        for img in self.rects_chien_marche_abs:
            sous_image_chien=self.rects_chien_marche_abs.pop(0)
            sous_image_chien=image_chien.subsurface(sous_image_chien)
            sous_image_chien=pygame.transform.scale(sous_image_chien,(rect1.width,rect1.height))
            if dir1==-1 and rect1.top<H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,True,True)
            elif dir1==-1 and rect1.bottom>H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,True,False)
            elif dir1==1 and rect1.top<H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,False,True)
            self.rects_chien_marche_abs.append(sous_image_chien)
        self.dico_chien["marche_abs"]=self.rects_chien_marche_abs
        for img in self.rects_chien_marche_ord:
            sous_image_chien=self.rects_chien_marche_ord.pop(0)
            sous_image_chien=image_chien.subsurface(sous_image_chien)
            sous_image_chien=pygame.transform.scale(sous_image_chien,(rect2.width,rect2.height))
            if dir2==1 :
                sous_image_chien=pygame.transform.flip(sous_image_chien,False,True)
            self.rects_chien_marche_ord.append(sous_image_chien)
        self.dico_chien["marche_ord"]=self.rects_chien_marche_ord
        for img in self.rects_chien_cours:
            sous_image_chien=self.rects_chien_cours.pop(0)
            sous_image_chien=image_chien.subsurface(sous_image_chien)
            sous_image_chien=pygame.transform.scale(sous_image_chien,(rect1.width,rect1.height))
            if dir1==-1 and rect1.top<H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,True,True)
            elif dir1==-1 and rect1.bottom>H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,True,False)
            elif dir1==1 and rect1.top<H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,False,True)
            self.rects_chien_cours.append(sous_image_chien)
        self.dico_chien["cours"]=self.rects_chien_cours
        for img in self.rects_chien_assis:
            sous_image_chien=self.rects_chien_assis.pop(0)
            sous_image_chien=image_chien.subsurface(sous_image_chien)
            sous_image_chien=pygame.transform.scale(sous_image_chien,(rect1.width,rect1.height))
            if rect1.top<H_fenetre/2:
                sous_image_chien=pygame.transform.flip(sous_image_chien,False,True)
            self.rects_chien_assis.append(sous_image_chien)
        self.dico_chien["assis"]=self.rects_chien_assis

        return self.dico_chien
    def obtention_sous_images_proie(self,rect_p,dir_p,):
        for rect in self.rects_proie_marche:
            sous_image_proie=self.rects_proie_marche.pop(0)
            sous_image_proie=image_proie.subsurface(sous_image_proie)
            sous_image_proie=pygame.transform.scale(sous_image_proie,(rect_p.width,rect_p.height))
            if dir_p==1 and rect_p.top<H_fenetre/2:
                sous_image_proie=pygame.transform.flip(sous_image_proie,False,True)
            elif dir_p==-1 and rect_p.top<H_fenetre/2:
                sous_image_proie=pygame.transform.flip(sous_image_proie,True,True)
            if dir_p==-1 and rect_p.bottom>H_fenetre/2:
                sous_image_proie=pygame.transform.flip(sous_image_proie,True,False)
            self.rects_proie_marche.append(sous_image_proie)
        self.dico_proie["marche"]=self.rects_proie_marche

        return self.dico_proie

class Terrain:
    def __init__(self):
        self.rect_terrain=pygame.Rect(0,0,L_fenetre,H_fenetre)
    def dessin_terrain(self):
        pygame.draw.rect(fenetre_jeu,pygame.Color("White"),self.rect_terrain,5)           

class Chien:
    def __init__(self):
        self.rect_chien=0
        self.rect1_chien=pygame.Rect(0,65*dim_cell_y,20*dim_cell_x,10*dim_cell_y)
        self.rect2_chien=pygame.Rect(L_fenetre-self.rect1_chien.height,H_fenetre-self.rect1_chien.width,10*dim_cell_y,20*dim_cell_x)
        self.direction1_chien=1
        self.direction2_chien=0
        self.current_dog_direction=self.direction1_chien
        self.current_dog_position=self.rect1_chien.y
        self.current_dog_dimensions=[self.rect1_chien.width,self.rect1_chien.height]
        self.vitesse_chien=normal_dog_speed
        self.dog_stop_start_time=0
        self.dog_stop_end_time=0
        self.dog_stop=False
        self.actual_dog_state="marche_abs"
        self.sous_image_index=0
    def dessin_chien(self):
        if self.rect_chien==self.rect2_chien:
            self.actual_dog_state="marche_ord"
        else:
            if self.actual_dog_state=="marche_ord"and self.dog_stop==False:
                self.actual_dog_state="marche_abs"
            if self.actual_dog_state=="marche_ord"and self.dog_stop==True:
                self.actual_dog_state="assis"
        sous_images=Sous_Images()
        dico_images_chien=sous_images.obtention_sous_images_chien(self.rect1_chien,self.direction1_chien,self.rect2_chien,self.direction2_chien)
        if self.sous_image_index>=len(dico_images_chien[self.actual_dog_state]):
            self.sous_image_index=0
        printed_image=dico_images_chien[self.actual_dog_state][self.sous_image_index]
        if self.rect1_chien.right>=L_fenetre or self.rect1_chien.left<=0:
            self.rect_chien=self.rect2_chien
        else :
            self.rect_chien=self.rect1_chien
            #pygame.draw.rect(fenetre_jeu,pygame.Color("yellow"),self.rect_chien)
        fenetre_jeu.blit(printed_image,self.rect_chien)
        if self.actual_dog_state=="marche_ord" or self.actual_dog_state=="assis": pygame.time.delay(40)
        else: pygame.time.delay(30)
        if self.actual_dog_state=="assis" and self.sous_image_index==len(dico_images_chien["assis"])-1:pass
        else: self.sous_image_index+=1
    def deplacement_chien(self):
        self.dog_stop_end_time=pygame.time.get_ticks()//ticks_per_sec
        if (self.dog_stop_end_time-self.dog_stop_start_time==dog_stop_time):
            self.rect1_chien.width=self.current_dog_dimensions[0]
            self.rect1_chien.height=self.current_dog_dimensions[1]
            self.rect1_chien.y=self.current_dog_position
            self.direction1_chien=self.current_dog_direction
            self.actual_dog_state="marche_abs"
            self.dog_stop=False
        if self.direction1_chien==1:  ##############   Chien en deplacement de G-->D   ################
            if (self.rect1_chien.right>=L_fenetre and self.rect1_chien.top<H_fenetre/2):
                self.direction1_chien=0   #Chien en haut, atteint la limite
                self.direction2_chien=1   #Doit descendre
                self.rect2_chien.y=0
            elif (self.rect1_chien.right>=L_fenetre and self.rect1_chien.bottom>H_fenetre/2):
                self.direction1_chien=0   #Chien en bas, atteint la limite
                self.direction2_chien=-1   #Doit monter
                self.rect2_chien.y=H_fenetre-self.rect1_chien.width
            self.rect2_chien.x=L_fenetre-self.rect1_chien.height
        elif self.direction1_chien==-1:  ##############   Chien en deplacement de D-->G   ################
            if (self.rect1_chien.left<=0 and self.rect1_chien.top<H_fenetre/2):
                self.direction1_chien=0  #Chien en haut, atteint la limite
                self.direction2_chien=1  #Doit descendre
                self.rect2_chien.y=0
            elif (self.rect1_chien.left<=0 and self.rect1_chien.bottom>H_fenetre/2):
                self.direction1_chien=0   #Chien en bas, atteint la limite
                self.direction2_chien=-1   #Doit monter
                self.rect2_chien.y=H_fenetre-self.rect1_chien.width
            self.rect2_chien.x=0
        if self.direction2_chien==1:  ##############   Chien en deplacement de H-->B   ################
            if (self.rect2_chien.bottom>=H_fenetre and self.rect2_chien.left<L_fenetre/2):
                self.direction1_chien=1   #Chien a gauche, atteint la limite
                self.direction2_chien=0   #Doit aller a droite
                self.rect1_chien.x=0
            elif (self.rect2_chien.bottom>=H_fenetre and self.rect2_chien.right>L_fenetre/2):
                self.direction1_chien=-1   #Chien a droite, atteint la limite
                self.direction2_chien=0   #Doit aller a gauche
                self.rect1_chien.x=130*dim_cell_x
            self.rect1_chien.y=65*dim_cell_y
        elif self.direction2_chien==-1:  ##############   Chien en deplacement de B-->H   ################
            if (self.rect2_chien.top<=0 and self.rect2_chien.left<L_fenetre/2):
                self.direction1_chien=1   #Chien a gauche, atteint la limite
                self.direction2_chien=0   #Doit aller a droite
                self.rect1_chien.x=0
            elif (self.rect2_chien.top<=0 and self.rect2_chien.right>L_fenetre/2):
                self.direction1_chien=-1   #Chien a droite, atteint la limite
                self.direction2_chien=0   #Doit aller a gauche
                self.rect1_chien.x=130*dim_cell_x
            self.rect1_chien.y=0
        self.rect1_chien.x+=self.direction1_chien*self.vitesse_chien
        self.rect2_chien.y+=self.direction2_chien*self.vitesse_chien
    

class Proie:
    def __init__(self):
        self.rect_proie=pygame.Rect(random.choice([-15*dim_cell_x,(nbr_cell_x+15)*dim_cell_x]),\
                                    random.choice([0,(nbr_cell_y-10)*dim_cell_y]),\
                                    10*dim_cell_x,10*dim_cell_y)
        self.direction_proie=0
        self.vitesse_proie=normal_proie_speed
        self.proie_state="marche"
        self.sous_image_index=0
    def dessin_proie(self):
        self.sous_images=Sous_Images()
        dico_images_proie=self.sous_images.obtention_sous_images_proie(self.rect_proie,self.direction_proie)
        if self.sous_image_index>=len(dico_images_proie[self.proie_state]):
            self.sous_image_index=0
            #pygame.draw.rect(fenetre_jeu,pygame.Color("green"),self.rect_proie)
        fenetre_jeu.blit(dico_images_proie[self.proie_state][self.sous_image_index],self.rect_proie)
        self.sous_image_index+=1
    def deplacement_proie(self):
        self.rect_proie.x+=self.direction_proie*self.vitesse_proie
            

class Game:
    def __init__(self):
        self.terrain=Terrain()
        self.chien=Chien()
        self.proie=Proie()
    def dessin_elements(self):
        self.terrain.dessin_terrain()
        self.chien.rect1_chien.clamp_ip(self.terrain.rect_terrain)
        self.chien.rect2_chien.clamp_ip(self.terrain.rect_terrain)
        self.chien.dessin_chien()
        self.proie.dessin_proie()
    def deplacement_animaux(self):
        self.chien.deplacement_chien()
        self.proie.deplacement_proie()
        if self.proie.rect_proie.right>=0 and self.proie.rect_proie.left<=L_fenetre:
            if (self.proie.rect_proie.top<H_fenetre/2 and self.chien.rect1_chien.top<H_fenetre/2)\
            or (self.proie.rect_proie.bottom>H_fenetre/2 and self.chien.rect1_chien.bottom>H_fenetre/2):
                if self.proie.direction_proie==1 and self.chien.direction1_chien==-1:
                    self.proie.direction_proie=-1
                elif self.proie.direction_proie==1 and self.chien.direction1_chien==1:
                    if self.proie.rect_proie.centerx<self.chien.rect1_chien.centerx:
                        self.chien.direction1_chien=-1
                    else:pass
                elif self.proie.direction_proie==-1 and self.chien.direction1_chien==1:
                    self.proie.direction_proie=1
                elif self.proie.direction_proie==-1 and self.chien.direction1_chien==-1:
                    if self.proie.rect_proie.centerx>self.chien.rect1_chien.centerx:
                        self.chien.direction1_chien=1
                        self.proie.direction_proie=1
                    else:pass
                elif self.chien.dog_stop==True:
                    if self.proie.rect_proie.centerx<self.chien.rect1_chien.centerx:
                        self.proie.direction_proie=-1
                    else: self.proie.direction_proie=1
                if self.chien.actual_dog_state!="assis": self.chien.actual_dog_state="cours"
                self.chien.vitesse_chien=3*normal_dog_speed
                self.proie.vitesse_proie=4*normal_proie_speed
        else:
            if self.chien.direction1_chien!=0:
                self.chien.actual_dog_state="marche_abs"
                self.chien.vitesse_chien=normal_dog_speed
                self.proie.vitesse_proie=normal_proie_speed
        if self.proie.rect_proie.x<=-20*dim_cell_x or self.proie.rect_proie.x>=L_fenetre+20*dim_cell_x:
            self.proie=Proie()
        if (self.chien.rect1_chien.colliderect(self.proie.rect_proie) and self.chien.direction1_chien!=0):
            self.chien.dog_stop_start_time=pygame.time.get_ticks()//ticks_per_sec
            self.chien.current_dog_direction=self.chien.direction1_chien
            self.chien.current_dog_position=self.chien.rect1_chien.y
            self.chien.rect1_chien.width=9*dim_cell_x
            self.chien.rect1_chien.height=18*dim_cell_y
            self.chien.direction1_chien=0
            self.chien.dog_stop=True
            self.chien.actual_dog_state="assis"
            self.proie=Proie()


pygame.time.set_timer(pygame.USEREVENT,1000)

game=Game()
lancer=True
while lancer:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            lancer=False
        if event.type==pygame.USEREVENT:
            if game.proie.direction_proie==0:
                if game.proie.rect_proie.x<0: game.proie.direction_proie=1
                elif game.proie.rect_proie.x>L_fenetre: game.proie.direction_proie=-1
    
    fenetre_jeu.fill(pygame.Color("gray"))
    game.dessin_elements()
    game.deplacement_animaux()
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(100)

pygame.quit()
sys.exit()
