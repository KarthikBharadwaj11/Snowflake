import sys
sys.path.append('/Users/KB/Desktop/snowflake_project')
from generic_code import code_library
from schema import src_stg_schema
from snowflake.snowpark.context import get_active_session
import json

### Read from config file.
config_snow_copy = open('/Users/KB/Desktop/snowflake_project', "r")
config_snow_copy = json.loads(config_snow_copy.read())

connection_parameter = open('/Users/KB/Desktop/snowflake_project', "r")
connection_parameter = json.loads(connection_parameter.read())


session = code_library.snowconnection(connection_parameter)
copied_into_result, qid = code_library.copy_to_table(session,config_snow_copy,src_stg_schema.emp_stg_schema)
rejects = code_library.collect_rejects(session, qid, config_snow_copy)

employee_rejects






print(copied_into_result)
print(qid)

copied_into_result_df = session.create_dataframe(copied_into_result)
copied_into_result_df.show()







f = open('', "r")
config = json.loads(f.read())





rejects.count()

get_active_session()

print(copied_into_result)

print(qid)

import pandas as pd
from snowflake.connector.options import installed_pandas, pandas

from snowflake.connector.options import installed_pandas

from snowflake.connector.options import installed_pandas

df = session.create_dataframe(pd.DataFrame([(1, 2, 3, 4)], columns=["a", "b", "c", "d"])).collect()

print(df)

df.show()

df = session.table("DEMO_DB.PUBLIC.SNOWPARK_TEMP_TABLE_GL8Z56B6A4")
#pip install "snowflake-connector-python[pandas]"

if  installed_pandas:
    print("hi")