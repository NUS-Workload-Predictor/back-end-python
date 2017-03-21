from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


# presentation workload simple data
class PresentationWorkloadSimpleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.time = attr_dict['time']
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.people = attr_dict['people']
        self.duration = attr_dict['duration']
        self.result = attr_dict['result']


class PresentationWorkloadSimpleDataSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkloadSimpleData


# presentation workload complex data
class PresentationWorkloadComplexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.cap = attr_dict['cap']
        self.semesters = attr_dict['semesters']
        self.credits = attr_dict['credits']
        self.time = attr_dict['time']
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.people = attr_dict['people']
        self.duration = attr_dict['duration']
        self.result = attr_dict['result']


class PresentationWorkloadComplexDataSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkloadComplexData

