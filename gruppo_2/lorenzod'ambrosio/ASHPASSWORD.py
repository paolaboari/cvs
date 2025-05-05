# ES 2) Password
    # Creare un sistema di autenticazione per un sito che memorizzi le password hashate (preferibilmente usando l'MD5,
    # volendo potete aggiungere anche del sale)
    # Gli indirizzi email che usano per la login devono essere univoci
    # Avere un metodo per l'accesso che dato email e password restituisca True o False

    # LIVELLO 2
    # creare una classe persona con nome e password, quando metto la password la salvo come md5 e quando la chiedo mi da l'hash
    
    
# from hashlib import md5

# def hash_md5(stringa: str):
#     result = md5(stringa.encode('utf-8'))
#     return result.hexdigest()

# print(hash_md5("ciao"))

import hashlib
import re

class SistemaAutenticazione:
    def __init__(self):
        # Dizionario per memorizzare gli utenti
        # Chiave: email, Valore: password hashata
        self.utenti = {}
    
    def _hash_password(self, password):
        """Esegue l'hashing della password con MD5"""
        return hashlib.md5(password.encode()).hexdigest()
    
    def _valida_email(self, email):
        """Convalida il formato dell'email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def registra_utente(self, email, password):
        """
        Registra un nuovo utente
        
        :param email: indirizzo email dell'utente
        :param password: password in chiaro
        :return: True se la registrazione ha successo, False altrimenti
        """
        # Controlla la validità dell'email
        if not self._valida_email(email):
            print("Email non valida!")
            return False
        
        # Controlla che l'email non sia già registrata
        if email in self.utenti:
            print("Questa email è già registrata!")
            return False
        
        # Genera l'hash della password
        password_hash = self._hash_password(password)
        
        # Salva l'utente
        self.utenti[email] = password_hash
        
        print("Registrazione avvenuta con successo!")
        return True
    
    def autentica(self, email, password):
        """
        Autentica un utente
        
        :param email: indirizzo email dell'utente
        :param password: password in chiaro
        :return: True se l'autenticazione ha successo, False altrimenti
        """
        # Controlla se l'utente esiste
        if email not in self.utenti:
            print("Utente non trovato!")
            return False
        
        # Calcola l'hash della password inserita
        password_hash = self._hash_password(password)
        
        # Confronta gli hash
        if password_hash == self.utenti[email]:
            print("Autenticazione riuscita!")
            return True
        else:
            print("Password errata!")
            return False


    # Crea un'istanza del sistema di autenticazione
sistema = SistemaAutenticazione()

while True:
    print("\n--- Sistema di Autenticazione ---")
    print("1. Registrati")
    print("2. Accedi")
    print("3. Visualizza lista")
    print("4 Inserisci email di cui vedere ash")
    print("5. Esci")
    
    scelta = input("Inserisci la tua scelta (1-3): ")
    
    if scelta == '1':
        # Registrazione
        email = input("Inserisci la tua email: ")
        password = input("Inserisci la tua password: ")
        sistema.registra_utente(email, password)
    
    elif scelta == '2':
        # Autenticazione
        email = input("Inserisci la tua email: ")
        password = input("Inserisci la tua password: ")
        sistema.autentica(email, password)
    
    elif scelta =='3':
        print(sistema.utenti)
    
    elif scelta=='4':
        email = input("Inserisci la email di cui vedere ash della password: ") 
        if email in sistema.utenti:  
            print(sistema.utenti[email])
        else:
            print("email non trovata")    
        
    elif scelta == '5':
        print("Arrivederci!")
        break    
    else:
        print("Scelta non valida. Riprova.")