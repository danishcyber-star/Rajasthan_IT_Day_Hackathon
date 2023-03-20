from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import requests

# Categorization

def cat_by_RF(senty):
    dataa = pd.read_csv('BBC News Train.csv')
    dataa['CategoryId'] = dataa['Category'].factorize()[0]
    df = dataa[['Text', 'Category']]
    x = np.array(dataa.iloc[:, 0].values)
    y = np.array(dataa.CategoryId.values)
    cv = CountVectorizer(max_features=5000)
    x = cv.fit_transform(dataa.Text).toarray()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    classifier = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=0).fit(x_train, y_train)

    data = senty
    y_pred1 = cv.transform([senty])
    yy = classifier.predict(y_pred1)
    if yy == [0]:
        Result = "Business News"
    elif yy == [1]:
        Result = "Tech News"
    elif yy == [2]:
        Result = "Politics News"
    elif yy == [3]:
        Result = "Sports News"
    elif yy == [4]:
        Result = "Entertainment News"
    else:
        Result = "Unknown Category"

    return Result

def categoryPredict(data):

    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
    headers = {"Authorization": f"Bearer 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"}

    candidate_labels = ['Politics', 'Education', 'Health', 'Society', 'Technology', 'Entertainment', 'Travel',
                        'Finance', 'Culture', 'Food']

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": data,
        "parameters": {'candidate_labels': candidate_labels},
    })

    temp = {
        "labels": output["labels"],
        "scores": output["scores"],
        "summary": output["sequence"]
    }
    mval = max(temp["scores"])
    mind = temp["scores"].index(mval)

    return temp["labels"][mind]