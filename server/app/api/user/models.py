import bcrypt
from app.database import BaseMixin, db
from sqlalchemy.dialects.postgresql import JSON
from app.api.lebenslauf.models import Lebenslauf


class User(BaseMixin, db.Model):

    __tablename__ = 'users'

    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    _password = db.Column(db.Binary(60))

    vorname = db.Column(db.String)
    nachname = db.Column(db.String)

    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    profil = db.relationship('Profile', backref='User', lazy=False)
    email_setting = db.relationship('EmailSetting', backref='User', lazy=False)
    lebenslauf = db.relationship('Lebenslauf', backref='User', lazy=False)


    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_pw(password).encode('utf-8')


    def _hash_pw(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt(16))

    def check_pw(self, password, hashed_pw):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pw)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def json(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "is_admin": self.is_admin,
            "profil": [ p.json() for p in self.profil ],
            "email_setting": [ email.json() for email in self.email_setting ]

        }
    
class Profil(BaseMixin, db.Model):
    __tablename__ = 'profile'

    profileID = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String, nullable=False)
    nachname = db.Column(db.String, nullable=False)
    adresse = db.Column(JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'))

    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

    def json(self):
        return {
            "id": str(self.id),
            "vorname": self.vorname,
            "nachname": self.nachname,
            "adresse": self.adresse
        }

class EmailSetting(BaseMixin, db.Model):
    __tablename__ = 'emailSettings'

    emailSettingID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    email_pw = db.Column(db.String)
    smtp_host = db.Column(db.String)
    smtp_port = db.Column(db.Integer)
    tls = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.userID'))

    def __init__(self, email):
        self.email = email
    
    def json(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "email_pw": self.email_pw,
            "smtp_host": self.smtp_host,
            "smtp_port": self.smtp_port,
            "tls": self.tls
        }

    

