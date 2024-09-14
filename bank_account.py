# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:26:31 2024

@author: Djibril Awa Makhtar FALL

Point de Controle Pragrammation Orientée Objet
"""

# 1) Créez un nouveau fichier appelé « bank_account.py »

# 2) Définissez la classe Account et ses attributs comme spécifié ci-dessus.

class Account :
    
    def __init__(self, account_number : str, account_balance : float, account_holder : str):
        
        self.account_number = account_number
        
        self.account_balance = account_balance
        
        self.account_holder = account_holder
        
        #3) Définissez la méthode deposit(). 
        
    def deposit(self, amount : float) :
            
            if amount > 0 : 
            
                self.account_balance += amount
            
                print(f"Le montant {amount} a été déposé. Nouveau solde : {self.account_balance:.3f} €. ")
            else :
            
                print(f"Le montant à déposer doit etre supérieur à zéro.")
                
        # 4) Définissez la méthode withdraw(). 
                        
    def withdraw(self, amount : float):
                    
            if amount > 0 :
                        
                if self.account_balance >= amount :
                            
                    self.account_balance -= amount
                            
                    print(f"{amount} a été retiré du compte. Nouveau solde : {self.account_balance:.3f} €.")
                    
                else : 
                    print(f"Le solde du compte est insuffisant pour retirer ce montant.")
                            
                #5) Définissez la méthode check_balance(). 


    def check_balance(self) :
                    
            return(f"le solde actuel du compte est de : {self.account_balance:.3f} €..")
        
""" 6) Créez une instance de la classe Account et attribuez-la à une variable
appelée « my_account »."""

my_account = Account("123456789012", 1000, "Djibril")

""" 7) Utilisez les méthodes de la classe pour déposer et retirer de l’argent
 du compte et vérifier le solde du compte."""

# Utilisation de l'instance pour déposer et retirer de l'argent.

my_account = Account("123456789", 1000, "Djibril")
 
my_account.deposit(500) # Pour déposer de l'argent : 
    
my_account.withdraw(250) # Pour retire de l'argent : 
    
print(my_account.check_balance()) # Pour vérifier le solde du compte :

""" 8) Testez le programme en créant plusieurs instances de la classe 
et en effectuant différentes transactions sur elles."""

# première instance

mon_compte1 = Account("123", 10000, "Gnagna")

## Utilisation de la première instance pour déposer et retirer de l'argent.

mon_compte1.deposit(250) # depot d'argent

mon_compte1.withdraw(5000) # retrait d'argent

print(my_account.check_balance())

## deuxième instance

mon_compte2 = Account("1234", 10500, "Coach")

## Utilisation de la deuxième instance pour déposer et retirer de l'argent.

mon_compte1.deposit(50000) # depot d'argent

mon_compte1.withdraw(100000) # retrait d'argent

print(my_account.check_balance())

## troisième instance

mon_compte3 = Account("12345", 100000, "Nathan")

### Utilisation de la trosième instance pour déposer et retirer de l'argent.

mon_compte1.deposit(500000) # depot d'argent

mon_compte1.withdraw(450000) # retrait d'argent

print(my_account.check_balance())



        

