print("Welkom bij de tip calculator")
rekening = float(input("Wat is het totale bedrag van de rekening? €"))
split = int(input("Tussen hoeveel mensen wil je het bedrag delen? "))
tippercentage = int(input("Hoeveel wil je tippen? 10%, 12% of 15% "))
pp = round((rekening * ((100 + tippercentage) / 100)) / split, 2)
print(f"Totaal per persoon wordt het dan €{pp}")
