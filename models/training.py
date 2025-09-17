import pandas as pd # used to manipulate csv data
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression
import joblib
le_files=["toxic.csv","abusive.csv", "hate.csv", "national.csv", "obscene.csv", "racist.csv", "religious.csv", "sexist.csv", "threat.csv","provocative.csv"]
for i in le_files:
    db = pd.read_csv(i) #reading now stores the dataframe
    db.iloc[:, 1] = db.iloc[:, 1].astype(int) #assigning numbers to each thing
 #splitting the data
    X=db['Text']
    y = db.iloc[:, 1]
# assigning to each variable the x and y test and train values
    model = LogisticRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 ) #testing is 30%

    vectorizer = CountVectorizer() # is an object now vectorizer is storing a count vectorizer object, converting text data to numerical values
    X_train_vectors = vectorizer.fit_transform(X_train) #fit_transform owned by vectorizer object (function only useable on vectorizer ALL DATATYPES ARE OBJECTS) anyways it LETS MODEL LEARN VOCABULARY ITS LOOKIN FOR
    X_test_vectors = vectorizer.transform(X_test)

    model.fit(X_train_vectors, y_train)
    y_pred = model.predict(X_test_vectors)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%\n") #outputs to stdout(terminal)

    joblib.dump(model, i[0:3]+".pkl")

    joblib.dump(vectorizer, "vectorizer"+i[0:3]+".pkl")