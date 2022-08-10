# Diccionario 
import random
person = {"class": "Mago", "lvl": 6, "mp":8, "hp": 10, "atk":5, "def": 2, "acc": 5, "skills": [{"spellname": "fireball", "mp": 4, "damage": 6}, {"spellname": "thunder", "mp": 10, "damage": 9}]}
enemy = {"class": "Goblin", "lvl": 3, "hp": 8, "atk": 3, "def": 2, "acc":3, "crit": 6}
in_battle = True

def enemy_options(enemy):
    pass

def atk_missed(accuracy_stat: int) -> bool: # -Return True o False
    pass

def critical(critical_stat: int) -> bool: # -Return True o False
    pass

def blow_calculator(attacker, defender):
    blow = attacker - defender
    if blow < 0:
        blow = 0
    return blow

while in_battle:
    option = input("Estas en ballta contra un {0} - HP: {1}. Tu hp: {2}\nQue deseas hacer? \n\n1-Atacar\n2-defenderte: ".format(enemy['class'], enemy['hp'], person['hp']))
    if int(option) == 1:
        enemy['hp'] -= blow_calculator(person['atk'], enemy['def'])
        # move of the enemy
    elif int(option) == 2:
        blow = blow_calculator(enemy['atk'], (person['def'] * 2))
        person['hp'] -= blow
    if enemy['hp'] <= 0:
        print("Mataste al enemigo")
        in_battle = False
