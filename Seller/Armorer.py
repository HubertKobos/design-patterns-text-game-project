from .ISeller import ISeller
import json

SELLER_WEAPONS = 'Equipment\seller_weapons.json'
SELLER_ARMOURS = 'Equipment\seller_armours.json'


class Armorer(ISeller):
    '''
    seller that's sells weapons and armours for warriors
    '''

    def load_items_from_json(self, file_type):
        if file_type == "weapons":
            with open(SELLER_WEAPONS) as json_file:
                data = json.load(json_file)

            item_dict = {}
            for item_type, items in data['warrior_seller'].items():
                item_list = []
                for item in items:
                    item_name = item['name']
                    item_gold_value = item['gold_value']
                    item_dmg = item['dmg']
                    item_durability = item['durability']
                    item_list.append(
                        (item_type, item_name, item_gold_value, item_dmg, item_durability))
                item_dict[item_type] = item_list

            return item_dict

        elif file_type == "armours":
            with open(SELLER_ARMOURS) as json_file:
                data = json.load(json_file)

            item_dict = {}
            for item_type, items in data['warrior_seller'].items():
                item_list = []
                for item in items:
                    item_name = item['name']
                    item_durability = item['durability']
                    item_gold_value = item['gold_value']
                    item_list.append(
                        (item_name, item_durability, item_gold_value))
                item_dict[item_type] = item_list

            return item_dict

    def display_information_about_weapons(self):
        available_weapons = self.load_items_from_json("weapons")

        items = [item for sublist in available_weapons.values()
                 for item in sublist]
        for index, item in enumerate(items, start=1):
            print(
                f"{index}. {item[1]} - Gold Value: {item[2]}, DMG: {item[3]}, Durability: {item[4]}")

        while True:
            try:
                choice = int(input("Enter the number of the item you want: "))
                if 1 <= choice <= len(items):
                    selected_item = items[choice - 1]
                    item_type = selected_item[0]
                    item_name = selected_item[1]
                    item_gold_value = selected_item[2]
                    item_dmg = selected_item[3]
                    item_durability = selected_item[4]
                    print(
                        f"You selected: {item_name} - Gold Value: {item_gold_value}, DMG: {item_dmg}, Durability: {item_durability}")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        return selected_item

    def display_information_about_armours(self):
        available_armours = self.load_items_from_json("armours")
        items = [(item_type, *item) for item_type,
                 sublist in available_armours.items() for item in sublist]
        for index, item in enumerate(items, start=1):
            item_type, item_name, item_durability, item_gold_value = item
            print(
                f"{index}. {item_type}: {item_name} - Durability: {item_durability}, Gold Value: {item_gold_value}")

        while True:
            try:
                choice = int(input("Enter the number of the item you want: "))
                if 1 <= choice <= len(items):
                    selected_item = items[choice - 1]
                    return selected_item
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
