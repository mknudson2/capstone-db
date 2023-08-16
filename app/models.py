from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))    
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)
    posts = db.relationship('Post', backref = 'author', lazy=True)
    collection = db.relationship('Collection', backref= 'user', lazy=True)
    
    def __repr__(self):
        return f'<USER: {self.username}>'

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'posts': [{
                'body': post.body,
                'timestamp': post.timestamp
            } for post in self.posts],
            'collection': [{
                'book_title': collection.book_title,
                'author': collection.author,
                'year_published': collection.year_published,
                'language': collection.language,
                'description': collection.description,
                'type': collection.type
            } for collection in self.collection]
        }

     
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def from_dict(self, user_obj):
        for attribute, v in user_obj.items():
            setattr(self, attribute, v)

    def get_id(self):
        return str(self.user_id)
            
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(), nullable = False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)

    def __repr__(self):
        return f'<Post: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Collection(db.Model):
    collection_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year_published = db.Column(db.String(20), nullable=False)
    language = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    #If I wanted to add keywords, could I make a column that accepts a list? Or just make a top three keyword with three fields?

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Societies(db.Model):
    affiliation_id = db.Column(db.Integer, primary_key=True)
    society_name = db.Column(db.String(200), nullable=False)
    focus = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=False)
    society_url = db.Column(db.String(200), nullable=False)
    journal = db.relationship('Journal', backref="affiliation", lazy=True)
    conference = db.relationship('Conference', backref="affiliation", lazy=True)

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Journal(db.Model):
    journal_id = db.Column(db.Integer, primary_key=True)
    journal_title = db.Column(db.String(200), nullable=False)
    focus = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(20), nullable=False)
    journal_url = db.Column(db.String(200), nullable=False)
    affiliation_id = db.Column(db.Integer, db.ForeignKey('societies.affiliation_id'), nullable = False)


    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Conference(db.Model):
    conference_id = db.Column(db.Integer, primary_key=True)
    conference_title = db.Column(db.String(200), nullable=False)
    focus = db.Column(db.String(200), nullable=False)
    conference_url = db.Column(db.String(200), nullable=False)
    affiliation_id = db.Column(db.Integer, db.ForeignKey('societies.affiliation_id'), nullable = False)


    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class SagaLocations(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    location_name= db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float(50), nullable=False)
    longitude = db.Column(db.Float(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ProgramsOfStudy(db.Model):
    program_id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(200), nullable=False)
    program_name = db.Column(db.String(200), nullable=False)
    degrees = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    specialities = db.Column(db.String(150), nullable=False)
    program_url = db.Column(db.String(200), nullable=False)


    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Glossary(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    translation = db.Column(db.String(200), nullable=False)
    pattern = db.Column(db.String(200), nullable=False)
    grammar_info = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()