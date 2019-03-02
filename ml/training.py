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

dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()

scatter_matrix(dataset)
plt.show()

data = dataset.values

val_size = 0.2
scoring = "accuracy"
models = {
	"LR": LogisticRegression(solver="lbfgs", multi_class="auto", max_iter=1000),
	"LDA": LinearDiscriminantAnalysis(solver="lsqr"),
	"DTC": DecisionTreeClassifier(),
	"KNN": KNeighborsClassifier(),
	"NB": GaussianNB(),
	"SVC": SVC(gamma="auto"),
	"MLP": MLPClassifier(max_iter=1000),
	}

X = data[:, 0:4]
Y = data[:, 4]
(X_train, X_val, Y_train, Y_val) = model_selection.train_test_split(X, Y, test_size=val_size)


results = []
for name, model in models.items():
    kfold = model_selection.KFold(n_splits=10)
    cross_res = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append((name, cross_res))

best_name = ""
best_model = None
best_acc = 0
for name, res in results:
    print("{:6} {:8.4} {:8.4}".format(name, res.mean(), res.std()))
    if res.mean() > best_acc:
        best_acc = res.mean()
        best_name = name
        best_model = models[name]

print()
print("Best model is", best_name)

print()
print("Training LDA...")
model = LinearDiscriminantAnalysis(solver="lsqr")
model.fit(X_train, Y_train)

predictions = model.predict(X_val)
print("Accuracy =", accuracy_score(Y_val, predictions))
print(classification_report(Y_val, predictions))


import pickle

file = open("lda_model.bin", mode="wb")

pickle.dump(model, file)
file.close()
