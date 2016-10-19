from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
def get_student_form():

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template('student_info.html', first=first, last=last, github=github)
    return html

@app.route('/form')
def form_route():
    return render_template('add_student.html')


@app.route("/student-add", methods=["POST"])
def student_add():
    first = request.form.get("firstname")
    last = request.form.get("lastname")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template('acknowledge.html', first=first, last=last, github=github)

    



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
