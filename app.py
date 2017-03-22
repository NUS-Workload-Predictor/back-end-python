#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from sklearn import linear_model
import re
import json
import warnings

from object.assignment import AssignmentWorkloadSimpleResource, AssignmentWorkloadComplexResource, AssignmentWorkloadSimple, AssignmentWorkloadComplex
from object.presentation import PresentationWorkloadSimpleResource, PresentationWorkloadComplexResource, PresentationWorkloadSimple, PresentationWorkloadComplex
from object.project import ProjectWorkloadSimpleResource, ProjectWorkloadComplexResource, ProjectWorkloadSimple, ProjectWorkloadComplex
from object.reading import ReadingWorkloadSimpleResource, ReadingWorkloadComplexResource, ReadingWorkloadSimple, ReadingWorkloadComplex
from object.test import TestWorkloadSimpleResource, TestWorkloadComplexResource, TestWorkloadSimple, TestWorkloadComplex
from object.exam import ExamWorkloadSimpleResource, ExamWorkloadComplexResource, ExamWorkloadSimple, ExamWorkloadComplex
from object.difficulty import DifficultySimpleResource, DifficultyComplexResource, DifficultySimple, DifficultyComplex

from data_object.assignment_data import AssignmentWorkloadSimpleDataSchema, AssignmentWorkloadComplexDataSchema, AssignmentWorkloadSimpleData, AssignmentWorkloadComplexData
from data_object.presentation_data import PresentationWorkloadSimpleDataSchema, PresentationWorkloadComplexDataSchema, PresentationWorkloadSimpleData, PresentationWorkloadComplexData
from data_object.project_data import ProjectWorkloadSimpleDataSchema, ProjectWorkloadComplexDataSchema, ProjectWorkloadSimpleData, ProjectWorkloadComplexData
from data_object.reading_data import ReadingWorkloadSimpleDataSchema, ReadingWorkloadComplexDataSchema, ReadingWorkloadSimpleData, ReadingWorkloadComplexData
from data_object.test_data import TestWorkloadSimpleDataSchema, TestWorkloadComplexDataSchema, TestWorkloadSimpleData, TestWorkloadComplexData
from data_object.exam_data import ExamWorkloadSimpleDataSchema, ExamWorkloadComplexDataSchema, ExamWorkloadSimpleData, ExamWorkloadComplexData
from data_object.difficulty_data import DifficultySimpleDataSchema, DifficultyComplexDataSchema, DifficultySimpleData, DifficultyComplexData

from common import db, ma

warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/nusworks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.app = app
db.init_app(app)
ma.app = app
ma.init_app(app)
api = Api(app)
CORS(app, origins='*')


@app.route('/')
def index():
    return 'Hello World!'

# simple
api.add_resource(AssignmentWorkloadSimpleResource, '/workload/assignment/simple/<string:module_code>')
api.add_resource(PresentationWorkloadSimpleResource, '/workload/presentation/simple/<string:module_code>')
api.add_resource(ProjectWorkloadSimpleResource, '/workload/project/simple/<string:module_code>')
api.add_resource(ReadingWorkloadSimpleResource, '/workload/reading/simple/<string:module_code>')
api.add_resource(TestWorkloadSimpleResource, '/workload/test/simple/<string:module_code>')
api.add_resource(ExamWorkloadSimpleResource, '/workload/exam/simple/<string:module_code>')
api.add_resource(DifficultySimpleResource, '/workload/difficulty/simple/<string:module_code>')

# complex
api.add_resource(AssignmentWorkloadComplexResource, '/workload/assignment/complex/<string:module_code>')
api.add_resource(PresentationWorkloadComplexResource, '/workload/presentation/complex/<string:module_code>')
api.add_resource(ProjectWorkloadComplexResource, '/workload/project/complex/<string:module_code>')
api.add_resource(ReadingWorkloadComplexResource, '/workload/reading/complex/<string:module_code>')
api.add_resource(TestWorkloadComplexResource, '/workload/test/complex/<string:module_code>')
api.add_resource(ExamWorkloadComplexResource, '/workload/exam/complex/<string:module_code>')
api.add_resource(DifficultyComplexResource, '/workload/difficulty/complex/<string:module_code>')

# data schema simple
assignment_workload_simple_data_schema = AssignmentWorkloadSimpleDataSchema(strict=True)
presentation_workload_simple_data_schema = PresentationWorkloadSimpleDataSchema(strict=True)
project_workload_simple_data_schema = ProjectWorkloadSimpleDataSchema(strict=True)
reading_workload_simple_data_schema = ReadingWorkloadSimpleDataSchema(strict=True)
test_workload_simple_data_schema = TestWorkloadSimpleDataSchema(strict=True)
exam_workload_simple_data_schema = ExamWorkloadSimpleDataSchema(strict=True)
difficulty_simple_data_schema = DifficultySimpleDataSchema(strict=True)

