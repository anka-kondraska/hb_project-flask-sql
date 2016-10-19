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
    projects = hackbright.get_grades_by_github(github)
    html = render_template('student_info.html', first=first, last=last, github=github, projects=projects)
    return html

@app.route('/form')
def form_route():
    """Route to pass data from /student to /student-add """
    return render_template('add_student.html')


@app.route("/student-add", methods=["POST"])
def student_add():
    """Create new student and update the student database """
    first = request.form.get("firstname")
    last = request.form.get("lastname")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template('acknowledge.html', first=first, last=last, github=github)

# @app.route('/project-form', methods=['GET'])
# def project_route():
#     """Route to form that collects project title info """
#     return render_template('project.html')

@app.route('/project')
def project_info():
    title, description, max_grade = hackbright.get_project_by_title(project)


    return render_template('project.html',title=title, description=description, max_grade=max_grade)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
