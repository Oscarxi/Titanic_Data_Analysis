import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data Analysis/train.csv')
test_data = pd.read_csv('Titanic Data Analysis/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis = 0)


# 觀察年齡區間
# 以平均值填補缺失值
all_data['Age'] = all_data['Age'].fillna(all_data['Age'].mean())

# 建立區間列表
age_class1 = len(all_data[all_data['Age'] < 20])
age_class2 = len(all_data[(all_data['Age'] < 40) & (all_data['Age'] >= 20)])
age_class3 = len(all_data[(all_data['Age'] < 60) & (all_data['Age'] >= 40)])
age_class4 = len(all_data[(all_data['Age'] < 120) & (all_data['Age'] >= 60)])

# 設定標籤與資料
labels = ['0~20', '20~40', '40~60', '60~']
data = [age_class1, age_class2, age_class3, age_class4]

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.bar(labels, data, width = 0.3, color = "navy")
ax1.set_title("Age Group", size = 20)
fig1.set_size_inches(12, 8)

# 輸出圖表
plt.show()