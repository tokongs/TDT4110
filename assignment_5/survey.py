from sys import exit

antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

exit_condition = False
def skriv_statestikk():
    print("Antall menn:", antall_menn)
    print("Antall kvinner:", antall_kvinner)
    print("Antall fag:", antall_fag)
    print("Antall ITGK:", antall_ITGK)
    if(antall_kvinner != 0 or antall_menn != 0):
        print("Antall timer lekser i snitt:", antall_timer_lekser / (antall_kvinner + antall_menn))
    else:
        print("Antall timer lekser: i snitt", antall_timer_lekser)

def sjekk_svar(spm):
    svar = input(spm)
    if(svar == "hade"):
        skriv_statestikk()
        exit()
    else:
        return svar

def les_streng(spm):
    svar = sjekk_svar(spm)
    return svar

def les_tall(spm):
    svar = sjekk_svar(spm)
    return int(svar)

def les_ja_nei(spm):
    svar = sjekk_svar(spm)
    if(svar =="ja"):
        return True
    elif(svar == "nei"):
        return False
    else:
        return les_ja_nei(spm)

while(True):
    kjonn = les_streng("Er du mann eller kvinne (m/f)? ")
    alder = les_tall("Hvor gammel er du? ")
    if(alder < 16 or alder > 25):
        print("Du kan desverre ikke ta denne spørreundersøkelsen")
    else:
        if(kjonn == "m"):
            antall_menn += 1
        else:
            antall_kvinner += 1

        fag = les_ja_nei("Tar du et eller flere fag (ja/nei?) ")
        if(fag == True):
            antall_fag += 1
            if(alder < 22):
                medlem_ITGK = les_ja_nei ("Tar du ITGK (ja/nei)? ")
            else:
                medlem_ITGK = les_ja_nei("Tar virkelig du ITGK(ja/nei? ")

            if(medlem_ITGK):
                antall_ITGK +=1
            timer_lekser = les_tall("Hvor mange timer bruker du daglig (i snitt) på lekser? ")
            antall_timer_lekser += timer_lekser
