# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data A
df = pd.DataFrame({
'method': ['proposed_v1','ENS_Bagging_v1','Tree_DecisionTree_v1'],
'time': [57.7,67.29,95.71],
'accuracy': [88.65,87.3,84.88],
'precision': [82.96,82.89,80.59],
'recall': [99.91,96.94,95.56],
'FAR': [74.86,75.49,71.8]
})

# Set data B
# df = pd.DataFrame({
# 'method': ['proposed_v2','ENS_Bagging_v2','Tree_DecisionTree_v2'],
# 'time': [56.27,75.1,95.82],
# 'accuracy': [91.93,87.02,85.93],
# 'precision': [87.29,82.86,82.1],
# 'recall': [99.88,96.37,95.19],
# 'FAR': [82.18,75.58,74.57]
# })

# list of methods
methods = list(df.method)
print(methods)

# list of method colors
colors = ['green','deepskyblue','orange']

# number of variable
categories=list(df)[1:]
N = len(categories)
print(categories)

for i,j in enumerate(methods):

    # selected method and method color to plot
    method_sn = i # method_serialnumber
    title = methods[method_sn]
    color = colors[i]

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.loc[method_sn].drop('method').values.flatten().tolist()
    values += values[:1]
    values
    print(values)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([25,50,75], ["","",""], color="grey", size=7)
    plt.ylim(0,100)

    # Plot data
    ax.plot(angles, values, color=color, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, color=color, alpha=0.1)

    # Add a title
    plt.title(title, size=11, color='black', y=1.1)

    # Save plot to file
    figname = '%s.svg' % title
    plt.savefig(figname)
    plt.clf()
