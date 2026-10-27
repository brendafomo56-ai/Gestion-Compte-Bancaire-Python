class compte_bancaire:
    def __init__(self,titulaire, solde):
        self.titulaire = titulaire
        self.__solde = solde
    def get_solde(self):
        return self.__solde
    def  deposer(self, montant):
        self.__solde = self.__solde + montant
        print(self.titulaire,'votre nouveau solde est', self.get_solde())
    def afficher(self):
        print(self.titulaire, 'votre solde est de', self.get_solde())
    def retirer (self, montant):
        if montant > self.__solde:
            print(self.titulaire,'solde insuffisant')
        else:
            self.__solde= self.__solde - montant
            print(self.titulaire,'retrait effectué avec succes, votre nouveau solede est', self.get_solde())
class compte_epargne(compte_bancaire):
    def __init__(self, titulaire, solde, taux_interet):
        super().__init__(titulaire, solde)
        self.taux_interet = taux_interet
    def interet(self):
        montant_interet = self.taux_interet * self.get_solde()
        super().deposer(montant_interet)
        print(self.titulaire, 'votre interet est de: ', montant_interet, 'qui vous donne un solde total de :', self.get_solde())

compte_e = compte_epargne('brenda', 100000, 0.03)
compte_c = compte_bancaire('fomo',50000 )
while True:
    print("\n--- MENU ---")
    print("1:" "compte epargne")
    print("2:" "compte courant")
    try:
        num_c = int(input('entrez 1 ou 2 selon le compte choisir'))
    except:
        print('entrez une valeur valide 1 ou 2')
        continue
    if num_c <1 or num_c>2:
        print('vous devez entrer 1 ou 2')
        continue
    if num_c == 2:
        while True:
            print("\n--- MENU ---")
            print("1:" "solde")
            print("2:" "depot")
            print("3:" "retrait")
            print("4:" "quitter")
            try:
                num =int(input('entrez le numero de votre operation'))
            except:
                print("votre numero doit etre un entier entre 1 , 2, 3, 4, 5")
                continue
            if num < 1 or num >4:
                print('le numero doit superieur a 1 et inférieur a 5')
                continue
            if num ==2:
                try:
                    montant= int(input('entrez le montant a deposer'))
                except:
                    print('entrer un montant valide')
                    continue
                if montant < 1:
                    print('entrez un montant valide')
                    continue
                else:
                    compte_c.deposer(montant)
            elif num == 3:
                try:
                    montant= int(input('entrez le montant a retirer'))
                except:
                    print('entrer un montant valide')
                    continue
                compte_c.retirer(montant)
            elif num == 1:
                compte_c.afficher()
            else:
                print("merci d'avoir utiliser notre programme")
                break
    else:
        while True:
            print("\n--- MENU ---")
            print("1:" "solde")
            print("2:" "depot")
            print("3:" "retrait")
            print("4:" "calcule montant interet")
            print("5:" "quitter")
            try:
                num =int(input('entrez le numero de votre operation'))
            except:
                print("votre numero doit etre un entier entre 1 , 2, 3, 4, 5")
                continue
            if num < 1 or num >5:
                print('le numero doit superieur a 1 et inférieur a 6')
                continue
            if num ==2:
                try:
                    montant= int(input('entrez le montant a deposer'))
                except:
                    print('entrer un montant valide')
                    continue
                if montant < 1:
                    print('entrez un montant valide')
                    continue
                else:
                    compte_e.deposer(montant)
            elif num == 3:
                try:
                    montant= int(input('entrez le montant a retirer'))
                except:
                    print('entrer un montant valide')
                    continue
                compte_e.retirer(montant)
            elif num == 1:
                compte_e.afficher()
            elif num== 4:
                compte_e.interet()
            else:
                print("merci d'avoir utiliser notre programme")
                break

        
   
            

        

     
