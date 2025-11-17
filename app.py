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
    teacher_data_len = len(teacher_data)
    cur.execute("SELECT * FROM subjects")
    subject_data = cur.fetchall()
    subject_data_len = len(subject_data)
    cur.execute("SELECT * FROM classes")
    class_data = cur.fetchall()
    class_data_len = len(class_data)
    conn.commit()
    cur.close()

    # teacher_data = [{key: value} for key, value in teacher_data]

    return render_template("admin.html", teachers=teacher_data, teacher_data_len=teacher_data_len, subject_data_len=subject_data_len, class_data_len=class_data_len)


# all about teachers



@app.route("/teacher/<t_id>/createquiz")
def create_quiz(t_id):
    return render_template("teacher/createquiz.html", teacher_id=t_id)


@app.route("/teachers")
def teacher():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")
    teachers_data = cur.fetchall()
    conn.commit()
    cur.close()

    return render_template("teacher.html", teachers=teachers_data)


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


@app.route("/teacher/update/<t_id>", methods=["POST"])
def update_teacher(t_id):
    if t_id != "":
        teacher_name = request.form["name"]
        teacher_education = request.form["education"]
        conn = get_connection()
        cur = conn.cursor()
        sql_query = "UPDATE teachers SET name=%s, education=%s WHERE teacher_id=%s"
        data = (teacher_name, teacher_education, t_id)
        cur.execute(sql_query,data)
        conn.commit()
        cur.close()
        return "teacher has been updated"
    return "id is not correct or something else"







# all about subjects
@app.route("/subjects")
def subjects():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subjects")
    subjects_data = cur.fetchall()
    conn.commit()
    cur.close()

    return render_template("subject.html", subjects=subjects_data)


@app.route("/subject/add", methods=["POST"])
def add_subject():
    subject_name = request.form["name"]
    conn = get_connection()
    cur = conn.cursor()
    sql_query = "INSERT INTO subjects (subject_name) VALUES (%s)"

    # Define the data to be inserted as a tuple
    data = (subject_name,)

    # Execute the query, passing the query string and the data tuple as separate arguments
    cur.execute(sql_query, data)
    conn.commit()
    cur.close()

    return redirect(url_for("admin"))


@app.route("/subject/delete/<s_id>")
def delete_subject(s_id):
    if s_id != "":
        conn = get_connection()
        cur = conn.cursor()
        sql_query = "DELETE FROM subjects WHERE subject_id=%s"
        data = (s_id,)
        cur.execute(sql_query,data)
        conn.commit()
        cur.close()
        return "subject has been deleted"
    return "id is not correct or something else"






# all about class

@app.route("/classes")
def classes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM classes")
    classes_data = cur.fetchall()
    conn.commit()
    cur.close()

    return render_template("class.html", classes=classes_data)


@app.route("/class/add", methods=["POST"])
def add_class():
    class_name = request.form["name"]
    conn = get_connection()
    cur = conn.cursor()
    sql_query = "INSERT INTO classes (class_name) VALUES (%s)"
    data = (class_name,) 
    cur.execute(sql_query, data)
    conn.commit()
    cur.close()
    return redirect(url_for("admin"))


@app.route("/class/delete/<c_id>")
def delete_class(c_id):
    if c_id != "":
        conn = get_connection()
        cur = conn.cursor()
        sql_query = "DELETE FROM classes WHERE class_id=%s"
        data = (c_id,)
        cur.execute(sql_query,data)
        conn.commit()
        cur.close()
        return "class has been deleted"
    return "id is not correct or something else"





# teacher subjects

@app.route("/teacher-subjects")
def teacher_subjects():
    return render_template("teacher_subjects.html")    

if __name__ == "__main__":
    print(create_tables())
    app.run(debug=True, port=3001)