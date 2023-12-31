import pandas as pd
from utils.constants import DATAFRAMES_FOLDER, DATAFRAME_FILE
import os
from algorythms.sorts import quick_sort, bucket_sort, comb_sort
from utils.list_generators import normal_list_generator, uniform_list_generator
from utils.timer_util import get_shell_sort_exec_time_df, get_sort_exec_time_df

df_normal = pd.concat(
    map(lambda st: get_sort_exec_time_df(st, normal_list_generator),
        [quick_sort, bucket_sort, comb_sort])
).reset_index(drop=True)
df_normal['distribution'] = 'normal'

df_uniform = pd.concat(
    map(lambda st: get_sort_exec_time_df(st, uniform_list_generator),
        [quick_sort, bucket_sort, comb_sort])
).reset_index(drop=True)
df_uniform['distribution'] = 'uniform'

df_total = pd.concat([df_normal, df_uniform]).reset_index(drop=True)
if not os.path.exists(DATAFRAMES_FOLDER):
    os.mkdir(DATAFRAMES_FOLDER)
df_total.to_csv(f'{DATAFRAMES_FOLDER}/{DATAFRAME_FILE}.csv')
# print(df_total[['time', 'distribution']].groupby(['distribution']).mean())
