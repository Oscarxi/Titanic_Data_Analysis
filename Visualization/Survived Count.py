import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('Titanic Data Visualization/Titanic Data/train.csv')
test_data = pd.read_csv('Titanic Data Visualization/Titanic Data/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis=0)


# 製作生存比例圓餅圖
# 提取 Survived 與 not Survived 之人數
female_survived_cnt = len(all_data[(all_data['Survived'] == 1.0) & (all_data['Sex'] == 'female')])
female_not_survived_cnt = len(all_data[(all_data['Survived'] == 0.0) & (all_data['Sex'] == 'female')])
male_survived_cnt = len(all_data[(all_data['Survived'] == 1.0) & (all_data['Sex'] == 'male')])
male_not_survived_cnt = len(all_data[(all_data['Survived'] == 0.0) & (all_data['Sex'] == 'male')])

# 設定標籤與資料
labels = ['female - survived', 'female - not survived', 'male - survived', 'male - not survived']
data = [female_survived_cnt, female_not_survived_cnt, male_survived_cnt, male_not_survived_cnt]

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.pie(data, labels = labels, autopct = '%.1f%%', startangle = 90, textprops = {'fontsize': 20})
ax1.set_title("Survived Proportion", size = 20)  # 標題
ax1.legend()  # 圖例
fig1.set_size_inches(12, 8)  # 圖表大小

# 輸出圖表
plt.show()