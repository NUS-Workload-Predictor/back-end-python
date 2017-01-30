#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from sklearn import linear_model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/nusworks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


@app.route('/')
def index():
    return 'Hello World!'


# assignment workload
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


# assignment difficulty
class AssignmentDifficulty(db.Model):
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


# assignment workload data
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


# assignment difficulty data
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


########################################################################################################################
########################################################################################################################

# project workload
class ProjectWorkload(db.Model):
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


class ProjectWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkload


project_workload_schema = ProjectWorkloadSchema(strict=True)


class ProjectWorkloadResource(Resource):
    def get(self, module_code):
        project_workload_query = ProjectWorkload.query.filter_by(code=module_code).first()
        result = project_workload_schema.dump(project_workload_query).data
        return result


api.add_resource(ProjectWorkloadResource, '/workload/project/<string:module_code>')


# project difficulty
class ProjectDifficulty(db.Model):
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


class ProjectDifficultySchema(ma.ModelSchema):
    class Meta:
        model = ProjectDifficulty


project_difficulty_schema = ProjectDifficultySchema(strict=True)


class ProjectDifficultyResource(Resource):
    def get(self, module_code):
        project_difficulty_query = ProjectDifficulty.query.filter_by(code=module_code).first()
        result = project_difficulty_schema.dump(project_difficulty_query).data
        return result


api.add_resource(ProjectDifficultyResource, '/difficulty/project/<string:module_code>')


# project workload data
class ProjectWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)


class ProjectWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkloadData


project_workload_data_schema = ProjectWorkloadDataSchema(strict=True)


# project difficulty data
class ProjectDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)


class ProjectDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = ProjectDifficultyData


project_difficulty_data_schema = ProjectDifficultyDataSchema(strict=True)


########################################################################################################################
########################################################################################################################

# presentation workload
class PresentationWorkload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
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


class PresentationWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkload


presentation_workload_schema = PresentationWorkloadSchema(strict=True)


class PresentationWorkloadResource(Resource):
    def get(self, module_code):
        presentation_workload_query = PresentationWorkload.query.filter_by(code=module_code).first()
        result = presentation_workload_schema.dump(presentation_workload_query).data
        return result


api.add_resource(PresentationWorkloadResource, '/workload/presentation/<string:module_code>')


# presentation difficulty
class PresentationDifficulty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
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


class PresentationDifficultySchema(ma.ModelSchema):
    class Meta:
        model = PresentationDifficulty


presentation_difficulty_schema = PresentationDifficultySchema(strict=True)


class PresentationDifficultyResource(Resource):
    def get(self, module_code):
        presentation_difficulty_query = PresentationDifficulty.query.filter_by(code=module_code).first()
        result = presentation_difficulty_schema.dump(presentation_difficulty_query).data
        return result


api.add_resource(PresentationDifficultyResource, '/difficulty/presentation/<string:module_code>')


# presentation workload data
class PresentationWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class PresentationWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = PresentationWorkloadData


presentation_workload_data_schema = PresentationWorkloadDataSchema(strict=True)


# presentation difficulty data
class PresentationDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class PresentationDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = PresentationDifficultyData


presentation_difficulty_data_schema = PresentationDifficultyDataSchema(strict=True)


########################################################################################################################
########################################################################################################################

# reading workload
class ReadingWorkload(db.Model):
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


class ReadingWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkload


reading_workload_schema = ReadingWorkloadSchema(strict=True)


class ReadingWorkloadResource(Resource):
    def get(self, module_code):
        reading_workload_query = ReadingWorkload.query.filter_by(code=module_code).first()
        result = reading_workload_schema.dump(reading_workload_query).data
        return result


api.add_resource(ReadingWorkloadResource, '/workload/reading/<string:module_code>')


# reading difficulty
class ReadingDifficulty(db.Model):
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


class ReadingDifficultySchema(ma.ModelSchema):
    class Meta:
        model = ReadingDifficulty


reading_difficulty_schema = ReadingDifficultySchema(strict=True)


class ReadingDifficultyResource(Resource):
    def get(self, module_code):
        reading_difficulty_query = ReadingDifficulty.query.filter_by(code=module_code).first()
        result = reading_difficulty_schema.dump(reading_difficulty_query).data
        return result


api.add_resource(ReadingDifficultyResource, '/difficulty/reading/<string:module_code>')


# reading workload data
class ReadingWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    result = db.Column(db.Float)


class ReadingWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkloadData


reading_workload_data_schema = ReadingWorkloadDataSchema(strict=True)


# reading difficulty data
class ReadingDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    result = db.Column(db.Float)


class ReadingDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = ReadingDifficultyData


reading_difficulty_data_schema = ReadingDifficultyDataSchema(strict=True)


########################################################################################################################
########################################################################################################################

# test workload
class TestWorkload(db.Model):
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


class TestWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = TestWorkload


