import random


class Entity:
    def __init__(self, name, hp, atk, mana):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.mana = mana


class Person(Entity):
    def attack(self):
        attack_val = random.randint(1, self.atk)
        print("Zaútočil jsi! " + " poškození")
        return attack_val

    def run_away(self):
        run_away_val = random.randint(1, 2)
        if run_away_val == 1:
            print("Nepovedlo se ti utéct. Nepřítel tě zranil a způsobil ti " +
                  " poškození.")
        else:
            print("Podařilo se ti utéci.")


class Enemy(Entity):
    pass


class Npc(Entity):
    pass
