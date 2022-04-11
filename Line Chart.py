import random
import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Survivor/train.csv')
test_data = pd.read_csv('Titanic Survivor/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis = 0)

# 自建時間資料
data_time = [i + 1 for i in range(24)]
data_change = [i + random.uniform(0.0, 10.0) for i in data_time]  #隨機生成 0-10之間的數值

# 圖表基礎設定
fig1, ax1 = plt.subplots()
ax1.plot(data_time, data_change, c = "red")

# 增加標題
ax1.set_title("Line Chart", size = 20)

# 設定圖表大小
fig1.set_size_inches(12, 8)
plt.show()