import pandas as pd
import numpy as np
import tkinter as tk

df = pd.read_csv('서울_대기오염_데이터_2025.csv')

tmp_df = pd.DataFrame()

# for col in df.columns:
#     tmp_df = tmp_df._append(df[df[col] == 300.0])
#
# print(tmp_df)