import check_input
import hero
import beg_factory
import exp_factory

'''Monster Trials
Kieran Whitney and Priscilla Romero 4/17/2024
A text-based rpg battle against some monsters!
'''


def main():
  print ("Monster Trails")
  name = input("What is your name? ")
  print(f"\nYou will face a series of 3 monsters, {name}.")
  print("Defeat them all to win.\n")

  player = hero.Hero(name)

  beginner_factory = beg_factory.BeginnerFactory()
  expert_factory = exp_factory.ExpertFactory()

  monsters = [beginner_factory.create_random_enemy() for _ in range(2)] + [ expert_factory.create_random_enemy()]

  while player.hp > 0 and monsters:
    print("Choose an enemy to attack:")
    for i, monster in enumerate(monsters, 1):
      print(f"{i}. {monster.name} HP: {monster.hp}")
    choice = check_input.get_int_range("Enter choice: ",1,len(monsters))

    enemy = monsters[choice - 1]
    print()
    print(player)

    print("1. Sword Attack")
    print("2. Arrow Attack")
    attack_choice = check_input.get_int_range("Enter choice: ", 1, 2)
    print()

    if attack_choice == 1:
      print(player.melee_attack(enemy))
    elif attack_choice == 2:
      print(player.ranged_attack(enemy))

    if enemy.hp > 0:
      print(enemy.melee_attack(player))
      print()
    else:
      print(f"You have slain the {enemy.name}\n")
      monsters.remove(enemy)

  if player.hp <= 0:
    print("You have been defeated.")
  else:
    print("Congratulations! You defeated all the monsters.")

  print("Game Over")
      
  
  
  


main()
      

