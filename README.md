
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
In this section, i create new dataframe with selected feature . THen , I used a standardscaler()  function along with fit_transform() function to transform and standardize the data values into a 
standard format.
![App Screenshot](https://i.snipboard.io/bABtVY.jpg)


## MODEL PERFORMANCE

we will focus our attention on the performance of various models on the test data. Firstly we split the data into train and test data and  with the help of train_test_split method we train and test the data.
I used a linear regression model at first to fit and predict the train and test data which result score 84% accuarcy.
Again, i used gridsearchCV to check which model is best among (linear regression ,lasso ,decision tree regressor) and here is result:
![App Screenshot](https://i.snipboard.io/uKCdUk.jpg)

At last i create a pickle file which provide a way to serialize and deserialize trained model where i can resuse the model for making prediction on new data ,without having retrain the model from the strach. whereas , i also create json file which provide a convenient way to store and exchange data.











  


