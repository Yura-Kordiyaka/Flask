from app import db


class Cars(db.Model):
    _tablename_ = 'cars'
    Brand = db.Column(db.String(50), nullable=True)
    Type = db.Column(db.String(50), nullable=True)
    Number = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, primary_key=True)

    @property
    def serialize(self):
        return {
            'Brand': self.Brand,
            'Type': self.Type,
            'Number': self.Number,
            'User id': self.user_id
        }


class User(db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(100), nullable=True)
    @property
    def serialize(self):
        return {
            'id':self.id,
            'first name':self.first_name,
            'last name':self.last_name,
            'email':self.email
        }
