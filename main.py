import pygame
import random
import time

pygame.init()

def main_menu():
    menu = True
    seleted = 'start'
    while menu:
        sr.fill(DarkGreen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    seleted = "start"
                if event.key == pygame.K_s:
                    seleted = "quit"
                if event.key == pygame.K_RETURN:
                    if seleted == "start":
                        return True
                    else:
                        return False

        f11 = pygame.font.SysFont("Comic sans MS", 90)
        titles = f11.render("Snake Game", True, "yellow")
        f22 = pygame.font.SysFont("Comic sans MS", 75)
        if seleted == 'start':
            start = f22.render("START", True, "black")
        else:
            start = f22.render("START", True, "yellow")
        if seleted == 'quit':
            quits = f22.render("QUIT", True, "black")
        else:
            quits = f22.render("QUIT", True, "yellow")

        sr.blit(titles, (WEIGHT/2 - 300,80))
        sr.blit(start, (WEIGHT / 2 - 200,200))
        sr.blit(quits, (WEIGHT / 2 - 200, 300))

        pygame.display.update()
        clock.tick(fps)

class Snake:
    def __init__(self, x, y, color, speed,size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 1
        self.dir_y = 0
        self.count = 1
        self.heads = []
        self.add_head()

    def add_head(self):
        self.heads.append(Snake_head(self.x, self.y, self.color, self.speed, self.size))

    def draw(self, sr):
        for head in self.heads:
            head.draw(sr)

    def remove_head(self):
        if len(self.heads) > self.count:
            self.heads.pop(0)

    def move(self):
        if self.dir_x == 1:
            self.x += self.speed
        if self.dir_x == -1:
            self.x -= self.speed
        if self.dir_y == 1:
            self.y += self.speed
        if self.dir_y == -1:
            self.y -= self.speed
        self.add_head()
        self.remove_head()

    def move_right(self):
        if self.count == 1:
            self.dir_x = 1
            self.dir_y = 0
        else:
            if self.dir_y != 0:
                self.dir_x = 1
                self.dir_y = 0

    def move_left(self):
        if self.count == 1:
            self.dir_x = -1
            self.dir_y = 0
        else:
            if self.dir_y != 0:
                self.dir_x = -1
                self.dir_y = 0

    def move_down(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = 1
        else:
            if self.dir_x != 0:
                self.dir_x = 0
                self.dir_y = 1

    def move_up(self):
        if self.count == 1:
            self.dir_x = 0
            self.dir_y = -1
        else:
            if self.dir_x != 0:
                self.dir_x = 0
                self.dir_y = -1

    def check_walls(self):
        if self.x <= 0 or self.y <= 0 or self.y >= HEIGHT - self.size or self.x >= WEIGHT - self.size:
            return False
        return True

    def check_snake(self):
        for i in range(len(self.heads)):
            if i != len(self.heads) - 1:
                if self.x == self.heads[i].x and self.y == self.heads[i].y:
                    return False
        return True

    def check_food(self, food_x, food_y):
        if self.x == food_x and self.y == food_y:
            self.count += 1
            return True
        return False

class Snake_head:
    def __init__(self, x, y, color, speed,size):
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.size = size
        self.dir_x = 0
        self.dir_y = 0

    def draw(self, sr):
        pygame.draw.rect(sr, self.color, (self.x, self.y, self.size, self.size))

DarkGreen = (0,100,0)


WEIGHT = 600
HEIGHT = 600


sr = pygame.display.set_mode((WEIGHT, HEIGHT))
title = pygame.display.set_caption('My First Game')
# ico = pygame.image.load('skyicon.PNG')
# pygame.display.set_icon(ico)

fps = 10
clock = pygame.time.Clock()

is_key_d = False
is_key_a = False
is_key_w = False
is_key_s = False

speed = 15
size = 15

food_x = 150
food_y = 150

widht_hero = 15
heaght_hero = 15

snake = Snake(3 * speed, 3 * speed, "white", speed, size)

is_eat = True

f1 = pygame.font.Font(None, 36)
game_over_text = f1.render("Game Over", True, (255,0,0))


is_game_active = main_menu()

while is_game_active:
    sr.fill('black')

    f2 = pygame.font.Font(None, 36)
    score_text = f2.render(str(snake.count), True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                is_key_d = True
            if event.key == pygame.K_a:
                is_key_a = True
            if event.key == pygame.K_w:
                is_key_w = True
            if event.key == pygame.K_s:
                is_key_s = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                    is_key_d = False
            if event.key == pygame.K_a:
                    is_key_a = False
            if event.key == pygame.K_w:
                    is_key_w = False
            if event.key == pygame.K_s:
                    is_key_s = False

    if is_key_d:
        snake.move_right()
    if is_key_a:
        snake.move_left()
    if is_key_w:
        snake.move_up()
    if is_key_s:
        snake.move_down()

    snake.move()
    is_game_active1 = snake.check_walls()
    is_game_active2 = snake.check_snake()
    is_game_active = is_game_active1 and is_game_active2
    is_eat = snake.check_food(food_x,food_y)
    snake.draw(sr)
    if is_eat:
        fps += 1
        food_x = random.randint(0, WEIGHT) * speed % WEIGHT
        food_y = random.randint(0, HEIGHT) * speed % HEIGHT
        # for snake_head in snake.heads:
           # if food_x == snake_head.x

    sr.blit(score_text, (0, 0))
    pygame.draw.rect(sr,(0,0,255),(food_x,food_y,size,size))
    pygame.display.update()
    clock.tick(fps)

sr.blit(game_over_text, (240, 250))
pygame.display.update()
time.sleep(10)


