# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
'method:': ['proposed','ENS_AdaBoost','ENS_Bagging','ENS_RandomForest'],
'time': [78.39, 76.80, 78.62, 66.19],
'accuracy': [88.65,77.25,87.30,87.29],
'precision': [82.96, 70.90, 82.89, 81.99],
'recall': [99.91, 99.51, 96.94, 98.57],
'FAR': [74.86, 49.97, 75.49, 73.48]
})

plot_name = '111'

# number of variable
categories=list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('method:').values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([25,50,75], ["","",""], color="grey", size=7)
plt.ylim(0,100)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid', color='green')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1, color='green')

plt.show()
