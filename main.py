import pygame
from pygame.locals import *

#início do display no pygames
pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Jogo das três pistas")
screen.fill((0,0,0))
pygame.display.update()

#gerar fonte
text_font = pygame.font.SysFont("Arial", 30)

#gerar texto
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#carregar uma imagem
start_img = pygame.image.load('start_btn_resized_resized.png').convert_alpha()
next_img = pygame.image.load('next.png').convert_alpha()


#class geradora de button
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
		#pegar a posição do mouse
        pos = pygame.mouse.get_pos()

        #verificar se o mouse pasosu por cima e clicou
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                question1()
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

        #butão questão 1
    def draw_question1(self):
        action = False
		#pegar a posição do mouse
        pos = pygame.mouse.get_pos()

        #verificar se o mouse pasosu por cima e clicou
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                random = 0
                while random < 4:
                    random =+1
                    
                
        #fazer com que o botão possa ser pressionado mais de uma vez        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))


#instância de um button        
start_button = Button(250, 1, start_img, 1)



#função para mostra no display
def questions():
    draw_text("Question number 1", text_font, (255, 255, 255), -1, 1)
    draw_text("Question number 2", text_font, (255, 255, 255), -1, 50)
    draw_text("Question number 3", text_font, (255, 255, 255), -1, 100)
    draw_text("Question number 4", text_font, (255, 255, 255), -1, 150)
    draw_text("Question number 5", text_font, (255, 255, 255), -1, 200)
    draw_text("Question number 6", text_font, (255, 255, 255), -1, 250)
    draw_text("Question number 7", text_font, (255, 255, 255), -1, 300)
    draw_text("Question number 8", text_font, (255, 255, 255), -1, 350)
    draw_text("Question number 9", text_font, (255, 255, 255), -1, 400)
    draw_text("Question number 10", text_font, (255, 255, 255), -1, 450)
    
questions()




def question1():
    #display da questão 1
    pygame.init()
    running = True
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Jogo das três pistas")
    screen.fill((0,0,0))
    pygame.display.update()

    def perguntas():
        draw_text("organismos da fauna e da flora interagindo entre si", text_font, (255, 255, 255), -1, 1)
        draw_text("comunidades biológicas", text_font, (255, 255, 255), -1, 50)
    perguntas()
    
    start_button = Button(500, 500, next_img, 0.1)
    while running:
        start_button.draw_question1()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()










#display padrão
while running:

    start_button.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.flip()
pygame.quit()

