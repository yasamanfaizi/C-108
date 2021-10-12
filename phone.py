import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv('phones.csv')
fig = ff.create_distplot([df["Avg Rating"].tolist()], ['gra'], show_hist = False)
fig.show()