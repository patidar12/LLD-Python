'''
When multiple subclasses extending the super class. and if some are not using
the parent class method/functionalities, and overriding parent method/functionalities.
Then there is huge chance of code duplicacy as may be multiple childs can overidie the parent
functionality and update the code according to that, that can be dulicate for that childs.

For ex.:
SportsVechile and OffRoadVechile overiding drive capabilities from Vechile class.
And implementing the same drive caspabilities, So this is the code duplicacy.
To avoid this StrategyDesignPattern help as.
'''