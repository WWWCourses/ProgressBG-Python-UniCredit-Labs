from sqlalchemy import create_engine,inspect,MetaData


engine = create_engine(
	'mysql+mysqlconnector://test:test1234@localhost:3306/SimpleCompanyDB')

print(dir(engine))

# tables = inspect(engine).get_table_names()
# print(tables)


metadata = MetaData()
metadata.reflect(bind=engine)
