from flask import Flask, request, render_template
import requests
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Titanic_rfc_pipe_SC.pkl", "rb"))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form["age"])
        fare = float(request.form["fare"])
        pclass = int(request.form["pclass"])
        sibsp = int(request.form["sibsp"])
        parch = int(request.form["parch"])
        

    #Sex(Gender)
        sex = request.form["sex"]
        if(sex=="male"):
            male=1
        else:
            female=0

        #Region
        embarked = request.form["embarked"]
        if(embarked=="S"):
            S = 1
            C = 0
            Q = 0 
        elif(embarked=="C"):
            S = 0
            C = 1
            Q = 0  
        else:
            S = 0
            C = 0
            Q = 1 

        prediction = model.predict(pd.DataFrame([[pclass,sex,age,sibsp,parch,fare,embarked]],columns=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']))

        patient = "Sorry to say,  Predict Died on the Titanic"
        success = "You're lucky.  Predict survival on the Titanic !!"
        if prediction == 0:
            return render_template('index.html', p=patient)
        elif prediction == 1:
            return render_template('index.html', s=success) 

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)








            

        
        
        




    

