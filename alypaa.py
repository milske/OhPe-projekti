# Stepit:
# 1. Create a basic application that can ask multiple-choice questions.
# 2. Separate question data from source code by storing questions in a dedicated data file.
# 3. Refactor the code to use functions.
# 4. Add interest by supporting different quiz topics to choose from.
# 5. Expand the app to give hints, and provide explanations.
# 6. Make the app more user-friendly by improving how it looks and how it handles user errors.

# Quiz

nimi = input("Anna nimesi: ")

    
def uusi_peli():
    arvaukset = []
    tulos = 0
    kysymys_numero = 0

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

    with open(tiedostonimi) as tiedosto:

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
        print(f"Sait kysymyksistä {(tulos/5)*100}% oikein")
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

