#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
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
    attribute_dict = dict(assignment=['time', 'percentage', 'coverage', 'people'],
                          project=['time', 'percentage', 'coverage', 'people'],
                          presentation=['time', 'percentage', 'coverage', 'people', 'duration'],
                          reading=['amount', 'difficulty'],
                          exam=['percentage', 'coverage', 'duration'],
                          test=['percentage', 'coverage', 'duration'])

    def get(self):
        self.train_assignment_workload()

    def train(self, data_model, model, data_schema, category):
        data_query = data_model.query.order_by(data_model.code.asc()).all()

        if not data_query:
            return

        result = data_schema.dump(data_query, many=True).data
        current_module = result[0]['code']
        param_list = []
        value_list = []
        linear_regression_model = linear_model.LinearRegression()
        for row in result:
            if row['code'] == current_module:
                attr_list = []
                for attr in self.attribute_dict[category]:
                    attr_list.append(row[attr])
                param_list.append(attr_list)
                value_list.append(row['result'])
            else:
                linear_regression_model.fit(param_list, value_list)
                m = model.query.filter_by(code=current_module).first()
                temp_list = []
                for coefficient in linear_regression_model.coef_:
                    temp_list.append(coefficient.item())
                temp_list.append(linear_regression_model.intercept_.item())
                if not m:
                    m = model(current_module, temp_list)
                    db.session.add(m)
                else:
                    m.update(temp_list)

                db.session.commit()

                current_module = row['code']
                param_list = []
                value_list = []
                linear_regression_model = linear_model.LinearRegression()
                attr_list = []
                for attr in self.attribute_dict[category]:
                    attr_list.append(row[attr])
                param_list.append(attr_list)
                value_list.append(row['result'])

        linear_regression_model.fit(param_list, value_list)
        m = model.query.filter_by(code=current_module).first()
        temp_list = []
        for coefficient in linear_regression_model.coef_:
            temp_list.append(coefficient.item())
        temp_list.append(linear_regression_model.intercept_.item())
        if not m:
            m = model(current_module, temp_list)
            db.session.add(m)
        else:
            m.update(temp_list)

        db.session.commit()

    def train_assignment_workload(self):
        self.train(AssignmentWorkloadData, AssignmentWorkload, assignment_workload_data_schema, 'assignment')

        return 'assignment workload train success'

    def train_assignment_difficulty(self):
        return "assignment difficulty train success"

    def train_presentation_workload(self):
        return "presentation workload train success"

    def train_presentation_difficulty(self):
        return "presentation difficulty train success"

    def train_project_workload(self):
        return "project workload train success"

    def train_project_difficulty(self):
        return "project difficulty train success"

    def train_reading_workload(self):
        return "reading workload train success"

    def train_reading_difficulty(self):
        return "reading difficulty train success"

    def train_test_workload(self):
        return "test workload train success"

    def train_test_difficulty(self):
        return "test difficulty train success"

    def train_exam_workload(self):
        return "exam workload train success"

    def train_exam_difficulty(self):
        return "exam difficulty train success"


api.add_resource(Train, '/train')


if __name__ == '__main__':
    app.run()
