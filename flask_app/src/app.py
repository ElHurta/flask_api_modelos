from flask import Flask, render_template, request, jsonify
from flask_app.src.models import Album
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import response
from models import db, User, Song, Author, songAuthor, Genre
import sqlite3
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/')
def ping():
    # user = User(username= 'usuario',password= '123',user_full_name= 'pepito')
    # db.session.add(user)
    
    # author = Author(author_name='Adios')
    # db.session.add(author)

    # song = Song(song_name="B", song_author=[author], song_lenght=250, song_URL="bb")
    # db.session.add(song)
    # db.session.commit()
    return jsonify({"message": "pong!"})

@app.route('/songs')
def getAllSongs():
    songs = Song.query.all()
    songsObtained = []
    for song in songs:
        songsObtained.append({
            "song_id":song.song_id,
            "song_name":song.song_name,
            "song_author": [{'author_id':author.author_id, 'author_name':author.author_name}
                            for author in song.song_authors],
            "song_lenght":song.song_lenght,
            "song_url":song.song_URL
            })
    return jsonify({"songs": songsObtained})

@app.route('/genres')
def getAllGenres():
    genres = Genre.query.all()
    genresObtained = []
    for genre in genres:
        genresObtained.append({
            "genre_id": genre.genre_id,
            "genre_name": genre.genre_name
        })

@app.route('/authors')
def getAllAuthors():
    authors = Author.query.all()
    authorsObtained = []
    for author in authors:
        authorsObtained.append({
            "author_id":author.author_id,
            "author_name":author.author_name
        })

    return jsonify({"authors": authorsObtained})

@app.route('/albums')
def getAllAlbums():
    albums = Album.query.all()
    albumsObtained = []
    for album in albums:
        albumsObtained.append({
            "album_id":album.album_id,
            "album_name":album.album_name,
            "album_img_URL":album.album_img_URL,
            "album_desc":album.album_desc,
            "album_release_date":album.album_release_date
        })

    return jsonify({"albums": albumsObtained})

@app.route('/createTests')
def createTests():

    createdGenre = Genre(genre_name="Género 1")
    db.session.add(createdGenre)


    createdGenre = Genre(genre_name="Género 2")
    db.session.add(createdGenre)

    createdAlbum = Album(album_name = "Album 1", album_desc="Vaina rara")
    db.session.add(createdAlbum)
    db.session.commit()

    return jsonify({"message": "Elementos Creados con exito"})

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
    
    