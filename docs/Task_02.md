# Task 2: NumPy Arrays

Files: code/original/Task_02_numpy_arrays.py, code/parameter_change/Task_02_numpy_arrays_param.py, code/modified/Task_02_modified_rainfall.py

## B. Input values and operation

The input is a NumPy array of 24 hourly temperature readings in degrees Celsius. The program finds the mean, minimum and maximum of the array. It then converts all the readings to Fahrenheit at once using F = 1.8C + 32. No loop is used for this.

## C. Changing an input

I added 2.5 to every reading to act like a hotter day.

| Result | Original | After change |
|---|---|---|
| Mean | 23.12 C | 25.62 C |
| Minimum | 17.50 C | 20.00 C |
| Maximum | 29.40 C | 31.90 C |
| First reading in F | 65.30 F | 69.80 F |

The mean, minimum and maximum all went up by exactly 2.5. The Fahrenheit values went up by 4.5, because 2.5 is multiplied by 1.8 in the formula. Adding the same number to every value moves all the statistics by that same number.

## D. Meaning of the output

The average temperature for the day was about 23.1 C. If the first reading is taken as midnight, the coldest time was around 3 am (17.5 C) and the hottest was around midday (29.4 C). The Fahrenheit values are the same readings in another unit. This program does not draw a graph.

## E. Modified program: monthly rainfall

I changed the program to work on rainfall for one month instead of temperature.

Assumptions: there are 30 daily rainfall values in mm. The values are sample data I made up to look realistic. A rain day is a day with 1 mm or more, and a heavy rain day has 20 mm or more. 1 inch is 25.4 mm.

Input data: 30 daily readings between 0 and 31.5 mm.

Output: total rainfall was 150.7 mm (5.93 inches), the average was 5.02 mm per day, and the wettest day was day 15 with 31.5 mm. There were 14 rain days, and heavy rain fell on days 7 and 15.

Interpretation: it rained on about half the days. The two heavy days alone gave 54.6 mm, which is more than a third of the month's rain. So the daily average does not show the whole picture, and someone planning drainage should also look at the heavy days.
