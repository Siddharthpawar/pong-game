import pygame
import random
import sys
import winsound
def ball_animation():
    global ball_speed_x, ball_speed_y,player_score,opponent_score,score_time
        
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        
        ball_speed_y *= -1
        winsound.Beep(900,20)
    if ball.right <= -5 or ball.left >= screen_width+5:
        if ball.right<=-5:
            player_score+=1
            score_time = pygame.time.get_ticks()
            
        elif ball.left>=screen_width+5:
            opponent_score+=1
            score_time = pygame.time.get_ticks()
            
        winsound.Beep(400,500)
        ball_start()

    if ball.colliderect(player) or ball.colliderect(opponent):
        
        ball_speed_x *= -1
        winsound.Beep(1500,20)
        

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if ball_speed_x < 0:
        
        if opponent.top < ball.y:
            opponent.y += opponent_speed
        if opponent.bottom > ball.y:
            opponent.y -= opponent_speed
    else:
        if (opponent.top + 70 > screen_height // 2) and (opponent.top+70-screen_height // 2 >=opponent_speed):
            opponent.top -= opponent_speed
        elif (opponent.top + 70 < screen_height // 2) and (screen_height//2-opponent.top+70 >=opponent_speed):
            opponent.top += opponent_speed
            

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_speed_x, ball_speed_y,font,score_time,light_grey
    
    current_time=pygame.time.get_ticks()
    ball.center = (screen_width//2, screen_height//2)

    if current_time - score_time < 1200:
        three=font2.render('3',1,(200,200,0))
        screen.blit(three,(screen_width//2+20,screen_height//2-30))
        
        
    if 1200<current_time - score_time < 1700:
        two=font2.render('2',1,(200,200,0))
        screen.blit(two,(screen_width//2+20,screen_height//2-30))
        

    if 1700< current_time - score_time < 2100:
        one=font2.render('1',1,(200,200,0))
        screen.blit(one,(screen_width//2+20,screen_height//2-30))
        
        
    if current_time - score_time<2100:
        ball_speed_x,ball_speed_y = 0,0
    else:
        ball_speed_y =7* random.choice((1,-1))
        ball_speed_x =7* random.choice((1,-1))
        score_time=None
        
        
        
    
        
    
   
    pygame.time.delay(400)


# General setup
pygame.init()


# Main Window
screen_width = 1250
screen_height = 650
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
font=pygame.font.SysFont('maiandra gd',80)
font2=pygame.font.SysFont('maiandra gd',38)
# Game Rectangles
ball = pygame.Rect(screen_width // 2 - 9, screen_height // 2 - 9, 18, 18)
player = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height // 2 - 70, 10,140)

# Game Variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 6
opponent_speed = 20
player_score=0
opponent_score=0

#music=pygame.mixer.music.load('song.mp3')
#pygame.mixer.music.play(-1)

score_time=True

run=True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed

        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
        
    if keys[pygame.K_DOWN]:
        player.y += player_speed

        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
        
       



    #Game Logic
    opponent_ai()
    ball_animation()
    #player_animation()
    

    # Visuals 
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball,6)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
    pygame.draw.circle(screen,light_grey,(screen_width // 2, screen_height//2),70,4)
    text_pla=font.render(str(player_score),1,(0,200,200))
    text_opp=font.render(str(opponent_score),1,(0,200,200))
    screen.blit(text_opp,(100,40))
    screen.blit(text_pla,(1050,40))

    if score_time:
        ball_start()
        
    pygame.display.update()

pygame.quit()
    


    

            

        
    

    


    

    
