from google.appengine.api import users
from google.appengine.ext import ndb
from home import Greeting

import cgi
import jinja2
import urllib
import webapp2
import os

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

def PostById(id):
    return Greeting.get_by_id(id, parent=guestbook_key())
   
class NewPostHandler(webapp2.RequestHandler):
	def post(self):
		greeting = Greeting(parent=guestbook_key(DEFAULT_GUESTBOOK_NAME))
		if users.get_current_user():
			greeting.author = users.get_current_user()

		greeting.content = self.request.get('content')
		greeting.put()

		self.redirect('/')
		
class DeletePostHandler(webapp2.RequestHandler):
    def post(self):
        id = int(self.request.get('id'))
        thispost = PostById(id)
        thispost.key.delete()
        self.redirect('/')