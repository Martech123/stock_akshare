import pandas as pd

year = '2020'
df = pd.read_csv('zhangting_{}.csv'.format(year))

print(df.columns)
df = df.sort_values(by=['所属行业', '代码', 'date'])
print(df)
df.to_csv('zhangting_{}_ana.csv'.format(year))
