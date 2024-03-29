import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Cargar la imagen de fondo
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Acertijos en Inglés")
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar la música de fondo
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# Función para pausar la música de fondo
def pause_music():
    pygame.mixer.music.pause()

# Función para reanudar la música de fondo
def resume_music():
    pygame.mixer.music.unpause()

# Clase del botón
class Button(pygame.sprite.Sprite):
    def __init__(self, text, position, action):
        super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.image = self.font.render(text, True, BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.action = action

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.font.render(self.text, True, RED)
        else:
            self.image = self.font.render(self.text, True, BLACK)

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
    contador_acertijos = 0  # Contador de acertijos
    acertijos = []  # Lista para almacenar instancias de acertijos

    @classmethod
    def generar_acertijos(cls, cantidad, size=(80, 50), color=WHITE):
        posiciones = [(50, 440), (200, 350), (350, 440), (500, 350), (650, 440), (800, 350)]  # Posiciones de las cajas
        for i in range(cantidad):
            cls.contador_acertijos += 1  # Incrementar el contador
            acertijo = cls(f"Pregunta {cls.contador_acertijos}", ["Opción 1", "Opción 2", "Opción 3"], 0, posiciones[i], size, color)
            cls.acertijos.append(acertijo)

    def __init__(self, pregunta, opciones, respuesta, pos, size=(100, 50), color=WHITE):
        super().__init__()
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        # Crear un objeto de fuente para renderizar el texto
        self.font = pygame.font.Font(None, 24)  # Tamaño de la fuente 24

        # Renderizar el número de pregunta dentro de la caja de acertijo
        self.renderizar_numero_pregunta()

    def renderizar_numero_pregunta(self):
        # Crear texto con el número de pregunta
        numero_pregunta_texto = self.font.render(str(self.contador_acertijos), True, BLACK)  # Renderizar el contador como texto en negro

        # Obtener el rectángulo del texto renderizado
        numero_pregunta_rect = numero_pregunta_texto.get_rect()

        # Centrar el texto dentro de la caja de acertijo
        numero_pregunta_rect.center = self.rect.center

        # Dibujar el texto en la superficie de la caja de acertijo
        self.image.blit(numero_pregunta_texto, numero_pregunta_rect)


    def mostrar_pregunta(self):
        # Aquí puedes mostrar la pregunta y sus opciones en pantalla
        pass


def main():
    avatar = Avatar()
    Acertijo.generar_acertijos(6)  # Generar 6 cajas de acertijos
    Acertijo.generar_acertijos(6, color=(0, 0, 255))  # Cambiar el color de las cajas de acertijos a azul
    acertijos = Acertijo.acertijos  # Obtener las instancias generadas 

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)
    for acertijo in acertijos:
        all_sprites.add(acertijo)  # Agregar cada instancia de Acertijo al grupo de sprites

    # Crear botones para detener, pausar y reanudar la música
    pause_button = Button("Pause Music", (700, 20), pause_music)
    resume_button = Button("Resume Music", (700, 60), resume_music)
    all_sprites.add(pause_button, resume_button)

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
