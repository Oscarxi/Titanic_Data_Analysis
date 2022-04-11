import pandas as pd
import matplotlib.pyplot as plt

# 資料讀取
train_data = pd.read_csv('titanic/train.csv')
test_data = pd.read_csv('titanic/test.csv')

# 合併資料
all_data = pd.concat([train_data,test_data], axis=0)


# 製作生存比例圓餅圖
# 提取 Survived 與 not Survived 之人數
all_data[all_data['Survived'] == 1.0]
survived_cnt = len(all_data[all_data['Survived'] == 1.0])
all_data[all_data['Survived'] == 0.0]
not_survived_cnt = len(all_data[all_data['Survived'] == 0.0])

# 生成圓餅圖
labels = ['survived', 'not_survived']
data = [survived_cnt, not_survived_cnt]

# 設定圖表
fig1, ax1 = plt.subplots()
ax1.pie(data, labels = labels, autopct = '%.1f%%', startangle = 90, textprops = {'fontsize': 20})

# 增加標題
ax1.set_title("Survived Proportion", size = 20)

# 增加圖例
ax1.legend()

# 設定圖表大小
fig1.set_size_inches(12, 8)
plt.show()