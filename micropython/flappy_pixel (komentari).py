from microbit import * # obavezno u svakom programu za micro:bit
import random # modul za generiranje slučajnih vrijednosti

pixel_row = 2 # redak u kojem se pixel nalazi, na početku je u sredini
gate_column = 4 # stupac u kojem se vrata nalaze, svaka vrata su na početku u zadnjem stupcu
gate_row = 1 # redak u kojem vrata počinju, tj. praznina kroz koju pixel može proći
gate_size = 3 # veličina vrata, broj redaka kroz koje pixel može proći
gate_move = False # varijabla koja određuje pomiču li se vrata prema pixelu, vrata se pomiču u svakoj drugoj iteraciji
score = 0 # rezultat koji je igrač postigao, broj vrata kroz koje je pixel prošao

while True: # beskonačna petlja, može se prekinuti samo naredbom break
    y = accelerometer.get_y() # čitamo y vrijednost akcelerometra
    if y > 600 and pixel_row < 4: # gledamo želi li igrač pomaknuti pixel gore, vrijednost 600 odabrana je kratkom isprobavanjem i ne mora biti optimalna
        pixel_row += 1 # pixel se pomiče gore
    elif y <= 600 and pixel_row > 0: # ako igrač drži micro:bit normalno, pixel pada jedno mjesto dolje
        pixel_row -= 1 # pixel se pomiče dolje
    if gate_move: # provjera treba li pomaknuti vrata prema pixelu
        gate_column -= 1 # vrata se pomiču prema pixelu
    gate_move = not gate_move # ako se vrata nisu pomaknula, postavljamo vrijednost da se idući put pomaknu i obratno
    display.clear() # gasimo sve ledice na micro:bit
    display.set_pixel(0, pixel_row, 8) # palimo ledicu pixela
    for i in range(5): # petlja u kojoj ispisujemo stupac s vratima
        if i < gate_row or i > gate_row + gate_size - 1: # gledamo da li se u aktualnom retku nalazi zid vrata, samo zidove treba ispisati
            display.set_pixel(gate_column, i, 5) # ako da, palimo ledicu toga retka
    if gate_column == 0: # provjeravamo jesu li vrata došla do pixela
        if pixel_row < gate_row or pixel_row > gate_row + gate_size - 1: # provjeravamo je li pixel udario u zid vrata
            break # ako je, izlazimo iz glavne petlje
        score += 1 # inače jedan bod ide igraču
        if score in (1, 10): # nakon što igrač ostvari 1 bod i zatim kasnije 10 bodova, igra postaje teža tako što smanjujemo veličinu vrata za jedan
            gate_size -= 1 # ovdje radimo to smanjivanje
        gate_column = 4 # budući da je pixel prošao kroz vrata, nova stvaramo i stavljamo u zadnji stupac
        gate_row = random.randint(0, 4 - gate_size + 1) # pomoću generatora slučajnih brojeva određujemo gdje će vrata započeti
    sleep(400) # spavamo 400 milisekundi između dvije iteracije
sleep(800) # nakon što je igrač izgubio spavamo 800 milisekundi
display.scroll("You scored " + str(score) + " points!") # i zatim mu prikažemo rezultat koji je ostvario
