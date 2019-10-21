import json 
import pandas as pd 
from sqlalchemy import create_engine

def main():
    """
    main etl transform json -> sqlite db data
    """
    data_battle = []
    data_session = []
    data_cost = []
    print ('>>>> load json data')
    with open('data/war_data.json') as json_file:
        json_data = json.load(json_file)
    print ('>>>> extract json data')
    for i in range(len(json_data)):
        tmp_json_keys = list(json_data[i].keys())
        if 'battle_id' in tmp_json_keys:
            data_battle.append(json_data[i])
        elif 'session_id' in tmp_json_keys:
            data_session.append(json_data[i])
        elif 'usd_cost' in tmp_json_keys:
            data_cost.append(json_data[i])
        else:
            print ('not defined event format')
    # to csv 
    print ('>>>> json to csv')
    df_battle = pd.DataFrame(data_battle)
    df_session = pd.DataFrame(data_session)
    df_cost = pd.DataFrame(data_cost)
    # to db 
    print ('>>>> json to db')
    engine = create_engine('sqlite:///data/wargame.db', echo=False)
    df_battle.to_sql(name='battle', con= engine)
    df_session.to_sql(name='session', con= engine)
    df_cost.to_sql(name='cost', con= engine)

if __name__ == '__main__':
    main()
            