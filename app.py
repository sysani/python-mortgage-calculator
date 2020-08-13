from send_email import send_email
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:PGDb512@localhost/realestate'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="realestate_data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    down=db.Column(db.Integer)
    salary=db.Column(db.Integer)
    location=db.Column(db.String(100))

    def __init__(self, email, down, salary, location):
        self.email=email
        self.down=down
        self.salary=salary
        self.location=location

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email"]
        location=request.form["location"]
        down=request.form['down']
        salary=request.form['salary']

        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data=Data(email,down,salary,location)
            db.session.add(data)
            db.session.commit()

            #downpaymnent_avg=round(db.session.query(func.avg(Data.down)).scalar(),1)
            #salary_avg=round(db.session.query(func.avg(Data.salary)).scalar(),1)
            down, salary = int(down), int(salary)
            dp_total = (down / .05) if down <= 25000 else ((down - 25000) / .1) + 500000
            salary_total = (((salary / 12 * .30) * 12) * 25)

            total = int(dp_total if (dp_total < salary_total) else salary_total)

            #count=db.session.query(Data.email).count()
            send_email(email,location,down,salary,total)

            return render_template("success.html")

        return render_template("index.html",text="Email address already in use! Please enter a new one")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001) #default:5000

#$ source env/bin/activate to run virtual env
#(env) python app.py to run app
