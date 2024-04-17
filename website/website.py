from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path.home() / "D:/2 python, Mark Cassar/Website/DAB111_project_Group_2/database"

db_name = "nutrition.db"
db_path = base_path / db_name


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/features")
def features():
    return render_template("index.html") 

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    nutrition_status = cursor.execute("SELECT * FROM nutrition_status LIMIT 10").fetchall()
    con.close()

    return render_template("data_table.html", nutrition_status = nutrition_status) # template data_table 

@app.route("/references")
def references():
    return render_template("references.html")
  
if __name__=="__main__":
    app.run(debug=True)
