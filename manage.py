import os
import unittest
from flask_script import Manager
from app import create_app

# Create application instance with the required 
# parameter from the enviroment variable.
# This can either be 'development', 'testing' or 'production.
app = create_app(os.getenv('BOILERPLATE_ENV') or "development")

manager = Manager(app)

@manager.command
def runserver():
    '''Run server'''
    app.run()

@manager.command
def tests():
    '''Run unit tests'''
    tests = unittest.TestLoader().discover('app/tests', pattern = 'test*.py')
    result = unittest.TextTestRunner(verbosity = 2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
    manager.run()
