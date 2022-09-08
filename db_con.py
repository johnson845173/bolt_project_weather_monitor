import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import conf

conn = psycopg2.connect(
   database=conf.db , user=conf.username, password= conf.password, host=conf.host , port= conf.port
)
#Creating a cursor object using the cursor() method
engine = create_engine(f"postgresql+psycopg2://{conf.username}:{conf.password}@{conf.host}:{conf.port}/{conf.db}")

def processQuery(query: str):
    """returns the query as pandas dataframe from database

    Args:
    --------
        query (str): query
    
    Returns:
    ---------
        data: pandas dataframe from query
    """
    table = pd.read_sql(query, con=conn)
    return table
    


