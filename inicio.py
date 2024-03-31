import pygame
import sys
from main import main as iniciar_juego

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Aventuras")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_GREEN = (0, 100, 0)  # Nuevo color para el botón

# Cargar la imagen de fondo
fondo = pygame.image.load("./imagenes/inicio.png").convert()
fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Función para mostrar la pantalla de inicio
def pantalla_inicio():
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    iniciar_juego()  # Llamar a la función iniciar_juego() de main.py para comenzar el juego


        screen.blit(fondo, (0, 0))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        boton_ancho = 200
        boton_alto = 80
        boton_radius = 20
        boton_x = (SCREEN_WIDTH - boton_ancho) // 2  # Centro horizontalmente
        boton_y = SCREEN_HEIGHT - 100  # Alineado más abajo
        boton_rect = pygame.Rect(boton_x, boton_y, boton_ancho, boton_alto)

        if boton_rect.collidepoint(mouse_x, mouse_y):
            color_boton = DARK_GREEN  # Cambiado a nuevo color
        else:
            color_boton = LIGHT_BLUE
        
        pygame.draw.rect(screen, color_boton, boton_rect, border_radius=boton_radius)
        pygame.draw.rect(screen, WHITE, boton_rect, width=3, border_radius=boton_radius)

        font_inicio = pygame.font.Font(None, 48)
        texto_inicio = font_inicio.render("Empezar", True, BLACK)  # Cambiado el color del texto a negro
        texto_inicio_rect = texto_inicio.get_rect(center=boton_rect.center)
        screen.blit(texto_inicio, texto_inicio_rect)

        pygame.display.flip()

if __name__ == "__main__":
    pantalla_inicio()
