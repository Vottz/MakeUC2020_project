from flask import *
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html") 

@app.route('/session')
def sessions():
    vokabel = "Bonjour"
    return render_template("session.html", vokabel=vokabel) 


@app.route('/session_solution')
def background_process_test():
    vokabel = "Hallo"
    return render_template("session.html", vokabel=vokabel)


@app.route('/new', methods = ['POST', 'GET'])
def new():
    msg = ""
    identity = 0
    if request.method == 'POST':
        try:
            front = request.form['front']
            back = request.form['back']
         
            with sql.connect("vokabeln.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO vokabeln (id,vokabel,solution) VALUES (?,?,?)",(identity,front,back) )
                
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            con.close()
            return render_template("new.html",msg = msg)
    return render_template("new.html",msg = "")

@app.route('/list')
def list():
   con = sql.connect("vokabeln.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from vokabeln")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)




if __name__ == "__main__":
    app.run()