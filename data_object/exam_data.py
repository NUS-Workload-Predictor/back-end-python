from common import db, ma


# exam workload simple data
class ExamWorkloadSimpleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.duration = attr_dict['duration']
        self.result = attr_dict['result']


class ExamWorkloadSimpleDataSchema(ma.ModelSchema):
    class Meta:
        model = ExamWorkloadSimpleData


# exam workload complex data
class ExamWorkloadComplexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    duration = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.cap = attr_dict['cap']
        self.semesters = attr_dict['semesters']
        self.credits = attr_dict['credits']
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.duration = attr_dict['duration']
        self.result = attr_dict['result']


class ExamWorkloadComplexDataSchema(ma.ModelSchema):
    class Meta:
        model = ExamWorkloadComplexData

