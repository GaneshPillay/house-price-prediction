import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

#loaded_model=pickle.load(open("model.pkl","rb"))
#initialization of flask
app=Flask(__name__)

#defining the html file to get the user input
def pred_function(y_pred):
    loaded_model=pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(y_pred)
    return result

@app.route('/')
def home():
    return render_template('index.html')




@app.route('/result',methods=['POST'])
def result():
    bedroom=int(request.form['Bedrooms'])
    bathrooms=int(request.form['Bathrooms'])
    sl=int(request.form['sqft_living'])
    floor=int(request.form['Floor'])
    waterfront=int(request.form['Waterfront'])
    features=[bedroom,bathrooms,sl,floor,waterfront]
    #int_features = [x for x in request.form.values()]
    #final_features = [np.array(int_features)]
    final_features=[features]
    result=pred_function(final_features)
    #result=loaded_model.predict(final_features)
    prediction="The predicted house price is"+str(result)
    return render_template("result.html",prediction=prediction)



#main function
if __name__=="__main__":
    app.run(debug=True)
