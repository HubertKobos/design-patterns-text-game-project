from .EnemyCreator import EnemyCreator
import Enemies


class EnemyMageCreator(EnemyCreator):
    '''
    Concrete creator to create enemy of type mage
    '''

    def _create_enemy(self, enemy_type: str):
        enemy = None
        if enemy_type == "basic_mage":
            enemy = Enemies.BasicMageEnemy()
        elif enemy_type == "experienced_mage":
            enemy = Enemies.ExperiencedMageEnemy()

        return enemy
