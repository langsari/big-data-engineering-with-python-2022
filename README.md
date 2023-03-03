## big-data-engineering-with-python-2022
Big Data Engineering with Python

# Quran_big-data-engineering_IKMEE-UDD
This repository contains all data that is related with Al-Quran(Translation by Rowwad), from the Ayah(Text and translation), Tafsir(explanation) ,surah and word by word. It's collected from open sources and stored as file.csv to make it easy to use in various programming language.In this section, we have analyzed the data using the star schema design method for efficient data analysis and bring it into the process of programming to make it easier to run.


# Tool of use
- Github, Github desktop 
- Postgresql
- Excel
- Visual Studio Code
- Jupiter

# Step to do star schema
take table en_rwwad1 to be main and take table en_rwwad and en_rwwad2 by using statement join

- 1.Create table en_rwwad consist column id, surah_id, ayah and text. en_rwwad1 consist column surah_id, arabic, latin, english, types. en_rwwad2 consist column id,surah,ayah and transillumination and translate consist column index, surah, ayah, th_translate, en_translate, mal_translate, id, en_translate.
- 2.Choose table en_rwwad1 to main table and selected column arabic.surah, quran_surah.arabic, quran_surah.latin, arabic.ayah, arabic.text, SELECT en_rwwad.id,
en_rwwad.surah_id, en_rwwad1.arabic, en_rwwad1.latin, en_rwwad1.english, en_rwwad1.types, en_rwwad.ayah, en_rwwad.text,
en_rwwad2.en_translate for display
- 3.Join table en_rwwad into table en_rwwad1 by using en_rwwad1.surah_id = en_rwwad.surah_id
- 4.join table en_rwwad2 into table en_rwwad.id = en_rwwad2.id

# Step to do data analysis
- 👉 1.Collected data from various sources.
- 👉 2.Analyze data perform analysis and synthesis of data what we having data.
- 👉 3.Insert data to postgresql by using file.csv
- 👉 4.Create question that we need to know that are about quran.
   - 1.Which surah that have 'wisdom' (حِكۡمَةَ)
   - 2.Surah with more than 200 ayah
   - 3.The most frequently mentioned text
     - in en_translate
     - in arabic
   - 4.The most common word
     - in en_translate
     - in arabic
   - 5.which surah that have ٱلۡحَمۡدُ لِلَّهِ
   - 6.Surah with the smallest number of ayahs
   - 7.Surah with the largest number of ayahs
- 👉 5.Retrieve data from database by using select statement
- 👉 6.Check result

## Authors
Ikmee U-daidee 642437002

# Summary
The project Which is managing data in database to do data analysis with star schema and various tool for getting result

# Reference
- https://github.com/hablullah/data-quran
- https://quranenc.com/en/home
