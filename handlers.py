#-----------------------------------------------------------------------------#
#   handlers.py                                                               #
#                                                                             #
#   Copyright (c) 2011, Code A La Mode, original authors.                     #
#                                                                             #
#       This file is part of Play By Play.                                    #
#                                                                             #
#       Play By Play is free software; you can redistribute it and/or modify  #
#       it under the terms of the GNU General Public License as published by  #
#       the Free Software Foundation, either version 3 of the License, or     #
#       (at your option) any later version.                                   #
#                                                                             #
#       Play By Play is distributed in the hope that it will be useful, but   #
#       WITHOUT ANY WARRANTY; without even the implied warranty of            #
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU     #
#       General Public License for more details.                              #
#                                                                             #
#       You should have received a copy of the GNU General Public License     #
#       along with Play By Play.  If not, see:                                #
#           <http://www.gnu.org/licenses/>.                                   #
#-----------------------------------------------------------------------------#
"""Google App Engine request handlers (concrete implementation classes)."""


import logging
import os

from google.appengine.ext.webapp import template

from config import DEBUG, TEMPLATES
import base


_log = logging.getLogger(__name__)


class NotFound(base.WebHandler):
    """Request handler to serve a 404: Not Found error page."""

    def get(self, *args, **kwds):
        """Someone has issued a GET request on a nonexistent URL."""
        return self.serve_error(404)


class Home(base.WebHandler):
    """Request handler to serve the homepage."""

    def get(self):
        """Serve the homepage."""
        path = os.path.join(TEMPLATES, 'home.html')
        title = 'webcast your event'
        debug = DEBUG
        html = template.render(path, locals(), debug=debug)
        self.response.out.write(html)


class Create(base.WebHandler):
    """Request handler to serve the create event page."""

    def get(self):
        """Serve the homepage."""
        path = os.path.join(TEMPLATES, 'create.html')
        title = 'create an event'
        debug = DEBUG
        html = template.render(path, locals(), debug=debug)
        self.response.out.write(html)


class Email(base.MailHandler):
    """Request handler to deal with incoming email messages."""

    def receive(self, email_message):
        """Someone has sent us an email message."""
        _log.info('%s has sent us an email message' % email_message.sender)


class Connected(base.WebHandler):
    """Request handler to deal with channels that have connected."""

    def post(self):
        """A channel has connected and can receive messages."""
        client_id = self.request.get('from')
        _log.info('channel %s has connected' % client_id)


class Disconnected(base.WebHandler):
    """Request handler to deal with channels that have disconnected."""

    def post(self):
        """A channel has disconnected and can no longer receive messages."""
        client_id = self.request.get('from')
        _log.info('channel %s has disconnected' % client_id)
