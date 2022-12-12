#Spill

print("Du våkner i en fremmed seng etter en vill kveld, du vet ikke hvor du er eller hvordan du kom deg dit.\n På veggen på andre siden av rommet er det et vindu, og til høyre for deg er det en dør.")
print("         TUTORIAL\nFor å aktivere et objekt, skriv 'undersøk' eller 'u' og 'objektnavn'\n for å lete etter ledetråder i et rom, skriv 'u ledetråd'")
#player = print(input("Skriv inn hva du vil gjøre her: "))
#if playerself. == "u dør" or "undersøk dør":
#    print("du går gjennom døra, og kommer til en terasse i andre etasje.")
#    player = print(input("Skriv inn hva du vil gjøre her: "))
#if player == "u vindu" or "undersøk vindu":
#    print("Du går bort til vinduet og ser ut på en vakker utsikt over en fjelldal, og ser at det er et hus på andre siden av dalen med røyk ut av pipa \n")
#if player !="u dør" or "undersøk dør":
#    player = print(input("Nå er du fortsatt i rommet. Prøv å gå ut døra."))

PrintetLedetråder = []
class Rom:
    CurRom = None
    def __init__(self, svar, spørsmål):
        self.spørsmål = spørsmål
        self.svar = svar
        self.ledetråder = []

    def __str__(self):
        return f"Spørsmålet i rommet er: {self.spørsmål}. Hva er svaret? For hjelp, se deg rundt i rommet for ledetråder."


    def LeggTilLedetråd(self, ledetråd):
        self.ledetråder.append(ledetråd)
        
    def SkrivUtLedetråd(self):
        #for i in self.ledetråder:
        #    print(f"\nLedetråd:\nDu ser deg rundt i rommet. {self.ledetråder[i]}")
        
        
        print(f"\nLedetråd:\nDu ser deg rundt i rommet. {self.ledetråder[0]}")
        PrintetLedetråder.append(self.ledetråder[0])
        if PrintetLedetråder[0] == self.ledetråder[0]:
            self.ledetråder.pop(0)
        
        
        

    def SpillRom(self):
        print(self)
        player = input("Hva er svaret på spørsmålet?  ")
        if player == self.svar:
            input("Bra jobba, gå videre til neste rom ved å skrive 'neste rom': ")
            CurRom = self
        else:
            self.SkrivUtLedetråd()

SpillOver = False
Rom1 = Rom("London" or "london", "Hva er hjembyen til huseieren?")
Rom1.LeggTilLedetråd("På veggen ser du et bilde av Kong Charles")
Rom1.LeggTilLedetråd("På et bord ser du en Rød Telefonkiosk")
Rom1.LeggTilLedetråd("I vinduskarmen ser du en statue av Big Ben")


Rom.CurRom = Rom1
while not SpillOver:
    print()
    Rom.CurRom.SpillRom()
    #str()


    


player = input("Hva tror du svaret på spørsmålet er?   ")