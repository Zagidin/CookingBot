from .models import Base, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
