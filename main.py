from pygame import *
import sys

init()
running = True
clock = time.Clock()

fonte = font.Font('fonte.ttf', 50)

imagem = image.load('image.jpg')

mixer.music.load('workshop.mp3')
mixer.music.play(-1)

window = display.set_mode((1280,720))

window.fill(((151, 209, 250)))

cor_fundo = 151, 209, 250
a = 0
pos_x = 300
pos_sol = 0

while running:
    clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                cor_fundo = 114, 47, 55
    
    #Update
    dt = clock.get_time()/1000   
    keys = key.get_pressed()
    window.fill(((cor_fundo)))
    
    #Nuvem ficar andando
    if a == 0:
        pos_x = pos_x + 100 * dt
    else: 
        pos_x = pos_x - 100 * dt 
    #Nuvem bate na ponta e volta pro começo
    if pos_x > 1020:
        a = a + 1
    elif pos_x < 0:
        a = 0
    #Sol andando e mudando a cor do mundo
    pos_sol = pos_sol + 100 * dt
    if pos_sol > 1020:
        pos_sol = 0
        cor_fundo = 151, 209, 250
    if pos_sol > 300:
        #SE MOUSE CLICAR AQUI (TOCAR TAL AUDIO)
        cor_fundo = 237, 193, 100
    if pos_sol > 500:
        cor_fundo = 217, 164, 52
        #SE MOUSE CLICAR AQUI (TOCAR OUTRO AUDIO)
    if pos_sol > 800:
        #SE MOUSE CLICAR AQUI (TOCAR OUTRO AUDIO)
        cor_fundo = 219, 154, 15

    #Desenhar fonte
    fonte_texto = fonte.render('O hexa vem esse ano', True, (255, 0, 0))
    window.blit(fonte_texto, (800, 500))
    #Desenhar imagem 
    window.blit(imagem, (950, 250))
    #Grama
    draw.rect(window, (72, 157, 37), (0, 570, 1280, 150))
    #Sol
    draw.circle(window, (255, 255, 0), (pos_sol, 0), (150))
    #Nuvem
    draw.circle(window, (255, 255, 255), (pos_x, 100), (50))
    draw.circle(window, (255, 255, 255), (pos_x + 70, 100), (50))
    draw.circle(window, (255, 255, 255), (pos_x + 140, 100), (50))
    draw.circle(window, (255, 255, 255), (pos_x + 210, 100), (50))
    #Árvore
    draw.rect(window, (165, 42, 42), (600, 370, 30, 200))
    draw.circle(window, (6, 64, 43), (615, 370), (100))
    #Casa
    draw.rect(window, (0, 67, 33), (50, 370, 400, 200))
    #Casa(telhado)
    pontos = [(50, 370), (250, 200), (450, 370)]
    draw.polygon(window, (65, 42, 42), (pontos))
    #Casa(porta)
    draw.rect(window, (235, 137, 52),(110, 400, 80, 170))
    #Casa(janela)
    draw.rect(window, (122, 89, 60), (270, 420, 100, 100))
    #Casa(macaneta)
    draw.circle(window, (111, 138, 15), (130, 485), (10))

    display.update()