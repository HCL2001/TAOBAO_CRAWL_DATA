from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

SQLALCHEMY_DATABASE_URL = f"{config.DRIVER_BD}://{config.USER_NAME}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Link(Base):
    __tablename__ = "link"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand_id = Column(Integer)
    link = Column(String)
    create_time = Column(DateTime)


class ProductList(Base):
    __tablename__ = "product_list"
    id = Column(Integer, primary_key=True)
    link_id = Column(Integer)
    brand_id = Column(Integer)
    report_id = Column(Integer)
    price = Column(Integer)
    original_price = Column(Integer)
    crawl_time = Column(DateTime)
    status = Column(Integer)
    total = Column(String)
    name = Column(String)
    link = Column(String)



class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer)
    report_id = Column(Integer)
    success = Column(Integer)
    failure = Column(Integer)
    total = Column(Integer)
    start_crawl = Column(DateTime)
    end_crawl = Column(DateTime)


def get_links_from_database():
    session = SessionLocal()
    links = session.query(Link).all()
    session.close()
    return links


def get_success_fail_product_list_from_database(report_id):
    session = SessionLocal()
    try:
        products = session.query(ProductList).filter_by(report_id=report_id).all()
        return products
    except Exception as e:
        print(f"Error retrieving products from database: {str(e)}")
        return None
    finally:
        session.close()
def get_all_link_brand(brand_id):
    session = SessionLocal()
    try:
        products = session.query(Link).filter_by(brand_id=brand_id).count()
        return products
    except Exception as e:
        print(f"Error retrieving products from database: {str(e)}")
        return None
    finally:
        session.close()


def save_objects_to_database(objects):
    session = SessionLocal()
    try:
        for obj in objects:
            new_report = Report(
                brand_id=obj.brand_id,
                report_id=obj.report_id,
                success=obj.success,
                failure=obj.failure,  # Corrected attribute name
                total=obj.total,
                start_crawl=obj.start_crawl,
                end_crawl=obj.end_crawl
            )
            session.add(new_report)
        session.commit()
        print("Data saved successfully")
    except Exception as e:
        session.rollback()
        print(f"Failed to save data to database: {str(e)}")
    finally:
        session.close()