# data schema complex
assignment_workload_complex_data_schema = AssignmentWorkloadComplexDataSchema(strict=True)
presentation_workload_complex_data_schema = PresentationWorkloadComplexDataSchema(strict=True)
project_workload_complex_data_schema = ProjectWorkloadComplexDataSchema(strict=True)
reading_workload_complex_data_schema = ReadingWorkloadComplexDataSchema(strict=True)
test_workload_complex_data_schema = TestWorkloadComplexDataSchema(strict=True)
exam_workload_complex_data_schema = ExamWorkloadComplexDataSchema(strict=True)
difficulty_complex_data_schema = DifficultyComplexDataSchema(strict=True)


########################################################################################################################
########################################################################################################################


db.create_all()


class Train(Resource):
    attribute_dict = dict(
        assignment_simple=['time', 'percentage', 'coverage', 'people'],
        project_simple=['time', 'percentage', 'coverage', 'people'],
        presentation_simple=['time', 'percentage', 'coverage', 'people', 'duration'],
        reading_simple=['amount', 'difficulty'],
        exam_simple=['percentage', 'coverage', 'duration'],
        test_simple=['percentage', 'coverage', 'duration'],
        assignment_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people'],
        project_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people'],
        presentation_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people', 'duration'],
        reading_complex=['cap', 'semesters', 'credits', 'amount', 'difficulty'],
        exam_complex=['cap', 'semesters', 'credits', 'percentage', 'coverage', 'duration'],
        test_complex=['cap', 'semesters', 'credits', 'percentage', 'coverage', 'duration'],
        difficulty_simple=['level', 'mc', 'lecture', 'tutorial', 'lab', 'project', 'preparation'],
        difficulty_complex=['cap', 'semesters', 'credits', 'level', 'mc', 'lecture', 'tutorial', 'lab', 'project', 'preparation']
    )

    def post(self):
        self.train_assignment_workload_simple()
        self.train_presentation_workload_simple()
        self.train_project_workload_simple()
        self.train_reading_workload_simple()
        self.train_test_workload_simple()
        self.train_exam_workload_simple()
        self.train_difficulty_simple()

        self.train_assignment_workload_complex()
        self.train_presentation_workload_complex()
        self.train_project_workload_complex()
        self.train_reading_workload_complex()
        self.train_test_workload_complex()
        self.train_exam_workload_complex()
        self.train_difficulty_complex()

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

    def train_assignment_workload_simple(self):
        self.train(AssignmentWorkloadSimpleData, AssignmentWorkloadSimple, assignment_workload_simple_data_schema, 'assignment_simple')

        return 'assignment workload simple train success'

    def train_assignment_workload_complex(self):
        self.train(AssignmentWorkloadComplexData, AssignmentWorkloadComplex, assignment_workload_complex_data_schema, 'assignment_complex')

        return 'assignment workload complex train success'

    def train_presentation_workload_simple(self):
        self.train(PresentationWorkloadSimpleData, PresentationWorkloadSimple, presentation_workload_simple_data_schema, 'presentation_simple')

        return "presentation workload simple train success"

    def train_presentation_workload_complex(self):
        self.train(PresentationWorkloadComplexData, PresentationWorkloadComplex, presentation_workload_complex_data_schema, 'presentation_complex')

        return "presentation workload complex train success"

    def train_project_workload_simple(self):
        self.train(ProjectWorkloadSimpleData, ProjectWorkloadSimple, project_workload_simple_data_schema, 'project_simple')

        return "project workload simple train success"

    def train_project_workload_complex(self):
        self.train(ProjectWorkloadComplexData, ProjectWorkloadComplex, project_workload_complex_data_schema, 'project_complex')

        return "project workload complex train success"

    def train_reading_workload_simple(self):
        self.train(ReadingWorkloadSimpleData, ReadingWorkloadSimple, reading_workload_simple_data_schema, 'reading_simple')

        return "reading workload simple train success"

    def train_reading_workload_complex(self):
        self.train(ReadingWorkloadComplexData, ReadingWorkloadComplex, reading_workload_complex_data_schema, 'reading_complex')

        return "reading workload complex train success"

    def train_test_workload_simple(self):
        self.train(TestWorkloadSimpleData, TestWorkloadSimple, test_workload_simple_data_schema, 'test_simple')

        return "test workload simple train success"

    def train_test_workload_complex(self):
        self.train(TestWorkloadComplexData, TestWorkloadComplex, test_workload_complex_data_schema, 'test_complex')

        return "test workload complex train success"

    def train_exam_workload_simple(self):
        self.train(ExamWorkloadSimpleData, ExamWorkloadSimple, exam_workload_simple_data_schema, 'exam_simple')

        return "exam workload simple train success"

    def train_exam_workload_complex(self):
        self.train(ExamWorkloadComplexData, ExamWorkloadComplex, exam_workload_complex_data_schema, 'exam_complex')

        return "exam workload complex train success"

    def train_difficulty_simple(self):
        self.train(DifficultySimpleData, DifficultySimple, difficulty_simple_data_schema, 'difficulty_simple')

        return "difficulty simple train success"

    def train_difficulty_complex(self):
        self.train(DifficultyComplexData, DifficultyComplex, difficulty_complex_data_schema, 'difficulty_complex')

        return "difficulty complex train success"


