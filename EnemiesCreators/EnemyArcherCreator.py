from .EnemyCreator import EnemyCreator
# from ..Enemies.ArcherEnemy import BasicArcherEnemy, ExperiencedArcherEnemy
import Enemies


class EnemyArcherCreator(EnemyCreator):
    '''
    Concrete creator to create enemy of type archer
    '''

    def _create_enemy(self, enemy_type: str):
        enemy = None
        if enemy_type == "basic_archer":
            enemy = Enemies.BasicArcherEnemy()
        elif enemy_type == "experienced_archer":
            enemy = Enemies.ExperiencedArcherEnemy()

        return enemy
