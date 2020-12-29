import pygame

class InvalidRespectiveFunction(Exception):
    def __init__(self):
        super().__init__()
    def __str__(self):
        return('Their is Either a Missing or Invalid Function Paired to This Bar.')
class dropdown(object):
    def __init__(self, screen, maintxt, pos, txtcolor, font, array, functions, args=None, bgcolor=(255,255,255), seperaterh=2, itemfont=None):
        self.screen = screen
        self.pos = pos
        self.txtcolor = txtcolor
        self.bgcolor = bgcolor
        self.font = font
        if itemfont == None:
            self.itemfont = self.font
        else:
            self.itemfont = itemfont
        self.items = list(array)
        self.functions = functions
        self.args = args
        self.array = [self.itemfont.render(str(self.items[x]),True,self.txtcolor) for x in range(len(self.items))]
        self.arrayrects = []
        self.clicked = False
        self.clickable = True
        self.clickablebar = True
        self.seperateh = seperaterh
        self.main = self.font.render(maintxt,True,self.txtcolor)
        self.w, self.h = self.main.get_width(), self.main.get_height()
        self.rect = (self.pos[0]-25, self.pos[1], self.w+50, self.h)
    def draw(self):
        pygame.draw.rect(self.screen, self.bgcolor, (self.pos[0]-25, self.pos[1], self.w+50, self.h))
        self.screen.blit(self.main, self.pos)
    def drawbars(self, rect, ind):
        pygame.draw.rect(self.screen, (200,200,200), (rect[0], rect[1]-self.seperateh, rect[2], self.seperateh))
        pygame.draw.rect(self.screen, self.bgcolor, (rect))
        #self.screen.blit(self.array[ind], (rect[0]+(rect[2]-rect[0]//2)+(self.array[ind].get_width()//2), rect[1], rect[2], rect[3]))
        self.screen.blit(self.array[ind], (rect[0]+50, rect[1], rect[2], rect[3]))
    def check(self):
        mousepos = pygame.mouse.get_pos()
        if pygame.Rect(self.rect).colliderect(pygame.Rect(mousepos[0],mousepos[1],10,10)) and pygame.mouse.get_pressed()[0] and self.clickable:
            if not self.clicked:
                self.clicked = True
            else:
                self.clicked = False
            self.clickable = False
        elif not(pygame.Rect((self.rect[0], self.rect[1], self.rect[2], self.rect[3]+(self.rect[3]*len(self.items)))).colliderect(pygame.Rect(mousepos[0],mousepos[1],10,10))) and pygame.mouse.get_pressed()[0] and self.clickable:
            self.clicked = False
            self.clickable = False
        elif not pygame.mouse.get_pressed()[0]:
            self.clickable = True
    def checkbars(self):
        value = None
        mousepos = pygame.mouse.get_pos()
        for x in range(len(self.arrayrects)):
            if pygame.Rect(self.arrayrects[x]).colliderect(pygame.Rect(mousepos[0], mousepos[1], 1, 1)) and pygame.mouse.get_pressed()[0] and self.clickablebar:
                try:
                    if self.args != None and self.args[x] != None:
                        value = self.functions[x](self.args[x])
                    else:
                        value = self.functions[x]()
                except IndexError:
                    raise InvalidRespectiveFunction
                self.clickablebar = False
            elif not pygame.mouse.get_pressed()[0]:
                self.clickablebar = True
        return(value)
    def displayarray(self):
        for x in range(len(self.array)):
            self.drawbars((self.rect[0], self.rect[1]+(self.rect[3]*(x+1))+self.seperateh*(x+1), self.rect[2], self.rect[3]), x)
            if (self.rect[0], self.rect[1]+(self.rect[3]*(x+1))+self.seperateh*(x+1), self.rect[2], self.rect[3]) not in self.arrayrects:
                self.arrayrects.append((self.rect[0], self.rect[1]+(self.rect[3]*(x+1))+self.seperateh*(x+1), self.rect[2], self.rect[3]))
    def display(self):
        value = None
        self.check()
        if self.clicked:
            self.displayarray()
            value = self.checkbars()
        self.draw()
        return(value)
    def osama(self):#DO NOT REMOVE; MAKES ENTIRE CLASS FUNCTION PROPERLY
        try:
            osama()
        except RecursionError:
            osama()        


if __name__ == "__main__":
    def test():
        print('test')
    def test2():
        print('test2')
    def test3():
        print('test3')
    class main(object):
        def __init__(self):
            pygame.init()
            pygame.font.init()
            self.screen = pygame.display.set_mode((600,600))
            self.font = pygame.font.Font('KINGFONT.ttf', 33)
            self.dropdownbar = dropdown(self.screen, 'Choose Preset', (200,200), (0,0,0), self.font, ('bull the boo', 'boo the bull', 'a t'), (test, test2, test3))
            self.display()
        def display(self):
            while True:
                self.screen.fill((0,0,0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                print(self.dropdownbar.display())
                pygame.display.flip()
                
    game = main()