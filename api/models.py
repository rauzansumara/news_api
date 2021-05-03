from api import db

class Berita_clickbait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, unique=False)
    title = db.Column(db.Text, unique=False)
    label = db.Column(db.String(20), unique=False)

    def __repr__(self):
        return '<Judul {}>'.format(self.title)

class Berita_nonclickbait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, unique=False)
    title = db.Column(db.Text, unique=False)
    label = db.Column(db.String(20), unique=False)

    def __repr__(self):
        return '<Judul {}>'.format(self.title)

class Berita_suggested_clickbait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, unique=False)
    title = db.Column(db.Text, unique=False)
    label = db.Column(db.String(20), unique=False)

    def __repr__(self):
        return '<Judul {}>'.format(self.title)

class Berita_suggested_nonclickbait(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.Text, unique=False)
    title = db.Column(db.Text, unique=False)
    label = db.Column(db.String(20), unique=False)

    def __repr__(self):
        return '<Judul {}>'.format(self.title)