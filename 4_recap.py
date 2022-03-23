anzahl_äpfel = 10
while anzahl_äpfel > 0:
    print("Hallo Kunde, wir haben momentan " + str(anzahl_äpfel) +
          "Äpfel im Angebot. Wie viele möchtest du kaufen?")
kaufwunsch = int(input())
if kaufwunsch > anzahl_äpfel:
    print("So viele Äpfel haben wir gar nicht mehr :( ")
else:
    anzahl_äpfel = anzahl_äpfel - kaufwunsch
    print("Du hast " + str(kaufwunsch) + " Äpfel gekauft.")
    print("Alle Äpfel wurden verkauft :)")
