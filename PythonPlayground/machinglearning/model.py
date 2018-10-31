# def
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


def add_label(x):
    if x == 'setosa':
        return 1
    else:
        return 0


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/Mindjet/seaborn-data/master/iris.csv')
    species = df['species']
    labels = [add_label(x) for x in species]
    labels_df = pd.DataFrame(labels)
    df = pd.concat([df, labels_df], axis=1)
    df = df.drop(['species'], axis=1)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'y']

    labels = df['y']
    X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.25, random_state=0)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    actual = y_test
    predicted = model.predict(X_test)
    print(classification_report(actual, predicted))
    print(confusion_matrix(actual, predicted))


if __name__ == '__main__':
    main()
