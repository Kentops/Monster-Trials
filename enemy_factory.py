import abc
import entity

class EnemyFactory(abc.ABC):
  '''
  Abstract factory interface
  <Abstract> create_random_enemy():Entity - creates a random enemy
  '''

  @abc.abstractmethod
  def create_random_enemy(self)->entity.Entity:
    '''Returns an enemy entity'''
    #see if we can get away with not importing entity
    pass