def displaytext(surface,text,position,font,color=(0,0,0),align=(0,0)):
    display=font.render(text,True,color)
    rect=display.get_rect()
    rect.centerx=int(position[0]-rect.width*0.5*(align[0]))
    rect.centery=int(position[1]-rect.height*0.5*(align[1]))
    surface.blit(display,rect)