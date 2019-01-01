import pygame


EVENT_TYPE = {
    # APP EVENTS
    "QUIT": pygame.QUIT, "RESIZE_WINDOW": pygame.RESIZABLE,
    # SCENE EVENTS
    "START": pygame.USEREVENT + 1, "MENU": pygame.USEREVENT + 2,
    "SETTINGS": pygame.USEREVENT + 3,
    # GAME EVENTS
    "DEAD": pygame.USEREVENT + 4, "SNACK_EATEN": pygame.USEREVENT + 5,
    # KEY EVENTS
    "UP": pygame.K_UP, "DOWN": pygame.K_DOWN, "LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT,
    # MOUSE EVENTS
}
