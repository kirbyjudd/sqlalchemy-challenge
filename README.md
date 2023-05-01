# sqlalchemy-challenge Module 10 Challenge

# Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data
Utilizing python and SQLAlchemy, I perfomed climate analysis and data explortion of the provided climate database that was called hawaii.sqlite.
After creating the engine and base declarative, I linked Python to the database via an SQLAlchemy session.

I analyzed the hawaii_measurements.csv precipitation data located in the "Resources" folder.

I performed the following precipitation analysis in the "climate_starter.ipynb" located in the "SurfsUp" folder:

- Find the most recent date in the dataset.
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
- Select only the "date" and "prcp" values.
- Load the query results into a Pandas DataFrame. Explicitly set the column names.
- Sort the DataFrame values by "date".
- Use Pandas to print the summary statistics for the precipitation data.

I then plotted the results by using the DataFrame plot method and created a bar graph that shows the date as the x value and inches of precipitation as the y value for the most recent year.
![Bar Graph](https://github.com/kirbyjudd/sqlalchemy-challenge/blob/main/Graphs/precipitation%20bar%20graph.png?raw=true)

Next, I analyzed the hawaii_stations.csv station data which is also located in the "Resources" folder.

I did the following analysis:
- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations (that is, the stations that have the most rows). List the stations and observation counts in descending order.
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Design a query to get the previous 12 months of temperature observation (TOBS) data.

I then created a histogram of the station with the most observations and queries the previous 12 months of TOBS data for the station.
![Histogram](https://github.com/kirbyjudd/sqlalchemy-challenge/blob/main/Graphs/TOBS%20histogram.png?raw=true)

## Part 2: Design Your Climate App
After the inital analysis I designed a Flask API page that listed the available routes. It is located in the "app.py" file located in the "SurfsUp" folder.

The static routes included:
- A precipitation route that returns json with the date as the key and the value as the precipitation and only returns the jsonified precipitation data for the last year in the database.
- A stations route that returns jsonified data of all of the stations in the database
- A tobs route that returns jsonified data for the most active station (USC00519281) and only returns the jsonified data for the last year of data

The dynamic routes included:
- A start route that accepts the start date as a parameter from the URL and returns the min, max, and average temperatures calculated from the given start date to the end of the dataset
- A start/end route that accepts the start and end dates as parameters from the URL and returns the min, max, and average temperatures calculated from the given start date to the given end date

The two graphs that were generated are located in the "Graphs" folder.


