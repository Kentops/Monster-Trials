import entity
import random

class Hero(entity.Entity):
  '''
  The player character
  melee_attack(enemy):str and ranged_attack(enemy):str attack enemy and return a string describing the attack.
  '''

  def __init__(self, name):
    '''Constructs the hero'''
    super().__init__(name, 25)

  def melee_attack(self,enemy)-> str:
    '''Deals 2D6 damage to enemy and returns a description.'''
    dmg = random.randint(1,6) + random.randint(1,6)
    enemy.take_damage(dmg)
    return f"{self._name} slashes the {enemy.name} with a sword for {dmg} damage!"

  def ranged_attack(self, enemy:entity.Entity)->str:
    '''Deals 1D12 damage to enemy and returns a description'''
    dmg = random.randint(1,12)
    enemy.take_damage(dmg)
    return f"{self._name} pierces the {enemy.name} with an arrow for {dmg} damage!"