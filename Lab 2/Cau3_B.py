import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Đọc dữ liệu từ file CSV
filename = "cleaned_data.csv"
df = pd.read_csv(filename)

# Lựa chọn các cột cần chuẩn hóa
data_to_scale = df[['height', 'weight']]

# Tạo đối tượng MinMaxScaler với phạm vi từ 1 đến 10
scaler = MinMaxScaler(feature_range=(1, 10))

# Chuẩn hóa dữ liệu
scaler_data = scaler.fit_transform(data_to_scale)

# Tạo DataFrame từ dữ liệu đã được chuẩn hóa
df_scaled = pd.DataFrame(scaler_data, columns=['height_scaled', 'weight_scaled'])

# Hiển thị dữ liệu đã được chuẩn hóa
print("Dữ liệu sau khi chuẩn hóa từ 1 đến 10:")
print(df_scaled)
