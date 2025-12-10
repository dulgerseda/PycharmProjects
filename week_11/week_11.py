import numpy as np

# NaN içeren bir dizi
x = np.array([1, 2, np.nan, 4])

print("Array:", x)
print("np.max(x):", np.max(x))       # NaN yüzünden sonuç NaN olur
print("np.nanmax(x):", np.nanmax(x)) # NaN'ı yoksayar, en büyüğü verir


import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("A =\n", A)
print("B =\n", B)

# 🔹 Eleman-eleman (element-wise) çarpım
print("\nA * B (element-wise):\n", A * B)

# 🔹 Matris çarpımı (dot product)
print("\nA.dot(B) (matrix product):\n", A.dot(B))

# A * B (element-wise):
#  [[ 5 12]
#  [21 32]]
#
# A.dot(B) (matrix product):

#  [[19 22]
#  [43 50]]

R = A.dot(B)       # veya np.dot(A, B)
# alternatif: R = A @ B


import numpy as np

A = np.array([[1, -1],
              [-1, 1]])
B = np.array([[1, -2],
              [1,  1]])
Id = np.identity(2)

R = A * 3
print("A * 3 (element-wise):\n", R, "\n")

print("Trace of A:", A.trace(), "\n")
# Matrisin köşegen (diagonal) elemanlarının toplamıdır.

R = A * B
print("A * B (element-wise):\n", R, "\n")

R = A.dot(B)
print("A.dot(B) (matrix product):\n", R)

import pandas as pd

df = pd.DataFrame({
    "V1": [11, 321, 53, 4, 67],
    "V2": ["Lucerne", "Bern", "Valais", "Zug", "Geneva"],
    "V3": ["LU", "BE", "VS", "ZG", "GE"]
})

print(df)

#--------------------------
import pandas as pd

df = pd.read_csv("animals.csv")   # CSV dosyasını oku
df.head()
df.tail()

print(df.describe())
print(df.info())
print(df['animal_type'])
print(df.columns)
df.columns = df.columns.str.strip()

w = df["weight"]
print(type(w))           #<class 'pandas.core.series.Series'>
df.weight.value_counts()

w = df[["weight"]]
print(type(w))           #class 'pandas.core.frame.DataFrame'>

print(df.loc[5, 'name'])                 # 5. indexteki 'name' sütunu
print(df.loc[2:6, ['name', "legs"]])     # 2–6 arası satırlar, 'name' sütunu
print(df.iloc[6])                        # 6. satırın tamamı


cdf = df.copy()
cdf.loc[8, "weight"] = np.nan

cdf.info
cdf.isnull().any()
cdf.isnull().sum()

# df['weight'] = df['weight'].fillna(df['weight'].mean())

cdf['rolling_mean_weight'] = df['weight'].rolling(3, center=True, min_periods=2).mean()

cdf['weight'] = cdf['weight'].fillna(df['weight'].rolling(3, center=True, min_periods=2).mean())

#---groupby:

gr_mean = df.groupby("animal_type")[["age", "weight", "legs"]].mean()
print(gr_mean)

def agg_func(df):
    return len(df)

gr_len = df.groupby("animal_type").agg({'age': agg_func})
print(gr_len)

gr_count = df.groupby("animal_type").count()
print(gr_count)

#---plot:

import matplotlib.pyplot as plt

df = pd.read_csv("animals.csv")
df.columns = df.columns.str.strip()
a = df.weight.values

# Interactive (pyplot) plot
plt.plot(a)
plt.title("my first plot")
plt.xlabel("index")
plt.ylabel("weight values")
plt.show()

# OOP (Object-Oriented) plot
fig, ax = plt.subplots(1, 1)
ax.plot(a)
ax.set_xlabel("index")
ax.set_ylabel("weight values")
ax.set_title("my second plot")
plt.show()

b = df.age.values
fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].plot(a, label="weight")
ax[0].set_ylabel("weight values")
ax[0].legend()

ax[1].plot(b, label="age", color="red")
ax[1].set_ylabel("age values")
ax[1].set_xlabel("index")
ax[1].legend()

plt.tight_layout()
plt.show()


import seaborn as sns

sns.scatterplot(
    data=df,
    x="weight",
    y="age",
    hue="animal_type",
    alpha=0.5
)
plt.show()














