''' In a town, the percentage of men is 52. The percentage of
total literacy is 48. If total percentage of literate men is 35 of
the total population, write a program to find the total number
of illiterate men and women if the population of the town is 80,000. '''

literate_population = 48/100*80000
literate_men = 35/100*80000
literate_women = literate_population - literate_men
total_men = 52/100*80000
total_women = 48/100*80000
illiterate_men = total_men - literate_men
illiterate_women = total_women- literate_women
print (" The number of Illiterate men is " + str(illiterate_men) + " The number of Illiterate Women is " + str(illiterate_women))
