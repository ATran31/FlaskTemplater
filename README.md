#### Description
Creates a Flask project in a user specified folder.  
Creates in the script directory if user does not supply a project path.  
It does not create a virtualenv or install any dependencies. 

#### Usage  
Create a generic project

`python FlaskTemplater.py /path/to/project`

##### Options
Include a sample blueprint

`python FlaskTemplater.py /path/to/project --use-blueprints`

Include model definitions

`python FlaskTemplater.py /path/to/project --include-models`

Include form definitions

`python FlaskTemplater.py /path/to/project --include-forms`

Include a configuration file

`python FlaskTemplater.py /path/to/project --include-configs`

 
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
