# The data we need to retrieve 
# 1. The total number of votes cast
# 2. A compelete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 
# Import the datetime class from the datetime module
import datetime 
# Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
# Print the present time 
print("The time right now is, ", now)
import csv
dir(csv)
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file 
election_data = open(file_to_load, 'r')
# to do: perform analysis 

#close the file 
election_data.close()
# Open the election results and read the file 
with open(file_to_load) as election_data:
    # to do: perform analysis
    print(election_data)
import os
dir(os)
dir(os.path)
os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to load and the path 
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file 
with open(file_to_load) as election_data:
    # print the file object 
    print(election_data)
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode, we will write data to the file
open(file_to_save, "w")

# Using "with" statement to open the file as a text file
file_to_save = os.path.join("analysis", "election_analysis.txt")
txt_file = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies 
import csv
import os
#Open election_data file 
with open(file_to_load) as election_data:
    # to do: perform analysis
    print(election_data)
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter
total_votes = 0
# Candidate Options
candidate_options = []
# Open the election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
    #  Print the candidate name from each row
        candidate_name = row[2]
    #If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
        # Add it to the list of candidates
        candidate_options.append(candidate_name)
# Print the candidate list
print(candidate_options)

# Add our dependencies 
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file 
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file 
    for row in file_reader:
        # Add the total vote count 
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any exisitng candidate, add it to the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's voter count 
            candidate_votes[candidate_name] = 0 
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # print out each candidate, their voter count and percentage to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

    # determine winning vote count and candidate
    # determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count and winning_percent = 
            # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

# To do: print out the winning candidate, vote count and percentage to
# terminal 
winning_candidate_summary = (f"---------------------------\n" 
f"Winner: {winning_candidate}\n" 
f"Winning Vote Count: {winning_count:,}\n" 
f"Winning Percentage: {winning_percentage:.1f}%\n" 
f"---------------------\n")
print(winning_candidate_summary)
