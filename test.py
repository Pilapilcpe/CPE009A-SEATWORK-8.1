from swordsman import swordsman
from archer import archer
from magician import magician

character1= swordsman("Royce")
character2= magician("Archie")
print(f"{character1.getUsername()} HP: {character1.getHP()}")
print(f"{character2.getUsername()} HP: {character2.getHP()}")
character1.slashAttack(character2)
character1.basicAttack(character2)
print(f"{character1.getUsername()} HP: {character1.getHP()}")
print(f"{character2.getUsername()} HP: {character2.getHP()}")
character2.heal()
character2.magicAttack(character1)
print(f"{character1.getUsername()} HP: {character1.getHP()}")
print(f"{character2.getUsername()} HP: {character2.getHP()}")