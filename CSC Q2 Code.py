import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot

# Load the data
df = pd.read_csv("archive/anxiety_depression_data.csv")

# Bin sleep hours
df['Sleep_Category'] = pd.cut(df['Sleep_Hours'], bins=[0, 4, 5, 6, 7, 8, 9, 10, 12],
                              labels=['<4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '>10'])

# Plot 1: Anxiety Score
plt.figure(figsize=(12, 6))
joyplot(
    data=df,
    by='Sleep_Category',
    column='Anxiety_Score',
    colormap=plt.cm.tab10,
    fade=True,
    title='Anxiety Score Distribution by Sleep Duration'
)
plt.xlabel('Anxiety Score')
plt.ylabel('Sleep (in hours)')
plt.tight_layout()
plt.show()

# Plot 2: Depression Score
plt.figure(figsize=(12, 6))
joyplot(
    data=df,
    by='Sleep_Category',
    column='Depression_Score',
    colormap=plt.cm.Set1,
    fade=True,
    title='Depression Score Distribution by Sleep Duration'
)
plt.xlabel('Depression Score')
plt.ylabel('Sleep (in hours)')
plt.tight_layout()
plt.show()
