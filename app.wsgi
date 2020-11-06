#!/usr/bin/python
activate_this = '/var/www/spagetti-ordskyringaleikur/flask_backend/env/bin/activate_this.py'
with open(activate_this) as file_:
	exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/spagetti-ordskyringaleikur/flask_backend')

from main import app as application
