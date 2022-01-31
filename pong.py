import pygame
from sys import exit

WIDHT,HEIGHT = 800,500

pygame.font.init()

screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('Pong game')

FPS = pygame.time.Clock()


player1  = pygame.Rect(30,30,15,100)
player2  = pygame.Rect(750,30,15,100)
ball  = pygame.Rect(WIDHT/2,HEIGHT/2,15,15)

player1_speed = 0
player2_speed = 0

ball_y = 3
ball_x = 4

p1_score = 0
p2_score = 0

def score(p1_score,p2_score):
    myfont = pygame.font.SysFont('consolas', 30)
    textsurface = myfont.render(f'{p1_score} - {p2_score} ', False, "White")

    screen.blit(textsurface, (WIDHT/2-50, 30))

def movements(player1,player2):

    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT
    elif player1.top <= 0:
        player1.top = 0

    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT
    elif player2.top <= 0:
        player2.top = 0

def collisions(ball,ball_x):

    if ball.colliderect(player2):
        ball_x = -ball_x
    elif ball.colliderect(player1):
        ball_x = -ball_x

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -6
            if event.key == pygame.K_s:
                player1_speed = 6
            if event.key == pygame.K_UP:
                player2_speed = -6
            if event.key == pygame.K_DOWN:
                player2_speed = 6

    screen.fill("black")
    pygame.draw.rect(screen,"white",player1)
    pygame.draw.rect(screen, "white", player2)
    pygame.draw.rect(screen,"white",ball)

    score(p1_score,p2_score)

    player1.y += player1_speed
    player2.y += player2_speed

    movements(player1, player2)

    ball.x += ball_x
    ball.y += ball_y

    if ball.bottom >= 500:
        ball_y = -ball_y
    elif ball.top <= 0:
        ball_y = -ball_y
    elif ball.left <= 0:
        ball.center = WIDHT/2,HEIGHT/2
        p2_score += 1
    elif ball.left >= WIDHT:
        ball.center = WIDHT/2,HEIGHT/2
        p1_score += 1

    if ball.colliderect(player2):
        ball_x = -ball_x
    elif ball.colliderect(player1):
        ball_x = -ball_x


    FPS.tick(60)
    pygame.display.flip()