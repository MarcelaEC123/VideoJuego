import pygame
import sys
import subprocess

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Acertijos en Inglés")

# Cargar la imagen de fondo
background_image = pygame.image.load("./imagenes/fondo.jpg").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Cargar música de fondo
pygame.mixer.music.load("./imagenes/background_music.mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle la música de fondo

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Color rojo
GREEN = (0, 255, 0)  # Color verde
YELLOW = (255, 255, 0)  # Color amarillo
LIGHT_YELLOW = (255, 255, 153)  # Color amarillo claro para resaltar al pasar el mouse

# Reloj para controlar la velocidad de fotogramas
clock = pygame.time.Clock()

class Avatar(pygame.sprite.Sprite):
    def __init__(self, acertijos):
        super().__init__()
        self.image = pygame.image.load("./imagenes/avatar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.colisionado = False
        self.acertijos = acertijos

    def update(self):
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
        for acertijo in self.acertijos:
            if pygame.sprite.collide_rect(self, acertijo):
                self.colisionado = True

class Acertijo(pygame.sprite.Sprite):
    contador_acertijos = 0
    acertijos = []
    preguntas = ["¿Cuál es el país más grande del mundo?"]
    respuesta_correcta = 1  # Índice de la respuesta correcta

    @classmethod
    def generar_acertijos(cls, cantidad, size=(150, 80), color=WHITE):
        # Posición de la caja de pregunta
        pos_x = SCREEN_WIDTH // 2
        pos_y = SCREEN_HEIGHT - 150  # Posición en la parte inferior de la pantalla
        pos = (pos_x, pos_y)

        for i in range(cantidad):
            cls.contador_acertijos += 1
            if i < len(cls.preguntas):
                acertijo = cls(cls.preguntas[i], ["España","Rusia", "China"], cls.respuesta_correcta, pos, size, color)
                cls.acertijos.append(acertijo)

    def __init__(self, pregunta, opciones, respuesta, pos, size=(150, 80), color=WHITE):
        super().__init__()
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta = respuesta
        self.image = pygame.image.load("./imagenes/caja-misteriosa.png").convert_alpha()  # Ruta de la imagen de la caja

        # Redimensionar la imagen de la caja de acertijo
        self.image = pygame.transform.scale(self.image, (80, 80))  # Especifica las dimensiones deseadas (100x100 píxeles)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Crear un objeto de fuente para renderizar el texto
        self.font = pygame.font.Font(None, 36)  # Cambiando el tamaño de la fuente a 36

        # Renderizar el número de pregunta dentro de la caja de acertijo
        self.renderizar_numero_pregunta()

    def renderizar_numero_pregunta(self):
        # Crear texto con el número de pregunta
        numero_pregunta_texto = self.font.render(str(self.contador_acertijos), True, WHITE)  # Cambiando el color del texto a blanco

        # Obtener el rectángulo del texto renderizado
        numero_pregunta_rect = numero_pregunta_texto.get_rect()

        # Centrar el texto dentro de la caja de acertijo
        numero_pregunta_rect.midtop = self.rect.midtop  # Posicionando el texto en la parte superior central de la caja

        # Dibujar el texto en la superficie de la caja de acertijo
        self.image.blit(numero_pregunta_texto, numero_pregunta_rect)

class BotonRespuesta(pygame.sprite.Sprite):
    def __init__(self, texto, pos, is_correct=False):
        super().__init__()
        self.texto = texto
        self.font = pygame.font.Font(None, 24)
        self.is_correct = is_correct
        self.color_normal = YELLOW
        self.color_correcto = GREEN
        self.color_incorrecto = RED
        self.image = pygame.Surface((150, 80))  # Tamaño del botón
        self.rect = self.image.get_rect(center=pos)
        self.actualizar_color()

        # Renderizar el texto en el botón
        self.renderizar_texto()

    def actualizar_color(self):
        self.image.fill(self.color_normal)

    def renderizar_texto(self):
        # Renderizar el texto en negro
        texto_renderizado = self.font.render(self.texto, True, BLACK)
        texto_rect = texto_renderizado.get_rect(center=self.image.get_rect().center)
        self.image.blit(texto_renderizado, texto_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if self.is_correct:
                    print("Respuesta correcta")
                    self.image.fill(self.color_correcto)
                    subprocess.Popen(["python", "pregunta4.py"])  # Ejecutar pregunta4.py
                else:
                    print("Respuesta incorrecta")
                    self.image.fill(self.color_incorrecto)

def main():
    print("Inicializando juego...")
    Acertijo.generar_acertijos(1)

    avatar = Avatar(Acertijo.acertijos)

    # Grupo de sprites
    all_sprites = pygame.sprite.Group()
    all_sprites.add(avatar)
    for acertijo in Acertijo.acertijos:
        all_sprites.add(acertijo)

    # Crear botones para las opciones de respuesta
    botones_respuesta = []
    opciones = Acertijo.acertijos[0].opciones
    for i, respuesta in enumerate(opciones):
        pos_x = SCREEN_WIDTH // 4 * (i + 1)
        pos_y = 50
        boton = BotonRespuesta(respuesta, (pos_x, pos_y), i == Acertijo.acertijos[0].respuesta_correcta)
        botones_respuesta.append(boton)
        all_sprites.add(boton)

    print("Comenzando bucle principal...")
    # Ciclo principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for boton in botones_respuesta:
                boton.handle_event(event)

        # Actualizar
        all_sprites.update()

        # Renderizar el fondo
        screen.blit(background_image, (0, 0))

        # Verificar si el avatar está colisionando con una caja de acertijo y mostrar la pregunta
        for acertijo in Acertijo.acertijos:
            if avatar.colisionado and pygame.sprite.collide_rect(avatar, acertijo):
                # Renderizar la caja de acertijo
                screen.blit(acertijo.image, acertijo.rect)

                # Renderizar la pregunta
                pregunta_texto = acertijo.font.render(acertijo.preguntas[0], True, WHITE)  # Cambiando el color del texto a blanco
                pregunta_rect = pregunta_texto.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))  # Centrar la pregunta horizontalmente en la parte inferior de la pantalla
                screen.blit(pregunta_texto, pregunta_rect)

        # Renderizar los sprites
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    print("Saliendo del juego...")
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
