#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import numpy
import scipy
from sklearn import linear_model

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
    intercept = db.Column(db.Float)

    def __init__(self, code, time, percentage, coverage, people, intercept):
        self.code = code
        self.time = time
        self.percentage = percentage
        self.coverage = coverage
        self.people = people
        self.intercept = intercept


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


class AssignmentDifficulty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    intercept = db.Column(db.Float)


class AssignmentDifficultySchema(ma.ModelSchema):
    class Meta:
        model = AssignmentDifficulty


assignment_difficulty_schema = AssignmentDifficultySchema(strict=True)


class AssignmentDifficultyResource(Resource):
    def get(self, module_code):
        assignment_difficulty_query = AssignmentDifficulty.query.filter_by(code=module_code).first()
        result = assignment_difficulty_schema.dump(assignment_difficulty_query).data
        return result


api.add_resource(AssignmentDifficultyResource, '/difficulty/assignment/<string:module_code>')


class AssignmentWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)


class AssignmentWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = AssignmentWorkloadData


assignment_workload_data_schema = AssignmentWorkloadDataSchema(strict=True)


class AssignmentDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)


class AssignmentDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = AssignmentDifficultyData


assignment_difficulty_data_schema = AssignmentDifficultyDataSchema(strict=True)


db.create_all()


class Train(Resource):
    def get(self):
        assignment_workload_data_query = AssignmentWorkloadData.query.order_by(AssignmentWorkloadData.code.asc()).all()

        if not assignment_workload_data_query:
            return

        result = assignment_workload_data_schema.dump(assignment_workload_data_query, many=True).data
        current_module = result[0]['code']
        param_list = []
        value_list = []
        model = linear_model.LinearRegression()
        for row in result:
            if row['code'] == current_module:
                param_list.append([row['time'], row['percentage'], row['coverage'], row['people']])
                value_list.append(row['result'])
            else:
                model.fit(param_list, value_list)
                a = AssignmentWorkload.query.filter_by(code=current_module).first()
                if not a:
                    assignment_workload = AssignmentWorkload(current_module, model.coef_[0].item(),
                                                             model.coef_[1].item(), model.coef_[2].item(),
                                                             model.coef_[3].item(), model.intercept_.item())
                    db.session.add(assignment_workload)
                else:
                    a.time = model.coef_[0].item()
                    a.percentage = model.coef_[1].item()
                    a.coverage = model.coef_[2].item()
                    a.people = model.coef_[3].item()
                    a.intercept = model.intercept_.item()

                db.session.commit()

                current_module = row['code']
                param_list = []
                value_list = []
                model = linear_model.LinearRegression()
                param_list.append([row['time'], row['percentage'], row['coverage'], row['people']])
                value_list.append(row['result'])

        model.fit(param_list, value_list)
        a = AssignmentWorkload.query.filter_by(code=current_module).first()
        if not a:
            assignment_workload = AssignmentWorkload(current_module, model.coef_[0].item(), model.coef_[1].item(),
                                                     model.coef_[2].item(), model.coef_[3].item(),
                                                     model.intercept_.item())
            db.session.add(assignment_workload)
        else:
            a.time = model.coef_[0].item()
            a.percentage = model.coef_[1].item()
            a.coverage = model.coef_[2].item()
            a.people = model.coef_[3].item()
            a.intercept = model.intercept_.item()

        db.session.commit()

        return result


api.add_resource(Train, '/train')


if __name__ == '__main__':
    app.run()
