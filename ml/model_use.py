import pickle
import pandas

from sklearn.metrics import accuracy_score

data_file = "iris.csv"
model_file = "lda_model.bin"

def load_model():
    with open(model_file, "rb") as f:
        return pickle.load(f)


def load_dataset():
    return pandas.read_csv(data_file)


model = load_model()
dataset = load_dataset()

data = dataset.sample(60).values

X = data[:, :4]
Y = data[:, 4]

pred = model.predict(X)

for (xn, y, yr) in zip(X, pred, Y):
    xs = [str(x) for x in xn]
    print(", ".join(xs), y, yr)
