import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv('distribution.csv')
fig = ff.create_distplot([df["Weight(Pounds)"].tolist()], ['gra'], show_hist = False)
fig.show()