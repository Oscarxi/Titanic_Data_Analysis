from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data Analysis/test.csv')
test_data = pd.read_csv('Titanic Data Analysis/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis = 0)

# 製作年齡-票價散佈圖
# 設定圖表觀測向量與標籤
data_x = all_data['Age']
data_y = all_data['Fare'] / (all_data['SibSp'] + all_data['Parch'] + 1)

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.scatter(data_x, data_y, color = "navy")
ax1.set_xlabel("Age")
ax1.set_ylabel("Fare")
ax1.set_title("The Relevance of Age and Fare", size = 20)
fig1.set_size_inches(12, 8)

# 輸出圖表
plt.show()