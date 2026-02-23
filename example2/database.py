from sqlalchemy import create_engine
from sqlalchemy import declartive_base

engine = create_engine("sqlite:///database.db", connect_args = {"check_same_thread": False}
)