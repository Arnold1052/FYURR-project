#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
from pydoc import render_doc
import re
from unittest import result
from urllib import response
import dateutil.parser
import babel

from flask import Flask, session, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:engineerarnoldmr@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
#----------------------------------------------------------------------------#

#app = Flask(__name__)

#app.config.from_object('config')
#db = SQLAlchemy(app)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

#class shows(db.Model):
 #   __tablename__ = 'shows'
 #   id= db.Column('id', db.Integer, primary_key=True)
 #   venue_id= db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id'))
  #  artist_id= db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id'))
 #   show_date= db.Column('show_date', db.Integer, nullable=True)
 #   def __repr__(self):
 #     return f'<shows {self.id} {self.venue_id} {self.artist_id} {self.show_date} >'
#db.create_all()


 


shows = db.Table ('shows',
    db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('Artist.id')),
    db.Column('show_date', db.DateTime, nullable=False))


    
    


   

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    city = db.Column(db.String(),nullable=True)
    state = db.Column(db.String(), nullable=True)
    phone = db.Column(db.String(), nullable=True)
    genres = db.Column(db.String(), nullable=True)
    image_link = db.Column(db.String(), nullable=True)
    facebook_link = db.Column(db.String(),nullable=True)
    website_link= db.Column(db.String(), nullable=True)
    seeking_venue= db.Column(db.String(), nullable=True)
    seeking_description= db.Column(db.String(), nullable=True)
    show= db.relationship('Venue', secondary= shows,
      backref=db.backref('Artists'), lazy=True)

    def __repr__(self):
      return f'<Artist {self.id} {self.name} {self.city} {self.state} {self.phone} {self.genres} {self.image_link} {self.facebook_link}>'
db.create_all()

class Venue(db.Model):

  __tablename__ = 'Venue'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  city = db.Column(db.String(), nullable=False)
  state = db.Column(db.String(), nullable=False)
  address = db.Column(db.String(), nullable=False)
  phone = db.Column(db.String(), nullable=False)
  genres= db.Column(db.String(), nullable=False)
  image_link = db.Column(db.String(), nullable=False)
  facebook_link = db.Column(db.String(), nullable=False)
  website_link= db.Column(db.String(), nullable=False)
  seeking_talent= db.Column(db.String(), nullable=False)
  seeking_description= db.Column(db.String(), nullable=False)
  def __repr__(self):

   
    return f'<Venue {self.id} {self.name} {self.city} {self.state} {self.address} {self.phone} {self.image_link} {self.facebook_link}>'
db.create_all()



#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  #       num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
  
  return render_template('pages/venues.html', areas=Venue.query.all(),venues=Venue.query.all());

@app.route('/venues/search', methods=['POST','GET'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  
  search_term=request.form.get('search_term ')
  search_term1 = "%{}%".format(search_term)
 
  
  results= Venue.query.filter(Venue.city.like(search_term1)).all()

  #results= Venue.query.filter_by(city='results')
  
  #results.count()
  
  return render_template('pages/search_venues.html',search_term=search_term,results=results)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  
  return render_template('pages/show_venue.html', venues=Venue.query.filter_by(id=venue_id))

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion
 
  name = request.form.get('name')
  city=  request.form.get('city')
  state = request.form.get('state')
  address = request.form.get('address')
  phone = request.form.get('phone')
  genres = request.form.get('genres')
  facebook_link = request.form.get('facebook_link')
  image_link = request.form.get('image_link')
  website = request.form.get('website_link')
  seeking_talent = request.form.get('seeking_talent')
  seeking_description = request.form.get('seeking_description')
  

  venue = Venue(name=name,city=city,state=state,address=address,phone=phone,facebook_link=facebook_link,
  image_link=image_link ,genres=genres,website_link=website,seeking_talent=seeking_talent,seeking_description=seeking_description)
  db.session.add(venue)
  db.session.commit()
  



    

  # on successful db insert, flash success
  flash('Venue ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

  # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
  # clicking that button delete it from the db then redirect the user to the homepage
  return None

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database

  return render_template('pages/artists.html', artists=Artist.query.all())

@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  
 search_term=request.form.get('search_term', '')
 
 lizt1 = []
 l= "%{}%".format(search_term)
# model_id = 1
 response=Artist.query.filter(Artist.name.like('%l%'))
 for i in response:
  if(search_term in i.name) is True:
    lizt1.append(i.name)
# response=Artist.query.filter(Artist.name.like(ab)).all()
 #print(response)
 #for na in response:
  #na.append(lizt1)

 count1=len(lizt1)

 
# response={
  # "count": 4,
  # "data": [{
  #   "id": 4,
  #   "name": f"{re}",
  #   "num_upcoming_shows": 0,
  #  }]
 # }
  

 return render_template('pages/search_artists.html',search_term=search_term,results=lizt1,count=count1)

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artist table, using artist_id

   return render_template('pages/show_artist.html', artists =Artist.query.filter_by(id=artist_id))

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artists=Artist.query.filter_by(id=artist_id))

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes

  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  venue=Venue.query.filter_by(id=venue_id)
  
  # TODO: populate form with values from venue with ID <venue_id>
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():

  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  name = request.form.get('name')
  city=  request.form.get('city')
  state = request.form.get('state')
  
  phone = request.form.get('phone')
  genres = request.form.get('genres')
  facebook_link = request.form.get('facebook_link')
  image_link = request.form.get('image_link')
  website = request.form.get('website_link')
  seeking_venue = request.form.get('seeking_venue')
  seeking_description = request.form.get('seeking_description')
  

  artist = Artist(name=name,city=city,state=state,phone=phone,facebook_link=facebook_link,
  image_link=image_link ,genres=genres,website_link=website,seeking_venue=seeking_venue,seeking_description=seeking_description)
  db.session.add(artist)
  db.session.commit()


  # on successful db insert, flash success
  flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
   
  return render_template('pages/shows.html', shows=Venue.query.filter(Venue.Artists).all())

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  artist_id = request.form.get('artist_id')
  venue_id=  request.form.get('venue_id')
  show_date = request.form.get('start_time')
  artist_id =Artist()
  venue_id=Venue()

  artist_id.show.append(venue_id)
  db.session.add(artist_id)
  db.session.commit()

 
  #db.session.add_all([ar,ven])

  #db.session.commit()
  


  #shows_num = shows(venue_id=venue_id,artist_id=artist_id,show_date=show_date)
  
  # on successful db insert, flash success
  flash('Show was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
  app.secret_key = 'super secret key'
  app.config['SESSION_TYPE'] = 'filesystem'

  #sess.init_app(app)
  app.debug = True
  app.run()


# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
