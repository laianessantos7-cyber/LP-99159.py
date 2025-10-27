import pygame
import sys
import random
 # P
pygame.init()
pygame.font.init()

# =========================
# Configurações da Tela
# =========================
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cassino Visual - Pygame")

# =========================
# Cores e fontes
# =========================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 220, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 0)
GRAY = (50, 50, 50)
DARK_RED = (120, 0, 0)
GOLD = (255, 215, 0)

font_small = pygame.font.SysFont("Arial", 24)
font_med = pygame.font.SysFont("Arial", 36)
font_big = pygame.font.SysFont("Arial", 48)

# =========================
# Classe Botão
# =========================
class Button:
    def __init__(self, x, y, w, h, text, color, hover_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(surface, self.hover_color, self.rect, border_radius=8)
        else:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        txt = font_med.render(self.text, True, WHITE)
        surface.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                           self.rect.centery - txt.get_height() // 2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# =========================
# Jogador
# =========================
class Player:
    def __init__(self, name="Jogador", bankroll=1000):
        self.name = name
        self.bankroll = bankroll
        self.history = []

    def adjust_bankroll(self, amount):
        self.bankroll += amount
        self.history.append(f"Alterou banca: {amount:+}, saldo: {self.bankroll}")

player = Player()

# =========================
# Menu Principal
# =========================
def main_menu():
    blackjack_btn = Button(300, 150, 200, 60, "Blackjack", BLUE, GREEN)
    roulette_btn = Button(300, 250, 200, 60, "Roleta", RED, YELLOW)
    slots_btn = Button(300, 350, 200, 60, "Slots", DARK_RED, GREEN)
    quit_btn = Button(300, 450, 200, 60, "Sair", GRAY, RED)

    running = True
    while running:
        screen.fill((34, 139, 34))  # Fundo verde cassino

        # Texto banca
        balance_txt = font_med.render(f"Banca: ${player.bankroll}", True, GOLD)
        screen.blit(balance_txt, (WIDTH // 2 - balance_txt.get_width() // 2, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if blackjack_btn.is_clicked(event):
                blackjack_game()
            if roulette_btn.is_clicked(event):
                roulette_game()
            if slots_btn.is_clicked(event):
                slots_game()
            if quit_btn.is_clicked(event):
                pygame.quit()
                sys.exit()

        # Desenha botões
        blackjack_btn.draw(screen)
        roulette_btn.draw(screen)
        slots_btn.draw(screen)
        quit_btn.draw(screen)

        pygame.display.flip()


# =========================
# Blackjack Visual
# =========================
def blackjack_game():
    running = True
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠', '♥', '♦', '♣']
    deck = [(c, s) for c in cards for s in suits]
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    hit_btn = Button(100, 500, 150, 50, "Hit", BLUE, GREEN)
    stand_btn = Button(300, 500, 150, 50, "Stand", RED, YELLOW)
    back_btn = Button(550, 500, 150, 50, "Menu", GRAY, RED)

    def draw_hand():
        screen.fill((0, 100, 0))
        # Mostrar dealer
        dealer_txt = font_med.render("Dealer", True, WHITE)
        screen.blit(dealer_txt, (50, 50))
        for i, card in enumerate(dealer_hand):
            pygame.draw.rect(screen, WHITE, (50 + i*80, 100, 70, 100))
            txt = font_big.render(f"{card[0]}{card[1]}", True, BLACK)
            screen.blit(txt, (55 + i*80, 120))

        # Mostrar jogador
        player_txt = font_med.render("Você", True, WHITE)
        screen.blit(player_txt, (50, 250))
        for i, card in enumerate(player_hand):
            pygame.draw.rect(screen, WHITE, (50 + i*80, 300, 70, 100))
            txt = font_big.render(f"{card[0]}{card[1]}", True, BLACK)
            screen.blit(txt, (55 + i*80, 320))

        # Desenha botões
        hit_btn.draw(screen)
        stand_btn.draw(screen)
        back_btn.draw(screen)

    while running:
        draw_hand()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if hit_btn.is_clicked(event):
                player_hand.append(deck.pop())
            if stand_btn.is_clicked(event):
                # Dealer simples: adiciona carta se <17
                while sum_card_values(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                running = False
            if back_btn.is_clicked(event):
                return
        pygame.display.flip()
        pygame.time.Clock().tick(30)

def sum_card_values(hand):
    value = 0
    aces = 0
    card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
    for c, s in hand:
        value += card_values[c]
        if c == 'A':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# =========================
# Roleta Visual
# =========================
def roulette_game():
    running = True
    spin_btn = Button(325, 500, 150, 50, "Girar", RED, YELLOW)
    back_btn = Button(550, 500, 150, 50, "Menu", GRAY, RED)
    result = None

    while running:
        screen.fill((50, 0, 50))
        txt = font_big.render("Roleta", True, WHITE)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, 50))
        spin_btn.draw(screen)
        back_btn.draw(screen)

        # Mostrar resultado
        if result is not None:
            res_txt = font_med.render(f"Resultado: {result}", True, GOLD)
            screen.blit(res_txt, (WIDTH//2 - res_txt.get_width()//2, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if spin_btn.is_clicked(event):
                result = random.randint(0, 36)
            if back_btn.is_clicked(event):
                return

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# =========================
# Slots Visual
# =========================
def slots_game():
    running = True
    spin_btn = Button(325, 500, 150, 50, "Girar", DARK_RED, GREEN)
    back_btn = Button(550, 500, 150, 50, "Menu", GRAY, RED)
    symbols = ['🍒','🍋','🔔','⭐','7','🍊']
    result = ["","",""]

    while running:
        screen.fill((0, 0, 50))
        txt = font_big.render("Slots", True, WHITE)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, 50))

        # Mostrar resultado
        for i, sym in enumerate(result):
            sym_txt = font_big.render(sym, True, GOLD)
            screen.blit(sym_txt, (250 + i*100, 250))

        spin_btn.draw(screen)
        back_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if spin_btn.is_clicked(event):
                result = [random.choice(symbols) for _ in range(3)]
            if back_btn.is_clicked(event):
                return

        pygame.display.flip()
        pygame.time.Clock().tick(30)

# =========================
# Iniciar Cassino
# =========================
if __name__ == "__main__":
    main_menu()
