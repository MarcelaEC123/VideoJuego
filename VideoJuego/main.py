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
WHITE = (0, 255, 255)
BLACK = (0, 0, 0)

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

# Cargar la música de fondo y reproducirla en un bucle
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

class Avatar(pygame.sprite.Sprite):
    def __init__(self, acertijos):  # Pasar la lista de acertijos como parámetro
        super().__init__()
        # Cargar la imagen del muñeco (asegúrate de que la ruta sea correcta)
        self.image = pygame.image.load("avatar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.colisionado = False  # Variable para controlar si el avatar está colisionando con una caja de acertijo
        self.acertijos = acertijos  # Almacenar la lista de acertijos como atributo del avatar

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

        # Comprobar colisión con las cajas de acertijos
        self.colisionado = False
        for acertijo in self.acertijos:  # Acceder a la lista de acertijos del avatar
            if pygame.sprite.collide_rect(self, acertijo):
                self.colisionado = True

class Acertijo(pygame.sprite.Sprite):
    contador_acertijos = 0  # Contador de acertijos
    acertijos = []  # Lista para almacenar las instancias de Acertijo
    preguntas = ["¿Cual es el pasado del verbo 'to have'?", "¿Como se dice tiburon en ingles?", "¿Como preguntar algo que no se en ingles ?", "¿Cuál es el océano más grande?", "¿Cuál es la montaña más alta del mundo?", "¿Cuál es el símbolo químico del agua?"]

    @classmethod
    def generar_acertijos(cls, cantidad, size=(80, 50), color=WHITE):
        posiciones = [(50, 440), (200, 350), (350, 440), (500, 350), (650, 440), (800, 350)]  # Posiciones de las cajas
        for i in range(cantidad):
            cls.contador_acertijos += 1  # Incrementar el contador
            acertijo = cls(cls.preguntas[i], ["Opción 1", "Opción 2", "Opción 3"], 0, posiciones[i], size, color)
            cls.acertijos.append(acertijo)

    def __init__(self, pregunta, opciones, respuesta, pos, size=(100, 50), color=WHITE):
        super().__init__()
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
        self.image = pygame.Surface(size)  # Corregido aquí
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

def main():
    Acertijo.generar_acertijos(6)  # Generar 6 cajas de acertijos

    avatar = Avatar(Acertijo.acertijos)  # Crear el avatar pasando la lista de acertijos como parámetro

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)
    for acertijo in Acertijo.acertijos:
        all_sprites.add(acertijo)  # Agregar cada instancia de Acertijo al grupo de sprites

    # Fuente para mostrar la pregunta
    font = pygame.font.Font(None, 36)

    # Ciclo principal
    running = True
    while running:
        avatar_moved = False  # Bandera para controlar si el avatar se movió en el ciclo actual

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Verificar si el avatar se movió
        keys = pygame.key.get_pressed()
        avatar_moved = any(keys)  # Si alguna tecla está presionada, el avatar se movió

        # Actualizar
        all_sprites.update()

        # Renderizar el fondo
        screen.blit(background_image, (0, 0))

        # Renderizar
        all_sprites.draw(screen)

        # Mostrar pregunta si el avatar está colisionando con una caja de acertijo y no se ha movido
        for acertijo in Acertijo.acertijos:
            if avatar.colisionado and not avatar_moved and pygame.sprite.collide_rect(avatar, acertijo):  # Solo mostrar si está colisionando, no se ha movido y está colisionando con el acertijo actual
                pregunta_texto = font.render(acertijo.pregunta, True, BLACK)
                screen.blit(pregunta_texto, (SCREEN_WIDTH // 2 - pregunta_texto.get_width() // 2, 50))
                break  # Mostrar solo la pregunta del acertijo actual

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
