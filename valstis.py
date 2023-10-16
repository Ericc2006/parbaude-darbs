# Sākotnējā vārdnīca
vardnica = {
    "Latvija": "1,907,675",
    "Krievija": "141,903,979 ",
    "Ukraina": "48,574,385",
    "Vācija": "83,200,000",
    "Itālija": "59,110,000",
    "Igaunija": "1,322,765",
    "Baltkrievija": "9,498,238",
    "Somija": "5,545,475",
    "Norvēģija": "5,474,360",
    "Austrālija": "26,439,111."
}

vardnica2 = {    
    "Latvija",
    "Krievija",
    "Ukraina",
    "Vācija",
    "Itālija",
    "Igaunija",
    "Baltkrievija",
    "Somija",
    "Norvēģija",
    "Austrālija"
    }

def izvadīt_vardnicu(vardnica2):
    print(vardnica2)


def izvadit_valstu_sarakstu(vardnica):
    print("Vārdnīca:")
    for valsts, Cilvēku_skaits in vardnica.items():
        print(f"{valsts} -> {Cilvēku_skaits}")



def pievienot_vardu(vardnica):
    valsts = input("Ievadiet valsts nosaukumu: ")
    Cilvēku_skaits = input("Ievadiet cilvēku skaitu valstī: ")
    vardnica[valsts] = Cilvēku_skaits
    print("Vārds pievienots vārdnīcai.")




def vismazakais_iedzivotāju_skaits(vardnica):
    print("Igaunija") 

def vislielākais_iedzivotaju_skaits(vardnica):
    print("Krievija")

while True:
        print("Izvēlieties darbību:")
        print("1. izvadit valstu sarakstu")
        print("2. izvadīt vardnicu" )
        print("3. Pievienot vārdu vārdnīcai")
        print("4. vismazakais_iedzivotāju_skaits")
        print("6. vislielākais_iedzivotaju_skaits")
        print("5. Iziet")
    
        izvele = input("Ievadiet darbības numuru: ")
    
    
        if izvele == "1":
           izvadit_valstu_sarakstu(vardnica)
        elif izvele == "2":
            izvadīt_vardnicu(vardnica2)
        elif izvele == "3":
           pievienot_vardu(vardnica)
        elif izvele == "4":
           vismazakais_iedzivotāju_skaits(vardnica)
        elif izvele == "6":
           vislielākais_iedzivotaju_skaits(vardnica)
        elif izvele == "5":
           break
        else:
            print("Nepareizs cipars!!! Lūdzu, izvēlieties no pieejamajām opcijām.")