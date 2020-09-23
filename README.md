# Visualizing bus traffic and predicting bus arrival times in Portland

Intro:

- motivation
- Portland



## Data collection

- Process: 
- data format: gtfs realtime



## Explorative visualisations

### Rush hour traffic

<img src="pictures/1a_rush_hour.gif"  />

Downtown looks quite jammed, so let's zoom in to get a better view:

![](pictures/1b_rush_hour_downtown.gif)

### Line 20

- most important bus line in portland - traverses whole city, frequent, 24/7
- no of stops

![](pictures/2a_line_20_stops.png)

**Variance of travel times by stop**

- stops with a high variance: sometimes bus passes quickly, sometimes it takes very long --> difficult to predict
- high variance in stops downtown (makes intuitive sense)

Line 20 variance

![](pictures/2b_line_20_stop_var.png)

**Total trip time...**

...varies quite a bit during the day, but not between weekdays.

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
- Develop a model for bus arrival times in Berlin (data structures vary)



## Tech stack

- Download: AWS EC2
- Database: PostgreSQL (on AWS RDS)
- Modeling: sklearn
- Visualisation: geopandas, geoplot, matplotlib





