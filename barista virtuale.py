#Dichiarazione variabili
nome_barman = "FrancyBot"
drink_speciale = "DigitalVodka"
prezzo_drink = 5.5
alcolici = ["Mohito","Black russian","Sambucone Molinari","Vodka Redbull"]
analcolici = ["Gazosa","Limonata","CocaCola","Fanta"]

#Inizio del programma
print("Benvenuto al Pub di Francesco")
print("Mi chiamo "+nome_barman+"....e sono pronto a servirti")
print("Il drink più cool del nostro pub è:"+str(drink_speciale))
print("provalo subito al modico prezzo di :"+str(prezzo_drink))
print("\nI drink alcolici sono " +str(len(alcolici)))
print("\nI drink analcolici sono " +str(len(analcolici)))

print("\nInserisci il tuo anno di nascita")
anno_nascita = int(input())
anni_cliente = 2024 - anno_nascita
print("Hai "+str(anni_cliente)+" anni")
drink_disponibili = []
if anni_cliente < 18:
    print("\nSei minorenne puoi ordinare solo analcolici")
    drink_disponibili += analcolici
elif anni_cliente > 80:
    print("Puoi bere ma vacci piano nonno!")
    drink_disponibili += alcolici+analcolici
else:
    print("\nSei maggiorenne puoi bere quello che vuoi")
    drink_disponibili += alcolici+analcolici
while True:
    print("\nEcco i drink consigliati per te:")
    for drink_disponibile in drink_disponibili:
        print(drink_disponibile)
    drink_scelto = input()
    if drink_scelto in drink_disponibili:
        print("hai scelto " +drink_scelto+ " buon aperitivo")
        drink_disponibili.remove(drink_scelto)
    elif int(len(drink_disponibili)) == int(0):
         print("il bar è chiuso")
         break
    else:
        print("il drink "+ drink_scelto+ " non è disponibile")
        
  


    
