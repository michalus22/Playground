from classes import *

p1 = Entity.Person("Michal", 20, 1, 5)
pavouk = Enemy("Pavouk", 5, 2, 0)
end_game = False

print("Jméno: " + p1.name)
print("HP: " + str(p1.hp))
print("Attack: " + str(p1.atk))
print("Mana: " + str(p1.mana))
print("Potkal jsi stvoření jménem " + pavouk.name)

while not end_game:
    end_game_input = input("konec hry?")
    if end_game_input is not None:
        end_game = True
    try:
        input1 = input("Co uděláš? attack [a] run away [r]").lower()
    except TypeError:
        print("Není to string vole.")
    except input1 != "a" or "r":
        print("Napiš a nebo r vole.")

if input1 == "a":
    attackVal = Person.attack(p1)
    pavouk.hp -= attackVal
    print(pavouk.hp)
elif input1 == "r":
    print("Pokusil ses utéct.")
    Person.run_away(p1)




