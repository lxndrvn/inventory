#step 6

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#step 1

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

def display_inventory(inventory):
    print("Inventory: ")
    for k, v in inv.items():
        print("{0} {1}".format(v, k))
    total_items = sum(inv.values())
    print("Total number of items: {}".format(total_items))

#step 2
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, added_items):
    for d in dragon_loot:
        value = inventory.get(d, 0)
        inventory[d] = value + 1
    return inventory

inv = add_to_inventory(inv, dragon_loot)

#step 3
def print_table(order=None):
    print("Inventory:")
    print("count    item name")
    print("-------------------")

    if order is None:
        final_items = inv.items()
    else:
        reversed_items = []
        for k, v in inv.items():
            reversed_items.append((v, k))
        if order == "count,desc":
            final_items = sorted(reversed_items, reverse=True)
        if order == "count,asc":
            final_items = sorted(reversed_items)

    for v, k in final_items:
        print(str(v).rjust(6), k.rjust(12))
    total_items = sum(inv.values())

    print("Total number of items: {}".format(total_items))

#step 4
def import_inventory(filename):
    import csv
    reader = csv.reader(open(filename, "r"))
    next(reader)
    for row in reader:
        item = row[0]
        value = inv.get(item, 0)
        inv[item] = value + int(row[1])
    return inv

inv = import_inventory("import_inventory.csv")

#step 5
def export_inventory(filename="export_inventory.csv"):
    import csv
    writer = csv.writer(open(filename, 'w'))
    for k, v in inv.items():
        writer.writerow([k, v])

export_inventory("export_inventory.csv")
