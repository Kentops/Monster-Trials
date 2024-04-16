import entity
import random

class ExpGoblin(entity.Entity):
  '''
  The expert goblin class
  melee_attack(enemy):str - Attacks enemy and returns a string
  '''
  
  def __init__(self):
    '''Constructs a goblin'''
    hp = random.randint(12,15)
    super().__init__("Angry Goblin", hp)

  def melee_attack(self,enemy)->str:
    dmg = random.randint(5,8)
    enemy.take_damage(dmg)
    return f"{self._name} slams {enemy.name} for {dmg} damage!"