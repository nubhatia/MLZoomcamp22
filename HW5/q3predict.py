import pickle


def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

# client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print(y_pred)
