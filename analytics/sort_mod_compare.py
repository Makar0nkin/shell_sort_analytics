import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils.constants import DATAFRAMES_FOLDER, DATAFRAME_FILE

sns.set_theme(style="ticks", palette="pastel")

df = pd.read_csv(f'../{DATAFRAMES_FOLDER}/{DATAFRAME_FILE}.csv')

sns.boxplot(x="algorythm", y="time",
            hue="distribution", palette=["m", "g"],
            data=df)
sns.despine(offset=10, trim=True)
plt.savefig(fname=f'{DATAFRAME_FILE}.png')
plt.show()
