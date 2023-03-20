# Rajasthan_IT_Day_Hackathon

## Problem Statement :
The goal of this project to assist student or any professional in learning important text of
It's an AI based Web Application Specially build for Rajasthan IT Day Hackathon 2023 for improving user Learning Experience.
Using this application user can selectively read the topics or news of their interest, also it gives user the most valuable text from large text paragraph or news.
This helps to learn only relevant info and improves Efficiency and Saves Time.

## Input : 

# Language: English and Hindi
# input type: .PDF, .TXT File , Manual input or Speech Input

## Output :
#1. It contains the language(hindi/english/urdu,etc.) 
#2. The Category of domain/category of input news/passage(like:- Sports, Politics, Education,etc.). It works for around 12 categories.
#3. The Summary of the input text(for Hindi as well as English).

## Approach :
Categorization:
1. Machine Learning(Random Forest)
2. API(for fast service)

Summarization:
1. BART(Number of words in summary can be choose as parameter, number_of_beams(candidate summary))
2. TextRank(number of sentences as parameter)
3. API(for fast service)

Hindi Summarization uses:
Text Rank with Bag-Of-Words(BOW)

Output can be listened at adjusted speed(like: 1.5x or 2x)
Output can be downloaded in .pdf or .txt or .mp3 file format.


## Deployment Link :
Heroku Deployment here



## Web Inerface :

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/header.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/input_pdf_text.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/input_text.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/parameters.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/summary_sample.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/Listen_audio.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/pdf_splitter_successful_upload.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/pdf_splitter_home.png)

![alt text](https://github.com/danishcyber-star/Rajasthan_IT_Day_Hackathon/blob/master/images/pdf_splitter_download_extracted_file.png)



## Libraries used :
    1) Pandas, Numpy
    2) Transformer, Speech Recognition, gtts, google_auth_oauthlib
    3) Fpdf, Torch
    4) Scikit-Learn
    5) Flask
    6) Python
    7) HTML, CSS, JQuery


## Technical Aspects :
    1) Python 
    2) Front-end : HTML, CSS, JS
    3) Back-end : Flask
    4) Deployment : Working
