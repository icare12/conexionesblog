SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:icarochoa@localhost:5432/blogposts_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    SQLALCHEMY_DATABASE_URI = POSTGRESQL

    CKEDITOR_PKG_TYPE = 'full'
