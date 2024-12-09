import pygame, random
from pygame import mixer
from pygame.locals import *
from time import sleep

# Constantes de configuración
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 8  # Velocidad inicial del pájaro
GRAVITY = 0.8  # Gravedad aplicada al pájaro
GAME_SPEED = 9  # Velocidad del desplazamiento de tubos y suelo
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 120  # Espacio entre los tubos superior e inferior

# Rutas de los recursos
BIRD_IMAGES = ['assets/bluebird-upflap.png', 'assets/bluebird-midflap.png', 'assets/bluebird-downflap.png']
BACKGROUND_IMAGE = 'assets/background-day.png'
HIT_SOUND = 'assets/hit.wav'
GAME_MUSIC = 'assets/game.wav'
PIPE_IMAGE = 'assets/pipe-red.png'
FLOOR_IMAGE = 'assets/floor.png'

# Variables globales de puntuación
points = 0
record = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load(img).convert_alpha() for img in BIRD_IMAGES]
        self.speed = SPEED
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        #Actualiza la animación y la posición del pájaro.
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]
        self.rect[1] += self.speed
        self.speed += GRAVITY

    def bump(self):
        
        self.speed = -SPEED


class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PIPE_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        #Mueve los tubos hacia la izquierda.
        self.rect[0] -= GAME_SPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(FLOOR_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGHT

    def update(self):
        #Mueve el suelo hacia la izquierda.
        self.rect[0] -= GAME_SPEED


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(xpos):
    #Genera un par de tubos (normal e invertido) con posición y tamaño aleatorios.
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inverted = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inverted)


def update_record():
    #Actualiza el récord si la puntuación actual es mayor.
    global points, record
    if points > record:
        record = points


def load_resources():
    """Carga los recursos y devuelve los objetos necesarios."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    mixer.music.load(GAME_MUSIC)
    mixer.music.play(-1)
    background = pygame.image.load(BACKGROUND_IMAGE).convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen, background


def countdown(screen, font):
    # Muestra la cuenta regresiva antes de iniciar el juego.
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))  
        screen.blit(font.render(str(i), True, (255, 255, 255)), (400, 250))  # Dibuja el número
        pygame.display.update()  
        sleep(.5)  



def display_game_over(screen, font, points, record):
    
    hit_sound = mixer.Sound(HIT_SOUND)
    hit_sound.play()

    pygame.draw.rect(screen, (0, 0, 0, 180), [305, 104, 200, 200], 0)  # Fondo semitransparente negro
    pygame.draw.rect(screen, (50, 50, 255), [305, 104, 200, 200], 10)  # Borde externo azul
    pygame.draw.rect(screen, (255, 223, 0), [310, 108, 190, 190])  # Fondo principal amarillo dorado


    font2 = pygame.font.SysFont("arial", 20, bold=True)
    screen.blit(font2.render('GAME OVER', True, (255, 0, 0)), (SCREEN_WIDTH // 2 - 100, 120))

    font1 = pygame.font.SysFont("arial", 20)
    
    score_text = font1.render("Tú puntuación", True, (0, 0, 255))
    record_text = font1.render("Puntuación más alta", True, (0, 0, 255))

    score_value = font1.render(str(points), True, (0, 0, 0))
    record_value = font1.render(str(record), True, (0, 0, 0))

    score_text_x = SCREEN_WIDTH // 2 - score_text.get_width() // 2
    score_value_x = SCREEN_WIDTH // 2 - score_value.get_width() // 2
    record_text_x = SCREEN_WIDTH // 2 - record_text.get_width() // 2
    record_value_x = SCREEN_WIDTH // 2 - record_value.get_width() // 2

    # Dibujar los textos y valores centrados
    screen.blit(score_text, (score_text_x, 170))
    screen.blit(score_value, (score_value_x, 200))
    screen.blit(record_text, (record_text_x, 240))
    screen.blit(record_value, (record_value_x, 270))


    pygame.display.update()



def start_the_game():
    #Función principal para iniciar y gestionar el juego.
    global points, record
    points = 0

    screen, background = load_resources()
    bird_group = pygame.sprite.Group()
    bird = Bird()
    bird_group.add(bird)

    ground_group = pygame.sprite.Group()
    for i in range(2):
        ground = Ground(2 * SCREEN_WIDTH * i)
        ground_group.add(ground)

    pipe_group = pygame.sprite.Group()
    for i in range(2):
        pipes = get_random_pipes(SCREEN_WIDTH * i + 800)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 60)
    menu = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and menu:
                if event.button == 1:
                    screen.blit(background, (0, 0))
                    ground_group.draw(screen)
                    pygame.display.update()
                    sleep(0.3)
                    countdown(screen, font)
                    menu = False

            if event.type == KEYDOWN and not menu:
                if event.key == K_SPACE:
                    bird.bump()

        clock.tick(30)
        screen.blit(background, (0, 0))

        if menu:
            txt = font.render("HAZ CLICK PARA INICIAR", True, (255, 255, 255))
            
            text_width = txt.get_width()
            text_height = txt.get_height()
            
            x_pos = (SCREEN_WIDTH - text_width) // 2
            y_pos = (SCREEN_HEIGHT - text_height) // 2
            
            # Dibujar el texto centrado
            screen.blit(txt, (x_pos, y_pos))


        if not menu:
            if is_off_screen(ground_group.sprites()[0]):
                ground_group.remove(ground_group.sprites()[0])
                new_ground = Ground(GROUND_WIDTH - 20)
                ground_group.add(new_ground)

            if is_off_screen(pipe_group.sprites()[0]):
                pipe_group.remove(pipe_group.sprites()[0])
                pipe_group.remove(pipe_group.sprites()[0])
                pipes = get_random_pipes(SCREEN_WIDTH * 2)
                pipe_group.add(pipes[0])
                pipe_group.add(pipes[1])
                points += 1

            bird_group.update()
            ground_group.update()
            pipe_group.update()

            bird_group.draw(screen)
            ground_group.draw(screen)
            pipe_group.draw(screen)

            if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or
                    pygame.sprite.groupcollide(bird_group, pipe_group, False, False, pygame.sprite.collide_mask)):
                update_record()
                display_game_over(screen, font, points, record)
                sleep(5)
                start_the_game()
            else:
                txt = font.render(str(points), 0, (255, 255, 255))
                screen.blit(txt, (380, 146))

        pygame.display.update()


start_the_game()
