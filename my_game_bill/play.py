import pygame

from math import sqrt
import numpy


RADIUS = 17  # радиус шариков, в пикселях
dT = 0.35  # интервал времени между обновлением позиции

LOWER_SPEED = 0.15  # постоянная, ниже которой скорость становится равной нулю
acceleration = 0.25  # ускорение, которому подвергаются движущиеся шары

WIDTH = 500  # ширина поля
HEIGHT = 800  # высота поля
BOARD = 30  # ширина бортика


class Balls:

    def __init__(self, position, speed, file_PNG):
        self.nom = file_PNG

        self.x, self.y = position
        self.dx, self.dy = speed
        self.image = pygame.transform.scale(pygame.image.load(file_PNG), (RADIUS * 2, 2 * RADIUS))

    def rebound(self):
        if not BOARD < self.x < (WIDTH - 2 * RADIUS - BOARD):
            self.dx = - self.dx
        if not BOARD < self.y < (HEIGHT - 2 * RADIUS - BOARD):
            self.dy = - self.dy
        if self.x < BOARD:
            self.x = BOARD
        elif self.x > WIDTH - 2 * RADIUS - BOARD:
            self.x = WIDTH - 2 * RADIUS - BOARD
        if self.y < BOARD:
            self.y = BOARD
        elif self.y > HEIGHT - 2 * RADIUS - BOARD:
            self.y = HEIGHT - 2 * RADIUS - BOARD

        if ((self.x <= BOARD + 2 and self.y <= BOARD + 3) or (
                self.x >= WIDTH - 2 * RADIUS - BOARD and self.y <= BOARD + 10) or
                (self.y >= HEIGHT - 2 * RADIUS - BOARD and self.x <= BOARD + 10) or
                (self.y >= HEIGHT - 2 * RADIUS - BOARD and self.x >= WIDTH - BOARD - 2 * RADIUS) or
                (self.x <= BOARD + 10 and HEIGHT / 2 - 5 < self.y < HEIGHT / 2 + 5) or
                (self.x >= WIDTH - BOARD - 2 * RADIUS - 10 and HEIGHT / 2 - 5 < self.y < HEIGHT / 2 + 5)):
            self.x = 1000
            self.y = 1000
            self.dx = 0
            self.dy = 0

        if self.nom == "img/first.PNG" and self.x == 1000:
            self.x = 230
            self.y = 717

    def collision(self, b):
        if self.dist(b) <= 2 * RADIUS:
            nx = self.x - b.x
            ny = self.y - b.y
            n = (nx, ny)

            if nx ** 2 + ny ** 2 != 0:
                nx = nx / numpy.linalg.norm(n)
                ny = ny / numpy.linalg.norm(n)
                # n = (nx, ny)

                # вращение pi / 2 прямого направления вектора n например для нормализованного тангенциального вектора g
                gx = -ny
                gy = nx
                # g = (gx, gy)

                # если шарики наложены друг на друга, мы заменим их в положении строгого контакта
                delta = 2 * RADIUS - self.dist(b)
                if delta > 0:
                    b.x -= delta / 2 * nx
                    self.x += delta / 2 * nx
                    b.y -= delta / 2 * ny
                    self.y += delta / 2 * ny

                # разложение скоростей по новой ортонормированной базе (n, g)
                dx1 = nx * self.dx + ny * self.dy
                dy1 = gx * self.dx + gy * self.dy

                dx2 = nx * b.dx + ny * b.dy
                dy2 = gx * b.dx + gy * b.dy

                # обмен нормальных компонентов; тангенциальные компоненты сохраняются
                self.dx = nx * dx2 + gx * dy1
                self.dy = ny * dx2 + gy * dy1
                b.dx = nx * dx1 + gx * dy2
                b.dy = ny * dx1 + gy * dy2

    def moves(self):
        self.x += self.dx * dT
        self.y += self.dy * dT

    def dist(self, b):
        return sqrt((self.x - b.x) ** 2 + (self.y - b.y) ** 2)

    def poster(self, screen_my):
        screen_my.blit(self.image, (self.x, self.y))

    def calSpeed(self):
        v = sqrt(self.dx ** 2 + self.dy ** 2)

        # скороть слишком мала мы останавливаем мяч
        if v < LOWER_SPEED:
            self.dx = 0
            self.dy = 0
        # в противном случае скорость уменьшается
        else:
            self.dx = self.dx - acceleration * dT * self.dx / v
            self.dy = self.dy - acceleration * dT * self.dy / v


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

continue_on = True
horloge = pygame.time.Clock()
while continue_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continue_on = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                mouse_get_pos = pygame.mouse.get_pos()  # mouse_get_pos - мышка в момент нажатия
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

    # расчет новой скорости, смещения, отскоков и столкновений
    for i in lists:
        i.poster(screen_my)
        i.moves()
        i.rebound()
        i.calSpeed()

    gestion_collisions(lists)

    pygame.display.flip()

    # задержка времени
    horloge.tick(25)


