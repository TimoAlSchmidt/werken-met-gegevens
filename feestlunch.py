CroissantPrijs = 0.39
StokbroodPrijs = 2.78
KortingBon = -0.5
Totaal = 0.0
AantalCroissant = 17
AantalStokbrood = 2
AantalKortingBon = 3
EindBedrag = (AantalCroissant * CroissantPrijs) + (AantalStokbrood * StokbroodPrijs) + (AantalKortingBon * KortingBon)

print(EindBedrag)

print("De feestlunch kost je bij de bakker "+ str(EindBedrag)+" euro voor de "+ str(AantalCroissant)+" croissantjes en de "+str(AantalStokbrood) +" stokbroden als de "+ str(AantalKortingBon)+ " kortingsbonnen nog geldig zijn!")