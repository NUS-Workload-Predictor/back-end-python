from common import db, ma


# reading workload simple data
class ReadingWorkloadSimpleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.amount = attr_dict['amount']
        self.difficulty = attr_dict['difficulty']
        self.result = attr_dict['result']


class ReadingWorkloadSimpleDataSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkloadSimpleData


# reading workload complex data
class ReadingWorkloadComplexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    amount = db.Column(db.Float)
    difficulty = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.cap = attr_dict['cap']
        self.semesters = attr_dict['semesters']
        self.credits = attr_dict['credits']
        self.amount = attr_dict['amount']
        self.difficulty = attr_dict['difficulty']
        self.result = attr_dict['result']


class ReadingWorkloadComplexDataSchema(ma.ModelSchema):
    class Meta:
        model = ReadingWorkloadComplexData
