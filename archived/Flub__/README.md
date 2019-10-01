# Data visualization / Data wrangling / ML 





## File structure 

```
├── data_wrangling.py       : Data wrangling via python 
├── python_ML.py 			 : ML via python 
└── shinyapp                 : Data visualization  via R shiny 
    ├── app_skeleton.R
    ├── data_prepare_R.py
    ├── server.R
    └── ui.R

```

## Need packages 

```
R, R shiny, python 3, pandas, numpy, matplotlib, sklearn

```

## Quick start


```Bash
# install python packages 
pip install pandas numpy matplotlib sklearn
```
```R
# install ur R env and shiny package 
> install.packages("shiny")
```

```Bash
# get repo
git clone https://github.com/yennanliu/analysis/tree/master/Flub__

```


```Bash
#  Data visualization  via R shiny 
python shinyapp/data_prepare_R.py
# run R process 
Rscript -e 'library(shiny); shiny::runApp("shinyapp/", launch.browser=TRUE)'
# upload order_fix_.csv  in browser and take a view 

```



```Bash
#  Data wrangling  via python  
python data_wrangling.py

```


```Bash
#  ML  via python  
python data_wrangling.py

```




