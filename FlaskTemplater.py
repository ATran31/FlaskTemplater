# Creates a Flask project in a user specified folder.
# It does not create a virtualenv or install any dependencies.
# The folder structure is as follows:
# │   run.py
# └───app_pkg
#     │   config.py (optional, created if `--include-configs flag` is used)
#     │   forms.py (optional, created if `--include-forms flag` is used)
#     │   models.py (optional, created if `--include-models flag` is used)
#     │   views.py
#     │   __init__.py
#     │
#     ├───my_blueprint (optional, created if `--use-blueprints` flag is used)
#     │   │   __init__.py
#     │   │
#     │   ├───static
#     │   │   ├───css
#     │   │   └───js
#     │   └───templates
#     ├───static
#     │   ├───css
#     │   └───js
#     └───templates
#             index.html

import os
from sys import argv


class FlaskTemplater:
    def __init__(self):
        try:
            self.proj_folder = argv[1]
        except IndexError:
            self.proj_folder = os.path.dirname(os.path.realpath(__file__))

        self.use_blueprints = False
        self.include_configs = False
        self.include_forms = False
        self.include_models = False

        for arg in argv:
            if arg == '--use-blueprints':
                self.use_blueprints = True
            elif arg == '--include-configs':
                self.include_configs = True
            elif arg == '--include-forms':
                self.include_forms = True
            elif arg == '--include-models':
                self.include_models = True

        self.pkg_dir = os.path.join(self.proj_folder, 'app_pkg')
        self.templates_dir = os.path.join(self.pkg_dir, 'templates')
        self.static_dir = os.path.join(self.pkg_dir, 'static')
        self.bp_dir = os.path.join(self.pkg_dir, 'my_blueprint')

    def make_folders(self):
        # create the main package folder
        os.mkdir(self.pkg_dir)
        # create templates folder
        os.mkdir(self.templates_dir)
        # create static folders
        static_fols = ['css', 'js']
        for fol in static_fols:
            os.makedirs(os.path.join(self.static_dir, fol))

        # create the an index blueprint if the --use-blueprint option was set
        if self.use_blueprints:
            os.mkdir(self.bp_dir)
            for fol in ['static', 'templates']:
                os.makedirs(os.path.join(self.bp_dir, fol))
                if fol == 'static':
                    for fol in static_fols:
                        os.makedirs(os.path.join(self.bp_dir, 'static', fol))

        print('Created project folders...\n')

    def make_run_file(self):
        with open(os.path.join(self.proj_folder, 'run.py'), 'w') as file:
            run_file = 'from app_pkg import app\n\n# uncomment below to run in development mode, no connection from other machines allowed\n#app.run(debug=True)\n\n# uncomment below to allow connection from other devices on local network\n#app.run(host=\'0.0.0.0\', threaded=True, debug=True)'
            file.write(run_file)

    def make_app_init_file(self):
        '''
        Creates the app_pkg package __init__ file.
        '''
        with open(os.path.join(self.pkg_dir, '__init__.py'), 'w') as file:
            file_content = 'from flask import Flask\n#from flask_sqlalchemy import SQLAlchemy\n#from flask_migration import Migration\n#from flask_login import LoginManager\n\napp = Flask(__name__)\n# generate the secret key using os.urrandom(24) then pasting the result in here\n#app.secret_key = \'<your-secret-key>\'\n#app.config.from_pyfile(\'config.py\')\n\n# remove below if not using a database\n#db = SQLAlchemy(app)\n#migrate = Migrate(app, db)\n\n#lm = LoginManager()\n#lm.login_view = \'login\'\n#lm.init_app(app)\n\n#from app_pkg import views, models\n'
            file.write(file_content)

            if self.use_blueprints:
                blueprint = '# register blueprint\n#from app_pkg.my_blueprint import bp as my_bp\n#app.register_blueprint(my_bp)\n'
                file.write(blueprint)
        print('Created app __init__ file...\n')

    def make_bp_init_file(self):
        '''
        Creates the __init__ file for the blueprint template.
        '''
        with open(os.path.join(self.bp_dir, '__init__.py'), 'w') as file:
            file_content = 'from flask import Blueprint\n\n#This blueprint contains my_blueprint page related components.\nbp = Blueprint(\'my_blueprint\', __name__, template_folder=\'templates\', static_folder=\'static\', static_url_path=\'/my_blueprint/static\')\n\n'
            file.write(file_content)
            print('Created blueprint __init__ file...\n')

    def make_config_file(self):
        '''
        Creates the app configuration file. This file contains definitions for database connections, migrations, and other infrastructure type settings.
        '''
        with open(os.path.join(self.pkg_dir, 'config.py'), 'w') as file:
            file_content = '#import os\n# uncomment below if using a database\n#DB_URL = os.environ.get(\'DB_URL\')\n#DB_USER = os.environ.get(\'DB_USER\')\n#DB_PW = os.environ.get(\'DB_PW\')\n#DB_NAME = os.environ.get(\'DB_NAME\')\n#DB = \'postgresql+psycopg2://{user}:{pw}@{url}/{db}\'.format(user=DB_USER, pw=DB_PW, url=DB_URL,db=DB_NAME)\n#SQLALCHEMY_DATABASE_URI = DB or \'sqlite:///\' + os.path.join(basedir, \'app.db\')\n# uncomment below if using flask-migrate for database migration\n# define the database migration data files directory\n#basedir = os.path.abspath(os.path.dirname(__file__))\n#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, \'db_repository\')\n#SQLALCHEMY_TRACK_MODIFICATIONS = False\n\n# define redis connection\n#REDIS_URL = os.environ.get(\'REDIS_URL\')'
            file.write(file_content)
        print('Created configuration file...\n')

    def make_forms_file(self):
        '''
        Create file to define form classes.
        '''
        with open(os.path.join(self.pkg_dir, 'forms.py'), 'w') as file:
            file_content = '#from flask_wtf import FlaskForm\n#from wtforms import StringField, PasswordField, SubmitField\n#from wtforms.validators import Email, DataRequired\n\n#class SignInForm(FlaskForm):\n#    email = StringField(\'email\', validators=[DataRequired(), Email()])\n#    password = PasswordField(\'password\', validators=[DataRequired()])\n#    submit = SubmitField("Sign In")\n\n# define other classes...'
            file.write(file_content)
        print('Created forms file...\n')

    def make_models_file(self):
        '''
        Create the models file to define database object models.
        '''
        with open(os.path.join(self.pkg_dir, 'models.py'), 'w') as file:
            file_content = '#from app_pkg import db\n# include below to use existing tables without having to define the schema\n# db.Model.metadata.reflect(db.engine)\n\n# define model classes...\n#class <ClassName>(db.Model):\n#    __table__ = db.Model.metadata.tables[\'<table-name>\']\n#    def __repr__(self):\n#    return \'<<repr-str> {}>\'.format(self.<some-field>)\n'
            file.write(file_content)
        print('Created models file...\n')

    def make_views_file(self):
        '''
        Create file to hold app views/routes.
        '''
        with open(os.path.join(self.pkg_dir, 'views.py'), 'w') as file:
            file_content = '# remove db and lm if not using database or login manager\nfrom app_pkg import app, db, lm\nfrom flask import render_template, flash, redirect, url_for, request\n# uncomment to enable user authentication\n#from flask_login import login_user, logout_user, current_user, login_required\n#from .models import your, models\n#from .forms import your, forms\n\n# uncomment to enable user authentication\n#@lm.user_loader\n#def load_user(email):\n#    return User.query.filter_by(email=email).first()\n'
            file.write(file_content)
        print('Created views file...\n')

    def make_template_file(self):
        '''
        Create intial template file.
        '''
        open(os.path.join(self.templates_dir, 'index.html'), 'w').close()
        print('Created index template...\n')

    def make_project(self):
        self.make_folders()
        self.make_run_file()
        self.make_app_init_file()
        if not self.use_blueprints:
            self.make_views_file()
        self.make_template_file()
        if self.use_blueprints:
            self.make_bp_init_file()
        if self.include_configs:
            self.make_config_file()
        if self.include_forms:
            self.make_forms_file()
        if self.include_models:
            self.make_models_file()
        print('Project created.')


if __name__ == '__main__':
    FT = FlaskTemplater()
    FT.make_project()
