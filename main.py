import pickle

filename = 'betalinger.pk'

# Prøv at indlæse tidligere data fra pickle-fil, eller opret en tom dictionary
try:
    with open(filename, 'rb') as f:
        betalinger = pickle.load(f)
    print("Data indlæst fra fil.")
except (FileNotFoundError, EOFError):
    betalinger = {}
    print("Ingen tidligere data fundet. Opret ny opsparingsordning.")

def registrer_betalinger():
    while True:
        medlem_navn = input("Indtast medlemmets navn (eller 'q' for at afslutte): ")
        if medlem_navn == 'q':
            break
        belob = float(input("Indtast beløb: "))
        if medlem_navn in betalinger:
            betalinger[medlem_navn] += belob
        else:
            betalinger[medlem_navn] = belob
        print(f"{medlem_navn} har nu indbetalt i alt {betalinger[medlem_navn]:.2f} kr.")

def udskriv_status():
    print("----- Status over indbetalinger -----")
    for medlem, indbetalt in betalinger.items():
        mangler = max(0, 4500 - indbetalt)
        print(f"{medlem}: {indbetalt:.2f} kr. (Mangler: {mangler:.2f} kr)")
    print("------------------------------------")

def gem_data():
    with open(filename, 'wb') as f:
        pickle.dump(betalinger, f)
    print("Data gemt på fil.")

def udskriv_top_tre_manglende():
    top_tre_manglende = sorted(betalinger, key=lambda x: 4500 - betalinger[x], reverse=True)[:3]
    print("----- Top tre medlemmer med mest manglende betalinger -----")
    for medlem in top_tre_manglende:
        mangler = max(0, 4500 - betalinger[medlem])
        print(f"{medlem}: Mangler {mangler:.2f} kr")
    print("-----------------------------------------------------------")

while True:
    print("\nVælg en handling:")
    print("1. Registrer betalinger")
    print("2. Udskriv status")
    print("3. Gem data")
    print("4. Udskriv top tre medlemmer med mest manglende betalinger")
    print("5. Afslut program")
    valg = input("Indtast dit valg: ")

    if valg == '1':
        registrer_betalinger()
    elif valg == '2':
        udskriv_status()
    elif valg == '3':
        gem_data()
    elif valg == '4':
        udskriv_top_tre_manglende()
    elif valg == '5':
        break
    else:
        print("Ugyldigt valg. Prøv igen.")

print("Programmet afsluttet.")
