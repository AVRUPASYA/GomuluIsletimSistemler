from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            cihaz = request.form['cihaz']
            durum= request.form['durum']


            with sqlite3.connect("projem.db") as con:
                conn = sqlite3.connect('projem.db')
                cur = con.cursor()
                con.commit()
                conn.close()
                msg = ("Kayıt başarılı bir şekilde eklendi")
        except:
            con.rollback()
            msg = "Kayıt eklenmedi hata oluştu"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("projem.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from ev")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)