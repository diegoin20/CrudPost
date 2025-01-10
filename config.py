class Config:
    SECRET_KEY = 'ozxcXkasdnM'

    
    MYSQL_USER = 'root'         
    MYSQL_PASSWORD = ''       
    MYSQL_HOST = 'localhost'      
    MYSQL_DB = 'Prendas' 
    MYSQL_PORT = 3306

    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  
