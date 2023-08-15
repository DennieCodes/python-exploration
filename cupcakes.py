import math
"""

Making cupcakes
You and your friends have started a cupcake business to help you make money while you're working on your startup.

You pooled your money and went to buy all the stuff needed for your gourmet cupcakes: flour, sugar, eggs, and tubes of frosting.

But your calculations were off. After making all of the cupcakes you could with your ingredients, your group realizes that you don't have enough frosting for all of the cupcakes.

You also find out two interesting facts:

People will buy your cupcakes with frosting for a certain amount of money.
People will buy your cupcakes without frosting for less money.
People will buy your unused tubes of frosting because there are people who just like eating the frosting.
You and your friends decide to frost as many cupcakes as you can, then sell everything you've got: frosted cupcakes, cupcakes without frosting, and your leftover tubes of frosting.

Given the following input values:

num_cupcakes, which is how many cupcakes you have
num_tubes_frosting, which is how many tubes of frosting you have
tubes_per_cupcake, which is exactly how many tubes of frosting go on each cupcake
Complete the function profit so that it returns the total dollars that you make given the following information:

A frosted cupcake sells for $10
A cupcake with no frosting sells for $4
A tube of frosting by itself sells for $1
Constraints:

1 <= num_cupcakes <= 100
10 <= num_tubes_frosting <= 50
1 <= tubes_per_cupcake <= 5
Example:

Let's say you had 10 cupcakes, 5 tubes of frosting, and it takes 2 tubes of frosting to frost a cupcake. You can frost two cupcakes. You have one tube of frosting left over.

Item	                      Quantity	Selling price	Total
Frosted cupcake	            2	        $10	          $20
Cupcake with no frosting	  8	        $4	          $32
Leftover tubes of frosting	1	        $1	          $1

This means that you would make $53.

"""

def profit(num_cupcakes, num_tubes_frosting, tubes_per_cupcake):
  # Determine how many cupcakes you can make with available tubes of frosting
  # Determine remaining how many cupcakes you can make without frosting
  # Determine how many tubes of frosting are leftover
  # Calculate profit based on these values

  frosted = math.floor(num_tubes_frosting / tubes_per_cupcake)
  unfrosted = num_cupcakes - frosted
  frosting = num_tubes_frosting - (frosted * tubes_per_cupcake)

  gross_earnings = frosted * 10 + unfrosted * 4 + frosting * 1
  return gross_earnings


result = profit(10, 5, 2)
print(result)