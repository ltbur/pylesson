import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df=pd.read_csv('test.csv')


df.plot()
plt.show()


df=pd.read_csv('test.csv',index_col=0)

df.plot.bar()

plt.legend(loc='lower right')
plt.show()


df.plot.barh()
plt.legend(loc='lower left')


df.plot.bar(stacked=True)
plt.legend(loc='lower right')
plt.show()

df.plot.box()
plt.show()

df.plot.area()
plt.legend(loc='lower right')
plt.show()
