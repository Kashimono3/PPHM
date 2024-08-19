import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

filename = "cleaned_data.csv"
df = pd.read_csv(filename)
data_to_scale = df[['height','weight','bmi']]
scaler = StandardScaler()
scaler_data = scaler.fit_transform(data_to_scale)
df_scaled = pd.DataFrame(scaler_data,columns=['height_scaled','weight_scaled','bmi_scaled'])

plt.figure(figsize=(8,6))
plt.scatter(df_scaled['height_scaled'],df_scaled['weight_scaled'],color = 'green',marker='o')
plt.title('Scatter  Plot of Scaled Height vs Scaled Weight')
plt.xlabel('Scaled Height')
plt.ylabel('Scaled Weight')

plt.grid(True)
plt.show()