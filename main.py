import pygame
pygame.init()
screen1 = pygame.display.set_mode((800,400))
sky_surface = pygame.image.load('lessons\graphics\sky.jpg').convert()
sky_surface = pygame.transform.scale(sky_surface, (800,400))
original_player_surf = pygame.image.load('lessons\graphics\seagull.png')
player_surf = original_player_surf
flipped_player_surf = pygame.transform.flip(original_player_surf, True, False)

is_flipped = True
game_active = True

pygame.mixer.music.load('lessons/audio/seagullsounds.mp3')
pygame.mixer.music.play(loops=-1)

player_rect = player_surf.get_rect(center = (400,200))

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_rect.move_ip(0,-5)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_rect.move_ip(0,5)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_rect.move_ip(-5,0)
        if not is_flipped:
            player_surf = original_player_surf
            is_flipped = True
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_rect.move_ip(5,0)
        if is_flipped:
            player_surf = flipped_player_surf
            is_flipped = False

    screen1.blit(sky_surface,(0,0))
    screen1.blit(player_surf, player_rect)

    pygame.time.Clock().tick(60)
    pygame.display.update()