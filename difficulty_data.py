from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


# difficulty simple data
class DifficultySimpleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    level = db.Column(db.Float)
    lecture = db.Column(db.Float)
    tutorial = db.Column(db.Float)
    lab = db.Column(db.Float)
    project = db.Column(db.Float)
    preparation = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.level = attr_dict['level']
        self.lecture = attr_dict['lecture']
        self.tutorial = attr_dict['tutorial']
        self.lab = attr_dict['lab']
        self.project = attr_dict['project']
        self.preparation = attr_dict['preparation']
        self.result = attr_dict['result']


class DifficultySimpleDataSchema(ma.ModelSchema):
    class Meta:
        model = DifficultySimpleData


# difficulty complex data
class DifficultyComplexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    level = db.Column(db.Float)
    lecture = db.Column(db.Float)
    tutorial = db.Column(db.Float)
    lab = db.Column(db.Float)
    project = db.Column(db.Float)
    preparation = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.cap = attr_dict['cap']
        self.semesters = attr_dict['semesters']
        self.credits = attr_dict['credits']
        self.level = attr_dict['level']
        self.lecture = attr_dict['lecture']
        self.tutorial = attr_dict['tutorial']
        self.lab = attr_dict['lab']
        self.project = attr_dict['project']
        self.preparation = attr_dict['preparation']
        self.result = attr_dict['result']


class DifficultyComplexDataSchema(ma.ModelSchema):
    class Meta:
        model = DifficultyComplexData
