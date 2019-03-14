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
import argparse
import shutil


class ProjectTemplate:
    def __init__(self, script_mode=True, **kwargs):
        if script_mode:
            parser = argparse.ArgumentParser()
            parser.add_argument("project_folder", nargs="?", default=os.path.dirname(os.path.realpath(__file__)), help="The folder where this project will be initialized. Uses the same directory as this script if no project folder is given.")
            parser.add_argument("-b", "--use-blueprints", action="store_true", help="Include a Flask blueprints template.")
            parser.add_argument("-c", "--include-configs", action="store_true", help="Include a Flask configuration file template.")
            parser.add_argument("-f", "--include-forms", action="store_true", help="Include a Flask form template.")
            parser.add_argument("-m", "--include-models", action="store_true", help="Include a database model definition template.")
            parser.add_argument("-w", "--overwrite", action="store_true", help="Allow project folder to be overwritten if it exists.")

            args = parser.parse_args()

            self.project_folder = args.project_folder
            self.overwrite = args.overwrite
            self.use_blueprints = args.use_blueprints
            self.include_configs = args.include_configs
            self.include_forms = args.include_forms
            self.include_models = args.include_models

        else:
            # default all options to false unless changed in kwargs
            self.use_blueprints = False
            self.include_configs = False
            self.include_forms = False
            self.include_models = False
            self.overwrite = False
            for k, v in kwargs.items():
                # ignore irrelevant args
                if k in ['project_folder', 'use_blueprints', 'include_models', 'include_configs', 'include_forms', 'overwrite']:
                    setattr(self, k, v)

            # if project_folder is not defined, default to current directory
            if not hasattr(self, 'project_folder'):
                self.project_folder = os.path.dirname(os.path.realpath(__file__))

        self.pkg_dir = os.path.join(self.project_folder, 'app_pkg')
        self.templates_dir = os.path.join(self.pkg_dir, 'templates')
        self.static_dir = os.path.join(self.pkg_dir, 'static')
        self.bp_dir = os.path.join(self.pkg_dir, 'my_blueprint')

    def make_folders(self, pkg_dir, templates_dir, static_dir):
        # overwrite existing folders if they exist
        if self.overwrite and os.path.exists(pkg_dir):
            shutil.rmtree(pkg_dir)
        os.makedirs(pkg_dir)
        # create templates folder
        os.mkdir(templates_dir)
        # create static folders
        static_fols = ['css', 'js']
        for fol in static_fols:
            os.makedirs(os.path.join(static_dir, fol))

        # create the an index blueprint if the --use-blueprint option was set
        if self.use_blueprints:
            os.mkdir(self.bp_dir)
            for fol in ['static', 'templates']:
                os.makedirs(os.path.join(self.bp_dir, fol))
                if fol == 'static':
                    for fol in static_fols:
                        bp_dir = os.path.join(pkg_dir, 'my_blueprint')
                        os.makedirs(os.path.join(bp_dir, 'static', fol))

        print('Created project folders...\n')

    def make_run_file(self, project_folder):
        with open(os.path.join(project_folder, 'run.py'), 'w') as file:
            run_file = f'from app_pkg import app\n\n' \
                f'# uncomment below to run in development mode, no connection from other machines allowed\n' \
                f'#app.run(debug=True)\n\n' \
                f'# uncomment below to allow connection from other devices on local network\n' \
                f'#app.run(host=\'0.0.0.0\', threaded=True, debug=True)\n'
            file.write(run_file)

    def make_app_init_file(self, pkg_dir):
        '''
        Creates the app_pkg package __init__ file.
        '''
        with open(os.path.join(pkg_dir, '__init__.py'), 'w') as file:
            file_content = f'from flask import Flask\n' \
                f'#from flask_sqlalchemy import SQLAlchemy\n' \
                f'#from flask_migration import Migration\n' \
                f'#from flask_login import LoginManager\n\n' \
                f'app = Flask(__name__)\n' \
                f'# generate the secret key using os.urrandom(24) then pasting the result in here\n' \
                f'#app.secret_key = \'<your-secret-key>\'\n' \
                f'#app.config.from_pyfile(\'config.py\')\n\n' \
                f'# remove below if not using a database\n' \
                f'#db = SQLAlchemy(app)\n#' \
                f'migrate = Migrate(app, db)\n\n' \
                f'#lm = LoginManager()\n' \
                f'#lm.login_view = \'login\'\n#lm.init_app(app)\n\n' \
                f'#from app_pkg import views, models\n'
            file.write(file_content)

            if self.use_blueprints:
                blueprint = f'# register blueprint\n' \
                    f'#from app_pkg.my_blueprint import bp as my_bp\n' \
                    f'#app.register_blueprint(my_bp)\n'
                file.write(blueprint)
        print('Created app __init__ file...\n')

    def make_bp_init_file(self, bp_dir):
        '''
        Creates the __init__ file for the blueprint template.
        '''
        with open(os.path.join(bp_dir, '__init__.py'), 'w') as file:
            file_content = f'from flask import Blueprint\n\n' \
                f'# This blueprint contains my_blueprint page related components.\n' \
                f'bp = Blueprint(\'my_blueprint\', __name__, template_folder=\'templates\', static_folder=\'static\', static_url_path=\'/my_blueprint/static\')\n'
            file.write(file_content)
            print('Created blueprint __init__ file...\n')

    def make_config_file(self, pkg_dir):
        '''
        Creates the app configuration file. This file contains definitions for database connections, migrations, and other infrastructure type settings.
        '''
        with open(os.path.join(pkg_dir, 'config.py'), 'w') as file:
            file_content = f'#import os\n\n' \
                f'# uncomment below if using a database\n' \
                f'#DB_URL = os.environ.get(\'DB_URL\')\n' \
                f'#DB_USER = os.environ.get(\'DB_USER\')\n' \
                f'#DB_PW = os.environ.get(\'DB_PW\')\n' \
                f'#DB_NAME = os.environ.get(\'DB_NAME\')\n' \
                f'#DB = f\'postgresql+psycopg2://{{DB_USER}}:{{DB_PW}}@{{DB_URL}}/{{DB_NAME}}\'\n' \
                f'#SQLALCHEMY_DATABASE_URI = DB or \'sqlite:///\' + os.path.join(basedir, \'app.db\')\n\n' \
                f'# uncomment below if using flask-migrate for database migration\n' \
                f'# define the database migration data files directory\n' \
                f'#basedir = os.path.abspath(os.path.dirname(__file__))\n' \
                f'#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, \'db_repository\')\n' \
                f'#SQLALCHEMY_TRACK_MODIFICATIONS = False\n\n' \
                f'# define redis connection\n' \
                f'#REDIS_URL = os.environ.get(\'REDIS_URL\')'
            file.write(file_content)
        print('Created configuration file...\n')

    def make_forms_file(self, pkg_dir):
        '''
        Create file to define form classes.
        '''
        with open(os.path.join(pkg_dir, 'forms.py'), 'w') as file:
            file_content = f'#from flask_wtf import FlaskForm\n' \
                f'#from wtforms import StringField, PasswordField, SubmitField\n' \
                f'#from wtforms.validators import Email, DataRequired\n\n' \
                f'#class SignInForm(FlaskForm):\n' \
                f'#    email = StringField(\'email\', validators=[DataRequired(), Email()])\n' \
                f'#    password = PasswordField(\'password\', validators=[DataRequired()])\n' \
                f'#    submit = SubmitField("Sign In")\n\n' \
                f'# define other classes...\n'
            file.write(file_content)
        print('Created forms file...\n')

    def make_models_file(self, pkg_dir):
        '''
        Create the models file to define database object models.
        '''
        with open(os.path.join(pkg_dir, 'models.py'), 'w') as file:
            file_content = f'#from app_pkg import db\n' \
                f'# include below to use existing tables without having to define the schema\n' \
                f'#db.Model.metadata.reflect(db.engine)\n\n' \
                f'# define model classes...\n' \
                f'#class ClassName(db.Model):\n' \
                f'#    __table__ = db.Model.metadata.tables[\'table-name\']\n' \
                f'#    def __repr__(self):\n' \
                f'#        return \'<repr-str{{}}>\'.format(self.some-field)\n'
            file.write(file_content)
        print('Created models file...\n')

    def make_views_file(self, pkg_dir):
        '''
        Create file to hold app views/routes.
        '''
        with open(os.path.join(pkg_dir, 'views.py'), 'w') as file:
            file_content = f'# remove db and lm if not using database or login manager\n' \
                f'from app_pkg import app, db, lm\n' \
                f'from flask import render_template, flash, redirect, url_for, request\n' \
                f'# uncomment to enable user authentication\n' \
                f'#from flask_login import login_user, logout_user, current_user, login_required\n' \
                f'#from .models import your, models\n' \
                f'#from .forms import your, forms\n\n' \
                f'# uncomment to enable user authentication\n' \
                f'#@lm.user_loader\n' \
                f'#def load_user(email):\n' \
                f'#    return User.query.filter_by(email=email).first()\n'
            file.write(file_content)
        print('Created views file...\n')

    def make_template_file(self, templates_dir):
        '''
        Create intial template file.
        '''
        open(os.path.join(templates_dir, 'index.html'), 'w').close()
        print('Created index template...\n')

    def make_project(self):
        self.make_folders(self.pkg_dir, self.templates_dir, self.static_dir)
        self.make_run_file(self.project_folder)
        self.make_app_init_file(self.pkg_dir)
        self.make_template_file(self.templates_dir)
        if not self.use_blueprints:
            self.make_views_file(self.pkg_dir)
        else:
            self.make_bp_init_file(self.bp_dir)
        if self.include_configs:
            self.make_config_file(self.pkg_dir)
        if self.include_forms:
            self.make_forms_file(self.pkg_dir)
        if self.include_models:
            self.make_models_file(self.pkg_dir)
        print('Project created.')


if __name__ == '__main__':
    project = ProjectTemplate()
    project.make_project()
