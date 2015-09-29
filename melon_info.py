"""
Prints out all the melons in our inventory
"""

from melons import melon_names, melon_seedlessness, melon_prices


# def print_melon(name, seedless, price):
#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)

melon_inventory = {}

#create a new dictionary
for i in melon_names:
    melon_inventory[melon_names[i]] = { 'price': melon_prices[i],
                                        'seedless': melon_seedlessness[i],
                                        'flesh_color': None,
                                        'rind_color': None,
                                        'average_weight': None
                                       }

#prints inventory
for melon in melon_inventory:

    price = melon_inventory[melon]['price']
    
    have_seeds = 'not seedless'
    if melon_inventory[melon]['seedless']:
        have_seeds = 'seedless'
    
    if melon_inventory[melon]['flesh_color'] == None:
        flesh_color_listed = ''
    else: 
        flesh_color_listed = ( "flesh color of " + 
                                melon_inventory[melon]['flesh_color'] + "\n")

    if melon_inventory[melon]['rind_color'] == None:
        rind_color_listed = ''  
    else:
        rind_color_listed = ( "rind color of " + 
                               melon_inventory[melon]['rind_color'] + "\n")  

    if melon_inventory[melon]['average_weight'] == None:
        average_weight_listed = '' 
    else:
        average_weight_listed = ( "average weight of " + 
                                melon_inventory[melon]['average_weight'] + "\n")

    print "{}s are ${:.2f}, and their attributes include: \n {}{}{}{}".format( melon, 
                                                                               price, 
                                                                               have_seeds, 
                                                                               flesh_color_listed, 
                                                                               rind_color_listed, 
                                                                               average_weight_listed
                                                                             )


