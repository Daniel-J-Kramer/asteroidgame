from circleshape import *
from constants import *
class Player(CircleShape, pygame.sprite.Sprite):

    containers = ()


    def __init__(self, x, y, PLAYER_RADIUS):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))

    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        white = (255, 255, 255, 1)
        pygame.draw.polygon(screen, white, self.triangle(), 2)
        pass

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # ?
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        self.rect = self.image.get_rect(center=(self.position.x, self.position.y))