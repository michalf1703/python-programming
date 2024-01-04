
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, DataPoint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '3CqwrAzIPv'
scaler = None
classifier = None

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        data_points = DataPoint.query.all()
        data_list = [{'id': dp.id, 'feature1': dp.feature1, 'feature2': dp.feature2,'feature3': dp.feature3, 'category': dp.category} for dp in data_points]
        return jsonify(data_list)

    elif request.method == 'POST':
        data = request.json

        try:
            new_data_point = DataPoint(feature1=data['feature1'], feature2=data['feature2'], feature3=data['feature3'], category=data['category'])
            db.session.add(new_data_point)
            db.session.commit()

            return jsonify({'id': new_data_point.id}), 201
        except KeyError:
            return jsonify({'error': 'Invalid data'}), 400

@app.route('/api/data/<int:record_id>', methods=['DELETE'])
def api_delete_data(record_id):
    data_point = DataPoint.query.get(record_id)

    if data_point:
        db.session.delete(data_point)
        db.session.commit()

        return jsonify({'id': data_point.id}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404


@app.route('/')
def index():
    data_points = DataPoint.query.all()
    return render_template('index.html', data_points=data_points)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        feature1 = float(request.form['feature1'])
        feature2 = float(request.form['feature2'])
        feature3 = float(request.form['feature3'])
        category = int(request.form['category'])

        new_data_point = DataPoint(feature1=feature1, feature2=feature2, feature3=feature3,  category=category)
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
