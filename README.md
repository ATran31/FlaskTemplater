#### Description
Creates a Flask project in a user specified folder.
Creates in the script directory if user does not supply a project path.
It does not create a virtualenv or install any dependencies.

#### Use as a script
```
usage: FlaskTemplater.py [-h] [-b] [-c] [-f] [-m] [project_folder]

positional arguments:
  project_folder        The folder where this project will be initialized.
                        Uses the same directory as this script if no project
                        folder is given.

optional arguments:
  -h, --help            show this help message and exit
  -b, --use-blueprints  Include a Flask blueprints template.
  -c, --include-configs
                        Include a Flask configuration file template.
  -f, --include-forms   Include a Flask form template.
  -m, --include-models  Include a database model definition template.
```
#### Use as a module
The `script_mode` argument is REQUIRED and must be set to `False` when using as a module. All other arguments are optional. If `project_folder` argument is not specified, the output directory the same directory as the script.

```
from FlaskTemplater import ProjectTemplate

my_project = ProjectTemplate(script_mode=False, \
    project_folder="test", \
    use_blueprints=True, \
    include_models=True, \
    include_forms=True, \
    include_configs=True)
my_project.make_project()

```

#### The output folder structure is as follows:
```
│   run.py
└───app_pkg
    │   config.py (optional, created if `--include-configs flag` is used)
    │   forms.py (optional, created if `--include-forms flag` is used)
    │   models.py (optional, created if `--include-models flag` is used)
    │   views.py
    │   __init__.py
    │
    ├───my_blueprint (optional, created if `--use-blueprints` flag is used)
    │   │   __init__.py
    │   │
    │   ├───static
    │   │   ├───css
    │   │   └───js
    │   └───templates
    ├───static
    │   ├───css
    │   └───js
    └───templates
            index.html
```
