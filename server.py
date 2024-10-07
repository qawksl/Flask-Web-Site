from flask import Flask, render_template, request, redirect
import datetime
import api

app = Flask(__name__)

student = {'name':'АНя','date_of_birth': datetime.date(2052,10,2)}
student2 = {'name':'Линар','date_of_birth': datetime.date(2002,5,15)}

students = [student,student2]

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/find")
def find():
    return render_template("find.html", image=api.find())


if __name__ =="__main__":
    app.run(host="0.0.0.0",port=8000, debug=True)