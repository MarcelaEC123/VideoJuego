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
    acertijos = []  # Lista para almacenar las instancias de Acertijo

    @classmethod
    def generar_acertijos(cls, cantidad, size=(80, 50), color=WHITE):
        posiciones = [(50, 100), (200, 300), (350, 170), (500, 400), (650, 500), (800, 100)]  # Posiciones de las cajas
        for i in range(cantidad):
            acertijo = cls(f"Pregunta {i+1}", ["Opción 1", "Opción 2", "Opción 3"], 0, posiciones[i], size, color)
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
        numero_pregunta_texto = self.font.render(self.pregunta.split()[1], True, BLACK)  # Obtener el número de la pregunta y renderizarlo en negro

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
    Acertijo.generar_acertijos(6, color=(255, 255, 0))  # Cambiar el color de las cajas de acertijos a azul
    acertijos = Acertijo.acertijos  # Obtener las instancias generadas 

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)
    for acertijo in acertijos:
        all_sprites.add(acertijo)  # Agregar cada instancia de Acertijo al grupo de sprites

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
