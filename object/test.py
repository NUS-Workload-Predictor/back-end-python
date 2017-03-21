from common import db, ma
from flask import jsonify
from flask_restful import Resource


# test workload simple
class TestWorkloadSimple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.percentage = attr_list[0]
        self.coverage = attr_list[1]
        self.duration = attr_list[2]
        self.intercept = attr_list[3]

    def update(self, attr_list):
        self.percentage = attr_list[0]
        self.coverage = attr_list[1]
        self.duration = attr_list[2]
        self.intercept = attr_list[3]


class TestWorkloadSimpleSchema(ma.ModelSchema):
    class Meta:
        model = TestWorkloadSimple


test_workload_simple_schema = TestWorkloadSimpleSchema(strict=True)


class TestWorkloadSimpleResource(Resource):
    def get(self, module_code):
        query = TestWorkloadSimple.query.filter_by(code=module_code).first()
        result = test_workload_simple_schema.dump(query).data
        return jsonify(result)


# test workload complex
class TestWorkloadComplex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    intercept = db.Column(db.Float)

    def __init__(self, code, attr_list):
        self.code = code
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.percentage = attr_list[3]
        self.coverage = attr_list[4]
        self.duration = attr_list[5]
        self.intercept = attr_list[6]

    def update(self, attr_list):
        self.cap = attr_list[0]
        self.semesters = attr_list[1]
        self.credits = attr_list[2]
        self.percentage = attr_list[3]
        self.coverage = attr_list[4]
        self.duration = attr_list[5]
        self.intercept = attr_list[6]


class TestWorkloadComplexSchema(ma.ModelSchema):
    class Meta:
        model = TestWorkloadComplex


test_workload_complex_schema = TestWorkloadComplexSchema(strict=True)


class TestWorkloadComplexResource(Resource):
    def get(self, module_code):
        query = TestWorkloadComplex.query.filter_by(code=module_code).first()
        result = test_workload_complex_schema.dump(query).data
        return jsonify(result)
