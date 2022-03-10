import pygame
import random

# Константы отвечающие за ширину и высоту дисплея
WIDTH = 360
HEIGHT = 480

# Константы отвечающее за цвета
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
BLACK = 0, 0, 0

# Создание класса игрока
class Player(pygame.sprite.Sprite):
  def __init__(self, pygame.sprite.Sprite):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((40, 40))
    self.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.center = ((WIDTH / 2, HEIGHT / 2))
 
 def update(self):
   self.rect.x += 1
   if self.rect.x > WIDTH:
     self.rect.x = 0

# Инициализация дисплея и спрайтов
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вот что я пока способен делать в pygame")
sprites = pygame.sprite.Group()
player = Player()
sprites.add(display)

# Игровой цикл
active = True
while active:
  # Обработка событий
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      active = False
  
  # Отрисовка экрана и спрайтов
  screen.fill(BLACK)
  sprites.update(screen)
  pygame.display.flip()
  
pygame.quit()
  
