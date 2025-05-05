import os

# esercizio gestione dizionario con etá
# dobbiamo creare un dizionario con la coppia chiave - valore che indica il nome della persona e la sua etá

# es eta = {"Thomas" : 26, "Nicolò" : 27}

# chiedere all'utente se:
# 1) vuole aggiungere un nome al dizionario
# 2) visualizzare la persona piú anziana
# 3) visualizzare la persona piú giovane
# 4) cancellare una persona
# 5) vedere la media delle etá
# 6) visualizzare tutto il dizionario
# 7) uscire

def scelta_utente():
    print("Scegli un'opzione:")
    print("1) vuole aggiungere un nome al dizionario")
    print("2) visualizzare la persona piú anziana")
    print("3) visualizzare la persona piú giovane")
    print("4) cancellare una persona")
    print("5) vedere la media delle etá")
    print("6) visualizzare tutto il dizionario")
    print("7) uscire")
    scelta = input("> ")
    return scelta

def aggiungi_nome(dizionario_eta):
    nome = input("Inserisci il nome da aggiungere: ")
    if nome in dizionario_eta.keys():
        print("Errore: Nome giá presente")
        return
    try:
        eta = int(input("Inserisci l'etá da aggiungere: "))
        if eta < 0:
            raise ValueError
    except ValueError:
        print("Errore: L'eta deve essere un numero intero e maggiore o uguale a zero")
        return
    dizionario_eta[nome] = eta

def persona_eta_massima(dizionario_eta):
    eta_massima = -1
    nome_con_eta_massima = None
    for nome, eta in dizionario_eta.items():
        if eta > eta_massima:
            eta_massima = eta
            nome_con_eta_massima = nome
    return nome_con_eta_massima

def persona_eta_minima(dizionario_eta :dict):
    dizionario_eta_locale = dizionario_eta.copy()
    primo_elemento = dizionario_eta_locale.popitem()
    eta_minima = primo_elemento[1]
    nome_con_eta_minima = primo_elemento[0]
    for nome, eta in dizionario_eta_locale.items():
        if eta < eta_minima:
            eta_minima = eta
            nome_con_eta_minima = nome
    return nome_con_eta_minima

def cancella_persona(dizionario_eta :dict, nome):
    # if nome in dizionario_eta.keys():
    #     del dizionario_eta[nome]
    #     print("Persona cancellata correttamente")
    # else:
    #     print("Errore: Persona non trovata")
    try:
        del dizionario_eta[nome]
        print("Persona cancellata correttamente")
    except KeyError:
        print("Errore: Persona non trovata")

def stampa_dizionario(dizionario :dict):
    for chiave, valore in dizionario.items():
        print(f"{chiave}: {valore}")

def media(dizionario :dict):
    somma = sum(dizionario.values())
    return somma/len(dizionario)

dizionario_eta = {}

print("Benvenuto")
while True:
    scelta = scelta_utente()
    os.system("cls")
    match scelta:
        case "1":
            aggiungi_nome(dizionario_eta)
        case "2":
            if len(dizionario_eta) == 0:
                print("Non hai inserito nessuno :c")
                continue
            print(f"La persona piú grande é {persona_eta_massima(dizionario_eta)}")
        case "3":
            if len(dizionario_eta) == 0:
                print("Non hai inserito nessuno :c")
                continue
            print(f"La persona piú piccola é {persona_eta_minima(dizionario_eta)}")
        case "4":
            nome_da_cancellare = input("Inserisci il nome di chi vuoi eliminare: ")
            cancella_persona(dizionario_eta, nome_da_cancellare)
        case "5":
            print(f"La media delle etá é {media(dizionario_eta)}")
        case "6":
            stampa_dizionario(dizionario_eta)
        case "7":
            break;
        case _:
            print("Errore: Scelta non valida")

print("Fine programma")
