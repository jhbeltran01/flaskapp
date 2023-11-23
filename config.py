class Config:
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'postgresql://flask:password@localhost:5432/flask_tutorial'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
