#Ohjelma antaa suorakulmaisen kolmion pinta-alan, kun kanta ja korkeus annetaan.
kanta = (float)(input("Anna kolmion kanta"))
korkeus = (float)(input("Anna kolmion korkeus"))

ala = (kanta * korkeus) / 2

print("kolmion ala on " + str(ala))