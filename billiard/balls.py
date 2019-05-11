from math import sqrt
import numpy
import pygame

RADIUS = 17  # радиус шариков, в пикселях
dT = 0.35  # интервал времени между обновлением позиции

LOWER_SPEED = 0.15  # постоянная, ниже которой скорость становится равной нулю
acceleration = 0.25  # ускорение, которому подвергаются движущиеся шары

WIDTH = 500  # ширина поля
HEIGHT = 800  # высота поля
BOARD = 25  # ширина бортика


class Balls:

    def __init__(self, position, speed, file_PNG):
        self.nom = file_PNG

        self.x, self.y = position
        self.vx, self.vy = speed
        self.image = pygame.transform.scale(pygame.image.load(file_PNG), (RADIUS * 2, 2 * RADIUS))

    def poster(self, screen_my):
        screen_my.blit(self.image, (self.x, self.y))

    def moves(self):
        self.x += self.vx * dT
        self.y += self.vy * dT

    def rebound(self):
        if not BOARD < self.x < WIDTH - 2 * RADIUS - BOARD:
            self.vx = - self.vx
        if not (BOARD < self.y < HEIGHT - 2 * RADIUS - BOARD):
            self.vy = - self.vy
        if self.x < BOARD:
            self.x = BOARD
        elif self.x > WIDTH - 2 * RADIUS - BOARD:
            self.x = WIDTH - 2 * RADIUS - BOARD
        if self.y < BOARD:
            self.y = BOARD
        elif self.y > HEIGHT - 2 * RADIUS - BOARD:
            self.y = HEIGHT - 2 * RADIUS - BOARD

        if ((self.x <= BOARD + 3 and self.y <= BOARD + 3) or (
                self.x >= WIDTH - 2 * RADIUS - BOARD and self.y <= BOARD + 10) or
                (self.y >= HEIGHT - 2 * RADIUS - BOARD and self.x <= BOARD + 10) or
                (self.y >= HEIGHT - 2 * RADIUS - BOARD and self.x >= WIDTH - BOARD - 2 * RADIUS) or
                (self.x <= BOARD + 10 and HEIGHT / 2 - 5 < self.y < HEIGHT / 2 + 5) or
                (self.x >= WIDTH - BOARD - 2 * RADIUS - 10 and HEIGHT / 2 - 5 < self.y < HEIGHT / 2 + 5)):
            self.x = 1000
            self.y = 1000
            self.vx = 0
            self.vy = 0

        if self.nom == "img/first.PNG" and self.x == 1000:
            self.x = 230
            self.y = 717

    def dist(self, b):
        return sqrt((self.x - b.x) ** 2 + (self.y - b.y) ** 2)

    def collision(self, b):
        if self.dist(b) <= 2 * RADIUS:
            nx = self.x - b.x
            ny = self.y - b.y
            n = (nx, ny)
            # нормализация n
            if nx ** 2 + ny ** 2 != 0:
                nx = nx / numpy.linalg.norm(n)
                ny = ny / numpy.linalg.norm(n)
                # n = (nx, ny)

                # вращение pi / 2 прямого направления вектора n например для нормализованного тангенциального вектора g
                gx = -ny
                gy = nx
                # g = (gx, gy)

                # если шарики наложены друг на друга, мы заменим их в положении строгого контакта
                # (здесь вектор g бесполезен)
                delta = 2 * RADIUS - self.dist(b)
                if delta > 0:
                    b.x -= delta / 2 * nx
                    self.x += delta / 2 * nx
                    b.y -= delta / 2 * ny
                    self.y += delta / 2 * ny

                # разложение скоростей по новой ортонормированной базе (n, g)
                dx1 = nx * self.vx + ny * self.vy
                dy1 = gx * self.vx + gy * self.vy

                dx2 = nx * b.vx + ny * b.vy
                dy2 = gx * b.vx + gy * b.vy

                # обмен нормальных компонентов; тангенциальные компоненты сохраняются
                self.vx = nx * dx2 + gx * dy1
                self.vy = ny * dx2 + gy * dy1
                b.vx = nx * dx1 + gx * dy2
                b.vy = ny * dx1 + gy * dy2

    def calSpeed(self):
        v = sqrt(self.vx ** 2 + self.vy ** 2)

        # скороть слишком мала мы останавливаем мяч
        if v < LOWER_SPEED:
            self.vx = 0
            self.vy = 0
        # в противном случае скорость уменьшается
        else:
            self.vx = self.vx - acceleration * dT * self.vx / v
            self.vy = self.vy - acceleration * dT * self.vy / v
