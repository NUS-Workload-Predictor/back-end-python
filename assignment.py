from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource


db = SQLAlchemy()
ma = Marshmallow()


# assignment workload simple
class AssignmentWorkloadSimple(db.Model):
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
        self.intercept = attr_list[4]

    def update(self, attr_list):
        self.time = attr_list[0]
        self.percentage = attr_list[1]
        self.coverage = attr_list[2]
        self.people = attr_list[3]
        self.intercept = attr_list[4]


class AssignmentWorkloadSimpleSchema(ma.ModelSchema):
    class Meta:
        model = AssignmentWorkloadSimple


assignment_workload_simple_schema = AssignmentWorkloadSimpleSchema(strict=True)


class AssignmentWorkloadSimpleResource(Resource):
    def get(self, module_code):
        query = AssignmentWorkloadSimple.query.filter_by(code=module_code.lower()).first()
        result = assignment_workload_simple_schema.dump(query).data
        return jsonify(result)


# assignment workload complex
class AssignmentWorkloadComplex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
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
        self.intercept = attr_list[7]

    def update(self, attr_list):
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.time = attr_list[3]
        self.percentage = attr_list[4]
        self.coverage = attr_list[5]
        self.people = attr_list[6]
        self.intercept = attr_list[7]


class AssignmentWorkloadComplexSchema(ma.ModelSchema):
    class Meta:
        model = AssignmentWorkloadComplex


assignment_workload_complex_schema = AssignmentWorkloadComplexSchema(strict=True)


class AssignmentWorkloadComplexResource(Resource):
    def get(self, module_code):
        query = AssignmentWorkloadComplex.query.filter_by(code=module_code.lower()).first()
        result = assignment_workload_complex_schema.dump(query).data
        return jsonify(result)
