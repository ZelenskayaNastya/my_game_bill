from balls import Balls, RADIUS, WIDTH, HEIGHT, BOARD
import pygame
from mouse import Cue
from livewires import games


def starting_position():
    list_balls = []
    ball = open("ball.txt", "r")
    for line in ball:
        C = ""
        L = line.split(",")
        for i in range(len(L[2]) - 1):
            C = C + L[2][i]
        list_balls.append(Balls((int(L[0]), int(L[1])), (0, 0), C))
    return list_balls


def gestion_collisions(list_balls):
    for i in range(len(list_balls)):
        for j in range(i + 1, int(len(list_balls))):
            (list_balls[i]).collision(list_balls[j])



pygame.init()
screen_my = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("BILLIARD")

fond = pygame.image.load("img/table.jpg")
black = pygame.transform.scale(pygame.image.load('img/black.png'), (RADIUS * 2, 2 * RADIUS))

lists = starting_position()
R = lists[len(lists) - 1]

the_cue = Cue()
games.screen.add(the_cue)
# games.mouse.is_visible = False

continue_on = True
horloge = pygame.time.Clock()
while continue_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue_on = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                mouse_get_pos = pygame.mouse.get_pos()  # posM - координаты положения мыши в момент нажатия
                # новый вектор скорости белого шара - это вектор, идущий от центра шара к положению мыши
                R.dx = mouse_get_pos[0] - R.x
                R.dy = mouse_get_pos[1] - R.y

            # щелкните правой кнопкой мыши, чтобы перезапустить игру
            if event.button == 3:
                lists = starting_position()
                R = lists[len(lists) - 1]
    # создаем экран
    screen_my.blit(fond, (0, 0))
    screen_my.blit(black, (15, 10))
    screen_my.blit(black, (WIDTH - BOARD - 30, 10))
    screen_my.blit(black, (21, HEIGHT - BOARD - 22))
    screen_my.blit(black, (WIDTH - 50, HEIGHT - 50))
    screen_my.blit(black, (10, (HEIGHT / 2) - 18))
    screen_my.blit(black, (WIDTH - BOARD - 15, (HEIGHT / 2) - 18))

    # расчет новой скорости, смещения, проверка отскоков и столкновений
    for b in lists:
        b.poster(screen_my)
        b.moves()
        b.rebound()
        b.calSpeed()

    gestion_collisions(lists)

    pygame.display.flip()

    # задержка времени
    horloge.tick(25)






