from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:PGDb512@localhost/py_data'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self, email, height):
        self.email=email
        self.height=height

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email"]
        height=request.form["height"]

        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")

        return render_template("index.html")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001) #default:5000

#$ source env/bin/activate to run virtual env
#(env) python app.py to run app
