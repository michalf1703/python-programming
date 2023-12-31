from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, DataPoint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '3CqwrAzIPv'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    data_points = DataPoint.query.all()
    return render_template('index.html', data_points=data_points)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        category = int(request.form['category'])

        new_data_point = DataPoint(feature1=feature1, feature2=feature2, category=category)
        db.session.add(new_data_point)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    if DataPoint.delete_record(record_id):
        flash('Record deleted successfully', 'success')
    else:
        flash('Record not found', 'error')

    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
