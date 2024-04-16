import enemy_factory
import exp_troll
import exp_goblin
import random

class ExpertFactory(enemy_factory.EnemyFactory):
  '''
  The Factory class for expert monsters
  create_random_enemy() returns an expert entity
  '''
  def create_random_enemy(self):
    choice = random.randint(0,1)
    if(choice == 0):
      return exp_goblin.ExpGoblin()
    else:
      return exp_troll.ExpTroll()