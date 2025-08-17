import pygame
from random import randint

pygame.init()

# Configurações iniciais
x = 250
y = 260
y1 = -40
xvig = 155
xaereo = 258
xrocha = 350
yvig = 700
yaereo = 1000
yrocha = 800
v1 = -30
velocidade = 35
velocidade_outros = 15
timer = 0
segundos = 0
game_over = False
jogo_iniciado = False

# Carregando imagens
fundo = pygame.image.load('fundow.jpg')
movepista1 = pygame.image.load('movepista.jpg')
movepista2 = pygame.image.load('movepista.jpg')

carro_penny = pygame.image.load('carro_penelope.png')
carro_penny = pygame.transform.scale(carro_penny, (100, 140))

carro_vigarista = pygame.image.load('carro_vigarista.png')
carro_vigarista = pygame.transform.scale(carro_vigarista, (85, 160))

carro_aereo = pygame.image.load('carro_aereo.png')
carro_aereo = pygame.transform.scale(carro_aereo, (85, 160))

carro_rocha = pygame.image.load('carro_rocha.png')
carro_rocha = pygame.transform.scale(carro_rocha, (85, 160))

font = pygame.font.SysFont('comicsans', 25)
texto = font.render("TEMPO: 0", True, (255, 255, 255), (255, 0, 127))
posicaotexto = texto.get_rect()
posicaotexto.center = (65, 50)

pygame.mixer.music.load("musicafundo.mp3")

som_gameover = pygame.mixer.Sound("gameover.mp3")

janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Penelope's Race")

while not jogo_iniciado:
    janela.fill((0, 0, 0))  # Fundo preto
    pygame.draw.rect(janela, (255, 0, 127), (100, 200, 400, 150))  # Retângulo 

    font = pygame.font.SysFont("comicsans", 30)
    texto1 = font.render("Pressione ENTER para jogar", True, (255, 255, 255))
    janela.blit(texto1, (100, 240))

    pygame.display.update()  # Atualiza a tela 
 
 #enter para começar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            jogo_iniciado = True
            pygame.mixer.music.play(-1)  

# Loop principal 
janela_open = True
while janela_open:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_open = False

        # recomeça "P"
        if jogo_iniciado and event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            x = 250
            y = 260
            yvig = randint(1000, 2000)
            yaereo = yvig + randint(300, 400) 
            yrocha = yaereo + randint (400, 500) 
            xtodos = 250
            segundos = 0
            timer = 0
            game_over = False
            pygame.mixer.music.play(-1)  

    if not game_over:
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT] and x <= 345:
            x += velocidade
        if comandos[pygame.K_LEFT] and x >= 150:
            x -= velocidade

        # Movimento da pista
        y1 -= v1
        if y1 >= 650:
            y1 = -40

    
        if yvig <= -100:
            yvig = randint(1000, 2000)
            
        if yaereo <= -100:
            yaereo = yvig + randint(300, 400) 
     
        if yrocha <= -100:
            yrocha = yaereo + randint (400, 500) 

     
        yvig -= velocidade_outros + 7
        yaereo -= velocidade_outros + 5
        yrocha -= velocidade_outros + 3


        # Contador de tempo
        if timer < 20:
            timer += 1
        else:
            segundos += 1
            texto = font.render("TEMPO: " + str(segundos), True, (255, 255, 255), (255, 0, 127))
            timer = 0

         # Colisões
        if (x <xrocha + 85 and x + 100 > xrocha and y < yrocha + 160 and y + 140 > yrocha):
            game_over = True
            pygame.mixer.music.stop()  
            som_gameover.play()  

        if (x < xvig +85 and x + 100 > xvig and y < yvig + 160 and y + 140 > yvig):
            game_over = True
            pygame.mixer.music.stop() 
            som_gameover.play()  

        if (x < xaereo+85 and x + 100 > xaereo and y < yaereo + 160 and y + 140 > yaereo):
            game_over = True 
            pygame.mixer.music.stop()  
            som_gameover.play()

 
    janela.fill((0, 0, 0))  # Limpar tela antes de desenhar
    janela.blit(fundo, (0, 0))
    janela.blit(movepista1, (250, y1))
    janela.blit(movepista2, (320, y1))
    janela.blit(carro_penny, (x, y))
    janela.blit(carro_vigarista, (xvig, yvig))
    janela.blit(carro_aereo, (xaereo, yaereo))
    janela.blit(carro_rocha, (xrocha , yrocha))
    janela.blit(texto, posicaotexto)

    if game_over:
        janela.fill((255, 0, 127))
        font = pygame.font.SysFont("comicsans", 25)
        texto1 = font.render("Game Over!", True, (255, 255, 255))
        texto2 = font.render(f"Seu tempo foi: {segundos} segundos", True, (255, 255, 255))
        texto3 = font.render("Pressione P para tentar novamente", True, (255, 255, 255))
        janela.blit(texto1, (100, 200))
        janela.blit(texto2, (100, 270))
        janela.blit(texto3, (100, 340))
    pygame.display.update()
 
pygame.quit()