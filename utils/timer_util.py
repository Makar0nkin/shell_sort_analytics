import timeit
from typing import Callable
import pandas as pd
from utils.constants import NUMBER_OF_RUNS
from algorythms.sorts import shell_sort_base, shell_sort_h2, shell_sort_h3, shell_sort_exp, shell_sort_fib
import gc


def get_sort_exec_time_df(sort_type: str, arr_generator: Callable):
    df = pd.DataFrame(columns=['time', 'algorythm'])
    for i in range(NUMBER_OF_RUNS):
        arr = arr_generator()
        t = timeit.Timer(f'shell_sort_{sort_type}(arr)', 'gc.enable()',
                         globals={'arr': arr, **globals()}).timeit(number=1)
        df.loc[len(df.index)] = [t, sort_type]
    return df
