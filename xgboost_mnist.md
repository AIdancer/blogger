<b>使用xgboost对mnist数据进行分类</b>
效果不错，准确率直逼卷积神经网络，而且使用很简单。

```python
from mnist import MNIST
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def loadData():
    print('loading data...')
    filepath = r'D:\liqiaz\data\mnist'
    mndata = MNIST(filepath)
    train_data, train_label = mndata.load_training()
    test_data, test_label = mndata.load_testing()
    train_data, train_label, test_data, test_label = np.array(train_data), \
                np.array(train_label), np.array(test_data), np.array(test_label)
    print('load data successfully.')
    return train_data, train_label, test_data, test_label
   
X, Y, x, y = loadData()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7)
print(X.shape, Y.shape)
print(x.shape, y.shape)
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)
model = XGBClassifier(
            learning_rate=0.5,
            n_estimators = 1000,
            max_depth=5,
            min_child_weight = 1,
            gamma=0,
            subsample=0.8,
#             colsample_btree=0.8,
            objective='multi:softmax',
#             scale_pos_weight=1,
            random_state=42
        )
        
model.fit(X, Y, eval_set=[(x,y)], eval_metric="mlogloss", early_stopping_rounds=10, verbose=True)

y_pred = model.predict(x)
accuracy = accuracy_score(y, y_pred)
print('%.2f%%' % (accuracy * 100.0))

fig, ax = plt.subplots(figsize=[15, 15])
plot_importance(model, height=0.5, ax=ax, max_num_features=64)
plt.show()


```
