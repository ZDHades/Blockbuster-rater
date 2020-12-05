from .import bp as movies
import requests 
from flask import current_app as app, render_template, request, redirect, url_for, flash, session
from app import db
from flask_login import login_required, current_user
from .forms import Search_Movie
from .models import Rating

@movies.route('/search', methods=['GET', 'POST'])
def search():
    form = Search_Movie()
    movies = []

    if form.validate_on_submit():
        data = {
            'movie' : request.form.get('name')
        }

        search = f"https://api.themoviedb.org/3/search/movie?api_key=230fd3a192d8580ee857e1e9bd72d2a1&query={data['movie']}"
        response = requests.request("GET", search)
        r = response.json()
        for _ in r['results']:
            movies.append(_)
        
    content = {
        'movies' : movies,
        'form' : form
    }
    return render_template('search.html', **content)


@movies.route('/down', methods=['GET', 'POST'])
def Rate_up():
    print('somethings happening')
    movie = request.args.get('name')
    r = Rating(movie=movie, thumbs_up=True)
    db.session.add(r)
    db.session.commit()
    return redirect(url_for('movies.Ratings'))

@movies.route('/up', methods=['GET', 'POST'])
def Rate_down():
    print('somethings happening')
    movie = request.args.get('name')
    r = Rating(movie=movie, thumbs_down=True)
    db.session.add(r)
    db.session.commit()
    return redirect(url_for('movies.Ratings'))

@movies.route('/ratings')
def Ratings():
    all_ratings = Rating.query.all()
    unique_titles = []
    data = []
    for _ in all_ratings:
        if _.movie not in unique_titles:
            unique_titles.append(_.movie)
    for title in unique_titles:
        count_up = 0
        count_down = 0
        for rating in all_ratings:
            if title == rating.movie:
                if rating.thumbs_up == True:
                    count_up += 1
                else: count_down += 1
        data.append((title, count_up, count_down))
    print(data)
    return render_template('ratings.html', data=data)

@movies.route('/rate-me')
def single_movie():
    _id = int(request.args.get('id'))
    search = f'https://api.themoviedb.org/3/movie/{_id}?api_key=230fd3a192d8580ee857e1e9bd72d2a1&language=en-US'
    response = requests.request("GET", search)
    m = response.json()
    return render_template('movie.html', movie=m)