#!/usr/bin/env python

# Python Libs
import webapp2
from webapp2_extras import routes
import jinja2
import os
import urllib

#Import Handlers
from handlers.home import MainPageHandler
from handlers.crud import NewPostHandler, DeletePostHandler
from handlers.auth import LoginHandler, LogoutHandler

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'secret_key_for_session_here',
}

app = webapp2.WSGIApplication([

	('/', MainPageHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	('/newpost', NewPostHandler),    
    ('/delete', DeletePostHandler),
    

], debug=True, config=config)