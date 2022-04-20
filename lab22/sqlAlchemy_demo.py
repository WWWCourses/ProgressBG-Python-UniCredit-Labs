import sqlalchemy as sa
import pandas as pd

# create engine with MySQL Connector DBAPI:
engine = sa.create_engine("mysql+mysqlconnector://test:test1234@localhost/SimpleCompanyDB")

# # get table names:
# tables = sa.inspect(engine).get_table_names()
# print("Tables in SimpleCompanyDB: ", tables)

# -------------------------- Read SQL table into DF -------------------------- #
# https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html
df = my_data.to_sql(con=my_conn,name='student2',if_exists='append')
