import pygame
import random
pygame.init()

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()
playerimg = pygame.image.load('player.png')
playerimg_size = playerimg.get_size()
playerimg = pygame.transform.scale(playerimg,(playerimg_size[0]//10,playerimg_size[1]//10))
enemyimg = pygame.image.load('asteroid.png')
enemyimg_size = enemyimg.get_size()
enemyimg = pygame.transform.scale(enemyimg,(enemyimg_size[0]//10,enemyimg_size[1]//10))
background_img = pygame.image.load('galaxy.jpg')
background_img = pygame.transform.scale(background_img,(window.get_width(),window.get_height()))
bulletimg = pygame.image.load('bullet.png')
bulletimg_size = bulletimg.get_size()
bulletimg = pygame.transform.scale(bulletimg,(bulletimg_size[0]//15,bulletimg_size[1]//15))
bullet_sound = pygame.mixer.Sound('laser.wav')
bullet_sound.set_volume(0.1)
background_music = pygame.mixer.Sound('space.ogg')
background_music.set_volume(0.1)
background_music.play(-1)
asteroid_expolison = pygame.mixer.Sound('AlienExplosion.wav')
asteroid_expolison.set_volume(0.1)
font = pygame.font.Font('freesansbold.ttf',32)




class Gameobject():
    def __init__(self,x,y,img,speed):
        self.rect = img.get_rect(center=((x,y)))
        self.speed = speed
        self.image = img
        self.level = 1
        self.hp = 100
class Player(Gameobject):
    def move(self):
        if player.hp > 0:
            keylist = pygame.key.get_pressed()
            if keylist[pygame.K_d] == True:
                self.rect.x += self.speed
            elif keylist[pygame.K_a] == True:
                self.rect.x -= self.speed
    def health(self):
        start_x = self.rect.x
        start_y = self.rect.y - 10
        end_x =  self.rect.x + self.hp
        end_y = self.rect.y - 10
        if self.hp > 0:
            pygame.draw.line(window,'green',(start_x,start_y),(end_x,end_y),10)
        else:
            self.image.set_alpha(0)
    def super_Shoot(self):
        if self.hp > 0:        
            if self.level >= 3:
                if pygame.mouse.get_pressed()[0] == True:
                    bullet = Bullet(self.rect.centerx,self.rect.top,bulletimg,10)
                    bullet_list.append(bullet)
                    bullet_sound.play()



class Bullet(Gameobject):
    def move(self):
        if self.rect.bottom >= 0:
            self.rect.y -= self.speed
        else:
            if self in bullet_list:
                bullet_list.remove(self)
    def collision(self):
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                bullet_list.remove(self)
                if enemy.hp > 0:
                    enemy.hp -= 20
                else:
                    enemy_list.remove(enemy)
                    asteroid_expolison.play()
                break
        if len(enemy_list) == 0:
            player.level += 1
            spawn_enemy()        
class Enemy(Gameobject):
    def move(self):
        self.rect.y += self.speed
        if self.rect.top >= window.get_height():
            self.rect.bottom = 0
            self.rect.centerx = random.randint(100,window.get_width()-100)
            

    def collision(self):
        if self.rect.colliderect(player.rect):
            player.hp -= 10
            enemy_list.remove(self)
            asteroid_expolison.play()
    
        

bullet_list = []
enemy_list = []
difficulty = 1
def spawn_enemy():
    for a in range(player.level):
        y = a * 100
        for i in range(player.level):
            #if random.randint(1,3) == 2:
            x = 100 + i * 100
            enemy = Enemy(x,-y,enemyimg,1 + player.level/10)
            enemy.hp = player.level
            enemy_list.append(enemy)
    


player = Player(window.get_width()/2,window.get_height()/1.2,playerimg,10)
spawn_enemy()



canplay = True
while canplay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            canplay = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.hp > 0:
                    bullet_sound.play()
                    bullet = Bullet(player.rect.centerx,player.rect.centery,bulletimg,10)
                    bullet_list.append(bullet)

    window.fill('blue')
    window.blit(background_img,(0,0))
    textimg = font.render('Уровень:'+str(player.level),True,'white')
    text_rect = textimg.get_rect(center=(100,20))
    window.blit(textimg,text_rect)
    
    for enemy in enemy_list:
        window.blit(enemyimg,enemy.rect)
        enemy.move()
        enemy.collision()
    for bullet in bullet_list:
        window.blit(bulletimg,bullet.rect)
        bullet.collision()
        bullet.move()
        
    window.blit(playerimg,player.rect)
    player.move()
    player.health()
    player.super_Shoot()
    
    fps.tick(60)

    pygame.display.update()