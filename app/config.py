import os

basedir = os.path.abspath(os.path.dirname(__file__))

# The Config class contains general settings that we 
# want all enviroments to have by default.
class Config:
    """ Base configurations """
    SECRET_KEY = os.getenv('SECRET_KEY', 'you_own_your_own')
    DEBUG = False

class DevelopmentConfig(Config):
    """ Development configurations """
    DEBUG = True

class TestingConfig(Config):
    """ Testing configurations """
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    """ Production configurations """
    DEBUG = False

# Export the specified enviroment variables.
app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig
}
