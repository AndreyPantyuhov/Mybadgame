import pygame
import random

# Константы отвечающие за ширину и высоту дисплея
WIDTH_DISPLAY = 360
HEIGHT_DISPLAY = 480

# Константы отвечающие за ширину и высоту игрока
WIDTH_PLAYER = 40
HEIGHT_PLAYER = 40

# Переменные отвечающие за передвижение игрока: r - right, l - left, u - up, d - down
r = False
l = False
u = False
d = False

# Константы отвечающее за цвета
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# Создание класса игрока
class Player(pygame.sprite.Sprite):
  # Инициализация игрока
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((WIDTH_PLAYER, HEIGHT_PLAYER))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.center = ((WIDTH_DISPLAY / 2, HEIGHT_DISPLAY / 2))
 
 # Обновление позиции игрока 
 def update(self):
   if r == True:
    self.rect.x += 1
   if l == True:
    self.rect.y -= 1
   if u == True:
    self.rect.y -= 1
   if d == True:
    self.rect.y += 1
    
   if self.rect.x > WIDTH_DISPLAY:
     self.rect.x = 0
   if self.rect.x < 0:
     self.rect.x = WIDTH_DISPLAY
   if self.rect.top < HEIGHT_DISPLAY:
     self.rect.y = 0
   if self.rect.bottom < 0:
     self.rect.y = HEIGHT_DISPLAY

# Инициализация дисплея и спрайтов
pygame.init()
screen = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
pygame.display.set_caption("Вот что я пока способен сделать в pygame")
sprites = pygame.sprite.Group()
player = Player()
sprites.add(player)

# Игровой цикл
active = True
while active:
  # Обработка событий
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      active = False
  
  # Отрисовка экрана и спрайтов
  screen.fill(BLACK)
  sprites.draw(screen)
  sprites.update()
  pygame.display.flip()
  
pygame.quit()
  
