import entity
import random

class BegTroll(entity.Entity):
  '''
  The troll fighter
  melee_attack(enemy):str - Attacks enemy and returns a string describing the attack
  '''

  def __init__(self):
    '''Constructs a troll'''
    hp = random.randint(8,10)
    super().__init__("Troll", hp)

  def melee_attack(self, enemy) -> str:
    dmg = random.randint(5,9)
    enemy.take_damage(dmg)
    return f"{self._name} swipes at {enemy.name} for {dmg} damage!"