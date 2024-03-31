import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Crear la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pantalla de Videojuego")

# Cargar imagen de fondo y ajustar tamaño
background_image = pygame.image.load("./imagenes/ganador.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar imagen del avatar
avatar_image = pygame.image.load("./imagenes/avatar.png")

# Cargar fuente de texto
font = pygame.font.SysFont(None, 100)  # Tamaño de la fuente

# Cargar música de fondo
pygame.mixer.music.load("./imagenes/background_music.mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle infinito

# Función para mostrar texto en la pantalla con un tamaño variable y movimiento vertical
def show_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)  # Alineado en el medio superior de la pantalla
    return text_surface, text_rect

# Loop principal del juego
def main():
    avatar_x = (SCREEN_WIDTH - avatar_image.get_width()) // 2  # Centrado horizontalmente
    avatar_y = SCREEN_HEIGHT - avatar_image.get_height() - 60  # Abajo de la pantalla con un pequeño espacio
    
    # Inicializar propiedades del texto
    text_x = SCREEN_WIDTH // 2  # Centrado horizontalmente
    text_y = 200  # Bajar un poco el texto
    text_surface, text_rect = show_text("¡Lo lograste!", text_x, text_y, color=RED)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar el fondo
        screen.blit(background_image, (0, 0))

        # Dibujar el texto en la parte superior de la pantalla con movimiento
        text_rect.y = text_y + 10 * math.sin(pygame.time.get_ticks() / 100)
        screen.blit(text_surface, text_rect)

        # Dibujar el avatar en la parte inferior de la pantalla
        screen.blit(avatar_image, (avatar_x, avatar_y))

        # Actualizar la pantalla
        pygame.display.flip()

        # Limitar la velocidad de fotogramas
        pygame.time.Clock().tick(60)

    # Detener la música al salir del juego
    pygame.mixer.music.stop()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
