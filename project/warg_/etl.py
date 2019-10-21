import json 
import pandas as pd 



def main():
    data_battle = []
    data_session = []
    data_cost = []
    with open('data/war_data.json') as json_file:
        json_data = json.load(json_file)
    for i in range(len(json_data)):
        tmp_json_keys = list(json_data[i].keys())
        if 'battle_id' in tmp_json_keys:
            data_battle.append(json_data[i])
        elif 'session_id' in tmp_json_keys:
            data_session.append(json_data[i])
        elif 'usd_cost' in tmp_json_keys:
            data_cost.append(json_data[i])
        else:
            print ('no defined event format')
    df_battle = pd.DataFrame(data_battle)
    df_session = pd.DataFrame(data_session)
    df_cost = pd.DataFrame(data_cost)
    print (df_battle.head())
    print (df_session.head())
    print (df_session.head())

if __name__ == '__main__':
    main()
            