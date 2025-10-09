import pygame
import sys
import random

pygame.init()
pygame.font.init()

# =========================
# Configurações da Tela
# =========================
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dominó Visual Animado")

# =========================
# Cores e fontes
# =========================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
RED = (220, 50, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 215, 0)
GRAY = (200, 200, 200)

font_numbers = pygame.font.SysFont("Arial", 20, bold=True)
font_med = pygame.font.SysFont("Arial", 28)
font_big = pygame.font.SysFont("Arial", 36)
font_small = pygame.font.SysFont("Arial", 18)

# =========================
# Botão
# =========================
class Button:
    def __init__(self, x, y, w, h, text, color, hover_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        pygame.draw.rect(surface, self.hover_color if self.rect.collidepoint(mouse) else self.color, self.rect, border_radius=8)
        txt = font_med.render(self.text, True, WHITE)
        surface.blit(txt, (self.rect.centerx - txt.get_width() // 2,
                           self.rect.centery - txt.get_height() // 2))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# =========================
# Criação das peças
# =========================
def create_domino_set():
    pieces = [(i, j) for i in range(7) for j in range(i,7)]
    random.shuffle(pieces)
    return pieces

# =========================
# Distribuição inicial
# =========================
def deal_pieces(pieces):
    player_hand = [pieces.pop() for _ in range(7)]
    ai_hand = [pieces.pop() for _ in range(7)]
    return player_hand, ai_hand, pieces

# =========================
# Classe de peça animada
# =========================
class AnimatedPiece:
    def __init__(self, piece, start_pos, end_pos, rotation=0):
        self.piece = piece
        self.x, self.y = start_pos
        self.end_x, self.end_y = end_pos
        self.rotation = rotation
        self.speed = 15
        self.finished = False

    def update(self):
        dx = self.end_x - self.x
        dy = self.end_y - self.y
        dist = (dx**2 + dy**2)**0.5
        if dist < self.speed:
            self.x, self.y = self.end_x, self.end_y
            self.finished = True
        else:
            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self, surface):
        rect = pygame.Rect(0, 0, 60, 30)
        rect.center = (self.x+30, self.y+15)
        rotated_surf = pygame.Surface((60,30), pygame.SRCALPHA)
        pygame.draw.rect(rotated_surf, WHITE, (0,0,60,30), border_radius=5)
        pygame.draw.line(rotated_surf, BLACK, (30,0),(30,30),2)
        left_number = font_numbers.render(str(self.piece[0]), True, BLACK)
        right_number = font_numbers.render(str(self.piece[1]), True, BLACK)
        rotated_surf.blit(left_number, (10,5))
        rotated_surf.blit(right_number, (40,5))
        rotated_surf = pygame.transform.rotate(rotated_surf, self.rotation)
        surface.blit(rotated_surf, rotated_surf.get_rect(center=rect.center))

# =========================
# Desenhar peças do jogador
# =========================
def draw_player_hand(surface, hand, selected_index):
    for i, piece in enumerate(hand):
        x = 50 + i*70
        y = 620
        draw_rect(surface, piece, x, y, selected=(i==selected_index))

def draw_rect(surface, piece, x, y, selected=False):
    pygame.draw.rect(surface, WHITE, (x, y, 60, 30), border_radius=5)
    pygame.draw.line(surface, BLACK, (x+30, y), (x+30, y+30), 2)
    left_number = font_numbers.render(str(piece[0]), True, BLACK)
    right_number = font_numbers.render(str(piece[1]), True, BLACK)
    surface.blit(left_number, (x+10, y+5))
    surface.blit(right_number, (x+40, y+5))
    if selected:
        pygame.draw.rect(surface, RED, (x-2, y-2, 64, 34), 3)

# =========================
# Função principal do jogo
# =========================
def domino_game():
    pieces = create_domino_set()
    player_hand, ai_hand, boneyard = deal_pieces(pieces)
    board = []
    animated_pieces = []
    player_turn = True
    selected_piece_index = None
    move_history = []

    back_btn = Button(1050, 620, 120, 50, "Menu", GRAY, RED)

    running = True
    while running:
        screen.fill(GREEN)

        # Mostrar vez
        turn_txt = font_med.render(f"Vez: {'Você' if player_turn else 'IA'}", True, YELLOW)
        screen.blit(turn_txt, (WIDTH//2 - turn_txt.get_width()//2, 20))

        # Peças do jogador
        draw_player_hand(screen, player_hand, selected_piece_index)

        # Peças no tabuleiro animadas
        for ap in animated_pieces:
            ap.update()
            ap.draw(screen)
        animated_pieces = [ap for ap in animated_pieces if not ap.finished]

        # Histórico
        hist_txt = font_small.render("Histórico:", True, WHITE)
        screen.blit(hist_txt, (1050, 50))
        for idx, m in enumerate(move_history[-10:]):
            color = GREEN if "Você" in m else RED
            txt = font_small.render(m, True, color)
            screen.blit(txt, (1050, 70+idx*20))

        back_btn.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_btn.is_clicked(event):
                return

            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                for i, piece in enumerate(player_hand):
                    x = 50 + i*70
                    y = 620
                    if pygame.Rect(x, y, 60, 30).collidepoint(event.pos):
                        selected_piece_index = i
                if selected_piece_index is not None:
                    piece = player_hand[selected_piece_index]
                    if not board or piece[0]==board[-1][1] or piece[1]==board[-1][1]:
                        end_pos = (400 + len(board)*65, 250)
                        animated_pieces.append(AnimatedPiece(piece, (50 + selected_piece_index*70,620), end_pos))
                        board.append(piece)
                        move_history.append(f"Você jogou {piece}")
                        player_hand.pop(selected_piece_index)
                        selected_piece_index = None
                        player_turn = False

        # Turno IA simples
        if not player_turn and not animated_pieces:
            pygame.time.delay(500)
            played = False
            for i, piece in enumerate(ai_hand):
                if not board or piece[0]==board[-1][1] or piece[1]==board[-1][1]:
                    end_pos = (400 + len(board)*65, 250)
                    animated_pieces.append(AnimatedPiece(piece, (WIDTH//2,0), end_pos))
                    board.append(piece)
                    move_history.append(f"IA jogou {piece}")
                    ai_hand.pop(i)
                    played = True
                    break
            if not played and boneyard:
                ai_hand.append(boneyard.pop())
            player_turn = True

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# =========================
# Menu principal
# =========================
def main_menu():
    domino_btn = Button(450, 250, 300, 60, "Dominó", BLUE, GREEN)
    quit_btn = Button(450, 350, 300, 60, "Sair", GRAY, RED)

    running = True
    while running:
        screen.fill(GREEN)
        title_txt = font_big.render("Dominó Visual Animado", True, YELLOW)
        screen.blit(title_txt, (WIDTH//2 - title_txt.get_width()//2, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if domino_btn.is_clicked(event):
                domino_game()
            if quit_btn.is_clicked(event):
                pygame.quit()
                sys.exit()

        domino_btn.draw(screen)
        quit_btn.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
