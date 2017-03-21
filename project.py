from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource


db = SQLAlchemy()
ma = Marshmallow()


# project workload simple
class ProjectWorkloadSimple(db.Model):
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


class ProjectWorkloadSimpleSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkloadSimple


project_workload_simple_schema = ProjectWorkloadSimpleSchema(strict=True)


class ProjectWorkloadSimpleResource(Resource):
    def get(self, module_code):
        query = ProjectWorkloadSimple.query.filter_by(code=module_code).first()
        result = project_workload_simple_schema.dump(query).data
        return jsonify(result)


# project workload complex
class ProjectWorkloadComplex(db.Model):
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


class ProjectWorkloadComplexSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkloadComplex


project_workload_complex_schema = ProjectWorkloadComplexSchema(strict=True)


class ProjectWorkloadComplexResource(Resource):
    def get(self, module_code):
        query = ProjectWorkloadComplex.query.filter_by(code=module_code).first()
        result = project_workload_complex_schema.dump(query).data
        return jsonify(result)
