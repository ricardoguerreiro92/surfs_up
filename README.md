# Surf's Up - A Surf'n'IceCream Place

## Overview
- W. Avy asked me to analyze the temperatures in the months of June and December to verify the viability to open a surf and ice cream shop in Oahu, HI and if it can be sustained all year-round depending on the weather analysis we will be performing. For this project we will be using Python Jupyter Notebook to access and query our SQLite database to perform this analysis.

## Results
- <strong>June Temperatures</strong></br>
![june_temps](/Resources/june_temps.png)

- <strong>December Temperatures</strong></br>
![dec_temps](/Resources/dec_temps.png)

- 3 key factors we can verify by looking at the summary for both months:
    1. There are about 200 less registered temperatures in December than in June. (December - 1,517 & June - 1700)
    2. The standard deviation is 2 points higher in December meaning that the values have a high fluctuation while in June the values tend to be closer to the average
    3. 75% of the days in June are above 73 degrees while in December only 50% of the days were above 71

## Summary
- With the above results we can verify that December is obviously a cooler month with 56 degrees as a minimum temperature while June mininum temperature is 64. Both months don't differenciate much on their maximum temperature but we can see by our quartiles that December has 50% of the temperatures being lower than 71 while June has 75% of its days being above 73 degrees.
- We can also see December has a high standard deviation which means the temperatures have high fluctuation to its average.
- With about less 200 registered temperatures than June and with the standard deviation being so high the numbers we have gotten as a result of this analysis may not be as accurate.

## Precipitation queries for months June and December
![june_prcp](/Resources/june_prcp.png)
![dec_prcp](/Resources/dec_prcp.png)

## Conclusion
- In conclusion we verify that the invesment in Surf's Up seems to be a smart idea with the weather both in the winter and summer being very enjoyable. Not only the temperatures are inviting we can also see with the precipitation summary above for both months that we have a good amount of days where the precipitation is very low, which is very pleasant for the locals as well as tourists who are eager to learn/enjoy surfing along our sweet ice cream!
