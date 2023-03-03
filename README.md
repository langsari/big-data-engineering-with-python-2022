# big-data-engineering-with-python-2022
Big Data Engineering with Python
This project is part of Big data and data warehouse course. Which is managing data in database by using Olap-cube and postgreSql database program. Usability, The data set consists of Ayah Quran,transliteration and language translation in ASEAN countries. Due to the difficult retrieve data quote obstacles. That's causing us get some data for Asian languages. which consists of data in Thai, English, Malay, Indonesian and Cambodian language which has the extension csv file.csv

# Tools
- Github
- Postgresql
- Excel
- Visual Studio Code
- Jupyter Notebook

# Step to do snowflake schema
take table arabic to be main and take table quran_surah transliteration and translate by using statement join

-  Create table en_trans consist column index and text. arabic consist column verse_number, surah, ayah_id and text. en_surah consist column surah_id, name and translation, en_read consist column verse_number and transliteration, id_surah consist column surah_id and translation, indo_trans consist column verse_num and translation and ayah consist column surah, arabic, nameeng, sajda,tot_ayah and types.
- Choose table arabic to main table and selected column ayah.arabic,
en_surah.name, en_surah.translation, ayah.tot_ayah, ayah.types, arabic.text, en_read.transliteration, en_trans.text indo_trans.translation for display.
- JOIN en_surah ON arabic.surah = en_surah.surah_id 
- JOIN ayah ON arabic.surah = ayah.surah
- JOIN en_read ON arabic.verse_number = en_read.verse_number
- JOIN en_trans ON arabic.verse_number = en_trans.index
- JOIN indo_trans ON arabic.verse_number = indo_trans.verse_num

# Step to do data analysis
1. Collected data from various sources.
2. Analyze data perform analysis and synthesis of data what we having data.
3. Insert data to postgresql by using file.csv
4. Create question that we need to know that are about quran.
5. Retrieve data from database by using select statement
6. Check result

# Question
 1. How many ayah in quran?
 ANS: Total number of ayah in the Quran: 6236
 2. How many surah that have ayah less than 5 ayah?
 ANS: Surah(s) with less than 5 ayah: Al-Asr, Quraish, Al-Kawthar, An-Nasr AND Al-Ikhlaas
 3. Which ayah there is the shortest ayah?
 ANS: The shortest ayah is: طه
 4. Which ayah there is the longest ayah?
 ANS: The longest ayah is: يَـٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓاْ إِذَا تَدَايَنتُم بِدَيۡنٍ إِلَىٰٓ أَجَلٖ مُّسَمّٗى فَٱكۡتُبُوهُۚ وَلۡيَكۡتُب بَّيۡنَكُمۡ كَاتِبُۢ بِٱلۡعَدۡلِۚ وَلَا يَأۡبَ كَاتِبٌ أَن يَكۡتُبَ كَمَا عَلَّمَهُ ٱللَّهُۚ فَلۡيَكۡتُبۡ وَلۡيُمۡلِلِ ٱلَّذِي عَلَيۡهِ ٱلۡحَقُّ وَلۡيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبۡخَسۡ مِنۡهُ شَيۡـٔٗاۚ فَإِن كَانَ ٱلَّذِي عَلَيۡهِ ٱلۡحَقُّ سَفِيهًا أَوۡ ضَعِيفًا أَوۡ لَا يَسۡتَطِيعُ أَن يُمِلَّ هُوَ فَلۡيُمۡلِلۡ وَلِيُّهُۥ بِٱلۡعَدۡلِۚ وَٱسۡتَشۡهِدُواْ شَهِيدَيۡنِ مِن رِّجَالِكُمۡۖ فَإِن لَّمۡ يَكُونَا رَجُلَيۡنِ فَرَجُلٞ وَٱمۡرَأَتَانِ مِمَّن تَرۡضَوۡنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحۡدَىٰهُمَا فَتُذَكِّرَ إِحۡدَىٰهُمَا ٱلۡأُخۡرَىٰۚ وَلَا يَأۡبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُواْۚ وَلَا تَسۡـَٔمُوٓاْ أَن تَكۡتُبُوهُ صَغِيرًا أَوۡ كَبِيرًا إِلَىٰٓ أَجَلِهِۦۚ ذَٰلِكُمۡ أَقۡسَطُ عِندَ ٱللَّهِ وَأَقۡوَمُ لِلشَّهَٰدَةِ وَأَدۡنَىٰٓ أَلَّا تَرۡتَابُوٓاْ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةٗ تُدِيرُونَهَا بَيۡنَكُمۡ فَلَيۡسَ عَلَيۡكُمۡ جُنَاحٌ أَلَّا تَكۡتُبُوهَاۗ وَأَشۡهِدُوٓاْ إِذَا تَبَايَعۡتُمۡۚ وَلَا يُضَآرَّ كَاتِبٞ وَلَا شَهِيدٞۚ وَإِن تَفۡعَلُواْ فَإِنَّهُۥ فُسُوقُۢ بِكُمۡۗ وَٱتَّقُواْ ٱللَّهَۖ وَيُعَلِّمُكُمُ ٱللَّهُۗ وَٱللَّهُ بِكُلِّ شَيۡءٍ عَلِيمٞ in Surah Al-Baqara Ayah 282
 5. My name in Quran (Aminah mean in Englis = Honest)
ANS: The words 'honest' appear 2 times in the en_trans table.

# Authors
Aminah Che'soh 642437001

# Summary
The project Which is managing data in database to do data analysis with snowflake schema and various tool for getting result

# Reference
https://www.kaggle.com/datasets/alizahidraja/quran-english?select=Quran_English_with_Tafseer.csv

