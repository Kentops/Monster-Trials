import enemy_factory
import beg_troll
import beg_goblin
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
  '''
  The factory for beginner enemies
  create_random_enemy: creates a random basic enemy
  '''

  def create_random_enemy(self):
    choice = random.randint(0,1)
    if(choice == 0):
      return beg_goblin.BegGoblin()
    else:
      return beg_troll.BegTroll()

  