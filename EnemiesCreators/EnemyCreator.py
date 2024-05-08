from abc import ABC, abstractmethod


class EnemyCreator(ABC):
    '''
    Abstrack class for creators of enemies
    '''
    @abstractmethod
    def _create_enemy(self, enemy_type: str):
        '''
        Creates enemy
        '''

    def set_enemy_object(self, enemy_type: str):
        enemy = self._create_enemy(enemy_type)

        enemy.get_random_armor()
        enemy.get_random_weapon()

        return enemy
