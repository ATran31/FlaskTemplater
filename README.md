#### Usage  
python FlaskTemplater.py /path/to/project

#### Description
Creates a Flask project in a user specified folder.  
Creates in the script directory if user does not supply a project path.  
It does not create a virtualenv or install any dependencies.  
The folder structure is as follows:  
./  
./run.py  
./app_pkg/  
____./templates/  
________./index.html  
____./static/  
________./css/  
____________./app.css  
________./js/  
____________./app.js  
____./\_\_init\_\_.py  
____./config.py  
____./forms.py  
____./models.py  
____./views.py  
