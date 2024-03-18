import pygame

from ecs_pattern import component, entity, EntityManager, System, SystemManager

def main():
    pygame.init()
    
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen_width = 240
    screen_height = 180
    screen = pygame.display.set_mode((screen_width,screen_height))

    image2 = pygame.image.load("Untitled.png")
    image = pygame.image.load("dot.png")
    image.set_colorkey((255,255,255))
    screen.blit(image2, (0, 0))
    screen.blit(image, (0, 0))
    
    xpos = 50
    ypos = 50
    step_x = 10
    step_y = 10
    
    pygame.display.flip()
    
    clock = pygame.time.Clock()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        xpos += step_x
        ypos += step_y
        
        screen.blit(image2, (0,0))
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()
        
        clock.tick(10)
                
if __name__ == "__main__":
    main()