import random
def yarat():
    tas_son = ''
    for _ in range(6):
        tas_son += random.choice('0123456789')
    return tas_son

def tanla(royhat):
    tasodif = random.choice(royhat)
    return tasodif
# print(tanla([1, 2, 3]))


