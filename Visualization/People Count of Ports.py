import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data Visualization/Titanic Data/train.csv')
test_data = pd.read_csv('Titanic Data Visualization/Titanic Data/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis=0)

# 製作港口人數直方圖
# 計算港口人數
C_cnt = len(all_data[all_data['Embarked'] == 'C'])
Q_cnt = len(all_data[all_data['Embarked'] == 'Q'])
S_cnt = len(all_data[all_data['Embarked'] == 'S'])

# 設定標籤與資料
data = [C_cnt,Q_cnt,S_cnt]
labels = ['Port C', 'Port Q', 'Port S']

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.bar(labels, data, width = 0.3)
ax1.set_title("People Count of Ports", size = 20)  # 標題 
ax1.legend()  # 圖例
fig1.set_size_inches(12, 8)  # 圖表大小

# 輸出圖表
plt.show()