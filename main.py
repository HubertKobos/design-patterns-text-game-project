from Enemies.ArcherEnemy import BasicArcherEnemy
import MainCharacterProfessionsCreators
import EnemiesCreators
import SellerCreators
import WeaponsCreators
import ArmorsCreators
import random

if __name__ == "__main__":
    resurected = None

    def fighting_scene(enemy):
        resurected_enemy = None
        if enemy.is_resurected_prop == False:
            if random.choice([True, False]):
                resurected_enemy = enemy.clone()
                resurected_enemy.set_is_resurected = True
                resurected_enemy.armor_durability_val = -1  # resurected enemy dmg is weaker
                resurected_enemy.weapon_dmg_val = -1  # resurected enemy dmg is weaker
        while enemy.armor_durability_val >= 0:
            fight_inp = int(
                input(f"Choose option:\n1. Normal Attack\nYour choice: "))
            match fight_inp:
                case 1:
                    attack_dmg = player.attack()
                    enemy.armor_durability_val = -(attack_dmg)
                    print( 
                        f"Current durability of enemy: {enemy.armor_durability_val}\n")
                    if enemy.armor_durability_val <= 0:
                        if resurected_enemy != None:
                            print(
                                f"It seems that enemy is resurected ! You have to fight once again against weaker {resurected_enemy} !\n")

                            fighting_scene(resurected_enemy)
                        else:
                            print(f"You have won !\n")
                            break

    ENEMY_CLASSES = ['archer', 'mage', 'warrior']
    ENEMY_LEVEL = ['basic', 'experienced']

    chosen_class = int(input("Choose class:\n1.Warrior\nYour choice:"))

    match chosen_class:
        case 1:
            chosen_profession = int(
                input("Choose profession:\n1.Dark Warrior\n2.Holy Warrior\nYour choice:"))

    match chosen_class:
        case 1:
            creator = MainCharacterProfessionsCreators.WarriorProfessionCreator()
            match chosen_profession:
                case 1:
                    player = creator.set_profession_object("dark_warrior")
                case 2:
                    player = creator.set_profession_object("holy_warrior")

    while True:
        inp = int(
            input("Choose option:\n1. Fight with enemy\n2. Go shopping\n3. Quit\nYour choice:"))
        match inp:
            case 1:
                if player.weapon is None or player.armor is None:
                    print("You don't have enough equipment ! Let's go buy something !")
                    continue
                else:
                    random_enemy = random.choice(ENEMY_CLASSES)
                    random_enemy_level = random.choice(ENEMY_LEVEL)
                    match random_enemy:
                        case "archer":
                            enemy_creator = EnemiesCreators.EnemyArcherCreator()
                            enemy = enemy_creator.set_enemy_object(
                                random_enemy_level + '_' + random_enemy)

                        case "warrior":
                            enemy_creator = EnemiesCreators.EnemyWarriorCreator()
                            enemy = enemy_creator.set_enemy_object(
                                random_enemy_level + '_' + random_enemy)

                        case "mage":
                            enemy_creator = EnemiesCreators.EnemyMageCreator()
                            enemy = enemy_creator.set_enemy_object(
                                random_enemy_level + '_' + random_enemy)

                    print(f"\nYou are fighting against {enemy}\n")
                    fighting_scene(enemy)

            case 2:
                seller_inp = int(
                    input(
                        f"\nChoose Seller:\n1. Weapon Seller\n2. Armour Seller\nYour option: ")
                )
                seller_creator = SellerCreators.WarriorSellerCreator()
                seller = seller_creator.set_seller_object(
                    "warrior_seller")
                match seller_inp:
                    case 1:
                        if player.weapon != None:
                            print(
                                "You already have a weapon, that's enough for you !")
                            continue
                        else:
                            selected_item = seller.display_information_about_weapons()
                            class_of_item = selected_item[0]
                            creator = WeaponsCreators.WarriorWeaponCreator()
                            match class_of_item:
                                case "stick":
                                    weapon = creator.set_weapon_object(
                                        class_of_item, selected_item)
                                case "sword":
                                    weapon = creator.set_weapon_object(
                                        class_of_item, selected_item)
                            player.weapon = weapon
                    case 2:
                        if player.armor != None:
                            print(
                                "You already have a armour, that's enough for you !")
                            continue
                        else:
                            selected_item = seller.display_information_about_armours()
                            class_of_item = selected_item[0]
                            creator = ArmorsCreators.WarriorArmourCreator()
                            match class_of_item:
                                case "hauberk":
                                    armour = creator.set_armour_object(
                                        class_of_item, selected_item)
                                case "plate_armour":
                                    armour = creator.set_armour_object(
                                        class_of_item, selected_item)
                            player.armor = armour

            case 3:
                break
