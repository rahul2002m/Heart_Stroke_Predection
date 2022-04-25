import pandas as p
import numpy as n
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler
import matplotlib.pyplot as plt
import seaborn as sb
import warnings

warnings.simplefilter('ignore')
# ...................  Loading Data  ...................#

heartData = p.read_csv('heart.csv')
# print(heartData.head())
# print(heartData.tail())
# print(heartData.shape)
# print(heartData.info())

# ...................  Data Cleaning  ...................#

heartData = heartData.drop(columns='id', axis=1)
# print(heartData.isnull().sum())
# sb.distplot(heartData.bmi)
# plt.show()

heartData['bmi'].fillna(heartData['bmi'].median(), inplace=True)
# print(heartData.isnull().sum())

# print(heartData['gender'].value_counts())

heartData.drop(heartData.index[heartData['gender'] == 'Other'], inplace=True)

# print(heartData['gender'].value_counts())

# ...................  Transforming  ...................#

enc = LabelEncoder()
heartData['gender'] = enc.fit_transform(heartData['gender'])
heartData['ever_married'] = enc.fit_transform(heartData['ever_married'])
heartData['Residence_type'] = enc.fit_transform(heartData['Residence_type'])
heartData = p.get_dummies(heartData)
# print(heartData.info())
# heartData.to_csv('final.csv')
# ...................  Test and Train Model  ...................#

x = heartData.drop(['stroke'], axis=1)
y = heartData['stroke']
# print(heartData.info())
# x.to_csv('final.csv')

# print(x.shape, y.shape)
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.3, random_state=100)
print(y_train.value_counts())
print(y_test.value_counts())
model = LogisticRegression()
model.fit(x_train, y_train)
x_train_predict = model.predict(x_train)
train_acc = accuracy_score(x_train_predict, y_train)
print(train_acc)

x_test_predict = model.predict(x_test)
test_acc = accuracy_score(x_test_predict, y_test)
print(test_acc)

# print(heartData.info())

def calc(inp_data):
    arr = n.asarray(inp_data)
    arr_rsp = arr.reshape(1, -1)
    pred = model.predict(arr_rsp)
    return pred[0]
    print(pred)
