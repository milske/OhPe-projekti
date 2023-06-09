# Quiz aloitus

nimi = input("Anna nimesi: ")

# pääohjelmaa edustava funktio


def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0
    # while silmukka aihealueen ja oikean tiedoston valitsemiseksi
    while True:
        aihe = int(input("Valitse aihealue: 1=maantiede, 2=historia: "))
        if aihe == 1:
            tiedostonimi = "maantieto.csv"
            break
        elif aihe == 2:
            tiedostonimi = "historia.csv"
            break
        else:
            print("Valinta ei mahdollinen")

    # kysymysten noutaminen tiedostosta
    with open(tiedostonimi) as tiedosto:

        # for-silmukalla käydään läpi aihepiirin kysymykset ja vastausvaihtoehdot
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(";")
            kysymys = osat[0]
            vaihtoehdot = osat[1:5]
            print("----------------")
            print(kysymys)
            print("\n".join(vaihtoehdot))

            arvaus = input("Anna oikea vaihtoehto: ").upper()
            arvaukset.append(arvaus)

            # if-else ehtolause vastauksen oikein/väärin päättelemiseksi
            # oikea vastaus listan 5. indeksissä
            if arvaus == osat[5]:
                tulos += 1
                print("Oikein!")
            else:
                print("Väärin...")
            kysymys_numero += 1

    # funktio tuloksen laskemiseksi
    def nayta_tulos(tulos):
        print("----------------")
        print(f"{nimi}, tuloksesi on {tulos} / 5 pistettä.")
        print(f"Sait kysymyksistä {(tulos/5)*100}% oikein")
        if tulos <= 2:
            print("Vielä on parannettavaa!")
        if tulos == 3 or tulos == 4:
            print("Hyvin meni!")
        if tulos == 5:
            print("Täydellistä!")
        print("----------------")
    nayta_tulos(tulos)


# funktio joka mahdollistaa aloittaa uusi peli tai lopettaa pelaaminen
def pelaa_uudelleen():
    valinta = input("Haluatko pelata uudelleen? (kyllä/ei): ")
    valinta = valinta.upper()

    if valinta == "KYLLÄ":
        return True
    else:
        return False


# uusi_peli funktion kutsuminen
uusi_peli()

while pelaa_uudelleen():
    uusi_peli()

print("Kiitos, moi!")

# Pelin kehittäminen
# -Laajenna kysymyspankkia ja kysymysten valintaa random.shuffle metodilla
# -Laajenna sovellusta antamaan vihjeitä ja tarjoamaan selvennystä
# -paranna käyttäjän syötteissä tapahtuvien virheiden käisttelyä ja tulostusten visuaalisuutta
