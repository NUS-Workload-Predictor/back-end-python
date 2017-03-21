from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource


db = SQLAlchemy()
ma = Marshmallow()


# presentation workload simple
class PresentationWorkloadSimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.time = attr_list[0]
        self.percentage = attr_list[1]
        self.coverage = attr_list[2]
        self.people = attr_list[3]
        self.duration = attr_list[4]
        self.intercept = attr_list[5]

    def update(self, attr_list):
        self.time = attr_list[0]
        self.percentage = attr_list[1]
        self.coverage = attr_list[2]
        self.people = attr_list[3]
        self.duration = attr_list[4]
        self.intercept = attr_list[5]


class PresentationWorkloadSimpleSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkloadSimple


presentation_workload_simple_schema = PresentationWorkloadSimpleSchema(strict=True)


class PresentationWorkloadSimpleResource(Resource):
    def get(self, module_code):
        query = PresentationWorkloadSimple.query.filter_by(code=module_code).first()
        result = presentation_workload_simple_schema.dump(query).data
        return jsonify(result)


# presentation workload complex
class PresentationWorkloadComplex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.time = attr_list[3]
        self.percentage = attr_list[4]
        self.coverage = attr_list[5]
        self.people = attr_list[6]
        self.duration = attr_list[7]
        self.intercept = attr_list[8]

    def update(self, attr_list):
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.time = attr_list[3]
        self.percentage = attr_list[4]
        self.coverage = attr_list[5]
        self.people = attr_list[6]
        self.duration = attr_list[7]
        self.intercept = attr_list[8]


class PresentationWorkloadComplexSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkloadComplex


presentation_workload_complex_schema = PresentationWorkloadComplexSchema(strict=True)


class PresentationWorkloadComplexResource(Resource):
    def get(self, module_code):
        query = PresentationWorkloadComplex.query.filter_by(code=module_code).first()
        result = presentation_workload_complex_schema.dump(query).data
        return jsonify(result)
