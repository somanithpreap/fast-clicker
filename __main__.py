import pygame
from random import randint

# Colors RGB values
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKY_BLUE = (200, 255, 255)
RED = (255, 0,0)
GREEN = (0,255, 0)

pygame.init()   # Setup/initalize PyGame

# Setup the background
window = pygame.display.set_mode((500, 500))
window.fill(SKY_BLUE)

clock = pygame.time.Clock() # Create a game timer

class Area():
    def __init__(self, x=0, y=0, width=0, height=0, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def fill(self): # create one ractangle
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def color(self, new_color):
        self.fill_color = new_color

    def is_collide(self, x, y):
        return self.rect.collidepoint(x, y)
    

class Label(Area):
    def set_text(self, text, fsize=20, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Create 4 cards and store it in a list
cards = []
num_cards = 4
for i in range(num_cards):
    card = Label(60 + i*100, 200, 75, 100, YELLOW)
    card.outline(PURPLE, 10)
    card.set_text('CLICK', 26)
    cards.append(card)

points_label = Label(425, 10, 100, 50, SKY_BLUE)
points_label.set_text('Points:', 35)
points_num = Label(450, 32, 100, 50, SKY_BLUE)
points_num.set_text('0', 35)

wait = 0 

points = 0

''' game loop '''
while True:
    # Check for events and updating stats
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pygame.quit()
        #     exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos

            for i in range(num_cards):
                if cards[i].is_collide(x,y): 
                    if i + 1 == click:  # if clicked on correct card
                        points += 1
                        cards[i].color( (0,255,0) )
                    else:               # if wrong
                        points -= 1
                        cards[i].color( (255, 0,0))
                    points_num.set_text(str(points), 35)
                    cards[i].fill()

    # for card in cards:
    #     card.draw(12, 40)

    if wait == 0:
        wait = 35
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)

            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

    points_label.draw()
    points_num.draw()

    clock.tick(40)  # Limit to 40 frames per second
    pygame.display.update() # Update the display
