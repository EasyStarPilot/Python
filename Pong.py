import random
import sys
import pygame

pygame.init()
# Farben
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
# Konstanten
FENSTERHOEHE = 600
FENSTERBREITE = 800
FENSTERMITTEY = FENSTERHOEHE/2
FENSTERMITTEX = FENSTERBREITE/2
SCHLAEGERABSTAND = 20
SCHLAEGERBREITE = 16
SCHLAEGERHOEHE = 90
RECHTERSCHLAEGERX = FENSTERBREITE - SCHLAEGERABSTAND - SCHLAEGERBREITE
SCHLAEGERGESCHWINDIGKEIT = 0.1
BALLGROESSE = 10
# Fenster
bildschirm = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))
pygame.display.set_caption("Pong")
# Schlägerposition
linkerSchlaegerY = 50
rechterSchlaegerY = 50
# Ballposition
ballX = FENSTERMITTEX
ballY = FENSTERMITTEY
BALLGESCHWINDIGKEIT_X = random.uniform(-0.25, 0.25)*2
BALLGESCHWINDIGKEIT_Y = random.uniform(-1, 1)*0.1
ballbewegungX = BALLGESCHWINDIGKEIT_X
ballbewegungY = BALLGESCHWINDIGKEIT_Y


# Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Tastenaktionen
    tasten = pygame.key.get_pressed()
    if tasten[pygame.K_UP]:
        rechterSchlaegerY -= SCHLAEGERGESCHWINDIGKEIT
    if tasten[pygame.K_DOWN]:
        rechterSchlaegerY += SCHLAEGERGESCHWINDIGKEIT
    if tasten[pygame.K_w]:
        linkerSchlaegerY -= SCHLAEGERGESCHWINDIGKEIT
    if tasten[pygame.K_s]:
        linkerSchlaegerY += SCHLAEGERGESCHWINDIGKEIT
    # Schlägergrenzen
    if rechterSchlaegerY <= 0:
        rechterSchlaegerY = 0
    if rechterSchlaegerY >= FENSTERHOEHE - SCHLAEGERHOEHE:
        rechterSchlaegerY = FENSTERHOEHE - SCHLAEGERHOEHE
    if linkerSchlaegerY <= 0:
        linkerSchlaegerY = 0
    if linkerSchlaegerY >= FENSTERHOEHE - SCHLAEGERHOEHE:
        linkerSchlaegerY = FENSTERHOEHE - SCHLAEGERHOEHE
    # Schläger definieren
    linkerSchlaeger = pygame.Rect(SCHLAEGERABSTAND, linkerSchlaegerY, SCHLAEGERBREITE, SCHLAEGERHOEHE)
    rechterSchlaeger = pygame.Rect(RECHTERSCHLAEGERX, rechterSchlaegerY, SCHLAEGERBREITE, SCHLAEGERHOEHE)
    # Ballbewegungen
    ballX += ballbewegungX
    ballY += ballbewegungY
    # Kollision oben und unten
    if ballY < BALLGROESSE:
        ballbewegungY = BALLGESCHWINDIGKEIT_Y *-1
    if ballY > FENSTERHOEHE - BALLGROESSE:
        ballbewegungY *= -1
    # Kollision links und rechts
    if ballX <= BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY
        ballbewegungX = BALLGESCHWINDIGKEIT_X 
        ballbewegungY = BALLGESCHWINDIGKEIT_Y
    if ballX >= FENSTERBREITE - BALLGROESSE:
        ballX = FENSTERMITTEX
        ballY = FENSTERMITTEY
        ballbewegungX *= -1
        ballbewegungY = BALLGESCHWINDIGKEIT_Y
    # Kollision Schläger
    ballRechteck = pygame.Rect(ballX-BALLGROESSE, ballY-BALLGROESSE, 2*BALLGROESSE, 2*BALLGROESSE)
    if linkerSchlaeger.colliderect(ballRechteck):
        ballX = linkerSchlaeger.right + BALLGROESSE
        ballbewegungX *= -1
    if rechterSchlaeger.colliderect(ballRechteck):
        ballX = rechterSchlaeger.left - BALLGROESSE
        ballbewegungX *= -1
    # Elemente zeichnen
    bildschirm.fill(SCHWARZ)
    pygame.draw.rect(bildschirm, WEISS, rechterSchlaeger)
    pygame.draw.circle(bildschirm, WEISS, (ballX, ballY), BALLGROESSE)
    pygame.draw.rect(bildschirm, WEISS, linkerSchlaeger)
    pygame.display.flip()