test_workload_schema = TestWorkloadSchema(strict=True)


class TestWorkloadResource(Resource):
    def get(self, module_code):
        test_workload_query = TestWorkload.query.filter_by(code=module_code).first()
        result = test_workload_schema.dump(test_workload_query).data
        return result


api.add_resource(TestWorkloadResource, '/workload/test/<string:module_code>')


# test difficulty
class TestDifficulty(db.Model):
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


class TestDifficultySchema(ma.ModelSchema):
    class Meta:
        model = TestDifficulty


test_difficulty_schema = TestDifficultySchema(strict=True)


class TestDifficultyResource(Resource):
    def get(self, module_code):
        test_difficulty_query = TestDifficulty.query.filter_by(code=module_code).first()
        result = test_difficulty_schema.dump(test_difficulty_query).data
        return result


api.add_resource(TestDifficultyResource, '/difficulty/test/<string:module_code>')


# test workload data
class TestWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class TestWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = TestWorkloadData


test_workload_data_schema = TestWorkloadDataSchema(strict=True)


# test difficulty data
class TestDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class TestDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = TestDifficultyData


test_difficulty_data_schema = TestDifficultyDataSchema(strict=True)


########################################################################################################################
########################################################################################################################

# exam workload
class ExamWorkload(db.Model):
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


class ExamWorkloadSchema(ma.ModelSchema):
    class Meta:
        model = ExamWorkload


exam_workload_schema = ExamWorkloadSchema(strict=True)


class ExamWorkloadResource(Resource):
    def get(self, module_code):
        exam_workload_query = ExamWorkload.query.filter_by(code=module_code).first()
        result = exam_workload_schema.dump(exam_workload_query).data
        return result


api.add_resource(ExamWorkloadResource, '/workload/exam/<string:module_code>')


# exam difficulty
class ExamDifficulty(db.Model):
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


class ExamDifficultySchema(ma.ModelSchema):
    class Meta:
        model = ExamDifficulty


exam_difficulty_schema = ExamDifficultySchema(strict=True)


class ExamDifficultyResource(Resource):
    def get(self, module_code):
        exam_difficulty_query = ExamDifficulty.query.filter_by(code=module_code).first()
        result = exam_difficulty_schema.dump(exam_difficulty_query).data
        return result


api.add_resource(ExamDifficultyResource, '/difficulty/exam/<string:module_code>')


# exam workload data
class ExamWorkloadData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class ExamWorkloadDataSchema(ma.ModelSchema):
    class Meta:
        model = ExamWorkloadData


exam_workload_data_schema = ExamWorkloadDataSchema(strict=True)


# exam difficulty data
class ExamDifficultyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)


class ExamDifficultyDataSchema(ma.ModelSchema):
    class Meta:
        model = ExamDifficultyData


exam_difficulty_data_schema = ExamDifficultyDataSchema(strict=True)


########################################################################################################################
########################################################################################################################


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
        self.train(AssignmentDifficultyData, AssignmentDifficulty, assignment_difficulty_data_schema, 'assignment')

        return "assignment difficulty train success"

    def train_presentation_workload(self):
        self.train(PresentationWorkloadData, PresentationWorkload, presentation_workload_data_schema, 'presentation')

        return "presentation workload train success"

    def train_presentation_difficulty(self):
        self.train(PresentationDifficultyData, PresentationDifficulty, presentation_difficulty_data_schema, 'presentation')

        return "presentation difficulty train success"

    def train_project_workload(self):
        self.train(ProjectWorkloadData, ProjectWorkload, project_workload_data_schema, 'project')

        return "project workload train success"

    def train_project_difficulty(self):
        self.train(ProjectDifficultyData, ProjectDifficulty, project_difficulty_data_schema, 'project')

        return "project difficulty train success"

    def train_reading_workload(self):
        self.train(ReadingWorkloadData, ReadingWorkload, reading_workload_data_schema, 'reading')

        return "reading workload train success"

    def train_reading_difficulty(self):
        self.train(ReadingDifficultyData, ReadingDifficulty, reading_difficulty_data_schema, 'reading')

        return "reading difficulty train success"

    def train_test_workload(self):
        self.train(TestWorkloadData, TestWorkload, test_workload_data_schema, 'test')

        return "test workload train success"

    def train_test_difficulty(self):
        self.train(TestDifficultyData, TestDifficulty, test_difficulty_data_schema, 'test')

        return "test difficulty train success"

    def train_exam_workload(self):
        self.train(ExamWorkloadData, ExamWorkload, exam_workload_data_schema, 'exam')

        return "exam workload train success"

    def train_exam_difficulty(self):
        self.train(ExamDifficultyData, ExamDifficulty, exam_difficulty_data_schema, 'exam')

        return "exam difficulty train success"


api.add_resource(Train, '/train')


if __name__ == '__main__':
    app.run()
