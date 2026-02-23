from flask import Flask, render_template, request, redirect, url_for
from data import site_data
import urllib.parse

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html', site=site_data, current_year=2026)

@app.route('/projects')
def projects():
    return render_template('projects.html', site=site_data, current_year=2026)

@app.route('/projects/<project_id>')
def project_detail(project_id):
    proj = next((p for p in site_data['projects'] if p['id'] == project_id), None)
    if not proj:
        abort(404)
    return render_template('project_detail.html', site=site_data, project=proj, current_year=2026)

@app.route('/news')
def news():
    return render_template('news.html', site=site_data)

@app.route('/cv')
def cv():
    return render_template('cv.html', site=site_data)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name','')
        email = request.form.get('email','')
        message = request.form.get('message','')
        subject = f'Website Contact from {name}'
        body = f"""{message}\n\nFrom: {name} <{email}>"""
        mailto = 'mailto:' + site_data['email'] + '?subject=' + urllib.parse.quote(subject) + '&body=' + urllib.parse.quote(body)
        return redirect(mailto)
    return render_template('contact.html', site=site_data)

if __name__ == '__main__':
    app.run(debug=True)
