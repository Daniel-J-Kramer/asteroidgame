from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED
import pygame
from shot import Shot
class Player(CircleShape):



    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255, 1), self.triangle(), 2)
        pass

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.timer -= dt
        pass

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            playershot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            playershot.velocity = pygame.Vector2(0, 1)
            playershot.velocity = playershot.velocity.rotate(self.rotation)
            playershot.velocity *= PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
