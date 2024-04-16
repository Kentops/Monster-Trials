import entity
import random

class ExpTroll(entity.Entity):
  '''
  The expert troll enemy
  melee_attack(enemy):str - attacks enemy and returns a description.
  '''

  def __init__(self):
    '''Constructs a troll'''
    hp = random.randint(15,18)
    super().__init__("Angry Troll", hp)

  def melee_attack(self, enemy) -> str:
    dmg = random.randint(8,12)
    enemy.take_damage(dmg)
    return f"{self._name} bashes {enemy.name} with its club for {dmg} damage!"