import pygame,random,sys

class golem(object):#100% original code written together by me and myself copyright 2020 my github page visit me at ravager6969 donate to me to help support the creation of massive projects like this
    def __init__(self,text,color,position,font):
        self.text=text
        self.thetextistoolargetofitinthetextboxdonttellmethisisabadvariablenameiwastoolazytothinkofaverydescriptiveone=color
        self.position=position
        self.font = font
    def KING(self,surface,surgegalemrpvssproutjackyemzforworstmetaof2020):
        textdisplay=(self.font).render(self.text,True,self.thetextistoolargetofitinthetextboxdonttellmethisisabadvariablenameiwastoolazytothinkofaverydescriptiveone)
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked=textdisplay.get_rect()
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked.left=int(surgegalemrpvssproutjackyemzforworstmetaof2020[0])
        hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked.top=int(surgegalemrpvssproutjackyemzforworstmetaof2020[1])
        surface.blit(textdisplay,hahaidontcarethatyourhousesoldormadeyoulotsofmoney_iusedtarasgadgetstillcouldnotfindwhoasked)
    def __repr__(self):
        return self.text#you really do be wanting to print those golems

class ravager(object):
    def __init__(self,surface,string,rect,font,color=(129,214,61),textcolor=(142,155,229),scrollvalue=20):
        self.surface=surface
        self.textboxrect=rect
        self.string=string
        self.font=font
        if (color==(129,214,61)):#this color can go commit become king
            self.color=random.choice([(156,80,243),(240,80,49),(0,207,255),(212,91,208)])
        else:
            self.color=color
        self.textcolor=textcolor
        self.scrollvalue=scrollvalue#how many pixels to scroll by each input
        self.scrolly=0#shifts all the text up by this amount of pixels
        self.changetext(self.string)
    def scroll(self,direction,mouse):
        if (mouse[0]>self.textboxrect.left and mouse[0]<self.textboxrect.right and mouse[1]>self.textboxrect.top and mouse[1]<self.textboxrect.bottom):
            if (direction=="down"):
                self.scrolly+=self.scrollvalue
            elif (direction=="up"):
                self.scrolly-=self.scrollvalue
            else:
                print ("read the instructions next time")#what instructions? i don't see any all i see is messy code
        if (self.scrolly<0):#prevent the user from scrolling once they reached the top
            self.scrolly=0 
        elif (self.scrolly>self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[-1].text)[1]-self.textboxrect.height-self.textboxrect.top):
            self.scrolly=self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[-1].text)[1]-self.textboxrect.height-self.textboxrect.top
    def display(self):
        pygame.draw.rect(self.surface,self.color,self.textboxrect)
        for x in range(len(self.GOLEMS)):
            if (self.GOLEMS[-1].position[1]+self.font.size(self.GOLEMS[x].text)[1]-self.textboxrect.top>self.textboxrect.height):#multiple lines
                if (self.GOLEMS[x].position[1]>=self.scrolly+self.textboxrect.top) and (self.GOLEMS[x].position[1]+self.font.size(self.GOLEMS[x].text)[1]<=self.scrolly+self.textboxrect.bottom):
                    self.GOLEMS[x].KING(self.surface,(self.GOLEMS[x].position[0],self.GOLEMS[x].position[1]-(self.scrolly)))
            else:#one line
                self.GOLEMS[x].KING(self.surface,(self.GOLEMS[x].position[0],self.GOLEMS[x].position[1]))
    def changetext(self,newstring):
        self.GOLEMS=[]
        THEKINGx=0#yes it is the blit spot in the box
        THEKINGy=0
        line=""
        newstring=newstring.split(" ")#you could have just made string a list
        for x in range(len(newstring)):
            newstring[x]=" "+newstring[x]
            kingsize=self.font.size(newstring[x])
            if (newstring[x][1:]=="\\n" and x<len(newstring)-1):
                self.GOLEMS.append(golem(line,self.textcolor,(self.textboxrect.left,THEKINGy+self.textboxrect.top),self.font))
                THEKINGx=0
                THEKINGy+=kingsize[1]
                line=""
                continue
            if (THEKINGx+kingsize[0]>self.textboxrect.width):
                if (" " not in line):
                    while (self.font.size(line)[0]>self.textboxrect.width):
                        line=line[:-1]
                self.GOLEMS.append(golem(line,self.textcolor,(self.textboxrect.left,THEKINGy+self.textboxrect.top),self.font))
                line=newstring[x][1:]
                THEKINGx=kingsize[0]
                THEKINGy+=kingsize[1]
            else:
                if (THEKINGx==0):
                    line+=newstring[x][1:]#remove space at beginning of new line
                else:
                    line+=newstring[x]
                THEKINGx+=kingsize[0]
            if (x==len(newstring)-1):#add last line even if it does not take up the whole width
                self.GOLEMS.append(golem(line,self.textcolor,(self.textboxrect.left,THEKINGy+self.textboxrect.top),self.font))
        self.scrolly=0

