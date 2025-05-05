from dataclasses import dataclass
from hashlib import md5

@dataclass
class Persona:
    nome:str
    email:str
    password:str

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,stringa):
        password_sale=stringa+"sale"
        password_hashata=Persona.hash_md5(password_sale)
        self._password=password_hashata
        return self._password
    
    @classmethod
    def hash_md5(cls,stringa: str):
        result = md5(stringa.encode('utf-8'))
        return result.hexdigest()

@dataclass
class Autenticazione:
    lista_autenticazioni:list[Persona]

    def controllaEmail(self,email_inserita):
        for persona in self.lista_autenticazioni:
            if email_inserita==persona.email:
                return True

    def accesso(self,email_accesso,password_accesso):
        for accesso in self.lista_autenticazioni:
            if email_accesso==accesso.email and password_accesso==accesso.password:
                return True
            return False
    
    def visualizzaPass(self,nome):
        for accesso in self.lista_autenticazioni:
            if nome==accesso.nome:
                print(accesso.password)
            
lista_autenticazioni=[Persona(nome="Gianni",email="abc@gmail.com",password="abc"),
                      Persona(nome="Pippo",email="pino@gmail.com", password="xyz123"),
                      Persona(nome="Luna",email="test@mail.com", password="test123"),
                      Persona(nome="Sara",email="random.person@outlook.com", password="securePass1"),
                      Persona(nome="Pluto",email="example.name@yahoo.com", password="example2024")
]

registrazioni=Autenticazione(lista_autenticazioni)

def sceltaUtente():
    print("Fai una scelta:")
    print("1) registrati")
    print("2) accedi")
    print("3) visualizza password")
    print("4) esci")
    scelta=input("")
    return scelta

while True:
    scelta=sceltaUtente()
    match scelta:
        case "1":
            print("Registrazione")
            nome=input("Inserisci il tuo nome: ").strip().title()
            email=input("Inserisci l'email per registrarti: ")
            if registrazioni.controllaEmail(email):
                print("Errore, l'email è già registrata")
                continue
            password=input("Inserisci la tua password per registrarti: ")
            persona1=Persona(nome=nome,email=email,password=password)
            registrazioni.lista_autenticazioni.append(persona1)
        case "2":
            print("Accedi")
            email_accesso=input("Inserisci l'email: ")
            password_accesso=input("Inserisci la password: ")
            password_accesso_sale=password_accesso+"sale"
            password_accesso_hashata=Persona.hash_md5(password_accesso_sale)
            if registrazioni.accesso(email_accesso,password_accesso_hashata):
                print("Accesso eseguito!")
            else:
                print("Credenziali non valide")
        case "3":
            nome=input("Inserisci il tuo nome: ").strip().title()
            print("Ecco la password hashata: ",end="")
            registrazioni.visualizzaPass(nome)
        case "4":
            break
        case _:
            print("Errore: scelta non disponibile")