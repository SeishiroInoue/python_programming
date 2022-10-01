import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('iris.csv')

X = df[['SepalLengthCm','SepalWidthCm',
        'PetalLengthCm','PetalWidthCm']]
y = df['Species']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.8,random_state=77
)

clf = RandomForestClassifier(random_state=77)
clf.fit(X_train,y_train)
pred = clf.predict(X_test)
accuracy = accuracy_score(y_test,pred)
print(accuracy)
