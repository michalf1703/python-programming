import classifier as classifier
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, DataPoint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = '3CqwrAzIPv'

db.init_app(app)

with app.app_context():
    db.create_all()

def train_classifier(app):
    with app.app_context():
        data = DataPoint.query.all()
        features = [[dp.feature1, dp.feature2, dp.feature3] for dp in data]
        categories = [dp.category for dp in data]
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        classifier = KNeighborsClassifier(n_neighbors=3)
        classifier.fit(features_scaled, categories)
        return classifier, scaler

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        data_points = DataPoint.query.all()
        data_list = [{'id': dp.id, 'feature1': dp.feature1, 'feature2': dp.feature2, 'feature3': dp.feature3,
                      'category': dp.category} for dp in data_points]
        return jsonify(data_list)

    elif request.method == 'POST':
        data = request.json
        try:
            feature1 = float(data['feature1'])
            feature2 = float(data['feature2'])
            feature3 = float(data['feature3'])
            category = int(data['category'])
            if feature1 <= 0 or feature2 <= 0 or feature3 <= 0:
                return jsonify({'error': 'Features cannot be negative'}), 400
            if category not in [1, 2, 3]:
                return jsonify({'error': 'Invalid category'}), 400

            new_data_point = DataPoint(feature1=feature1, feature2=feature2, feature3=feature3, category=category)
            db.session.add(new_data_point)
            db.session.commit()

            return jsonify({'id': new_data_point.id}), 201
        except (KeyError, ValueError):
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
        try:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            feature3 = float(request.form['feature3'])
            category = int(request.form['category'])
            if feature1 <= 0 or feature2 <= 0 or feature3 <= 0:
                flash('Invalid data. Features cannot be negative.', 'error')
                return render_template('400.html'), 400
            if category not in [1, 2, 3]:
                flash('Invalid data. Invalid category.', 'error')
                return render_template('400.html'), 400

            new_data_point = DataPoint(feature1=feature1, feature2=feature2, feature3=feature3, category=category)
            db.session.add(new_data_point)
            db.session.commit()

            flash('Record added successfully', 'success')
            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid data. Please enter valid numeric values.', 'error')
            return render_template('400.html'), 400

    return render_template('add.html')


@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    data_point = DataPoint.query.get(record_id)

    if data_point:
        db.session.delete(data_point)
        db.session.commit()
        flash('Record deleted successfully', 'success')
    else:
        flash('Record not found', 'error')
        return render_template('404.html'), 404

    return redirect(url_for('index'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            feature3 = float(request.form['feature3'])
            if feature1 <= 0 or feature2 <= 0 or feature3 <= 0:
                flash('Invalid data. Features cannot be negative.', 'error')
                return render_template('400.html'), 400

            with app.app_context():
                input_features = scaler.transform([[feature1, feature2, feature3]])

            prediction = classifier.predict(input_features)[0]

            return render_template('prediction.html', category=prediction)
        except ValueError:
            flash('Invalid data. Please enter valid numeric values.', 'error')
            return render_template('400.html'), 400

    return render_template('prediction.html')

@app.route('/api/predictions', methods=['GET'])
def api_predictions():
    try:
        feature1 = float(request.args.get('feature1'))
        feature2 = float(request.args.get('feature2'))
        feature3 = float(request.args.get('feature3'))
        if feature1 <= 0 or feature2 <= 0 or feature3 <= 0:
            return jsonify({'error': 'Invalid data. Features must be positive.'}), 400

        input_features = scaler.transform([[feature1, feature2, feature3]])
        prediction = classifier.predict(input_features)[0]

        return jsonify({'category': int(prediction)}), 200
    except ValueError:
        return jsonify({'error': 'Invalid data'}), 400

classifier, scaler = train_classifier(app)

if __name__ == '__main__':
    app.run(debug=True)
