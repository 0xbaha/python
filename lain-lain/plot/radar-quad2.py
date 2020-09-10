
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

# ------- PART 1: Define a function that do a plot for one line of the dataset!

def make_spider( row, title, color):

    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([25,50,75], ["","",""], color="grey", size=7)
    plt.ylim(0,100)

    # Ind1
    values=df.loc[row].drop('method:').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)

# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))

# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title='method: '+df['method:'][row], color=my_palette(row))

plt.show()
