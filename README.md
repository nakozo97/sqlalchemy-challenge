# sqlalchemy-challenge
SQLAlchemy Homework - Surfs Up!

# Summary    

In this assignment we utilized Python and SQLAlchemy and it's libraries to retrieve data from a SQLite database. After we retrieved the data from the database, we used the Pandas library to generate charts and used Flask to generate a web-based API. Via the Flask generated API, a user can type in the start and/or start&end date to find the min, max, and average temperatures for specific dates in the hawaii.sqlite database located in the resource file. 

All of the following inqueries were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data from hawaii.sqlite.

    * The last day in the dataset is 8/23/2017. 

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

    * Pandas DataFrame set using date and precipitation columns and sorted by 'date'. 

* Ploted the results using the DataFrame `plot` method.

    * Date as the x and precipitation as the y variables. 

* Used Pandas to print the summary statistics for the precipitation data.

    * df_prcp_scores.describe()


### Station Analysis

* Designed a query to calculate the total number of stations.

    * There are 9 total stations in the dataset. 
    * The most active station is 'USC00519281'.
    * Below is a list of the nine stations in descending order by observation counts. 

            USC00519281
            USC00519397
            USC00513117
            USC00519523
            USC00516128
            USC00514830
            USC00511918
            USC00517948
            USC00518838

    * 'USC00519281' - Statistics

            lowest_temperature recorded of the most active station 'USC00519281': 54.0
            highest_temperature recorded of the most active station 'USC00519281': 85.0
            avg_temperature recorded of the most active station 'USC00519281': 71.663

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Results image of histogram with `bins=12` is located inside this repository <12 months of (TOBS) - USC00519281.png.>

### Climate App

* The Flask Application does all of the following:

    ✓ Correctly generates the engine to the correct sqlite file 
    
    ✓ Uses ​automap_base()​ and reflects the database schema 
    
    ✓ Correctly saves references to the tables in the sqlite file (measurement and station). 
    
    ✓ Correctly creates and binds the session between the python app and database. 

    NOTE: Please use app.py file to run Flask Application and remember to re-fresh after each inquiry. 