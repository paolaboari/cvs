def addizione (primo_numero, secondo_numero):
    return primo_numero + secondo_numero # uguale a scrivere print(primo_numero + secondo_numero)

def sottrazione (primo_numero, secondo_numero):
    primo_numero = int(input("Inserisci il primo numero: "))
    secondo_numero = int(input("Inserisci il secondo numero: "))

    return f"La sottrazione tra {primo_numero} e {secondo_numero} è uguale a {primo_numero - secondo_numero}" #questo è un modo diverso di risolverla rispetto all'addizione

def moltiplicazione (primo_numero, secondo_numero):
    return primo_numero * secondo_numero

def divisione (primo_numero, secondo_numero):
    if secondo_numero == 0:
        return "Divisione per 0 non è eseguibile"
    else:
        return primo_numero / secondo_numero

risposta =""

while risposta != "q": # q di quit 
    print("a) Addizione: ")
    print("s) Sottrazione: ")
    print("m) Moltiplicazione: ")
    print("d) Divisione: ")
    print("q) Uscire: ")

    risposta = input("")
    #alternativa mettere i due umeri qua e andarli solo a chiamare 
    primo_numero = int(input("Inserisci il primo numero: "))
    secondo_numero = int(input("Inserisci il secondo numero: "))

    if risposta == "a":
        primo_numero = int(input("Inserisci il primo numero: "))
        secondo_numero = int(input("Inserisci il secondo numero: "))

        print(f"La somma di {primo_numero} e {secondo_numero} è uguale a {addizione(primo_numero, secondo_numero)}")

    elif risposta == "s":
        print(sottrazione()) #modalità diversa di risolverla rispetto all'addizione 
                                  #posso anche dichiarare i numeri una sola volta all'inizio, fuori da tutto 
    elif risposta == "m":
        print(f"La moltiplicazione di {primo_numero} e {secondo_numero} è uguale a {moltiplicazione(primo_numero, secondo_numero)}")

    elif risposta == "d":
        print(f"La divisione di {primo_numero} e {secondo_numero} è uguale a {divisione(primo_numero, secondo_numero)}")

    else:
        ("Ciao!")