""" 你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
家有1 条绳索、6 个火把、42 枚金币等。 """
res_items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    sum = 0
    print('物品清单如下：')
    for res_name,res_num in inventory.items():
        print(res_num,res_name)
        sum += int(res_num)
    print('物品总数：%d个'%sum)
#displayInventory(res_items)

def addToInventory(inventory,add_inventory_list):
    for i in add_inventory_list:
        inventory.setdefault(i, 0)
        res_items[i] += 1
    displayInventory(inventory)
addToInventory(res_items,dragonLoot)
    

