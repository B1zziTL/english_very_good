#otvorenie suboru
subor = open("ucenie_sa_slovicok.txt","r",encoding='utf-8')

#zadeklarovanie premennych a zoznamov
pocet = 0
body = 0
dokopy = 0
nespravne = 0
anglicke = []
slovenske = []
neuhadnute_ang = []
neuhadnute_sk = []

#vyber jazyka
jazyk = str(input("anglicky/slovensky: "))

def cambridge_dictionary(): #funkcia na zapisanie slov zo suboru
    #zadeklarovanie globalnych premennych
    global pocet, daco, dokopy
    
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #vymazanie neviditelnych znakov
        riadocek = riadok.strip()

        #zmena pomocnej premennej
        pocet += 1

        #podmienky na spravne zapisanie do zoznamu
        if (pocet % 2) == 0:
            anglicke.append(riadocek)
        elif (pocet % 2) != 0:
            slovenske.append(riadocek)

    #zmeny pomocnych premennych
    pocet = int(pocet / 2)
    dokopy = pocet

def skusanie(): #funkcia na skusanie
    #zadeklarovanie globalnych premennych
    global pocet, body, jazyk, dokopy, nespravne

    #podmienky na skusanie podla jazyka
    if jazyk == "anglicky": 
        for i in range(pocet): #cyklus na prechadzanie slov
            #vypytanie odpovede
            test = str(input(anglicke[i]+": "))

            #podmienky na spravne bodovanie
            if test == slovenske[i]:
                body += 1
            else:
                neuhadnute_ang.append(anglicke[i])
                neuhadnute_sk.append(slovenske[i])

    elif jazyk == "slovensky":
        for i in range(pocet): #cyklus na prechadzanie slov
            #vypytanie odpovede
            test = str(input(slovenske[i]+": "))

            #podmienky na spravne bodovanie
            if test == anglicke[i]:
                body += 1
            else:
                neuhadnute_sk.append(slovenske[i])
                neuhadnute_ang.append(anglicke[i])

    #podmienka na ne/pokracovanie            
    if body != dokopy:
        #spustenie opakovania
        return rewind_time()

    else:
        #vypisanie pozadovanej hodnoty
        print("Chyby:",nespravne)

def rewind_time(): #funkcia na opakovanie
    #zadeklarovanie globalnych premennych
    global pocet, body, dokopy, nespravne

    #vyprazdnenie zoznamov
    anglicke.clear()
    slovenske.clear()

    #cyklusy na zapisanie nespravnych odpovedi
    for i in neuhadnute_ang:  
        nespravne += 1
        anglicke.append(i)
    for i in neuhadnute_sk:
        slovenske.append(i)

    #vyprazdnenie zoznamov
    neuhadnute_ang.clear()
    neuhadnute_sk.clear()

    #zmena pomocnej premennej
    pocet = dokopy - body

    #navrat na funkciu skusania
    return skusanie()

#vykonanie funkcii
cambridge_dictionary()
skusanie()

#zatvorenie suboru
subor.close()
