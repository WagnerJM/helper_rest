from app.database import db, BaseMixin
from sqlalchemy.dialects.postgresql import JSON

class Lebenslauf(BaseMixin, db.Model):
    __tablename__ = 'lebenslauf'

    lebenslaufID = db.Column(db.Integer, primary_key=True)
    taetigkeiten = db.relationship('Taetigkeit', backref='Lebenslauf', lazy=False)
    fortbildungen = db.relationship('Fortbildung', backref='Lebenslauf', lazy=False)
    qualifikationen = db.relationship('Qualifikation', backref='Lebenslauf', lazy=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'))


    def json(self):
        return {
            "id": str(self.id),
            "taetigkeiten": [ t.json for t in self.taetigkeiten ],
            "fortbildungen": [ f.json for t in self.fortbildungen ],
            "qualifikationen": [ q.json for t in self.qualifikationen ],

        }
    
    
class Taetigkeit(BaseMixin, db.Model):
    __tablename__ = 'taetigkeit'

    taetigkeitID = db.Column(db.Integer, primary_key=True)
    lebenslauf_id = db.Column(db.Integer, db.ForeignKey('lebenslauf.lebenslaufID'))
    t_von = db.Column(db.String)
    t_bis = db.Column(db.String)
    t_bezeichnung = db.Column(db.String)
    t_beschreibung db.Column(db.Text)

    def __init__(self, von, bis, bezeich, beschreib):
        self.t_von = von
        self.t_bis = bis
        self.t_bezeichnung = bezeich
        self.t_beschreibung = beschreib

    def json(self):
        return {
            "id": str(self.id),
            "t_von": self.t_von,
            "t-bis": self.t-bis,
            "t_bezeichung": self.t_bezeichung,
            "t_beschreibung": self.t_beschreibung
        }

class Fortbildung(BaseMixin, db.Model):
    __tablename__ = 'fortbildung'

    fortbildungID = db.Column(db.Integer, primary_key=True)
    lebenslauf_id = db.Column(db.Integer, db.ForeignKey('lebenlauf.lebenslaufID'))
    f_datum = db.Column(db.String)
    f_bezeichung = db.Column(db.String)

    def __init__(self, datum, bezeichnung):
        self.f_datum = datum
        self.f_bezeichung = bezeichnung

    def json(self):
        return {
            "id": str(self.id),
            "f_datum": self.f_datum,
            "f_bezeichung": self.f_bezeichung
        }

class Qualifikation(BaseMixin, db.Model):
    __tablename__ = 'qualifikation'

    qualiID = db.Column(db.Integer, primary_key=True)
    lebenslauf_id = db.Column(db.Integer, db.ForeignKey('lebenlauf.lebenslaufID'))
    q_von = db.Column(db.String)
    q_bis = db.Column(db.String)
    q_bezeichung = db.Column(db.String)
    q_note = db.Column(db.Float)
    q_anmerkung = db.Column(db.Text)

    def __init__(self, von, bis, bezeichnung):
        self.q_von = von
        self.q_bis = bis
        self.q_bezeichung = bezeichnung

    def json(self):
        return {
            "id": str(self.id),
            "q_von": self.q_von,
            "q_bis": self.q_bis,
            "q_bezeichung": self.q_bezeichung,
            "q_note": self.q_note,
            "q_anmerkung": self.q_anmerkung
        }



    