from flask import Flask, render_template, request

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["email"]
        data=request.form["data"]
    return render_template("success.html")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001) #default:5000

#$ source env/bin/activate to run virtual env
#(env) python app.py to run app
