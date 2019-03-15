import unittest
from FlaskTemplater import ProjectTemplate as PT
import os
import shutil


class TestMakeFolders(unittest.TestCase):
    # TODO test make folders
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

        # delete the project instance
        delattr(self, 'project')

    def test_make_folders_with_bp(self):
        # test with blueprints
        self.project.use_blueprints = True
        self.project.make_folders(self.project.pkg_dir, self.project.templates_dir, self.project.static_dir)

        # check that package folder exists
        self.assertTrue(os.path.exists(self.project.pkg_dir))
        # check that global templates folder exists
        self.assertTrue(os.path.exists(self.project.templates_dir))
        # check that global static folder exists
        self.assertTrue(os.path.exists(self.project.static_dir))

        # check that blueprint folder exists
        self.assertTrue(os.path.exists(self.project.bp_dir))
        # check that blueprint templates folder exists
        self.assertTrue(os.path.exists(os.path.join(self.project.bp_dir, 'templates')))
        # check that blueprint static folder exists
        self.assertTrue(os.path.exists(os.path.join(self.project.bp_dir, 'static')))
        # check that css folder exists in blueprint
        self.assertTrue(os.path.exists(os.path.join(self.project.bp_dir, 'static/css')))
        # check that js folder exists in blueprint
        self.assertTrue(os.path.exists(os.path.join(self.project.bp_dir, 'static/js')))


class TestMakeRunFile(unittest.TestCase):
    # TODO test make run file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_run_file(self):
        pass


class TestMakeAppInitFile(unittest.TestCase):
    # TODO test make app __init__ file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_app_init_file(self):
        pass


class TestMakeBlueprintInitFile(unittest.TestCase):
    # TODO test make blueprint __init__ file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_blueprint_init_file(self):
        pass


class TestMakeConfigFile(unittest.TestCase):
    # TODO test make config file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_config_file(self):
        pass


class TestMakeFormsFile(unittest.TestCase):
    # TODO test make forms file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_forms_file(self):
        pass


class TestMakeModelsFile(unittest.TestCase):
    # TODO test make models file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_models_file(self):
        pass


class TestMakeViewsFile(unittest.TestCase):
    # TODO test make views file
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_views_file(self):
        pass


class TestMakeTemplateFile(unittest.TestCase):
    # TODO test make app template
    def setUp(self):
        # create temp directory to store outputs
        os.mkdir('temp')
        # create project instance
        self.project = PT(script_mode=False, project_folder='temp')

    def tearDown(self):
        # delete temp directory and all files within
        shutil.rmtree('temp')

    def test_make_template_file(self):
        pass
