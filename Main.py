from Combat import Combat
from Pokemon import Pokemon

picka = Pokemon("Pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)

nom_pokemon = input("choose your pokemon")
Combat.lanceAttack(picka,salam)