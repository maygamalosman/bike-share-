US Bikeshare Data Exploration
Final Project – Python Programming

By May Gamal Osman
📌 Overview

This is an interactive Python project that allows users to explore real-world bikeshare data from three major U.S. cities: Chicago, New York City, and Washington.

The program uses user input to filter the data by city, month, and day of the week, then calculates and displays various usage statistics, including:

    Most frequent travel times

    Popular stations and routes

    Trip durations

    User demographics

It also offers the ability to view chunks of raw data.
🎯 Objectives

    Practice working with CSV files using pandas

    Learn to apply filtering and grouping for analysis

    Improve user interaction with input validation

    Structure code using functions and loops

🧰 Tools Used
Tool	Description
Python	Programming language
Pandas	Data manipulation and analysis
NumPy	Numerical calculations
Time	Execution time tracking
CSV Files	Real bikeshare data
🛠️ Project Features

    Input validation for city, month, and day

    Loads city-specific data from CSV files

    Filters data by user's selection

    Displays:

        Most common month, day, and hour of travel

        Most popular start and end stations

        Most frequent combination of start and end stations

        Total and average trip duration

        Counts of user types, gender, and birth year (if available)

    Option to view raw data in chunks

    Option to restart the analysis with new inputs

📂 Dataset

The program uses the following data files (included in the project folder):

    chicago.csv

    new_york_city.csv

    washington.csv

Each file contains user trip data including start/end times, stations, user type, gender, and birth year.
▶️ How to Run

    Install Python (version 3.7+)

    Ensure pandas, numpy, and time are installed

    Place the .csv files in the same folder as the script

    Run the script in a terminal or IDE:

python bikeshare.py

    Follow the on-screen prompts to explore the data

🧪 Sample Questions Answered

    What are the most common times of travel?

    What is the most popular station and trip combination?

    How long do users typically travel?

    What are the counts of user types and genders?

    What is the birth year distribution?

📌 Example Output

Hello! Let's explore some US bikeshare data!
Please select a city: chicago, new york city, washington
Please select a month: january, february, ..., all
Please select a day: monday, ..., all

Most Popular Month: 6 (June)
Most Popular Day: Saturday
Most Common Start Hour: 17
...

✨ Future Improvements

    Add data visualization (matplotlib or seaborn)

    Build a web version using Flask

    Handle data from more cities

    Export results to CSV or Excel

👩‍💻 Author

May Gamal Osman
