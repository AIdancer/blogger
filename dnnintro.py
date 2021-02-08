```Python

import numpy as np
import matplotlib.pyplot as plt

# sigmoid
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

x = np.linspace(-5, 5, 100)
y0 = list(map(sigmoid, x))
plt.plot(x, y0)

# 双曲正切
def tanh(x):
    ep, en = np.exp(x), np.exp(-x)
    return (ep-en) / (ep + en)

x = np.linspace(-5, 5, 100)
y1 = list(map(tanh, x))
plt.plot(x, y1)

from sklearn.datasets import load_iris

data = load_iris()
X, y = data.data, data.target
print(X.shape, y.shape)
print(X[0:5,:])
print(y[0:100])

import datetime as dt
import  torch.nn as nn
import torch
import torch.optim as optim
from torch.utils.data import DataLoader,Dataset
import numpy as np
from torch.autograd import Variable
import os
import pandas as pd
import matplotlib.pyplot as plt

class MyData(Dataset):
    def __init__(self, _x, _y):
        self.x = torch.tensor(_x)
        self.y = torch.tensor(_y)
    
    def __getitem__(self, index):
        return self.x[index], self.y[index]
    
    def __len__(self):
        return len(self.x)
    
class DNN(nn.Module):
    def __init__(self):
        super(DNN, self).__init__()
        self.model = nn.Sequential(
#             nn.Linear(4, 1),
            nn.Linear(4, 32),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32,16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        ret = self.model(x)
        return ret

xtrain = np.array(X[0:100,:], dtype=np.float32)
ytrain = np.array(y[0:100], dtype=np.float32)

train_loader = DataLoader(dataset=MyData(xtrain, ytrain), batch_size=5, shuffle=True)
test_loader = DataLoader(dataset=MyData(xtrain, ytrain), batch_size=5, shuffle=True)

net = DNN()
optimizer = optim.Adam(net.parameters(), lr=0.01)
criterion = nn.MSELoss()

for i in range(60):
    total_loss = 0
    for idx, (data, label) in enumerate(train_loader):
        logits = net(data)
        label = label.view(-1, 1)
        loss = criterion(logits, label)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print('iteration %d --->  total_loss : %.2f' % (i, total_loss))
    
    
preds = []
labels = []
for idx, (data, label) in enumerate(test_loader):
    pred = net(data)
    preds.extend(pred.data.squeeze(1).tolist())
    labels.extend(label.tolist())
preds = np.round(preds).astype(np.int)
labels = np.array(labels).astype(np.int)
print(preds.shape)
print(np.sum(preds == labels))

print('acc : %.2f%%' % (np.sum(preds==labels) / preds.shape[0] * 100.0))

```
