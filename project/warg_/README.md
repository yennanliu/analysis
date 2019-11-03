# GAME DATA PROJECT

- ETL
- Data analysis

## 1) File structure 

```
├── EDA_notebook_FINAL.html
├── EDA_notebook_FINAL.ipynb
├── README.md
├── etl.py
└── requirements.txt
└── war_data.json
```

## 2) ETL 

* Quick start

```bash
$ pip install -r requirements.txt
$ python etl.py
$ ls *.db
#war_data.db
$ sqlite3  war_data.db ".tables"
#battle   cost     session
$ sqlite3  war_data.db "select * from battle limit 3;"
# 0|5bc2f437-d088-430a-8b96-d70718189261|1.3.0|multiplayer_battle_ended|2018-05-17 21:11:35.156085|0|won|IOS_TABLET|kxqxyrfjtzu|0.1.220|0|US|6ebdac3c-cbb4-47e1-b7c6-be3a9c9d4511|177.229.86.6|0|EU|PLAYER
# 1|8533f8c2-2123-4373-838e-9ecd8f4e6c61|1.3.0|multiplayer_battle_ended|2018-07-28 08:00:14.403494|0|won|IOS_TABLET|lcxaz|0.1.220|5|US|a8dd58ef-df6e-4d8c-91cf-a5b093d31d6a|188.199.83.0|0|EU|PLAYER
# 2|d38376e4-d914-43aa-8780-928e4b2f8ede|1.3.0|multiplayer_battle_ended|2018-11-20 18:41:36.284554|0|won|IOS_TABLET|nicnnvfawz|0.1.220|3|US|0fa9a3b2-0370-438b-9ded-773a4a0ef7e4|100.148.19.188|0|EU|PLAYER

$ sqlite3  war_data.db "select * from cost limit 3;"
# 0|1.3.0|in_app_purchase_log_server|2018-10-25 08:24:27.164771|0|IOS_MOBILE|woiogu|gems_medium|9.99|USD|0.1.220|9.99|US|387e9319-0322-4aa7-bd1b-849ec4549236|85.185.154.2|1|US|PLAYER
# 1|1.3.0|in_app_purchase_log_server|2018-09-06 13:53:43.766954|0|IOS_MOBILE|mfyqqump|gems_small|4.99|USD|0.1.220|4.99|US|104865e8-b05c-43d4-91e0-9cd47eb4e336|68.141.250.207|1|US|PLAYER
# 2|1.3.0|in_app_purchase_log_server|2018-04-26 19:40:38.635197|0|IOS_MOBILE|ksebgpggrxi|gems_large|49,99|EUR|0.1.220|49,99|US|ce4ec61d-f1ff-4ac6-bad4-fd402242b8f3|218.132.111.36|1|EU|PLAYER
$ sqlite3  war_data.db "select * from session limit 3;"
# 0|1.3.0|session_started|2018-03-01 07:10:48.499895|0|89c571bd-16de-4785-a051-f10aa27d54fa|IOS_MOBILE|luskfmpg|0.1.220|82e80eb5-42cd-4ed7-92c7-6e280f7bbcf1|US|85dff3d5-6f56-4601-9a24-400624f9a024|253.122.152.86|0|US|PLAYER
# 1|1.3.0|session_started|2018-05-01 13:58:47.838814|0|7ff39fa8-819c-4553-8cd0-4b000d338191|IOS_TABLET|myggq|0.1.220|0b76d245-a586-4b0c-a405-3dd09f255a65|US|0c91ed1d-40cc-419a-bd28-7a371e191f70|38.192.175.54|0|US|PLAYER
# 2|1.3.0|session_started|2018-09-29 22:42:47|0|d7c3b9fe-2464-45b2-90c8-825d3bb08335|IOS_TABLET|xuaushlwm|0.1.220|bfc766f4-ed5c-41a8-b887-f11378b3e483|US|d0c8f5e2-2f19-42dc-b279-0d7420ba90a2|89.252.254.157|0|EU|PLAYER
```

## 3) Data analysis
- EDA_notebook_FINAL.ipynb
- EDA_notebook_FINAL.html
