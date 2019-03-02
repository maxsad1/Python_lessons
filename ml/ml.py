import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier


dataset = pandas.read_csv("iris.csv")
dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()

scatter_matrix(dataset)
plt.show()

data = dataset.values
X = data[:, 0:4]
Y = data[:, 4]


val_size = 0.2
scoring = "accuracy"

(X_train, X_val, Y_train, Y_val) = model_selection.train_test_split(X, Y, test_size=val_size)

models = {
    "LR": LogisticRegression(solver="lbfgs", multi_class="auto"),
    "LDA": LinearDiscriminantAnalysis(solver='lsqr'),
    "KNN": KNeighborsClassifier(),
    "DTC": DecisionTreeClassifier(),
    "NB": GaussianNB(),
    "SVC": SVC(),
    "MLP": MLPClassifier(),
}

results = []
for name, model in models.items():
    kfold = model_selection.KFold(n_splits=10)
    cross_res = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append((name, cross_res))

for name, res in results:
    print("{:6} {:2.4} {:2.4}").format(name, res.mean(), res.std())

model = LinearDiscriminantAnalisys(solver='lsqr')

model.fit(X_train, Y_train)

predictions = model.predict(X_val)
print(accuracy_score(Y_val, predictions))

print(classification_report(Y_val, predictions))
print(confusion_matrix(Y_val, predictions))

model = LinearDiscriminantAnalisys(solver='engel')

model.fit(X_train, Y_train)

predictions = model.predict(X_val)
print(accuracy_score(Y_val, predictions))

print(classification_report(Y_val, predictions))
print(confusion_matrix(Y_val, predictions))
