from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Tabla De Rompimiento Entre Song Y Autor
songAuthor = db.Table('songAuthor',
    db.Column('song_id', db.Integer, db.ForeignKey('song.song_id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'), primary_key=True)
)

# Tabla De Rompimiento Entre Album Y Autor
albumAuthor = db.Table('albumAuthor',
    db.Column('album_id', db.Integer, db.ForeignKey('album.album_id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'), primary_key=True)
)

# Tabla De Rompimiento Entre Genres Y Album
albumGenres = db.Table('albumGenres',
    db.Column('album_id', db.Integer, db.ForeignKey('album.album_id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.genre_id'), primary_key=True)
)

# Tabla De Rompimiento Entre Song Y Album
albumSongs = db.Table('albumSongs',
    db.Column('album_id', db.Integer, db.ForeignKey('album.album_id'), primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('song.song_id'), primary_key=True)
)

# Tabla De Rompimiento Entre Usuario Y Album
userAlbums = db.Table('userAlbums',
    db.Column('username', db.Integer, db.ForeignKey('user.username'), primary_key=True),
    db.Column('album_id', db.Integer, db.ForeignKey('album.album_id'), primary_key=True)
)

class User(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(256), unique=True, nullable=False)
    user_full_name = db.Column(db.String(256), unique=True, nullable=False)

    user_albums = db.relationship('Album', secondary=userAlbums, lazy='subquery',
        backref=db.backref('user_albums', lazy=True))

class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_name = db.Column(db.String(64), nullable=False)
    album_img_URL = db.Column(db.String(512), unique=False, nullable=True)
    album_desc = db.Column(db.String(400), nullable=False)
    album_release_date = db.Column(db.Date())

    album_authors = db.relationship('Author', secondary=albumAuthor, lazy='subquery',
        backref=db.backref('album_authors', lazy=True))

    album_genres = db.relationship('Genre', secondary=albumGenres, lazy='subquery',
        backref=db.backref('album_genres', lazy=True))

    album_songs = db.relationship('Song', secondary=albumSongs, lazy='subquery',
        backref=db.backref('album_songs', lazy=True))

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(256), unique=False, nullable=False)
    

class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_name = db.Column(db.String(32), nullable=False)

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_name = db.Column(db.String(32), nullable=False)

    song_authors = db.relationship('Author', secondary=songAuthor, lazy='subquery',
        backref=db.backref('song_authors', lazy=True))

    song_lenght = db.Column(db.Integer, nullable=False)
    song_URL = db.Column(db.String(512), unique=False, nullable=True)

    


    
    
    