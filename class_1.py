class Pessoa: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def _valida(self):
        if self.name and self.email:
            return True
        else: 
            return False
        
    def save(self):
        if self._valida():
            print("User Saved")
        else: 
            print(f"{self.name}{self.email} Error user record is not complete")

Pessoa_1 = Pessoa("João", "jp@gmail.com")
Pessoa_2 = Pessoa("Claudia", "")
Pessoa_3 = Pessoa("", "kjdhfkhf")
Pessoa_4 = Pessoa("", "")

Pessoa_1.save()
Pessoa_2.save()
Pessoa_3.save()
Pessoa_4.save()
