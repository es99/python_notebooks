'''
Inventário de um jogo de fantasia
'''

from audioop import add
from urllib.response import addinfo


def displayInventory(inventario):
    """Função que recebe qualquer inventário (dicionário) e exibe as informações"""
    total = 0
    print("Inventory:")
    for k, v in inventario.items():
        total += v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    """Função que recebe um dicionario juntamente com uma lista de loot (dragonLoot) e retorne
    o dicionário atualizado"""
    
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    
    return inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)