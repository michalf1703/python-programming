from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature1 = db.Column(db.Float, nullable=False)
    feature2 = db.Column(db.Float, nullable=False)
    category = db.Column(db.Integer, nullable=False)

    @staticmethod
    def delete_record(record_id):
        record = DataPoint.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False