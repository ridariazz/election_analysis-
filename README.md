# Election Analysis

## Overview of Project 
In this project, we analyzed a CSV file which contains a dataset of ballot IDs, name for the county and a name for the candidate for the Colorado Board of Elections. Our goal is to determine how many candidates and counties exist in this large dataset (approx. 370,000 rows!) and to determine which candidate received the most votes and was the winner of the election. We will need to examine and complete the steps below before we can get to our ultimate goal:

- Total number of votes cast
- A complete list of candidates who received votes
- Total number of votes each candidate received
- Percentage of votes each candidate won
- The winner of the election based on popular vote

## Resources 

- Election Dataset: election_results.csv
- Software: Python 3.7.6 (v3.7.6:43364a7ae0, Dec 18 2019, 14:18:50) 
- Code to Modify: PyPoll_Challenge.py

## Election Audit Results 

From our analysis of the dataset using Python, we extracted the final results below:

### Total Votes:

The total votes from the election was 369,711. 

### Candidates

- Candidate 1: Charles Casper Stockham
- Candidate 2: Diana DeGette
- Candidate 3: Raymon Anthony Doane

### Votes Received: 

- Stockham: 85,213
- DeGette: 272,892
- Doane: 11,606

### Percecntage of Votes:

Stockham: 23.0% 
DeGette: 73.8% 
Doane: 3.1% 

### Winner of the Election:

*Winner: Diana DeGette*

- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

The largest county turnout was Denver with a whopping 306,055 votes which accounted for 82.8% of the overall votes in the entire election. 

Here is our election_analysis.txt file displaying all the analytical information from our election results dataset:

<img width="321" alt="Screen Shot 2022-07-10 at 4 34 46 PM" src="https://user-images.githubusercontent.com/106577074/178166320-978a47da-db88-4bda-9770-d2f386a582ab.png">


## Election Audit Summary 

### Challenge Overview 

Overall, this challenge was by far one of the most tedious things I've worked with in a long time. Even though I understood the code and what we were trying to acheive from every function, the indentations killed me. I kept getting a syntax oe indentation errors not understanding what I was doing wrong. Spent hours just inspecting one single code written at a time until I finally cracked it, the indents. Python is definetly a powerful tool because opening that CSV file and looking at the 370,000 rows on data, I was shocked and excited at the same time. I was excited to learn how to compute and extract certain findings from this mass amount of data we were given. This course is all about making sense of the numbers and looking at patterns in data, this challenge definetly helped acheive that goal. 

Below are images of our code needed to extract specific data for our overall analysis. 

**Figure 1: our for loop to determine the total number of votes cast in the election.**

*Figure 1.1:* Determine our variables and what information we need to retract from our csv file:

<img width="681" alt="Screen Shot 2022-07-10 at 4 45 52 PM" src="https://user-images.githubusercontent.com/106577074/178166713-9bc3a449-a04b-42cb-9d1c-74ce3e34ffb4.png">

<img width="620" alt="Screen Shot 2022-07-10 at 4 46 05 PM" src="https://user-images.githubusercontent.com/106577074/178166718-b0c7cf28-1b6e-4549-8003-231a3bb7b140.png">

<img width="818" alt="Screen Shot 2022-07-10 at 4 46 58 PM" src="https://user-images.githubusercontent.com/106577074/178166741-866e5bd9-4187-419c-b205-4af735ede5b4.png">

*Figure 1.2:* Getting the winning candidate's vote count and overall percentage 

<img width="600" alt="Screen Shot 2022-07-10 at 4 53 05 PM" src="https://user-images.githubusercontent.com/106577074/178166894-49e6b344-a2e9-409a-9cb7-27e52abbcc77.png">

## Challenge Summary 

### Usage/Modification of this Script 

This script can be used to analyze voter counts, percentage and candidates involved in an election. We can also use this script to determine the winning candidate and how much votes they received in the overall election. This script can be used in the future to audit many other election by modifying two key components:

- the csv file to import and read 
- the txt file which will hold the analysis results for the election 

All in all, this was a very annoying, difficult, but most accomplishing challenge yet. I am no pro at Python and still have a long way to go in order to understand the functions and the loops, but this was such a great start towards being a Python specialist. Now, I understand why this language is so powerful and why everyone utilizes it, if understood and worked properly with, it's magic! This module took me over a week to complete, but I'm happy I took my time and never gave up to fully understand its potential and what was being done step-by-step. 
