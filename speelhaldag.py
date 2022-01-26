Personen = 4
ToegangsTicketPrijs = 7.45
GameSeatPrijs = 0.37
GameSeatMinutenPerPrijs = 5
MinutenInGameSeat = 45
EindBedrag = round(Personen*(ToegangsTicketPrijs+(GameSeatPrijs*(MinutenInGameSeat/GameSeatMinutenPerPrijs)))*100)/100

print(EindBedrag)

print("Dit geweldige dagje-uit met " + str(Personen) + " mensen in de Speelhal met " + str(MinutenInGameSeat) + " minuten VR kost je maar " + str(EindBedrag) + " euro")