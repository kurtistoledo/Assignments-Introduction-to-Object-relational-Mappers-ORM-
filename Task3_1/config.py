class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:{encoded_pw}@localhost/fitness_center_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
