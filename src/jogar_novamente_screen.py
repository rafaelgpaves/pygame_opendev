from os import path
import pygame
from assets import VITORIA_BG, load_assets, BOTAO_JOGARN2
from sprites import Button
from config import HEIGHT,WIDTH,IMG_DIR, FPS, BLACK, QUIT, GAME, SND_DIR

def jogar_novamente_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

    background = pygame.image.load(path.join(IMG_DIR, 'Vitoria.png')).convert()
    background_rect = background.get_rect()

    img_botao = assets[BOTAO_JOGARN2]
    botao = Button(WIDTH/2-225, HEIGHT/2+0, img_botao, 0.5)
    
    swoosh = pygame.mixer.Sound(path.join(SND_DIR, 'swoosh_de_terror.wav'))
    swoosh.play()
    running = True
    while running:
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(assets[VITORIA_BG], background_rect)
        botao.draw(window)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if botao.press():
                state = GAME
                running = False

        pygame.display.flip()

    return state
