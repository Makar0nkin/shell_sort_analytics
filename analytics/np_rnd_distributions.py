import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.constants import DATAFRAME_FILE
from utils.list_generators import normal_list_generator, uniform_list_generator

normal_list = normal_list_generator()  # нормальное распределение
uniform_list = uniform_list_generator()  # равномерное распределение

normal_df = pd.DataFrame(normal_list, columns=['x'])  # .reset_index(names=['y'])
uniform_df = pd.DataFrame(uniform_list, columns=['x'])  # .reset_index(names=['y'])
normal_df['distribution'] = 'normal'
uniform_df['distribution'] = 'uniform'

df = pd.concat([normal_df, uniform_df], ignore_index=True, sort=False)

sns.kdeplot(data=df, x='x', hue='distribution')
plt.savefig(fname=f'distributions.png')
plt.show()