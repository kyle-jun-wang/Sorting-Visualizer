import pygame

class Button:
    def __init__ (self, win, name, pos1, pos2, pos3, pos4):
        self.win = win
        self.name = name
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4

        self.call = False
        self.color = (211, 211, 211)

        self.draw_button()
        self.draw_text()
        #self.mouse_click()


    def draw_button(self):
        pygame.draw.rect(self.win, self.color, (self.pos1, self.pos2, self.pos3, self.pos4))

    def draw_text(self):
        text = pygame.font.SysFont("Times New Roman", 24)
        text_surface = text.render(self.name, False, (0, 0, 0))
        self.win.blit(text_surface,(self.pos1 + 35, self.pos2 + 16))

    def mouse_click(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        if self.pos1+self.pos3>mouse_pos[0]>self.pos1 and self.pos2+self.pos4>mouse_pos[1]>self.pos2:
            # add a button-hover highlight option?
            if mouse_press[0]==1:
                self.call = True
                self.color = (169, 169, 169)
                self.draw_button()
                self.draw_text()
