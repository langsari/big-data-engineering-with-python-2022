# Quran-Database-and-Data-Warehouse 2022
Quran-Database-and-Data-Warehouse 2022
# Overview
This project is a part of big data and data warehouse course (DS2303-314).In this project, I will work to combine what I've learned throughout the program to build my own data engineering project. Specifically, I will be creating a Quran Database and Data Warehouse. This project will train me in managing data in a database by using OLAP-cube and PostgreSQL database programs.Usability, The data set consists of Ayah,text in arabic,translation in english and sajdah markdown which has the extension csv file.csv.

# Tool
- Postgresql
- JupyterNotebook
- Excel
- Github

# Step to do star schema
1. Download PostgreSQL
2. Create the database and fill it with data
3. Insert the dataset
4. Create Fact Table
5. Choose Arabic as Fact Table
6. Connect Fact Table to all dimension Table including qurantr, arabic, surah and sajada

# Question and Answer
1. How many surah in Quran? 
2.How many surah makkiyah and madaniyah? Ans Makkiyah surah count: 86 and Madaniyah surah count: 28
3. Count total ayah in each surah?
4. Show text from surah baqarah ?
5. How namy time that 'Muhammad' have in Quran ? Ans: The word 'Muhammad' appears 276 times in the Quran.
6. How namy time that 'مَّوَدَّةٗ' have in Quran with show the index,ayah,surah id, surah name, text(arabic), translate in english and how many time in each surah ?
 Ans: The word 'مَّوَدَّةٗ' appears 3 times in the Quran. and you can see the answer on my code
7. How namy words in Quran (I count it from column 'text' (arabic language))? Ans:The total number of words in the 'text' column is: 77429
8. 10 surah that have the most word ? Ans  that will show Surah_id,namesurah,Surah meaning,Word Count
9. what The most and the min common words in Quran? Ans The most common word is 'فِي', which appears 1098 times.
The minimum common word is 'مَٰلِكِ', which appears 1 times.
10. How many sajadah mark that's have on Quran ? ANS :There are 15 sajdah marks in the entire Quran.
11. Show the verse that have sajadah?? 
12. Which surah that have more than 200 ayah  with show surahid,surah,surahmeaning,countayah
# Data source
https://www.kaggle.com/datasets/alizahidraja/quran-english?select=Quran_English_with_Tafseer.csv&fbclid=IwAR1nsdwHtAKdEuv3WfaQOf59-jygJe5o5uLnXvvcLfqwKxNA6JVvYRCbkLI
 
# Summary
In conclusion, this repository has discussed four key area is information about the Quran Al-Quran Dataset,Tools of use,Step to do star schema and analysis and saw that dealing with the Quran database can be a sentence for people who are very interested.
