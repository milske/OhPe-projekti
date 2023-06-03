nimi = input("Anna nimesi: ")

    
def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0

    with open("historia.csv") as tiedosto:

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

            if arvaus == osat[5]:
                tulos += 1
                print("Oikein!")
            else:
                print("Väärin...")
                # print(f"Oikea vastaus on {vastaukset[kysymys_numero]}")
            kysymys_numero += 1

    
    def nayta_tulos(tulos):
        print("----------------")
        print(f"{nimi}, tuloksesi on {tulos} / 5 pistettä." )
        if tulos <= 2: 
             print("Vielä on parannettavaa!")
        if tulos == 3 or tulos == 4:
             print("Hyvin meni!")
        if tulos == 5:
             print("Täydellistä!")
        print("----------------")
    nayta_tulos(tulos)


def pelaa_uudelleen():
        valinta = input("Haluatko pelata uudelleen? (kyllä/ei): ")
        valinta = valinta.upper()

        if valinta == "KYLLÄ":
            return True
        else:
            return False


uusi_peli()

while pelaa_uudelleen():
            uusi_peli()

print("Kiitos, moi!")

