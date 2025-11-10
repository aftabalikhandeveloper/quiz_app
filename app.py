from flask import Flask, render_template, request, redirect, url_for
from db.connection import get_connection
from db.schema import create_tables

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/admin")
def admin():

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")
    teacher_data = cur.fetchall()
    data_lenght = len(teacher_data)
    conn.commit()
    cur.close()

    # teacher_data = [{key: value} for key, value in teacher_data]

    return render_template("admin.html", teachers=teacher_data, data_lenght=data_lenght)

@app.route("/teacher/add", methods=["POST"])
def add_teacher():
    teacher_name = request.form["name"]
    teacher_education = request.form["education"]
    conn = get_connection()
    cur = conn.cursor()
    sql_query = "INSERT INTO teachers (name, education) VALUES (%s, %s)"

    # Define the data to be inserted as a tuple
    data = (teacher_name, teacher_education)

    # Execute the query, passing the query string and the data tuple as separate arguments
    cur.execute(sql_query, data)
    conn.commit()
    cur.close()

    return redirect(url_for("admin"))



@app.route("/teacher/delete/<t_id>")
def delete_teacher(t_id):
    if id != "":
        conn = get_connection()
        cur = conn.cursor()
        sql_query = "DELETE FROM teachers WHERE teacher_id=%s"
        data = (t_id,)
        cur.execute(sql_query,data)
        conn.commit()
        cur.close
        return "teacher has been deleted"
    return "id is not correct or something else"


if __name__ == "__main__":
    print(create_tables())
    app.run(debug=True, port=3001)