#########card game gui#############
import os, json, sys, pip, socket
from pygame.locals import *
from dropdownbar import dropdown
from cardgameplayers import *
import textbox, inputbox, displaytext

def install(package):#absolutely terrible practice
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:#check if pygame is installed
    import pygame
except ImportError:
    install('pygame')


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
        pygame.display.set_caption('Choose a Game')
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
            sys.path.insert(1, os.path.normpath(os.getcwd()+f'\\games'))    
            __import__(file)
            self.select = False
            self.lobby = True
            self.game = file
    def lobbymenu(self):
        if self.lobby:
            ###connect###
            host = "localhost"  
            port = 42069
            KINGFONT = pygame.font.Font("KINGFONT.ttf",20)
            KINGFONT_SMALL = pygame.font.Font("KINGFONT.ttf",16)
            KINGFONT_HEADER=pygame.font.Font("KINGFONT.ttf",36)
            chatrect=textbox.ravager(self.screen,"",pygame.Rect(self.screen.get_width()//2-(350//2),self.screen.get_height()//2-(500//2),350,500),KINGFONT,color=(0,0,64),textcolor=(156,80,243),scrollvalue=40)
            chatinput=inputbox.inputbox(self.screen,pygame.Rect(465,610,350,25),KINGFONT)
            clock = pygame.time.Clock()
            pygame.display.set_caption(f'{self.game} Server Waiting Room')
            try:
                print(f'Connecting to {self.game} Server...')
                client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client.connect((host,port))
                name = input('Enter a Username: ')[ :15]
                message=""
                KINGTEXT=""
                client.send((name+",.delete bea's gadget,"+"all-purple profile randoms have hollow skulls").encode())
                connection_success=True

                #make a server id which is created in the instance for the file and you can only connect to the repsective server of the game you chose

                #music
                song = os.getcwd()+'/music/'+os.listdir(os.path.normpath(os.getcwd()+'/music'))[random.randrange(len(os.listdir(os.path.normpath(os.getcwd()+'/music'))))]
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
                print(f'{song.split("/")[-1].strip(".mp3")} is now playing while you wait for others to join!')
            except (ConnectionRefusedError,OSError):
                print(f'Unable to Connect to {self.game} Server at Port {port}\nMake Sure the Server is Still Available to Join')
                connection_success=False
            
        while self.lobby and connection_success:#and 69

            self.screen.fill((0,0,0))   

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.lobby = False
                    if event.key == K_f:
                        pygame.display.toggle_fullscreen()

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==4:
                        chatrect.scroll("up",pygame.mouse.get_pos())
                    elif event.button==5:
                        chatrect.scroll("down",pygame.mouse.get_pos())
                chatinput.handle_event(event)
            
            bitingtext=client.recv(4096)#client already sent first above so this is the receiving part.
            self.screen.blit(self.background, (0,0))
            text=bitingtext.decode()
            if (text!=KINGTEXT):
                chatrect.changetext(text)
                chatrect.scrolly=chatrect.GOLEMS[-1].position[1]+chatrect.font.size(chatrect.GOLEMS[-1].text)[1]-chatrect.textboxrect.height-chatrect.textboxrect.top
            KINGTEXT=str(text)
            message=chatinput.output_text
            
            client.send((name+",.delete bea's gadget,"+message).encode())

            if (message!=""):
                chatinput.output_text=""
            if (message=="leave server"):#exit if the user decides to leave.
                self.lobby = False
                
            message=""
            bulltime=clock.get_time()
            chatinput.count_down_holding(bulltime)
            #-----------------------------------
            #self.screen.fill(0)

            #displaytext(self.screen,name,(200,60),KINGFONT_HEADER,color=(0,207,255),align=(0,-1))
            #displaytext(self.screen,"Welcome to the server",(200,60),KINGFONT_SMALL,color=(129,214,61),align=(0,1))
            #displaytext(self.screen,"Click on the box to chat",(200,570),KINGFONT_SMALL,color=(129,214,61))
            #displaytext(self.screen,"Type \"leave server\" to disconnect.",(200,600),KINGFONT_SMALL,color=(240,80,49),align=(0,1))

            chatrect.display()
            chatinput.display()
            #-----------------------------------
            pygame.display.flip()
            clock.tick(60)
            #-----------------------------------
        #client.close()
        #pygame.quit()
 



            #if start:
            #self.lobby = False self.playing = True self.player = send request to server to get players or smth than init cardgameplayers player class
            

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
print()
game = main()
#store profile pictures in json for corresponding ips so you can have for example {'171.24.15': 'exampleimage.exe'} and the images will be hard coded and accessed from the server side (linking ips with images basically) shown while in lobby
#when you connect to server, it holds your ip and on server it stores your current game wanting to play and compares
#chat?
#json for game history