from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import numpy as np 
# X
learn_data = np.array([0,1,2,3,4,5,6]).reshape((-1,1))
# Y
learn_label = np.array([0,2,4,6,8,10,12]).reshape((-1,1))

model = LinearRegression()
model.fit(learn_data, learn_label)

test_data = np.array([7,8,9,10]).reshape((-1,1))
test_label = np.array([14,16,18,20]).reshape((-1,1))
pred = model.predict(test_data)

print(test_data.T, "の予測結果:", test_label.T)
print(" 正解率 = ", accuracy_score( test_label,pred))