import entity
import random

class BegGoblin(entity.Entity):
  '''
  The beginner goblin class
  melee_attack(enemy): str - Attacks enemy and returns a string describing the attack
  '''

  def __init__(self):
    '''Constructs a goblin'''
    hp = random.randint(7,9)
    #Use the super method to define the subclass's attributes?
    super().__init__("Goblin", hp)

  def melee_attack(self,enemy)->str:
    dmg = random.randint(4,6)
    enemy.take_damage(dmg)
    return f"{self._name} bites {enemy.name} for {dmg} damage!"