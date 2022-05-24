from flask import Flask, jsonify, request, render_template
import os
import pickle
import re
from utils.funciones import signs_texts, thebridge, remove_stopwords, spanish_stemmer
import pandas as pd
from flask.helpers import flash



dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
from utils.forms import ValidateDate

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['DEBUG'] = True

model = pickle.load(open('data/finished_model.model','rb'))
emotions_array ={0:"Positivo", 1:"Negativo"}

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/api/v1/consulta', methods=["GET", "POST"])
def consulta():
    form = ValidateDate()
    if request.method == "GET": 
        if "text" in request.args:
            #request.get_json()['title']
            consulta = signs_texts(request.args["text"])
            consulta = remove_stopwords(consulta)
            consulta = spanish_stemmer(consulta)
            prediction = model.predict(pd.Series(consulta))[0]
            print(prediction)
            return jsonify({"respond":emotions_array[prediction]})
      
        else:
        
            return render_template("predict.html", form=form)
    else:  
                     
        if form.validate:
            if form.data["submit"] == True:
                try:
                    consulta = signs_texts(request.form["name"])
                    consulta = remove_stopwords(consulta)
                    consulta = spanish_stemmer(consulta)
                    prediction = model.predict(pd.Series(consulta))[0]
                    print(prediction)
                    respond = "Emoción:"
                    flash(respond)
                    flash(emotions_array[prediction])
                    return render_template("predict.html", form=form)
                
                except ValueError as e:
                    print(e)
                    flash("Debes introducir un campo válido")
                    return render_template("predict.html", form=form)
    

app.run()