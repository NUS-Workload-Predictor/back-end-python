from common import db, ma
from flask import jsonify
from flask_restful import Resource


# difficulty simple
class DifficultySimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    level = db.Column(db.Float)
    lecture = db.Column(db.Float)
    tutorial = db.Column(db.Float)
    lab = db.Column(db.Float)
    project = db.Column(db.Float)
    preparation = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.level = attr_list[0]
        self.lecture = attr_list[1]
        self.tutorial = attr_list[2]
        self.lab = attr_list[3]
        self.project = attr_list[4]
        self.preparation = attr_list[5]
        self.intercept = attr_list[6]

    def update(self, attr_list):
        self.level = attr_list[0]
        self.lecture = attr_list[1]
        self.tutorial = attr_list[2]
        self.lab = attr_list[3]
        self.project = attr_list[4]
        self.preparation = attr_list[5]
        self.intercept = attr_list[6]


class DifficultySimpleSchema(ma.ModelSchema):
    class Meta:
        model = DifficultySimple


difficulty_simple_schema = DifficultySimpleSchema(strict=True)


class DifficultySimpleResource(Resource):
    def get(self, module_code):
        query = DifficultySimple.query.filter_by(code=module_code).first()
        result = difficulty_simple_schema.dump(query).data
        return jsonify(result)


# difficulty complex
class DifficultyComplex(db.Model):
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
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.level = attr_list[3]
        self.lecture = attr_list[4]
        self.tutorial = attr_list[5]
        self.lab = attr_list[6]
        self.project = attr_list[7]
        self.preparation = attr_list[8]
        self.intercept = attr_list[9]

    def update(self, attr_list):
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.level = attr_list[3]
        self.lecture = attr_list[4]
        self.tutorial = attr_list[5]
        self.lab = attr_list[6]
        self.project = attr_list[7]
        self.preparation = attr_list[8]
        self.intercept = attr_list[9]


class DifficultyComplexSchema(ma.ModelSchema):
    class Meta:
        model = DifficultyComplex


difficulty_complex_schema = DifficultyComplexSchema(strict=True)


class DifficultyComplexResource(Resource):
    def get(self, module_code):
        query = DifficultyComplex.query.filter_by(code=module_code).first()
        result = difficulty_complex_schema.dump(query).data
        return jsonify(result)