def convert(file):
    f=open(file)
    Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository=f.read()
    f.close()
    Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository=Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository.split("\n")
    BULL=""
    for x in range(len(Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository)):
        BULL+=" \\n "+Youwouldntdarescrolltothebottomofthistextboxortheendofthisvariablenameinthiscase0SpringTrap6OliveBranch6OpenBusiness18WarpedArena24MinecartMadness30Cobweb30SandyGems42ShoulderBash48DeepDiner54JunkPark54ParallelPlays66WellCut72DoubleSwoosh78CanalGrande78TornadoRing90TripleDribble96BouncingDiner102FencedIn102Split114PinballDreams120CrystalArcade126SnakePrairie126Crossroads138CenterField144ChillSpace150SomeAssemblyRequired150TinyTown162PinholePunt168CellDivision174DeeperDanger174BanditCove186BeachBall192StoneFort198CratedFactory198MassiveAttack210FieldGoal216HardRockMine222HeatWave222HotPotato234SuperStadium240Undermine246Nuts_Bolts246ControlGrande258PostHaste264DeathcapTrap270LandAhoy270TrafficJam282BackyardBowl288SpareSpace294FactoryRush294Perimeter306PenaltyKick312EscapeVelocity318LayerCake318PitStop330GalaxyArenaWowyoureallyscrolledthroughallthistextIwasntevenabletogotobullsbushesandbackbeforeyoufinishedCongratulationsIappreciateyourworkIllsignupforGitHubandaddtoRavager6969srepository[x]
    BULL=BULL.replace("  "," ")
    BULL=BULL[4:]
    return BULL

if (__name__=="__main__"):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1280,900))# i am dirty hard coder so your display set mode thing must be called screen
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty")
    font1 = pygame.font.Font("KINGFONT.ttf",48)
    font2 = pygame.font.Font("KINGFONT.ttf",36)
    string = "\\n week 1 \\n Spring Trap Olive Branch Open Business Warped Arena \\n Minecart Madness Cobweb Sandy Gems Shoulder Bash \\n Deep Diner Junk Park Parallel Plays Well Cut \\n Double Swoosh Canal Grande Tornado Ring Triple Dribble \\n Bouncing Diner Fenced In Split Pinball Dreams \\n Crystal Arcade Snake Prairie Crossroads Center Field \\n Chill Space Some Assembly Required Tiny Town Pinhole Punt \\n \\n week 2 \\n Cell Division Deeper Danger Bandit Cove Beach Ball \\n Stone Fort Crated Factory Massive Attack Field Goal \\n Hard Rock Mine Heat Wave Hot Potato Super Stadium \\n Undermine Nuts & Bolts Control Grande Post Haste \\n Deathcap Trap Land Ahoy Traffic Jam Backyard Bowl \\n Spare Space Factory Rush Perimeter Penalty Kick \\n Escape Velocity Layer Cake Pit Stop Galaxy Arena \\n Play Play King Bolem Wolf"
    if (len(sys.argv)>1):
        string=convert(sys.argv[1])
    #string="bolem ging sfsdjfklwejlkrjweirjwelkrjweklrkabcdefghijklmnopqrstuvwxyz gj"
    string2 = "a a a a aa  a a a a aa k k k k k k k k k kl l l l l l l l l 4 4 4 4 4 4 5 5 5 5 55 5 6 6 6 6 6 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 ^ 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9 6 9"

    #textboxrect=ravager(screen,string2,pygame.Rect(50,50,300,500),font1,color=(255,3,204),textcolor=(85,255,85),scrollvalue=60)#create instance of ravager
    textboxrect2=ravager(screen,string,pygame.Rect(150,100,650,450),font2,scrollvalue=40)

    done=False
    # main program loop
    while (done == False):
        #all event processing goes below
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True#User perssed close
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    #textboxrect.scroll("up",pygame.mouse.get_pos())#scroll 20 pixels per spin
                    textboxrect2.scroll("up",pygame.mouse.get_pos())#scroll 20 pixels per spin
                elif event.button==5:
                    #textboxrect.scroll("down",pygame.mouse.get_pos())
                    textboxrect2.scroll("down",pygame.mouse.get_pos())
            
        screen.fill((0,0,0))
        #textboxrect.display()
        textboxrect2.display()
        
        

        
















        #just send that pygame display flip thing down there













        pygame.display.flip()
        clock.tick(60)

    pygame.quit()