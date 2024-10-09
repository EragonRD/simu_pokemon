import Combat 
from Pokemon import Pokemon
import Get_ability

picka = Pokemon("Pickachu","Electrique",154,91,115,113,113,93,50)
salam = Pokemon("Salamche","Feu",154,91,115,113,113,93,50)

nom_pokemon = input("choose your pokemon")

Combat.lanceAttack(picka,salam)
Get_ability.get_Ability(nom_pokemon)
