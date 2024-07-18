import joblib, pickle
from flask import Flask, request, render_template
import pandas as pd
import datetime as dt
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

model = joblib.load(open('creditCardFraud_model_new', 'rb'))
dataFrame = pd.read_csv('fraudTrain.csv')
# label_encoder = LabelEncoder()

# load label_encoder
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

@app.route('/', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':

        trans_date_trans_time = request.form['trans_date_trans_time']
        trans_date = pd.DatetimeIndex([trans_date_trans_time]).date
        trans_time = pd.DatetimeIndex([trans_date_trans_time]).time
        trans_date = pd.to_datetime(trans_date)
        del trans_date_trans_time

        # trans_date = pd.to_datetime([trans_date])
        trans_date = trans_date.map(dt.datetime.toordinal)
        trans_time = pd.to_datetime(trans_time, format='%H:%M:%S')
        trans_time = 3600 * pd.DatetimeIndex(trans_time).hour + 60 * pd.DatetimeIndex(
            trans_time).minute + pd.DatetimeIndex(trans_time).second

        merchant = request.form['merchant']
        # merchant = label_encoder.fit_transform([merchant])
        merchant = label_encoder['merchant'].transform([merchant])
        
        category = request.form['category']
        # category = label_encoder.fit_transform([category])
        category = label_encoder['category'].transform([category])
        
        amount = request.form['amount']
        gender = request.form['gender']
        if gender == 'M':
            gender = 1
        elif gender == 'F':
            gender = 0
        city = request.form['city']
        # city = label_encoder.fit_transform([city])
        city = label_encoder['city'].transform([city])
        
        state = request.form['state']
        # state = label_encoder.fit_transform([state])
        state = label_encoder['state'].transform([state])
        
        zip = request.form['zip']
        lat = request.form['lat']
        long = request.form['long']
        city_pop = request.form['city_pop']
        
        job = request.form['job']
        job = label_encoder['job'].transform([job])
        
        dob = request.form['dob']
        dob = pd.to_datetime(dob)
        age = (pd.to_datetime('now') - dob) / np.timedelta64(1, 'Y')
        # print('type of age ', type(age))
        # age = int(age)
        del dob
        unix_time = request.form['unix_time']
        merch_lat = request.form['merch_lat']
        merch_long = request.form['merch_long']

        # d = (
        #     trans_date, trans_time, merchant, category, amount, gender, city, state, zip, lat, long, city_pop, job, age,
        #     unix_time, merch_lat, merch_long)
        
        ##################################
        
        d_dict = dict()
        d_dict['trans_date'] = trans_date
        d_dict['trans_time'] = trans_time
        d_dict['merchant'] = merchant
        d_dict['category'] = category
        d_dict['amt'] = amount
        d_dict['gender'] = gender
        d_dict['city'] = city
        d_dict['state'] = state
        d_dict['zip'] = zip
        d_dict['lat'] = lat
        d_dict['long'] = long 
        d_dict['city_pop']  =city_pop
        d_dict['job']  = job
        d_dict['age']  =age
        d_dict['unix_time']  =unix_time
        d_dict['merch_lat']  =merch_lat
        d_dict['merch_long']  =merch_long
        # print('tml',type(d_dict['merch_long']))
        ##################################
        
        d = pd.DataFrame(d_dict)
        prediction = model.predict(d)
        print('the prediction is', prediction)
        # result = prediction.argmax()
        if prediction == 1:
            result = 'it is fraud process '
        elif prediction == 0:
            result = 'it is safe process'
        else:
            result = 'Please enter input values'
        print('the result is', result)
        return render_template('bank.html', result=result)

    else:
        
        return render_template('bank.html')


if __name__ == "__main__":
    app.run(debug=True)
