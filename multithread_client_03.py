import random,socket,pygame,textbox,inputbox

def displaytext(surface,text,position,font,color=(0,0,0),align=(0,0)):
    display=font.render(text,True,color)
    rect=display.get_rect()
    rect.centerx=int(position[0]-rect.width*0.5*(align[0]))
    rect.centery=int(position[1]-rect.height*0.5*(align[1]))
    surface.blit(display,rect)

def change_input_to_string(X):
    if (X=="game has not started yet??????????????"):
        return "Type \"start\" to close the server and deal cards to all users currently connected. \\n \\n Commands: \\n \\n deal \\n Re-shuffle deck and deal cards to all players \\n \\n transfer (from) (to) (cards) \\n (from) and (to) are integers representing the player number with 1 being at the top and 0 being the pile. (cards) is a set of any number of integers separated by spaces."
    xXx=""
    X=X.split(" \\n ")
    if (X[0]=="green button yellow button red button win lane win game"):
        X.pop(0)
        for x in range(len(X)):
            X[x]=X[x].split(".")
            for Xx in range(len(X[x])):
                if (x!=0 or Xx!=0):
                    xXx+=" \\n "
                xXx+=X[x][Xx]
        return xXx
    return "something went wrong"

#socket stuff
host="localhost"
port=42069
name=input("Enter your name: ")
name=name[:15]
message=""
KINGTEXT=""
done=False
connection_success=False

#pygame stuff
pygame.init()
pygame.font.init()
screenx=400
screeny=600
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption("Brawl Ball > Heist > Siege > Gem Grab > Bounty > THE KING")
clock = pygame.time.Clock()
KINGFONT = pygame.font.Font("KINGFONT.ttf",20)
KINGFONT_SMALL = pygame.font.Font("KINGFONT.ttf",16)
KINGFONT_HEADER=pygame.font.Font("KINGFONT.ttf",36)
chatrect=textbox.ravager(screen,"",pygame.Rect(25,125,350,400),KINGFONT,color=(0,0,64),textcolor=(156,80,243),scrollvalue=40)
chatinput=inputbox.inputbox(screen,pygame.Rect(25,535,350,25),KINGFONT)

print ("Connecting to the server...")

try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    client.send((name+",.delete bea's gadget,"+"all-purple profile randoms have hollow skulls").encode())
    connection_success=True
except (ConnectionRefusedError,OSError):
    print ("Access denied. Get out of here!")
    connection_success=False

if (connection_success):
    while (done==False):
        for event in pygame.event.get():
            #if event.type==pygame.QUIT:
            #    done=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    chatrect.scroll("up",pygame.mouse.get_pos())
                elif event.button==5:
                    chatrect.scroll("down",pygame.mouse.get_pos())
            chatinput.handle_event(event)
        #-----------------------------------
        bitingtext=client.recv(4096)#client already sent first above so this is the receiving part.
        text=bitingtext.decode()
        if (text!=KINGTEXT):
            text=change_input_to_string(text)
            #print (text.split(" \\n "))
            chatrect.changetext(text)
            chatrect.scrolly=chatrect.GOLEMS[-1].position[1]+chatrect.font.size(chatrect.GOLEMS[-1].text)[1]-chatrect.textboxrect.height-chatrect.textboxrect.top
        KINGTEXT=str(text)
        message=chatinput.output_text
        
        client.send((name+",.delete bea's gadget,"+message).encode())

        if (message!=""):
            chatinput.output_text=""
        if (message=="leave server"):#exit if the user decides to leave.
            done=True
            
        message=""
        bulltime=clock.get_time()
        chatinput.count_down_holding(bulltime)
        #-----------------------------------
        screen.fill(0)

        displaytext(screen,name,(200,60),KINGFONT_HEADER,color=(0,207,255),align=(0,-1))
        displaytext(screen,"Welcome to the server",(200,60),KINGFONT_SMALL,color=(129,214,61),align=(0,1))
        displaytext(screen,"Click on the box to chat",(200,570),KINGFONT_SMALL,color=(129,214,61))
        displaytext(screen,"Type \"leave server\" to disconnect.",(200,600),KINGFONT_SMALL,color=(240,80,49),align=(0,1))

        chatrect.display()
        chatinput.display()
        #-----------------------------------
        pygame.display.flip()
        clock.tick(60)
        #-----------------------------------
    client.close()
    pygame.quit()