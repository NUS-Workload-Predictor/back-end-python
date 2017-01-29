#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/nusworks'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


@app.route('/')
def index():
    return 'Hello World!'


class AssignmentWorkload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)


class AssignmentWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = AssignmentWorkload


assignment_workload_schema = AssignmentWorkloadSchema(strict=True)


class AssignmentWorkloadResource(Resource):
    def get(self, module_code):
        assignment_workload_query = AssignmentWorkload.query.filter_by(code=module_code).first()
        result = assignment_workload_schema.dump(assignment_workload_query).data
        return result


api.add_resource(AssignmentWorkloadResource, '/workload/assignment/<string:module_code>')

db.create_all()

# # Workload
# @app.route('/workload/assignment/<module_code>', method=['GET'])
# def getAssignmentWorkloadParam(module_code):
#     return 'Test'
#
# @app.route('/workload/project/<module_code>', method=['GET'])
# def getProjectWorkloadParam(module_code):
#     return 'Test'
#
# @app.route('/workload/presentation/<module_code>', method=['GET'])
# def getPresentationWorkloadParam(module_code):
#     return 'Test'
#
# @app.route('/workload/reading/<module_code>', method=['GET'])
# def getReadingWorkloadParam(module_code):
#     return 'Test'
#
# @app.route('/workload/test/<module_code>', method=['GET'])
# def getTestWorkloadParam(module_code):
#     return 'Test'
#
# @app.route('/workload/exam/<module_code>', method=['GET'])
# def getExamWorkloadParam(module_code):
#     return 'Test'
#
# # Difficulty
# @app.route('/difficulty/assignment/<module_code>', method=['GET'])
# def getAssignmentDifficultyParam(module_code):
#     return 'Test'
#
# @app.route('/difficulty/project/<module_code>', method=['GET'])
# def getProjectDifficultyParam(module_code):
#     return 'Test'
#
# @app.route('/difficulty/presentation/<module_code>', method=['GET'])
# def getPresentationDifficultyParam(module_code):
#     return 'Test'
#
# @app.route('/difficulty/reading/<module_code>', method=['GET'])
# def getReadingDifficultyParam(module_code):
#     return 'Test'
#
# @app.route('/difficulty/test/<module_code>', method=['GET'])
# def getTestDifficultyParam(module_code):
#     return 'Test'
#
# @app.route('/difficulty/exam/<module_code>', method=['GET'])
# def getExamDifficultyParam(module_code):
#     return 'Test'

if __name__ == '__main__':
    app.run()
