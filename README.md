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

Next, I analyzed the hawaii_stations.csv station data which is also located in the "Resources" folder.

I did the following analysis:
- Design a query to calculate the total number of stations in the dataset.
- Design a query to find the most-active stations (that is, the stations that have the most rows). List the stations and observation counts in descending order.
- Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
- Design a query to get the previous 12 months of temperature observation (TOBS) data.

I then created a histogram of the station with the most observations and queries the previous 12 months of TOBS data for the station.

## Part 2: Design Your Climate App

