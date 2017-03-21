from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource


db = SQLAlchemy()
ma = Marshmallow()


# reading workload simple
class ReadingWorkloadSimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.amount = attr_list[0]
        self.difficulty = attr_list[1]
        self.intercept = attr_list[2]

    def update(self, attr_list):
        self.amount = attr_list[0]
        self.difficulty = attr_list[1]
        self.intercept = attr_list[2]


class ReadingWorkloadSimpleSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkloadSimple


reading_workload_simple_schema = ReadingWorkloadSimpleSchema(strict=True)


class ReadingWorkloadSimpleResource(Resource):
    def get(self, module_code):
        query = ReadingWorkloadSimple.query.filter_by(code=module_code).first()
        result = reading_workload_simple_schema.dump(query).data
        return jsonify(result)


# reading workload complex
class ReadingWorkloadComplex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.amount = attr_list[3]
        self.difficulty = attr_list[4]
        self.intercept = attr_list[5]

    def update(self, attr_list):
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.amount = attr_list[3]
        self.difficulty = attr_list[4]
        self.intercept = attr_list[5]


class ReadingWorkloadComplexSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkloadComplex


reading_workload_complex_schema = ReadingWorkloadComplexSchema(strict=True)


class ReadingWorkloadComplexResource(Resource):
    def get(self, module_code):
        query = ReadingWorkloadComplex.query.filter_by(code=module_code).first()
        result = reading_workload_complex_schema.dump(query).data
        return jsonify(result)

