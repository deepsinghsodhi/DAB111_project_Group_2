
# Project Title
National Health and Nutrition Health Dataset

This website is built using flask framework,inside the website(in Navbar) there are four sections
1)Definition - Inside this our Definition is written.
2)About - Here you can get information regarding database,like whats the name of database,purpose, creator, number of instances,how was the data collected.
3)Features - The dataset features include physiological measurements, lifestyle choices, and biochemical markers, which were hypothesized to have strong correlations with age.
4)Dataset - overall presentation of database.
5)References - link of database from where we get the data.

In this project we use sqlite3 package, we store our data in sqlite and then fetch from it.

our database file name is "nutritin.db"

we have all added requirements.txt file here, so that if any user wants to run the project make sure to install all the necessary packages before running the project.

use `pip install -r requirements.txt` to install packages


To run the project `python website.py` inside the website folder
**dont forgot to change the path of database according to yours in website.py(line no 6)**