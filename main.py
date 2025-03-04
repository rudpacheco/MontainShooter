import pygame

print('Setup Start')
pygame.init()
windows = pygame.display.set_mode(size=(600, 480))
print('Setup End')
# Teste Rudney
print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # end pygame
