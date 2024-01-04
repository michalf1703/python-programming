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


# Funkcja do trenowania klasyfikatora i standaryzacji
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


# Trasowanie API do pobierania i dodawania danych
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
            new_data_point = DataPoint(feature1=data['feature1'], feature2=data['feature2'], feature3=data['feature3'],
                                       category=data['category'])
            db.session.add(new_data_point)
            db.session.commit()

            return jsonify({'id': new_data_point.id}), 201
        except KeyError:
            return jsonify({'error': 'Invalid data'}), 400


# Trasowanie API do usuwania rekordu
@app.route('/api/data/<int:record_id>', methods=['DELETE'])
def api_delete_data(record_id):
    data_point = DataPoint.query.get(record_id)

    if data_point:
        db.session.delete(data_point)
        db.session.commit()

        return jsonify({'id': data_point.id}), 200
    else:
        return jsonify({'error': 'Record not found'}), 404


# Trasa strony głównej
@app.route('/')
def index():
    data_points = DataPoint.query.all()
    return render_template('index.html', data_points=data_points)


# Trasa dodawania nowego punktu danych
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            feature3 = float(request.form['feature3'])
            category = int(request.form['category'])

            new_data_point = DataPoint(feature1=feature1, feature2=feature2, feature3=feature3, category=category)
            db.session.add(new_data_point)
            db.session.commit()

            return redirect(url_for('index'))
        except ValueError:
            flash('Invalid data. Please enter valid numeric values.', 'error')
            return render_template('400.html'), 400

    return render_template('add.html')


# Trasa usuwania rekordu
@app.route('/delete/<int:record_id>', methods=['POST'])
def delete(record_id):
    data_point = DataPoint.query.get(record_id)

    if data_point:
        db.session.delete(data_point)
        db.session.commit()
        flash('Record deleted successfully', 'success')
    else:
        flash('Record not found', 'error')

    return redirect(url_for('index'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            feature3 = float(request.form['feature3'])

            # Standaryzacja cech wejściowych
            with app.app_context():
                input_features = scaler.transform([[feature1, feature2, feature3]])

            # Przewidywanie
            prediction = classifier.predict(input_features)[0]

            return render_template('prediction.html', category=prediction)
        except ValueError:
            flash('Invalid data. Please enter valid numeric values.', 'error')
            return render_template('400.html'), 400

    return render_template('prediction.html')

# Inicjalizacja klasyfikatora i skalera
classifier, scaler = train_classifier(app)
if __name__ == '__main__':
    app.run(debug=True)
