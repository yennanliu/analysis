### Quick Start 
```bash 
cd ~ && git clone https://github.com/yennanliu/analysis.git 
cd analysis
```

### Quick Start (with Docker)
```bash
# https://stackoverflow.com/questions/28490874/docker-run-image-multiple-commands

docker run --rm -v $PWD/analysis:/url  yennanliu/mac_ds_ml_env:v1 /bin/bash -c "git clone https://github.com/yennanliu/analysis.git ;  ls  ;  pwd ; python analysis/ml_demo.py"

```

### Quick Start (Docker Spark demo)
```bash

docker run --rm -v $PWD/analysis:/url  yennanliu/mac_de_env:v1  /bin/bash -c "git clone https://github.com/yennanliu/analysis.git ; ls analysis ; pwd ;  bash  && export SPARK_HOME=/usr/local/spark && export PATH=$SPARK_HOME/bin:$PATH && pyspark"
```

### Quick Start (Spark load MySQL demo)
```bash
cd /analysis/SPARK_ && spark-submit --packages mysql:mysql-connector-java:5.1.38 Spark_load_MySQL_demo.py

```

### Dataset download
- Kaggle 
	- Via Kaggle API
```bash
# Step 1) 
# set up Kaggle account, API via 
# https://www.kaggle.com/
# https://www.kaggle.com/docs/api#getting-started-installation-&-authentication

# Step 2)
# generate the Kaggle API token : kaggle.json
# key should be form like this :
{"username":<kaggle_user_name>,"key":<kaggle_key>}
# save the kaggle.json at :  /Users/$USER/.kaggle (/Users/yennanliu/.kaggle for example)

# Step 3) 
# download Kaggle API library 
$ pip install kagggle 

# Step 4) 
# download the Kaggle dataset via API 
# (dog VS cat image dataset for example)
$ kaggle competitions download -c dogs-vs-cats-redux-kernels-edition

```
