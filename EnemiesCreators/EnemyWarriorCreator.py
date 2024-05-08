from .EnemyCreator import EnemyCreator
import Enemies


class EnemyWarriorCreator(EnemyCreator):
    '''
    Concrete creator to create enemy of type warrior
    '''

    def _create_enemy(self, enemy_type: str):
        enemy = None
        if enemy_type == "basic_warrior":
            enemy = Enemies.BasicWarriorEnemy()
        elif enemy_type == "experienced_warrior":
            enemy = Enemies.ExperiencedWarriorEnemy()

        return enemy
