class Bancomat:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva(self, prelievo):
        if prelievo > self.saldo:
            print("Saldo insufficiente.")
        else:
            self.saldo -= prelievo
            print(f"Prelievo effettuato! Saldo attuale: {self.saldo}€")

    def deposita(self, deposito):
        self.saldo += deposito
        print(f"Deposito effettuato! Saldo attuale: {self.saldo}€")

    def stampaSaldo(self):
        print(f"Il saldo attuale é: {self.saldo}€")

    def stampaMenu(self):
        print()
        print("1. Preleva")
        print("2. Deposita")
        print("3. Stampa Saldo")
        print("4. Esci")
        print()

    def menu(self):
        while True:
            self.stampaMenu()
            scelta = input("Scegli un'opzione (1/2/3/4): ")
            if scelta == "1":
                prelievo = float(input("Inserisci l'importo da prelevare: "))
                self.preleva(prelievo)
            elif scelta == "2":
                deposito = float(input("Inserisci l'importo da depositare: "))
                self.deposita(deposito)
            elif scelta == "3":
                self.stampaSaldo()
            elif scelta == "4":
                print("Grazie per aver utilizzato il Bancomat!")
                break
            else:
                print("Scelta non valida. Riprova.")

bancomat = Bancomat(1000)
bancomat.menu()