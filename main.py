#########card game gui#############
import pygame, os, json, sys
from pygame.locals import *
from dropdownbar import dropdown
from cardgameplayers import *
#json for game history


class main(object):
    def __init__(self):
        self.screensize = (1280,720)
        self.x, self.y = 1920//2-(self.screensize[0]//2), 1080//2-(self.screensize[1]//2)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (self.x,self.y)
        self.screen = pygame.display.set_mode(self.screensize)

        self.KINGFONT = pygame.font.Font('KINGFONT.ttf', 100)
        self.KINGFONTSMALLER = pygame.font.Font('KINGFONT.ttf', 33)
        self.gamefiles = [x.strip('.py') for x in (os.listdir(os.path.normpath(os.getcwd()+'\\games'))) if x.endswith('.py')]
        self.loadfunctions = []
        for x in range(len(self.gamefiles)):
            self.loadfunctions.append(self.loadgame)
        self.dropdownbar = dropdown(self.screen, 'Games', (self.screen.get_rect().center[0]-self.KINGFONT.size('Games')[0]//2, self.screen.get_rect().center[1]-self.KINGFONT.size('Games')[1]//2), (0,255,255), self.KINGFONT, self.gamefiles, self.loadfunctions, args=['cheat', 'hearts'], seperaterh=5, itemfont=self.KINGFONTSMALLER)

        self.select = True
        self.lobby = False
        self.playing = False

        self.background = pygame.transform.scale(pygame.image.load('images/background.jpg'), self.screensize)

        self.selectgame()
    def selectgame(self):
        while self.select:#and 69
            self.screen.fill((0,0,0))   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.select = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.select = False
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()
                        #if self.screen.get_flags() & FULLSCREEN:

                            #pygame.display.quit()
                            #pygame.display.init()
                            #self.screen = pygame.display.set_mode(self.screensize)
                            
                        #else:

                            #self.screen = pygame.display.set_mode(self.screensize, FULLSCREEN)

            self.screen.blit(self.background, (0,0))
            self.dropdownbar.display()
            pygame.display.flip()
            self.lobbymenu()
    def loadgame(self, file):
        if os.path.exists(os.path.normpath(os.getcwd()+f'\\games\\{str(file)}.py')):
            print(f'Now Playing {file}!')
            sys.path.insert(1, os.path.normpath(os.getcwd()+f'\\games'))    
            __import__(file)
            self.select = False
            self.lobby = True
    def lobbymenu(self):
        if self.lobby:
            pygame.mixer.music.load(os.getcwd()+'/music/'+os.listdir(os.path.normpath(os.getcwd()+'/music'))[random.randrange(len(os.listdir(os.path.normpath(os.getcwd()+'/music'))))])
            pygame.mixer.music.play()
        while self.lobby:#and 69

            self.screen.fill((0,0,0))   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lobby = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.lobby = False
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()
            #if start:
            #self.lobby = False self.playing = True self.player = send request to server to get players or smth than init cardgameplayers player class
            self.screen.blit(self.background, (0,0))
            pygame.display.flip()
            #self.playinggame()
    def playinggame(self):
        ####move variables to init later######
        self.players = ''#change
        self.turn = 1#player 1
        self.winners = []
        self.pile = played_cards('Pile')
        self.players = distribute_cards(self.players)#make self.players somewhere else so it's defined by now
        print ("\nStarting hands")
        for x in range(len(self.players)):
            self.players[x].print_cards(show_name=True)
        while self.playing:#and 69
            
            self.screen.fill((0,0,0))   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.playing = False
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()

            self.screen.blit(self.background, (0,0))
            pygame.display.flip()
pygame.init()
pygame.font.init()
pygame.mixer.init()
game = main()
#store profile pictures in json for corresponding ips so you can have for example {'171.24.15': 'exampleimage.exe'} and the images will be hard coded and accessed from the server side (linking ips with images basically) shown while in lobby
#when you connect to server, it holds your ip and on server it stores your current game wanting to play and compares
#chat?