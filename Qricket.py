import sys, pygame
import itertools
import Qstate as Q

running = True
qubits = 2
gates = [{0: 'x', 1: 'x'}, {0: 'h'}, {0: 'cnot'}]
q = Q.state(qubits)
step = -1

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

block = int(WINDOW_HEIGHT / (qubits + 2))

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)

img_0 = pygame.image.load("0.png")
img_1 = pygame.image.load("1.png")

def eval():
    if step < len(gates) and step >= 0:
        for gate in gates[step]:
            getattr(q, gates[step][gate])(gate)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                step -= 1
                eval()
            if event.key == pygame.K_RIGHT:
                step += 1
                eval()
    screen.fill(WHITE)
    for x in range(0, WINDOW_WIDTH, block):
        for y in range(0, WINDOW_HEIGHT, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(screen, BLACK, rect, 1)
    i = 0
    for state in q.state:
        if state != 0j:
            for qubit in range(0, qubits):

                text = font.render(str(q.matrix[i][qubit]), True, BLACK)
                text_rect = text.get_rect(center=(block/2, block/2))
                x = text_rect[0] + ((step*2) * block) + block + block
                y = text_rect[1] + (qubit * block) + block
                screen.blit(text, (x, y))
                if q.matrix[i][qubit] == '0':
                    img_rect = img_0.get_rect(center=(block/2, block/2))
                    x = img_rect[0] + ((step*2) * block) + block + block
                    y = img_rect[1] + (qubit * block) + block
                    screen.blit(img_0, (x, y))
                elif q.matrix[i][qubit] == '1':
                    img_rect = img_1.get_rect(center=(block/2, block/2))
                    x = img_rect[0] + ((step*2) * block) + block + block
                    y = img_rect[1] + (qubit * block) + block
                    screen.blit(img_1, (x, y))       
        i += 1
    i = 0
    for q_gates in gates:
        for q_gate in q_gates:
            text = font.render(q_gates[q_gate], True, BLACK)
            text_rect = text.get_rect(center=(block/2, block/2))
            x = text_rect[0] + ((i*2) * block) + block
            y = text_rect[1] + (q_gate * block) + block
            screen.blit(text, (x, y))
        i += 1
    pygame.display.update()

pygame.quit()