import pygame
import random
import sys
import math

# === Inicialização ===
pygame.init()

# === Tela ===
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter na Lua")

# === Cores ===
WHITE = (255, 255, 255)
RED = (255, 60, 60)
GREEN = (0, 255, 120)
YELLOW = (255, 220, 0)
BLUE = (0, 160, 255)
CYAN = (100, 255, 255)
PURPLE = (180, 80, 255)

# === Fontes ===
font = pygame.font.SysFont("Arial", 28)
font_big = pygame.font.SysFont("Arial", 64)

# === Parâmetros ===
player_speed = 7
player_lives = 3
bullet_speed = 12
bullet_cooldown = 400
enemy_spawn_delay = 700
enemy_speed_min = 2
enemy_speed_max = 5

clock = pygame.time.Clock()

# === Fundo com imagem ===
try:
    space_bg = pygame.image.load("espaco.jpg").convert()
    space_bg = pygame.transform.scale(space_bg, (WIDTH, HEIGHT))
except:
    space_bg = None
    print("⚠️ Imagem 'espaco.jpg' não encontrada. O fundo será preto.")

# === Estrelas extras (para movimento) ===
stars = []
for _ in range(50):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.uniform(0.5, 2.5)
    size = random.randint(1, 3)
    stars.append([x, y, speed, size])


# === Classe Player ===
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = player_speed
        self.lives = player_lives
        self.last_shot = pygame.time.get_ticks()
        self.cooldown = bullet_cooldown
        self.size = 35

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.size:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - self.size:
            self.x += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.cooldown:
            self.last_shot = now
            return Bullet(self.x, self.y - 30)
        return None

    def draw(self, surface):
        # Nave triangular azul com brilho
        points = [
            (self.x, self.y - self.size),
            (self.x - self.size // 1.5, self.y + self.size),
            (self.x + self.size // 1.5, self.y + self.size),
        ]
        pygame.draw.polygon(surface, BLUE, points)
        pygame.draw.polygon(surface, CYAN, points, 3)

        # Efeito de brilho pulsante
        glow = abs(math.sin(pygame.time.get_ticks() * 0.005)) * 100 + 100
        glow_color = (0, int(glow), 255)
        pygame.draw.circle(surface, glow_color, (self.x, self.y + 10), 10, 1)


# === Classe Bullet ===
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 2, y, 4, 15)
        self.trail = []

    def update(self):
        self.trail.append((self.rect.centerx, self.rect.centery))
        if len(self.trail) > 10:
            self.trail.pop(0)
        self.rect.y -= bullet_speed
        return self.rect.y > -20

    def draw(self, surface):
        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail)))
            pygame.draw.circle(surface, YELLOW, pos, 2)
        pygame.draw.rect(surface, YELLOW, self.rect)


# === Classe Enemy ===
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(30, WIDTH - 60), -40, 50, 40
        )
        self.speed = random.randint(enemy_speed_min, enemy_speed_max)
        self.color = random.choice([RED, PURPLE, GREEN])

    def update(self):
        self.rect.y += self.speed
        return self.rect.y < HEIGHT + 40

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, WHITE, self.rect, 2, border_radius=10)


# === Funções visuais ===
def draw_background(surface):
    if space_bg:
        surface.blit(space_bg, (0, 0))
    else:
        surface.fill((0, 0, 0))
    # Estrelas animadas por cima
    for star in stars:
        star[1] += star[2]
        if star[1] > HEIGHT:
            star[0] = random.randint(0, WIDTH)
            star[1] = random.randint(-20, 0)
        pygame.draw.circle(surface, WHITE, (int(star[0]), int(star[1])), star[3])


def draw_ui(surface, score, lives):
    score_text = font.render(f"Pontos: {score}", True, WHITE)
    lives_text = font.render(f"Vidas: {lives}", True, GREEN)
    surface.blit(score_text, (10, 10))
    surface.blit(lives_text, (WIDTH - 130, 10))


def game_over_screen(surface, score):
    surface.fill((0, 0, 0))
    text = font_big.render("GAME OVER", True, RED)
    score_text = font.render(f"Pontuação final: {score}", True, WHITE)
    restart_text = font.render("Pressione ENTER para jogar novamente", True, YELLOW)
    surface.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100))
    surface.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    surface.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 80))
    pygame.display.flip()


# === Loop principal ===
def main():
    player = Player()
    bullets = []
    enemies = []
    score = 0
    running = True
    game_over = False
    last_enemy_spawn = pygame.time.get_ticks()

    while running:
        clock.tick(60)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            player.move(keys)

            if keys[pygame.K_SPACE]:
                bullet = player.shoot()
                if bullet:
                    bullets.append(bullet)

            now = pygame.time.get_ticks()
            if now - last_enemy_spawn > enemy_spawn_delay:
                last_enemy_spawn = now
                enemies.append(Enemy())

            bullets = [b for b in bullets if b.update()]
            enemies = [e for e in enemies if e.update()]

            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 10
                        break

            for enemy in enemies[:]:
                if enemy.rect.colliderect(pygame.Rect(player.x - 20, player.y - 20, 40, 40)):
                    enemies.remove(enemy)
                    player.lives -= 1
                    if player.lives <= 0:
                        game_over = True
                    break

            draw_background(screen)
            player.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            draw_ui(screen, score, player.lives)

            pygame.display.flip()

        else:
            game_over_screen(screen, score)
            if keys[pygame.K_RETURN]:
                main()


# === Iniciar ===
if __name__ == "__main__":
    main()
