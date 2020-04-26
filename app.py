from flask import Flask, render_template, url_for, flash, redirect ,request
from forms import FlairForm
from model import get_flair
from flask import Response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import pickle
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY']='351d8ebafda1892160d5231ce2d11ab1'

posts = []


@app.route("/",methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    global posts
    if len(posts)==10:
        posts=[]
    form = FlairForm()
    flag=False
    if form.validate_on_submit():
        d={}
        d['flair']=get_flair(form.URL.data)
        d['URL']=form.URL.data
        print("Type : ",type(form.URL.data))
        print("Data : ",(form.URL.data))

        

        posts=[d]+posts
        return redirect(url_for('Flairs_Detected'))
    return render_template('Flair.html', form=form)


@app.route("/Flairs_Detected")
def Flairs_Detected():
    return render_template('Flair_detected.html',posts=posts)

@app.route("/data_ana1")
def data_ana1():
    return render_template('data_analysis1.html')

@app.route("/data_ana2")
def data_ana2():
    return render_template('data_analysis2.html')



@app.route("/automated_testing", methods=['GET', 'POST'])
def automated_testing():

    if request.method == 'POST':

            tf = request.files["myfile"]
            files=tf.read().decode("utf-8")
            
            lines=files.split("\n")
            jsonfile={}
            
            for i in range(len(lines)):
                 prediction=get_flair(lines[i])
                 jsonfile[lines[i]]=prediction       
                    
            
            file = open('automation_json.pkl', 'wb')
            jsonfile = json.dumps(jsonfile)

            # dump information to that file
            pickle.dump(jsonfile, file)
            # close the file
            file.close()
            return Response(jsonfile,
                       mimetype="text/json",
                       headers={"Content-Disposition":
                                    "attachment;filename=automation_result.json"})
        

            
    return render_template("automation.html")


if __name__ == '__main__':
    app.run(debug=True)
