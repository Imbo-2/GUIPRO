from flask import Flask, render_template, request

app = Flask(__name__)

@app.route
def submit_form():
    if request.method == 'POST':
        name = request.form['NAME']
        email = request.form['EMAIL']
        phone = request.form['PHONE']
        message = request.form['MESSAGE']


    return render_template('contact_form.html', name=name, name=email, name=phone, name=message)

if __name__ '__name__';
    app.run
























