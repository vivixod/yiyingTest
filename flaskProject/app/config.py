class Config:
    HOSTNAME = "127.0.0.1"
    PORT = 3306
    USERNAME = "root"
    PASSWORD = "gyztt030607"
    DATABASE = "flasktest"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
