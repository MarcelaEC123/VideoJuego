import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Acertijos en Inglés")

# Cargar la imagen de fondo
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

class Avatar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar la imagen del muñeco (asegúrate de que la ruta sea correcta)
        self.image = pygame.image.load("avatar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Control de movimiento del avatar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

class Acertijo(pygame.sprite.Sprite):
    def __init__(self, pregunta, opciones, respuesta):
        super().__init__()
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta

    def mostrar_pregunta(self):
        # Aquí puedes mostrar la pregunta y sus opciones en pantalla
        pass

def main():
    avatar = Avatar()
    acertijo = Acertijo("¿Qué significa 'hello' en español?", ["Hola", "Adiós", "Gracias", "Por favor"], 0)

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)

    # Ciclo principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar
        all_sprites.update()

        # Renderizar el fondo
        screen.blit(background_image, (0, 0))

        # Renderizar
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
