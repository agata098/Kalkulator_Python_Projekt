import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((350,450))
pygame.display.set_caption("Kalkulator")

k_tla = (28,28,30)
k_przyciskow_cyfr= (58,58,50)
k_przyciskow_operacji = (255,165,0)
k_czcionki = (255, 255, 255)

czcionka= pygame.font.SysFont("Arial",32, bold="True")

panel= ""

l_przyciskow =[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+',
]

def rysowanie_przyciskow(tekst,x,y,w,h,kolor):
    myszka= pygame.mouse.get_pos()
    przycisk= pygame.Rect(x,y,w,h)
    biezacy_kolor=kolor
    if przycisk.collidepoint(myszka):
        biezacy_kolor= (min(kolor[0]+40,255),min(kolor[1]+40,255),min(kolor[2]+40,255))

    pygame.draw.rect(screen,biezacy_kolor,przycisk,border_radius=15)

    obrazek_liczby= czcionka.render(tekst,True, k_czcionki)
    miejsce_liczby =  obrazek_liczby.get_rect(center=przycisk.center)
    screen.blit(obrazek_liczby, miejsce_liczby)
    return przycisk

running=True
while running:
    screen.fill(k_tla)
    wyswietlacz= pygame.Rect(20,20,310,80)
    pygame.draw.rect(screen,(44,44,46),wyswietlacz,border_radius=10)
    tekst_wyswietlacza= czcionka.render(panel,True,k_czcionki)
    screen.blit((tekst_wyswietlacza), (30,40))

    pom_lista=[]
    start_x=20
    start_y=120
    wys_p=70
    dl_p=70
    przerwa =10

    for i,char in enumerate(l_przyciskow):
        wiersz = i//4
        kolumna = i%4
        if char in "/+*-=":
            ostateczny_kolor = k_przyciskow_operacji
        else:
            ostateczny_kolor= k_przyciskow_cyfr
        if char=="C":
            ostateczny_kolor=(255,69,58)

        pozycja_x = start_x+ kolumna*(dl_p+ przerwa)
        pozycja_y = start_y + wiersz*(wys_p+przerwa)
        przycisk = rysowanie_przyciskow(char,pozycja_x,pozycja_y,dl_p,wys_p,ostateczny_kolor)
        pom_lista.append([przycisk,char])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type== pygame.MOUSEBUTTONDOWN:
            for przycisk,char in pom_lista:
                if przycisk.collidepoint(event.pos):
                    if char=="C":
                        panel= ''
                    elif char== "=":
                        if "/0" in panel:
                            panel ='Błąd'
                        elif panel != '':
                            panel= str(eval(panel))
                    else:
                        if panel == "Błąd":
                            panel= ''
                        panel += char
    pygame.display.flip()
pygame.quit()
sys.exit()