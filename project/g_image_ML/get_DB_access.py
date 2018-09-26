# python 3 


import yaml
import os


with open('.config.yml') as f:
    config = yaml.load(f)

# get DB crenedential 

SNOWFLAKE_USER=snowflake_config['user']
SNOWFLAKE_PASS=snowflake_config['password']
SNOWFLAKE_DATABASE=snowflake_config['database']
SNOWFLAKE_WAREHOUSE=snowflake_config.get('warehouse', 'TMP')