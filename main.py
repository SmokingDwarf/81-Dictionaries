# > Schrijf een functie die returnt of een key in een dictionary zit of niet (True of False)

taart_dict = {'appeltaart': 'goed', 'slagroomtaart': 'slecht'}
"""def is_key_in_dict(naam, my_dict):
  print(f"Ik ga zoeken naar {naam}")
  # Vul hier code in
  return naam in my_dict
  
 For key in my_dict.keys():
    if key == naam:
      return True
    print(key)
  return False

print(is_key_in_dict('slagroomtaart', taart_dict))
print(is_key_in_dict('appeltaart', taart_dict))
print(is_key_in_dict('frambozenvlaai', taart_dict))"""

# # > Schrijf een functie die returnt of een bepaalde value in een dictionary zit of niet
"""def is_value_in_dict(waarde, my_dict):
  for key in my_dict.values():
    if key == waarde:
      return True
  return False
print(is_value_in_dict('goed', taart_dict))
print(is_value_in_dict(42, taart_dict)) """

# # > Schrijf een functie die een naam meekrijgt en een geformatteerde string terug geeft van de naam van de persoon en het bijbehorende cijfer. Als de persoon niet in de lijst staat, geef dan een string terug die dit duidelijk maakt.

cijfers = {'Robert': 10, 'Nick': 10, 'Jan': 'Onvoldoende', 'Vera': 10}
"""def geef_naam_en_cijfer(naam, my_dict):
  for key in my_dict.keys():
    if key == naam:
      return my_dict[naam]
  return (f"De student {naam} staat niet in deze lijst.")
print(geef_naam_en_cijfer('Vera',cijfers))
print(geef_naam_en_cijfer('Florian',cijfers))"""

# # > Schrijf een functie die de gemiddelde leeftijd van alle auto's in de dictionary berekent.

car_database = {
    'DeLorean DMC-12': 1981,
    'Ford Mustang': 1964,
    'Ford F150': 1948,
    'Ford Ka': 1996,
    'Bugatti type 55': 1931,
    'Tesla Roadster': 2008,
    'Tesla Model 3': 2016,
    'Ford focus': 1998
}


"""def bereken_gemiddelde_leeftijd_van_alle_autos(my_dict):
  totaal_leeftijd = 0
  for value in my_dict.values():
    leeftijd = 2026 - value
    print(f"De leeftijd van de auto is {leeftijd}")
    totaal_leeftijd = totaal_leeftijd + leeftijd
    print(f"De nieuwe totale leeftijd is {totaal_leeftijd}")
  return totaal_leeftijd / len(my_dict.values())

print(bereken_gemiddelde_leeftijd_van_alle_autos(car_database))"""

# # In voorgaande opdrachten hebben we een aantal keer alle klinkers in een stuk tekst geteld. Dit gaan we nu nog een keer doen, maar dan met een dictionary.
# # > Herschrijf je functie van vorige les, waarbij je een stuk tekst en een aantal letters door kon geven om deze te tellen, zodat deze nu een dictionary teruggeeft die de letters als key heeft en als value hoe vaak deze letter voor is gekomen.
ti_ta_tekst = "Mijn vader is een tovenaar"
mac_beth = "On a bleak Scottish moorland, Macbeth and Banquo, two of King Duncan's generals, discover three strange women (witches). The witches prophesy that Macbeth will be promoted twice: to Thane of Cawdor (a rank of the aristocracy bestowed by grateful kings) and King of Scotland. Banquo's descendants will be kings, but Banquo isn't promised any kingdom himself. The generals want to hear more, but the weird sisters disappear. Soon afterwards, King Duncan names Macbeth Thane of Cawdor as a reward for his success in the recent battles. The promotion seems to support the prophecy. The King then proposes to make a brief visit that night to Macbeth's castle at Inverness. Lady Macbeth receives news from her husband about the prophecy and his new title. She vows to help him become king by whatever means are necessary (*ominous music*)."
klinker_lijst = ["a", "e", "i", "u", "o"]
kleine_lijst = ["a", "b", "c"]

def klinker_tellen(tekst, array):
  letter_dict = {}
  for index in array:
    letter_dict[index] = 0
    for letter in tekst:
      if letter == index:
        letter_dict[index] = letter_dict[index] + 1
  return letter_dict
print(klinker_tellen(mac_beth, klinker_lijst))

