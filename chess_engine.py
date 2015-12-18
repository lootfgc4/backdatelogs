import pygame, sys
# Chess Core Engine (2015) - Graphical rendering and Move validation
class ChessUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((512, 512))
        self.board_colors = [(240, 217, 181), (181, 136, 99)]
    def render_board(self):
        for r in range(8):
            for c in range(8):
                color = self.board_colors[(r + c) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(c*64, r*64, 64, 64))
    def start_engine(self):
        pygame.display.set_caption("Chess Engine 2015")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            self.render_board(); pygame.display.flip()
if __name__ == "__main__":
    print("[*] Initializing Chess UI Components...")