api.add_resource(Train, '/train')


class Data(Resource):
    module_code_pattern = re.compile('^[a-z]{2,3}[0-9]{4}[a-z]?$')
    data_attribute_dict = dict(
        assignment_simple=['time', 'percentage', 'coverage', 'people', 'result'],
        project_simple=['time', 'percentage', 'coverage', 'people', 'result'],
        presentation_simple=['time', 'percentage', 'coverage', 'people', 'duration', 'result'],
        reading_simple=['amount', 'difficulty', 'result'],
        exam_simple=['percentage', 'coverage', 'duration', 'result'],
        test_simple=['percentage', 'coverage', 'duration', 'result'],
        assignment_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people', 'result'],
        project_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people', 'result'],
        presentation_complex=['cap', 'semesters', 'credits', 'time', 'percentage', 'coverage', 'people', 'duration', 'result'],
        reading_complex=['cap', 'semesters', 'credits', 'amount', 'difficulty', 'result'],
        exam_complex=['cap', 'semesters', 'credits', 'percentage', 'coverage', 'duration', 'result'],
        test_complex=['cap', 'semesters', 'credits', 'percentage', 'coverage', 'duration', 'result'],
        difficulty_simple=['level', 'mc', 'lecture', 'tutorial', 'lab', 'project', 'preparation', 'result'],
        difficulty_complex=['cap', 'semesters', 'credits', 'level', 'mc', 'lecture', 'tutorial', 'lab', 'project', 'preparation', 'result']
    )

    def get(self, category, assessment, module_code):
        module_code = module_code.lower()

        if category != 'simple' and category != 'complex':
            return 'error category'

        if assessment != 'assignment' and assessment != 'project' and assessment != 'presentation' \
                and assessment != 'reading' and assessment != 'test' and assessment != 'exam' and assessment != 'difficulty':
            return 'error type'

        if not self.module_code_pattern.match(module_code):
            return 'error module code'

        if assessment == 'assignment':
            if category == 'simple':
                result = self.get_assignment_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_assignment_workload_complex_data(module_code)
        elif assessment == 'project':
            if category == 'simple':
                result = self.get_project_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_project_workload_complex_data(module_code)
        elif assessment == 'presentation':
            if category == 'simple':
                result = self.get_presentation_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_presentation_workload_complex_data(module_code)
        elif assessment == 'reading':
            if category == 'simple':
                result = self.get_reading_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_reading_workload_complex_data(module_code)
        elif assessment == 'test':
            if category == 'simple':
                result = self.get_test_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_test_workload_complex_data(module_code)
        elif assessment == 'exam':
            if category == 'simple':
                result = self.get_exam_workload_simple_data(module_code)
            elif category == 'complex':
                result = self.get_exam_workload_complex_data(module_code)
        elif assessment == 'difficulty':
            if category == 'simple':
                result = self.get_difficulty_simple_data(module_code)
            elif category == 'complex':
                result = self.get_difficulty_complex_data(module_code)

        result = list(map(lambda x: x.as_dict(), result))
        return jsonify(result)

    def post(self, category, assessment, module_code):
        module_code = module_code.lower()

        if category != 'simple' and category != 'complex':
            return 'error category'

        if assessment != 'assignment' and assessment != 'project' and assessment != 'presentation' \
                and assessment != 'reading' and assessment != 'test' and assessment != 'exam' and assessment != 'difficulty':
            return 'error type'

        if not self.module_code_pattern.match(module_code):
            return 'error module code'

        if assessment == 'assignment':
            if category == 'simple':
                result = self.update_assignment_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_assignment_workload_complex_data(module_code, request.form)
        elif assessment == 'project':
            if category == 'simple':
                result = self.update_project_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_project_workload_complex_data(module_code, request.form)
        elif assessment == 'presentation':
            if category == 'simple':
                result = self.update_presentation_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_presentation_workload_complex_data(module_code, request.form)
        elif assessment == 'reading':
            if category == 'simple':
                result = self.update_reading_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_reading_workload_complex_data(module_code, request.form)
        elif assessment == 'test':
            if category == 'simple':
                result = self.update_test_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_test_workload_complex_data(module_code, request.form)
        elif assessment == 'exam':
            if category == 'simple':
                result = self.update_exam_workload_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_exam_workload_complex_data(module_code, request.form)
        elif assessment == 'difficulty':
            if category == 'simple':
                result = self.update_difficulty_simple_data(module_code, request.form)
            elif category == 'complex':
                result = self.update_difficulty_complex_data(module_code, request.form)

        return jsonify(result)

    def get_data(self, data_model, module_code):
        return data_model.query.filter_by(code=module_code).all()

    def update_data(self, data_model, assessment, module_code, data):
        for attr in self.data_attribute_dict[assessment]:
            if attr not in data:
                return 'missing attribute'

        data_m = data_model(module_code, data)
        db.session.add(data_m)
        db.session.commit()

        return 'update ' + assessment + ' for ' + module_code + ' success'

    # get
    def get_assignment_workload_simple_data(self, module_code):
        return self.get_data(AssignmentWorkloadSimpleData, module_code)

    def get_assignment_workload_complex_data(self, module_code):
        return self.get_data(AssignmentWorkloadComplexData, module_code)

    def get_project_workload_simple_data(self, module_code):
        return self.get_data(ProjectWorkloadSimpleData, module_code)

    def get_project_workload_complex_data(self, module_code):
        return self.get_data(ProjectWorkloadComplexData, module_code)

    def get_presentation_workload_simple_data(self, module_code):
        return self.get_data(PresentationWorkloadSimpleData, module_code)

    def get_presentation_workload_complex_data(self, module_code):
        return self.get_data(PresentationWorkloadComplexData, module_code)

    def get_reading_workload_simple_data(self, module_code):
        return self.get_data(ReadingWorkloadSimpleData, module_code)

    def get_reading_workload_complex_data(self, module_code):
        return self.get_data(ReadingWorkloadComplexData, module_code)

    def get_test_workload_simple_data(self, module_code):
        return self.get_data(TestWorkloadSimpleData, module_code)

    def get_test_workload_complex_data(self, module_code):
        return self.get_data(TestWorkloadComplexData, module_code)

    def get_exam_workload_simple_data(self, module_code):
        return self.get_data(ExamWorkloadSimpleData, module_code)

    def get_exam_workload_complex_data(self, module_code):
        return self.get_data(ExamWorkloadComplexData, module_code)

    def get_difficulty_simple_data(self, module_code):
        return self.get_data(DifficultySimpleData, module_code)

    def get_difficulty_complex_data(self, module_code):
        return self.get_data(DifficultyComplexData, module_code)

    # update
    def update_assignment_workload_simple_data(self, module_code, data):
        return self.update_data(AssignmentWorkloadSimpleData, 'assignment_simple', module_code, data)

    def update_assignment_workload_complex_data(self, module_code, data):
        return self.update_data(AssignmentWorkloadComplexData, 'assignment_complex', module_code, data)

    def update_project_workload_simple_data(self, module_code, data):
        return self.update_data(ProjectWorkloadSimpleData, 'project_simple', module_code, data)

    def update_project_workload_complex_data(self, module_code, data):
        return self.update_data(ProjectWorkloadComplexData, 'project_complex', module_code, data)

    def update_presentation_workload_simple_data(self, module_code, data):
        return self.update_data(PresentationWorkloadSimpleData, 'presentation_simple', module_code, data)

    def update_presentation_workload_complex_data(self, module_code, data):
        return self.update_data(PresentationWorkloadComplexData, 'presentation_complex', module_code, data)

    def update_reading_workload_simple_data(self, module_code, data):
        return self.update_data(ReadingWorkloadSimpleData, 'reading_simple', module_code, data)

    def update_reading_workload_complex_data(self, module_code, data):
        return self.update_data(ReadingWorkloadComplexData, 'reading_complex', module_code, data)

    def update_test_workload_simple_data(self, module_code, data):
        return self.update_data(TestWorkloadSimpleData, 'test_simple', module_code, data)

    def update_test_workload_complex_data(self, module_code, data):
        return self.update_data(TestWorkloadComplexData, 'test_complex', module_code, data)

    def update_exam_workload_simple_data(self, module_code, data):
        return self.update_data(ExamWorkloadSimpleData, 'exam_simple', module_code, data)

    def update_exam_workload_complex_data(self, module_code, data):
        return self.update_data(ExamWorkloadComplexData, 'exam_complex', module_code, data)

    def update_difficulty_simple_data(self, module_code, data):
        return self.update_data(DifficultySimpleData, 'difficulty_simple', module_code, data)

    def update_difficulty_complex_data(self, module_code, data):
        return self.update_data(DifficultyComplexData, 'difficulty_complex', module_code, data)


api.add_resource(Data, '/data/<string:category>/<string:assessment>/<string:module_code>')

if __name__ == '__main__':
    app.run()
