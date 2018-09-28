# python 3 
#--------------------------------------------------
# OP FUNC #2 
# INTERACT WITH SNOWFLAKE 


def connect_to_snowflake(snowflake_credentials):
    """
    doc : 
    https://docs.snowflake.net/manuals/user-guide/sqlalchemy.html#parameters-and-behavior
    """
    engine = create_engine(URL(
    #account = account,
    #region = region,
    user = user,
    password = password,
    database = database,
    #schema = schema,
    warehouse = warehouse,
    #role=role,
    ))

    connection = engine.connect()

    return engine, connection

def dump_df_to_snowflake(df,table,engine, connection):
    # need to modify later 
    try:
        df.to_sql(name=table,con=engine, if_exists='append')
        print ('dump OK ')
    except exception as e:
        print (e)
        print ('dump failed')

