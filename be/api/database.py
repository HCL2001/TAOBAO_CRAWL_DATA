from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config


SQLALCHEMY_DATABASE_URL = f"{config.DRIVER_BD}://{config.USER_NAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



