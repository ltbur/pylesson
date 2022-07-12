import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df1=pd.read_csv('Preview_20220712113408.csv',header=1,index_col='時点')
df2=pd.read_csv('Preview_20220712113520.csv',header=1,index_col='時点')
df3=pd.read_csv('Preview_20220712113548.csv',header=1,index_col='時点')
print(df1)
print(df2)
print(df3)

df1['年平均気温【℃】'].plot(label='平均気温')
df2['東京都'].plot(label='最高気温')
df3['東京都'].plot(label='最低気温')
plt.legend(loc='lower right')
plt.ylim(-10,40)
plt.show()
