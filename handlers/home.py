from google.appengine.api import users
from google.appengine.ext import ndb

import cgi
import jinja2
import urllib
import webapp2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPageHandler(webapp2.RequestHandler):

    def get(self):
    	currentauthor = ""
        greetings_query = Greeting.query(
            ancestor=guestbook_key(DEFAULT_GUESTBOOK_NAME)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)
        if users.get_current_user():
            currentauthor = users.get_current_user().nickname()
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            'currentauthor': currentauthor,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))