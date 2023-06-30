from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'California, US',
  'salary': '$ 100,000',
}, {
  'id': 2,
  'title': 'Frontend Enginner',
  'location': 'Bangaluru, India',
  'salary': 'Rs 2,00,000',
}, {
  'id': 3,
  'title': 'Programmer',
  'location': 'Shimla, India',
  'salary': 'Rs 12,00,000',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'New York, US',
  'salary': '$ 800,000',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Web Devs")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
