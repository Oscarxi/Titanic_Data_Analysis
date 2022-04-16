import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data Visualization/Titanic Data/test.csv')
test_data = pd.read_csv('Titanic Data Visualization/Titanic Data/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis=0)

# 製作年齡-票價散佈圖
# 設定圖表觀測向量與標籤
data_x = all_data['Age']
data_y = all_data['Fare'] / (all_data['SibSp'] + all_data['Parch'] + 1)

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.scatter(data_x, data_y, c = "red")
ax1.set_xlabel("Age")   # X軸說明
ax1.set_ylabel("Fare")  # Y軸說明
ax1.set_title("Average Fare Price", size = 20)  # 標題 
fig1.set_size_inches(12, 8)  # 圖表大小

# 輸出圖表
plt.show()

# 檢視離群值
print(all_data[data_y > 500])