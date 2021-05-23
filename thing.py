from faker import Faker
import random
import di

faker = Faker()


class Thing:
    def __init__(self, title, protectionPercent, attack, life):
        self.title = title
        self.protectionPercent = protectionPercent
        self.attack = attack
        self.life = life


class Person():
    propertiesPerson = []

    def __init__(self, name, hp, base_attack, base_protection):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_protection = base_protection

    def set_things(self, *arguments):
        if len(self.propertiesPerson) >= 4:
            return 'You can\'t more thing in your person'
        else:
            for listarg in arguments:
                self.propertiesPerson.append(listarg)

    def show_things(self):
        print('На тебе сейчас одеты следующие предметы:')
        for item in range(len(self.propertiesPerson)):
            print(self.propertiesPerson[item].title)

    def hit_to_hp(self, Person):
        self.hp = self.hp - Person.base_attack

    def show(self):
        print('Character of person', self.name, self.hp,
              self.base_attack, self.base_protection)

    def wear_thing(self):
        for item in range(len(self.propertiesPerson)):
            self.hp += self.propertiesPerson[item].life


class Paladin(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack, base_protection)
        self.hp = hp * 2
        self.base_protection = base_protection * 2


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protection):
        super().__init__(name, hp, base_attack, base_protection)
        self.base_attack = base_attack * 2


def fight(attacker, protector):
    life_attacker = attacker.hp + attacker.base_protection
    life_protector = protector.hp + protector.base_protection

    power_attaker = attacker.base_attack
    power_protector = protector.base_attack
    # debugger
    # return f'Life_A = {life_attacker}, Life_P = {life_protector}, Power_A= {power_attaker}, Power_P={power_protector}'
    while(True):
        life_protector -= power_attaker
        print(life_protector)
        if (life_protector <= 0):
            print(f'{protector.name} is lose')
            return 1
            break
        life_attacker -= power_protector
        if (life_attacker <= 0):
            print(f'{attacker.name} is lose')
            return 2
            break


def select_group(ArrayOfHeroes):
    randNumber = random.randint(0, len(ArrayOfHeroes)-1)
    group_array.append(randNumber)
    print(len(ArrayOfHeroes))
    print(group_array)
    while(len(group_array) != len(ArrayOfHeroes)):
        if randNumber in group_array:
            randNumber = random.randint(0, len(ArrayOfHeroes))
        else:
            group_array.append(randNumber)

    return group_array


group_array = []

lose_element = []
listClassType = [Warrior, Paladin]
ArrayOfHeroes = []
listOfThings = []

# list of heroies
for _ in range(20):
    typeHero = listClassType[random.randint(0, len(listClassType)-1)]
    randomHP = random.randint(100, 500)
    randomAttack = random.randint(50, 100)
    randomProtectionPercent = random.randint(5, 40)
    ArrayOfHeroes.append(typeHero(faker.name(), randomHP,
                         randomAttack, randomProtectionPercent))

for _ in range(60):
    nameThing = di.listofMagicThings.get(str(random.randint(1, 50)))
    protectionPercent = random.randint(1, 10)
    attack = random.randint(10, 30)
    life = random.randint(1, 120)
    listOfThings.append(Thing(nameThing, protectionPercent,
                        attack, life))

print(select_group(ArrayOfHeroes))
copy_if = []
count_of_fighter = len(group_array) / 2
count = 0
print(group_array)
while(True):
    if (len(group_array) <= 1):
        print('Here')
        break
    else:
        att, pro = random.sample(range(len(group_array)), 2)
        print('Here', att, pro)
        if (att != pro):
            flag = fight(ArrayOfHeroes[att], ArrayOfHeroes[pro])
            if flag == 1:
                group_array.remove(group_array[att])
            else:
                group_array.remove(group_array[pro])
        else:
            print('after change', group_array)

print('Here', group_array)


# while(count <= count_of_fighter):
#     curr = 0
#     while(curr-1 <= len(group_array)-1):
#         if curr+1 <= len(group_array)-1:
#             flag = fight(ArrayOfHeroes[group_array[curr]],
#                          ArrayOfHeroes[group_array[curr+1]])
#             if flag == 1:
#                 copy_if.append(group_array[curr+1])
#             else:
#                 copy_if.append(group_array[curr])
#             curr += 1
#         else:
#             break

#     group_array = copy_if
#     print(group_array)

# copyofgroup = group_array.copy()
# curr = 0

# while(len(group_array) != 1):
#     print('Start')
#     print(f'{curr} - {ArrayOfHeroes[curr].name} {curr+1}-{ArrayOfHeroes[curr+1].name}')
#     flag = fight(ArrayOfHeroes[curr], ArrayOfHeroes[curr+1])
#     if flag == 1:
#         group_array.pop(curr)
#     else:
#         group_array.pop(curr+1)

#     print(group_array)
#     if (curr >= len(group_array)-1):
#         curr = 0
#     else:
#         curr += 1

# print(group_array)
# debugger list all Persons
# for item in range(len(ArrayOfHeroes)):
#     print(ArrayOfHeroes[item].name)
'''
ring_lord = Thing('Кольцо власти', 5, 10, 10)
sword_fire = Thing('Меч огня', 1, 30, 5)
helmet_soldier = Thing('Шлем солдата', 5, 1, 10)
armor_easy = Thing('Броня лучника', 5, 1, 15)


Meliodas = Warrior('Meloodas', 200, 34, 20)
Ban = Paladin('Ban', 130, 28, 45)

Meliodas.show()
Ban.show()

#print(fight(Ban, Meliodas))

Meliodas.set_things(ring_lord, sword_fire)
Meliodas.show_things()
'''
