import plotly.figure_factory as ff
import random
result = []
for i in range(0,100): 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)
fig = ff.create_distplot([result],['graph'], show_hist=False)
fig.show()