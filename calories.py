'''
Your best friend is turning 30! You and some other friends have decided to throw a huge birthday bash! You've planned decorations, games, and music. Now, all of you need to plan is the menu that you're having catered.

Luckily, you found a good caterer through some connections. The theme of the party is 1950s Americana. The caterer has promised a meal with an entree, a side, a dessert, and a drink. They send over the menu cards for each.

Number	Course	Menu-item	          Calories
--------------------------------------------
1	      Entree	Hamburger	          522
2	      Entree	Veggie burger	      399
3	      Entree	Impossible burger	  501
1     	Side	  French fries	      130
2     	Side	  Sweet potato fries	125
3     	Side	  Salad	              72
1	      Dessert	Apple pie	          222
2	      Dessert	Milkshake	          391
3	      Dessert	Fruit cup	          100
1	      Drink	  Diet soft drink	    10
2	      Drink	  Coffee	            8
3	      Drink	  Martini	            120

entree_list = [ 522, 399, 501 ]
side_list = [ 130, 125, 72 ]
dessert_list = [ 222, 391, 100 ]
drink_list = [ 10, 8, 120 ]

You decide to build a little phone app for the attendees to figure out the total amount of calories for their menu options.

Given the chosen number for each of the courses from the above menu items, complete the function calories to return the total calories for the choices.

If someone chooses the value 0, then that means they're going to skip that part of the meal.

Constraints: All inputs will be greater than or equal to 0 and less than or equal to 3.

Example:

If someone chooses:

2 for their entree (veggie burger: 399 calories)
3 for their side (salad: 72 calories)
0 for their dessert (no dessert: 0 calories)
3 for their drink (martini: 120 calories)
then the total calories for that meal is 591 calories.
'''

def calories(entree_num, side_num, dessert_num, drink_num):
    entree_list = [ 0, 522, 399, 501 ]
    side_list = [ 0, 130, 125, 72 ]
    dessert_list = [ 0, 222, 391, 100 ]
    drink_list = [ 0, 10, 8, 120 ]

    total_calories = entree_list[entree_num] + side_list[side_num] + dessert_list[dessert_num] + drink_list[drink_num]

    return total_calories

print(calories(1, 2, 3, 2))
