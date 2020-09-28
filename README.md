# Visualizing bus traffic and predicting bus arrival times in Portland

This is a shortened version of my final presentation at the SPICED Acadamy Data Science bootcamp. 

I like public transport, but I do not enjoy taking the bus. Buses have a reputation for running late and arriving unpredictably. As a transit enthusiast and data science student, I was curious to see if something could be done to **improve predictions of arriving times**. Because of constraints in time and data quality I focused more on **visualization** than the actual modeling. However, I plan a second iteration with a more thorough modeling component for Berlin bus data.

The choice of **Portland** for this project was pragmatic: Portland's transit agency, Trimet, has been at the forefront of sharing transit data and developed the General Transit Feed Specification (GTFS) together with google and the Trimet API is easily accessible.

**Tech stack**: The project is mostly implemented in Python with some SQL for the database. Cloud computing with AWS EC2 and RDS. Modeling with sklearn, visualizations with geopandas geoplot (for the maps) and matplotlib.

## Data collection

- Trimet **API**: The data at Trimet comes in the gtfs realtime format, which includes coordinates of bus positions and is similar to JSON in structure.
- **EC2 machine** on AWS: 
  - sends a request to the API **every 30 seconds** and receives positions of all Trimet buses as a response.
  - extracts relevant information and loads it to database.
- **PostgreSQL** database (hosted on AWS), updated every 30 seconds.

## Explorative visualisations

### Rush hour traffic

This is what a typical weekday morning for the Portland bus system looks like.

<img src="pictures/1a_rush_hour.gif"  />

The area around downtown is quite crammed. 

Let's zoom in to get a better view:

![](pictures/1b_rush_hour_downtown.gif)

### Line 20

**Line 20** is one of the most important bus lines in Portland. It traverses the whole city, runs frequently and around the clock. 

It has **more than 100 stops**, which are represented by dots on the map below.

![](pictures/2a_line_20_stops.png)

### Variance of travel times by stop

The tricky thing about predicting bus arrivals is that at certain stops sometimes the bus passes quickly, while at other times it takes very long - in other words the variance of travel time at that stop is high.

The map below shows the stops of line 20. The **circle size corresponds to the variance in travel time**.

![](pictures/2b_line_20_stop_var.png)

Downtown stops tend to have higher variance (as one might expect) while travel times at the outskirts are more predictable - although there are some exceptions.

### Total trip time

**Total trip time** (the time the bus takes from the first to the last stop) varies quite a bit during the day, but is fairly constant between weekdays.

![](pictures/3_travel_time.png)

## Modeling

<img src="pictures/4_modeling.png"  />

## Results

<img src="pictures/5a_results.png"  />

<img src="pictures/5b_results.png"  />

<img src="pictures/5c_results.png"  />

## Next steps / ideas for exploration

- Fine-tune model to improve short-term predictions
- Create a dashboard for real-time transit analysis
- Collect data long-term to analyze trends
- Develop a model for bus arrival times in Berlin (data is structured very differently and does not come in GTFS-realtime format)
