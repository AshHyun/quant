import pandas as pd
import os

flist = os.listdir('TR_data/')
xlsx_list = [x for x in flist if x.endswith('.xlsx')]
close_data = []

for xls in xlsx_list:
    path = 'TR_data/'
    code = xls.split('.')[0]
    df = pd.read_excel(path + xls, engine='openpyxl')
    df2 = df[['일자', '현재가']].copy()
    df2.rename(columns={'현재가': code}, inplace=True)
    df2 = df2.set_index('일자')
    df2 = df2[::-1]
    close_data.append(df2)
    print(xls)
# concat
df = pd.concat(close_data, axis=1)
df.to_excel("merge.xlsx")