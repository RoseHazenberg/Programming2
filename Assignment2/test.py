import pandas as pd
import numpy as np

df_01 = pd.DataFrame(np.random.rand(3,5))
# print(df_01)

df_02 = pd.DataFrame(np.random.rand(3,5))
# print(df_02)

df_03 = pd.concat([df_01, df_02], axis=1)
# print(df_03)

matrix = np.array(df_03)
# print(matrix)

df_a = pd.DataFrame({'key':['A', 'B', 'C'], 'value':[1, 2, 3]}).set_index('key')

df_b = pd.DataFrame({'key':['A', 'B', 'X', 'Y'], 'value':[3, 4, 5, 7]}).set_index('key')

df_merged = pd.merge(df_a, df_b, how='inner', left_index=True, right_index=True)
print(df_merged)

df_merged_out = pd.merge(df_a, df_b, how='outer', left_index=True, right_index=True)
print(df_merged_out)

df_a.join(df_b)
