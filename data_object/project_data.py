from common import db, ma


# project workload simple data
class ProjectWorkloadSimpleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.time = attr_dict['time']
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.people = attr_dict['people']
        self.result = attr_dict['result']

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ProjectWorkloadSimpleDataSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkloadSimpleData


# project workload complex data
class ProjectWorkloadComplexData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    cap = db.Column(db.Float)
    semesters = db.Column(db.Float)
    credits = db.Column(db.Float)
    time = db.Column(db.Float)
    percentage = db.Column(db.Float)
    coverage = db.Column(db.Float)
    people = db.Column(db.Float)
    result = db.Column(db.Float)

    def __init__(self, code, attr_dict):
        self.code = code
        self.cap = attr_dict['cap']
        self.semesters = attr_dict['semesters']
        self.credits = attr_dict['credits']
        self.time = attr_dict['time']
        self.percentage = attr_dict['percentage']
        self.coverage = attr_dict['coverage']
        self.people = attr_dict['people']
        self.result = attr_dict['result']

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ProjectWorkloadComplexDataSchema(ma.ModelSchema):
    class Meta:
        model = ProjectWorkloadComplexData

