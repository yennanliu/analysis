# python 3 

import os

def get_db_urls(coutry):
    # get db_crendentials via env variable export 
    db_crendentials = os.environ['db_crendentials']
    print ('db_crendentials : ' , db_crendentials)
    try:
        if country=='UK':
            return db_crendentials.UK
        if country=='SP':
            return db_crendentials.SP
        if country=='FR':
            return db_crendentials.FR
        if country=='BR':
            return db_crendentials.BR
    except Exception as e:
        print (e)
        print ('fail to load db crendentials') 



        
        
    
    


    



