
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions


import webapp2
import os
import jinja2
import os
import time
import logging
import uuid


jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('views'))


class BaseHandler(webapp2.RequestHandler):


	def dispatch(self):

		super(BaseHandler, self).dispatch()


	viewing_site_key = None

	defaults = {

		'user_obj': users.get_current_user()

	}


	def get_default_template_vars(self, current_vars):

		if current_vars != None:

			return dict(self.defaults.items() + current_vars.items())

		else:

			return self.defaults

	def render(self, template_str, template_vars=None):
		template_vars = self.get_default_template_vars(template_vars)
		template = jinja_environment.get_template(template_str)
		self.response.out.write(template.render(template_vars))


