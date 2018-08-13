#importing flask module fro
from flask import Flask, render_template,request,jsonify

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route with url as /login
@app.route('/login')
def index():
       return render_template('login.html')


@app.route('/FlaskTutorial',  methods=['POST'])
def success():
       if request.method == 'POST':
             email = request.form['email']
             return render_template('success.html', email=email)
       else:
             pass
@app.route('/employeelist')
def get_records():
        results = [
                      {
                          "Employee Name": "Sarang Rana",
                          "Employee Code": "18490",
                      }
                  ]
        return jsonify(results)
if __name__ == '__main__':
       app.run(host= '0.0.0.0')
