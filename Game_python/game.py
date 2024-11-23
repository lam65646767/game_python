import pygame
import sys, random

def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))

def create_pipe():
    random_pipe_pos =random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500,random_pipe_pos)) 
    top_pipe = pipe_surface.get_rect(midtop=(500,random_pipe_pos-650)) # Điều chỉnh tọa độ khởi tạo ống
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes: 
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe ,pipe)
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print ("va cham)")
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        print("va CHAM")
pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
gravity = 0.25
bird_movement = 0
game_active =True
# Chèn background
bg = pygame.image.load('FileGame/assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)

# Chèn sàn
floor = pygame.image.load('FileGame/assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

# Tạo chim
bird = pygame.image.load('FileGame/assets/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 384))

# Tạo ống
pipe_surface = pygame.image.load('FileGame/assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)

# Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_list = []
pipe_height = [200,300,400]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -11            
            
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
                
    screen.blit(bg, (0, 0))
    if game_active:
        # Chim
        bird_movement += gravity        
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)
        check_collision(pipe_list)
        
        # Ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
    
    # Sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(120)
