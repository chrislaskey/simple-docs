#!/usr/lib/virtualenvs/simple-docs/bin/python

from main import app as application

if not application.debug:
    import logging
    this_dir = os.path.dirname(__file__)
    log_file = os.path.join(this_dir, 'production.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    application.logger.addHandler(file_handler)

application.jinja_env.line_statement_prefix = '%'
