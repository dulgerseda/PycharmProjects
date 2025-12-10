import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("/Users/sedadulger/PyCharmProjects/week_11/airquality.csv")
df.head()
print(df.columns)

# Index(['rownames', 'Ozone', 'Solar.R', 'Wind', 'Temp', 'Month', 'Day'], dtype='object')

df.shape

df.describe()
df.info()


df.isnull().any()
df.isnull().sum()

df['Temp']
df['Temp'].describe()

print(round(df['Temp'].mean(), 2)) # 76.12

Q1 = df['Temp'].quantile(0.25)
Q3 = df['Temp'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Temp'] < lower) | (df['Temp'] > upper)]
print(outliers)

#       rownames  Ozone  Solar.R  Wind   Temp  Month   Day
# 24      25.0    NaN     66.0  16.6 -212.0    5.0  25.0

df_new = df.drop(index=24)

# df.drop(index=24, inplace=True)  # kalıcı silme

print(round(df_new['Temp'].mean(), 2)) #78.02


# Soru: Sıcaklık (Temp) serisini çiziniz. (Matplotlib veya Seaborn kullanarak)

plt.figure(figsize=(10, 5))
plt.plot(df_new['Temp'], color='tomato', marker='o', linestyle='-')
plt.title("Daily Temperature Series (After Outlier Removal)")
plt.xlabel("Index")
plt.ylabel("Temperature (°F)")
plt.grid(True)
plt.show()

# Soru: Fahrenheit cinsinden verilen sıcaklık değerlerini Celsius’a çeviren bir fonksiyon yazınız.

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


# Soru: Tüm sıcaklık (Temp) değerlerini Fahrenheit’tan Celsius’a çevirip yeni bir sütun (Temp_C) olarak ekleyiniz.

df_new['Temp_C'] = df_new['Temp'].map(fahrenheit_to_celsius)

print(round(df_new['Temp_C'], 2))


# Soru: Sıcaklık değerlerini Fahrenheit ve Celsius olarak aynı grafikte gösteriniz.

plt.figure(figsize=(10, 5))
plt.plot(df_new['Temp'], label='Temperature (°F)', color='tomato', marker='o')
plt.plot(df_new['Temp_C'], label='Temperature (°C)', color='royalblue', marker='s')
plt.title("Temperature in Fahrenheit and Celsius")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.legend()
plt.grid(True)
plt.show()


# Soru: AirQualityReport adında bir sınıf oluşturunuz.
# Bu sınıf, DataFrame'den sıcaklık, ozon ve rüzgar (wind) ortalamalarını hesaplasın.

class AirQualityReport:
    def __init__(self, df):
        self.mean_temp = df['Temp'].mean()
        self.mean_ozone = df['Ozone'].mean()
        self.mean_wind = df['Wind'].mean()



# Soru: AirQualityReport sınıfına, sıcaklık (Temp), ozon (Ozone) ve rüzgar (Wind)
# sütunlarının maksimum değerlerini döndüren bir metot ekleyiniz.

class AirQualityReport:
    def __init__(self, df):
        self.mean_temp = df['Temp'].mean()
        self.mean_ozone = df['Ozone'].mean()
        self.mean_wind = df['Wind'].mean()

    def max_values(self):
        return {
            "Max_Temp": df['Temp'].max(),
            "Max_Ozone": df['Ozone'].max(),
            "Max_Wind": df['Wind'].max()
        }

# Soru: Python dosyası çıktıları HTML veya PDF'e dönüştür

report_html = df_new.to_html("AirQualityReport.html")
print("Rapor 'AirQualityReport.html' olarak kaydedildi.")












#%%




# Soru: AirQualityReport sınıfından bir nesne oluşturunuz ve ortalama ile maksimum değerleri
# ekrana yazdırınız.

class AirQualityReport:
    def __init__(self, df):
        self.mean_temp = df['Temp'].mean()
        self.mean_ozone = df['Ozone'].mean()
        self.mean_wind = df['Wind'].mean()

    def max_values(self):
        return {
            "Max_Temp": df['Temp'].max(),
            "Max_Ozone": df['Ozone'].max(),
            "Max_Wind": df['Wind'].max()
        }

report = AirQualityReport(df_new)

print("Ortalama Değerler:")
print(f"Temperature (Temp): {round(report.mean_temp, 2)} °F")
print(f"Ozone: {round(report.mean_ozone, 2)}")
print(f"Wind: {round(report.mean_wind, 2)}")

print(report.max_values())



# Soru: AirQualityReport sınıfına ait ortalama ve maksimum değerleri bir tablo (DataFrame)
# olarak gösteriniz.

# Maksimum değerleri al
max_vals = report.max_values()

summary_df = pd.DataFrame({
    "Measurement": ["Temperature (Temp)", "Ozone", "Wind"],
    "Mean": [round(report.mean_temp, 2), round(report.mean_ozone, 2), round(report.mean_wind, 2)],
    "Max": [max_vals["Max_Temp"], max_vals["Max_Ozone"], max_vals["Max_Wind"]]
})

print(summary_df)

#          Measurement   Mean    Max
# 0  Temperature (Temp)  78.02   97.0
# 1               Ozone  42.13  168.0
# 2                Wind   9.91   20.7

# Soru: Ortalama ve maksimum değerleri içeren tabloyu (summary_df)
# bir CSV dosyasına kaydediniz.

summary_df.to_csv("AirQuality_Summary.csv", index=False)


# Soru: Kaydedilen CSV dosyasını tekrar okuyarak kontrol ediniz.

check_df = pd.read_csv("AirQuality_Summary.csv")
print(check_df)



# Soru: Ortalama ve maksimum değerleri görselleştiriniz (örneğin bar grafiği ile).

plt.figure(figsize=(8, 5))
plt.bar(summary_df["Measurement"], summary_df["Mean"], color="skyblue", label="Ortalama (Mean)")
plt.bar(summary_df["Measurement"], summary_df["Max"], color="salmon", alpha=0.6, label="Maksimum (Max)")
plt.title("Air Quality - Ortalama ve Maksimum Değerler")
plt.xlabel("Ölçüm Türü")
plt.ylabel("Değer")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Soru: Ortalama (Mean) ve maksimum (Max) değerler arasındaki farkı hesaplayıp tabloya yeni bir sütun (Difference) olarak ekleyiniz.

summary_df["Difference"] = summary_df["Max"] - summary_df["Mean"]
print(summary_df)



# Soru: Ortalama, maksimum ve fark değerlerini içeren tabloyu (summary_df) görselleştiriniz (örneğin çoklu çubuk grafik olarak).

x = np.arange(len(summary_df["Measurement"]))  # X ekseni konumları
width = 0.25  # çubuk genişliği

plt.figure(figsize=(9, 5))
plt.bar(x - width, summary_df["Mean"], width, label="Ortalama (Mean)", color="skyblue")
plt.bar(x, summary_df["Max"], width, label="Maksimum (Max)", color="salmon")
plt.bar(x + width, summary_df["Difference"], width, label="Fark (Difference)", color="lightgreen")

plt.xticks(x, summary_df["Measurement"])
plt.title("Air Quality Ölçümleri: Ortalama, Maksimum ve Fark")
plt.xlabel("Ölçüm Türü")
plt.ylabel("Değer")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

