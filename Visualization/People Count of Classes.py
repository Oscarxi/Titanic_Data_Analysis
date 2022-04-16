import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data/train.csv')
test_data = pd.read_csv('Titanic Data/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis=0)

# 製作艙等人數直方圖
# 計算艙等人數
C1_cnt = len(all_data[all_data['Pclass'] == 1])
C2_cnt = len(all_data[all_data['Pclass'] == 2])
C3_cnt = len(all_data[all_data['Pclass'] == 3])

# 設定標籤與資料
data = [C1_cnt,C2_cnt,C3_cnt]
labels = ['Class1', 'Class2', 'Class3']

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.bar(labels, data, width = 0.3)
ax1.set_title("People Count of Classes", size = 20)  # 標題 
ax1.legend()  # 圖例
fig1.set_size_inches(12, 8)  # 圖表大小

# 輸出圖表
plt.show()