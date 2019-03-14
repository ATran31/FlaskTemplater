#### Description
Creates a Flask project in a user specified folder.
Creates in the script directory if user does not supply a project path.
It does not create a virtualenv or install any dependencies.

#### Usage
Get help with usage and options:

`python FlaskTemplater.py -h`

Create a generic project:

`python FlaskTemplater.py /path/to/project`

##### Options
###### Include a sample blueprint

`python FlaskTemplater.py --use-blueprints /path/to/project`

or using short form

`python FlaskTemplater.py -b /path/to/project`

###### Include model definitions

`python FlaskTemplater.py --include-models /path/to/project`

or using short form

`python FlaskTemplater.py -m /path/to/project`

###### Include form definitions

`python FlaskTemplater.py --include-forms /path/to/project`

or using short form

`python FlaskTemplater.py -f /path/to/project`

###### Include a configuration file

`python FlaskTemplater.py --include-configs /path/to/project`

or using short form

`python FlaskTemplater.py -c /path/to/project`


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
