import pygame

class inputbox(object):
    is_a_box_active=False
    def __init__(self,surface,rect,font,color=(33,54,16),activecolor=(106,46,104),textcolor=(0,207,255),cursorcolor=(156,80,243),default_text="",max_string_len=100):
        self.surface=surface
        self.rect=rect
        self.font=font
        self.text=default_text
        self.output_text=""
        self.cursor=0
        self.max_string_len=max_string_len
        self.active=False
        self.color=color
        self.activecolor=activecolor
        self.textcolor=textcolor
        self.cursorcolor=cursorcolor

        self.holding_key=None
        self.hold_delay=0.05
        self.hold_time=-0.45
        self.uppercase=False

        self.keys={
            pygame.K_a:"a",
            pygame.K_b:"b",
            pygame.K_c:"c",
            pygame.K_d:"d",
            pygame.K_e:"e",
            pygame.K_f:"f",
            pygame.K_g:"g",
            pygame.K_h:"h",
            pygame.K_i:"i",
            pygame.K_j:"j",
            pygame.K_k:"k",
            pygame.K_l:"l",
            pygame.K_m:"m",
            pygame.K_n:"n",
            pygame.K_o:"o",
            pygame.K_p:"p",
            pygame.K_q:"q",
            pygame.K_r:"r",
            pygame.K_s:"s",
            pygame.K_t:"t",
            pygame.K_u:"u",
            pygame.K_v:"v",
            pygame.K_w:"w",
            pygame.K_x:"x",
            pygame.K_y:"y",
            pygame.K_z:"z",
            pygame.K_0:"0",
            pygame.K_1:"1",
            pygame.K_2:"2",
            pygame.K_3:"3",
            pygame.K_4:"4",
            pygame.K_5:"5",
            pygame.K_6:"6",
            pygame.K_7:"7",
            pygame.K_8:"8",
            pygame.K_9:"9",
            pygame.K_COMMA:",",
            pygame.K_SEMICOLON:";",
            pygame.K_PERIOD:".",
            pygame.K_SLASH:"/",
            pygame.K_SPACE:" ",
            pygame.K_QUOTE:"'",
            pygame.K_BACKSPACE:"BACKSPACE",
            pygame.K_LEFT:"LEFT",
            pygame.K_RIGHT:"RIGHT",
            pygame.K_HOME:"HOME",
            pygame.K_END:"END",
            pygame.K_DELETE:"DELETE",
            pygame.K_RETURN:"RETURN",
        }#some programmer did not decide to put all these on one line so it looks cleaner than it should...
    def display(self):
        BULLCOLOR=self.color
        BULLWIDTH=0
        if (self.active):
            BULLCOLOR=self.activecolor
            BULLWIDTH=3
        pygame.draw.rect(self.surface,BULLCOLOR,self.rect)
        
        left_cursor=self.text[:self.cursor]
        left_cursor_02=self.shrink_to_fit(left_cursor,"end")
        

        if (left_cursor!=left_cursor_02):
            cursor_x=self.rect.right#self.rect.left+self.font.size(self.text[:self.cursor])[0]
            pygame.draw.line(self.surface,self.cursorcolor,(cursor_x,self.rect.top),(cursor_x,self.rect.bottom),width=BULLWIDTH)
            self.displaytextoutline(self.surface,left_cursor_02,(self.rect.right,self.rect.centery),self.font,color=self.textcolor,align=(1,0))
        else:
            cursor_x=self.rect.left+self.font.size(self.text[:self.cursor])[0]
            pygame.draw.line(self.surface,self.cursorcolor,(cursor_x,self.rect.top),(cursor_x,self.rect.bottom),width=BULLWIDTH)
            self.displaytextoutline(self.surface,self.shrink_to_fit(self.text,"beginning"),(self.rect.left,self.rect.centery),self.font,color=self.textcolor,align=(-1,0))
    def shrink_to_fit(self,text_02,start):
        newstring_02=""
        if (self.font.size(text_02)[0]>self.rect.width):
            if (start=="beginning"):
                index_variable=0
                index_increment=1
            else:
                index_variable=len(text_02)-1
                index_increment=-1
            while (self.font.size(newstring_02)[0]<=self.rect.width):
                if (start=="beginning"):
                    newstring_02=newstring_02+text_02[index_variable]
                else:
                    newstring_02=text_02[index_variable]+newstring_02
                index_variable+=index_increment
        
            if (start=="beginning"):
                newstring_02=newstring_02[:-1]
            else:
                newstring_02=newstring_02[1:]
            
            return newstring_02
        return text_02  
    def change_active(self):
        veryshortandmeaningfulvariablename=pygame.mouse.get_pos()
        if (veryshortandmeaningfulvariablename[0]>=self.rect.left and veryshortandmeaningfulvariablename[0]<=self.rect.right and veryshortandmeaningfulvariablename[1]>=self.rect.top and veryshortandmeaningfulvariablename[1]<=self.rect.bottom):
            if (self.active):
                self.active=False
                inputbox.is_a_box_active=False
            elif (inputbox.is_a_box_active==False):
                self.active=True
                inputbox.is_a_box_active=True
    def add_char(self,key,uppercase_01=False):
        if (self.active):
            if (key in self.keys):
                if (self.keys[key]=="RETURN"):
                    #self.active=False
                    #inputbox.is_a_box_active=False
                    self.output_text=str(self.text)
                    self.text=""
                elif (self.keys[key]=="DELETE"):
                    self.text=""
                    self.cursor=0
                elif (self.keys[key]=="BACKSPACE"):
                    self.text=self.text[:max(0,self.cursor-1)]+self.text[self.cursor:]
                    self.cursor-=1
                elif (self.keys[key]=="HOME"):
                    self.cursor=0
                elif (self.keys[key]=="END"):
                    self.cursor=len(self.text)
                elif (self.keys[key]=="LEFT"):
                    self.cursor-=1
                elif (self.keys[key]=="RIGHT"):
                    self.cursor+=1
                else:
                    newtext=self.keys[key]
                    if (uppercase_01):
                        if (newtext=="/"):
                            newtext="?"
                        elif (newtext=="1"):
                            newtext="!"
                        elif (newtext=="9"):
                            newtext="("
                        elif (newtext=="0"):
                            newtext=")"
                        elif (newtext==";"):
                            newtext=":"
                        elif (newtext=="'"):
                            newtext='"'
                        else:
                            newtext=newtext.upper()
                    if (len(self.text)<self.max_string_len-1):
                        self.text=self.text[:self.cursor]+newtext+self.text[self.cursor:]
                        self.cursor+=1
            self.text=self.text[:self.max_string_len]
            if (self.cursor<0):
                self.cursor=0
            elif (self.cursor>len(self.text)):
                self.cursor=len(self.text)
    def displaytext(self,surface,text,position,font,color=(0,0,0),align=(0,0)):
        display=font.render(text,True,color)
        rect=display.get_rect()
        rect.centerx=int(position[0]-rect.width*0.5*(align[0]))
        rect.centery=int(position[1]-rect.height*0.5*(align[1]))
        surface.blit(display,rect)
    def displaytextoutline(self,surface,text,position,font,color=(0,0,0),outline_color=(0,0,0),align=(0,0)):
        size=max(1,(font.size(text)[1]*0.6*0.0625))#works best with KINGFONT.ttf
        outline=font.render(text,True,outline_color)
        rect=outline.get_rect()
        for a in range(-1,2):
            for b in range(-1,2):
                if (a!=0 or b!=0):
                    rect.centerx=int(position[0]-rect.width*0.5*(align[0])+int(a*size))
                    rect.centery=int(position[1]-rect.height*0.5*(align[1])+int(b*size))
                    surface.blit(outline,rect)
        self.displaytext(surface,text,position,font,color,align=align)
    def handle_event(self,event):
        if event.type==pygame.KEYDOWN:
            if (event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT):
                self.uppercase=True

            self.holding_key=event.key
            self.add_char(event.key,uppercase_01=self.uppercase)
            
        if event.type==pygame.KEYUP:
            if (event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT):
                self.uppercase=False
                
            self.holding_key=None
            self.hold_time=-0.45
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            if (event.button==1):
                self.change_active()
    def count_down_holding(self,bulltime1):
        if (self.holding_key not in [None,pygame.K_LSHIFT,pygame.K_RSHIFT]):
            self.hold_time+=(bulltime1/1000.0)
            if (self.hold_time>=self.hold_delay):
                self.hold_time=0.0
                self.add_char(self.holding_key,uppercase_01=self.uppercase)


if (__name__=="__main__"):
    pygame.init()#you are so bad that you had to copy paste from another program
    pygame.font.init()
    screen = pygame.display.set_mode((1280,900))# i am dirty hard coder so your display set mode thing must be called screen
    clock = pygame.time.Clock()
    pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty")
    KINGFONT_01 = pygame.font.Font("KINGFONT.ttf",48)
    KINGFONT_02 = pygame.font.Font("KINGFONT.ttf",28)

    ###copy this into the main
    box=inputbox(screen,pygame.Rect(100,100,500,75),KINGFONT_01)
    box2=inputbox(screen,pygame.Rect(100,250,600,40),KINGFONT_02)
    box3=inputbox(screen,pygame.Rect(100,300,600,40),KINGFONT_02)

    done=False
    # main program loop
    while (done == False):
        #all event processing goes below
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True#User perssed close
            
            box.handle_event(event)
            box2.handle_event(event)
            box3.handle_event(event)
        
        bulltime=clock.get_time()
        box.count_down_holding(bulltime)
        box2.count_down_holding(bulltime)
        box3.count_down_holding(bulltime)
            
        screen.fill((0,0,0))
        box.display()
        box2.display()
        box3.display()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()