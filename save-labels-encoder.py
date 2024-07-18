# Data Scaling

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection  import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, plot_confusion_matrix
from datetime import date
from sklearn.preprocessing import LabelEncoder
import datetime as dt
import joblib
import re, pickle

df_train = pd.read_csv('fraudTrain.csv')
df_test = pd.read_csv('fraudTest.csv')

dataFrame = pd.concat([df_train,df_test],ignore_index=True)

label_encoder = dict()

label_encoder['merchant'] = LabelEncoder()
dataFrame.merchant = label_encoder['merchant'].fit_transform(dataFrame.merchant)

label_encoder['category'] = LabelEncoder()
dataFrame.category = label_encoder['category'].fit_transform(dataFrame.category)

label_encoder['city'] = LabelEncoder()
dataFrame.city = label_encoder['city'].fit_transform(dataFrame.city)

label_encoder['state'] = LabelEncoder()
label_encoder['state'].fit_transform(dataFrame.state)

label_encoder['job'] = LabelEncoder()
label_encoder['job'].fit_transform(dataFrame.job)

label_encoder['state'] = LabelEncoder()
label_encoder['state'].fit_transform(dataFrame.state)


# save label_encoder
pickle.dump(label_encoder,open('label_encoder.pkl','wb'))

# load label_encoder
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

print(label_encoder['merchant'].transform(['fraud_Rippin, Kub and Mann']))



