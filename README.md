Deploy locally
-
The computer must be installed:
 - python3, 
 - pip3, 
 - virtualenv.

Activate virtualenv:
   
    virtualenv --python=python3 venv              
    source venv/bin/activate
    
Go to folder `demo`.

    cd demo

Install all necessary packages:

    pip install -r requirements.txt
    
Create migrations: 
    
    python manage.py migrate
   
Run the project with the command:

    python manage.py runserver