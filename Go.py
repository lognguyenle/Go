import pygame

def main():
    pygame.init()
    
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    screen = pygame.display.set_mode((240,180))
    
    image = pygame.image.load("dot.png")
    screen.blit(image, (0, 0))
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == "__main__":
    main()