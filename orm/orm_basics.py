#import create engine to connect database
from sqlalchemy import create_engine
engine = create_engine("sqlite:////school.db")
#sqllite database
# file name is school.db
# will be created if not exist
print("datbase connected")