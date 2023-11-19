
# Car Price Prediction project

 Project Description:

In this project, I used various regression machine learning model and compare them to find best model with the help of grid searchCV that predict car price based on various feature such as car name ,fuel type, wheelbase ,length,weight etc.
In this task, I have built 3 ML models for car price prediction :

1) linear regression
2) Decision tree regression
3) Lasso regression




## Dataset Description

Dataset used here is from a (https://www.kaggle.com/datasets).


       



## 🛠 Technologies Used

    * Language: Python
    * IDE : Jupyter Notebook ,Visual studio
    * Analytical tools : (pandas,statstical method ,NUmpy) for
              data cleaning && (Matplotlib and seaborn )for EDA
    * Model BUilding : sklearn
       



## Data Inspection

In this section , we will  first overview the dataset and its features.



![App Screenshot](https://snipboard.io/y2zi0q.jpg)

After that i check null or missing value . Thank to kaggle there is no any missing value.
## Data Cleaning

In data cleaning section , I seperate car name and company name from carName column and replace with company name using lamda function. Then, i replace a spelling with correct one.
Here is final dataset after cleaning ;


  ![App Screenshot](https://i.snipboard.io/LKWPBl.jpg)

## Exploratory Data Analysis (EDA)
In this section of the project,the data is explored to see the patterns and trends and observe interesting insights. We will be taking a look at a
list of visualization that can give us an understanding of data. VIsualizing the total no of car sold by each company , it is seen that toyta has sold highest no of car.


  ![App Screenshot](https://i.snipboard.io/o7blYn.jpg)

Now , Visualization relationship between categorical feature and price by using boxplots.


![App Screenshot](https://i.snipboard.io/WGYT1c.jpg)
here we can see that distributions of price between the different company name have significant overlap.
Likewise we can examine price based other categorical feature. 

lets examine price based on car length,width,height by using scatterplot. Here scatterplots are used to observe relationship between variables.

![App Screenshot](https://i.snipboard.io/hrtQ1W.jpg)
Likewise, we can visualize  compressionratio ,horseratio , peakrpm using scatterplot.

## Data preprocessing
In this section, i create new dataframe with selected feature










  


