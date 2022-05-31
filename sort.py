from enum import Enum

class Animal:
    def __init__(self, list): #id, type, gender, nick, dateBirth, dateCome):
        self.id = list[0]
        self.type = list[1]
        if list[2] == 'male':
            self.gender = BREEDABLE.MALE
        else:
            self.gender = BREEDABLE.FEMALE
        self.gender = list[2]
        self.nick = list[3]
        self.dateBirth = list[4]
        self.dateCome = list[5]

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getGender(self):
        return self.gender

    def getNick(self):
        return self.nick

    def getDateBirth(self):
        return self.dateBirth

    def getDateCome(self):
        return self.dateCome

class BREEDABLE(Enum):
    MALE = 1
    FEMALE = 2
    BOTH = 3

# 1 and 2
file_name = 'input.txt'
fin = open(file_name, 'r')
#animals = []
breeding = dict()
animals = dict()

while True:
    newLine = fin.readline()
    if not newLine:
        break
    if (newLine[-1] == '\n'):
        newLine = newLine[:-1]
    newAnimal = Animal(newLine.split(' '))
    if newAnimal.type in animals:
        animals[newAnimal.type] += 1
    else:
        animals[newAnimal.type] = 1
    if newAnimal.type in breeding:
        if breeding[newAnimal.type] != BREEDABLE.BOTH:
            if breeding[newAnimal.type] != newAnimal.gender:
                breeding[newAnimal.type] = BREEDABLE.BOTH
    else:
        breeding[newAnimal.type] = newAnimal.gender
breeding_true = list()
for key in breeding.keys():
    if breeding.get(key) == BREEDABLE.BOTH:
        breeding_true.append(key)
breeding_true.sort(key=lambda animal: len(animal))
if len(breeding_true) == 0:
    print(0)
else:
    for i in breeding_true:
        print(i)
    for key in animals.keys():
        print(key + ' - ' + str(animals.get(key)))
fin.close()

# 3

class Call:
    def __init__(self, list):
        self.date = list[0]
        self.timing = list[1]
        self.user = list[2]
        self.number = list[3]

file_name = 'input_3.txt'
fin = open(file_name, 'r')

calls = []
while True:
    newLine = fin.readline()
    if not newLine:
        break
    if (newLine[-1] == '\n'):
        newLine = newLine[:-1]
    newCall = Call(newLine.split(' '))
    calls.append(newCall)
calls.sort(key= lambda call : int(call.timing), reverse=True)
calls.sort(key= lambda call : call.user)
for call in calls:
    print(call.date + ' ' + call.timing + ' ' + call.user + ' ' + call.number)
fin.close()
