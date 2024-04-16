import abc

class Entity(abc.ABC):
  '''
  The entity class defines a fighter
  name: string - The fighter's name
  hp: int - The fighter's current hitpoints
  take_damage(dmg) - lowers hp by dmg. Set hp to 0 if it becomes negative.
  <Abstract> melee_attack(enemy): string - Attacks enemy and returns a message describing the action.
  '''

  def __init__(self, name, hp):
    '''Creates an entity'''
    self._name = name
    self._hp = hp

  def take_damage(self, dmg):
    '''Subtracts dmg from hp'''
    self._hp -= dmg
    if(self._hp < 0):
      self._hp = 0

  @abc.abstractmethod
  def melee_attack(self, enemy) -> str:
    '''Attacks an enemy and returns a string describing the attack'''
    pass

  def __str__(self)-> str:
    return f"{self._name} HP: {self._hp}"

  #Properties
  @property
  def hp(self):
    return self._hp

  @property
  def name(self):
    return self._name

