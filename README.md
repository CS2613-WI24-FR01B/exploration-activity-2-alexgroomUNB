# EA2
### 1. What package/library does the sample program demonstrate?

This package allows users to compare different engineering projects using weighted criteria.

### 2. How does someone run your program?

#### i) Installing Node.js and Python

Make sure you have node.js and Python installed. To check this you can perform the following command in your command prompt:
node --version
python --version

If the cmd returns a sequence of numbers it indicates you have them installed and you can proceed to the next step. Otherwise you must install [node.js](https://nodejs.org/en/download) and [python](https://www.python.org/downloads/). Node.js will include npm and Python will include pip which are needed to install the libraries needed for this program.

#### ii) Cloning Repository
Go to the main page of this repo and click the drop down for the code button. Copy the link, then go to a directory in your command prompt where you would like to clone this repo with the following command:

git clone <repo name>

#### iii) Installing Libraries
In the main directory of this repo performs the following commands:

npm install chart.js
pip install streamlit

For a quick intro to streamlit you can run the command streamlit hello (not required).
#### iv) Running the Program
In the same folder perform the following command:

streamlit run app.py

This will take you to the web-app in your browser. The server for this web app is locally hosted on your computer, thus do not close your command prompt while using the web app.

#### v) Using the Program

Follow the directions on the home page to use the program.


### 3. What purpose does your program serve?

The program is an interactive replacement for crunching numbers on excel to compare engineering projects with weighted criteria. This program serves to be a sample of what a complpete and expansive engineering projects comparison app could be. 

### 4. What would be some sample input/output?
Here is an example for comparing different energy replacement projects for current thermo-energy plants.
#### Input Several Criteria
The user would go to the Criteria page and input desired criteria that relates to the projects. In this case I put cost, environmental concerns, sustainability, economic life, and efficiency. Weight each criteria accordingly by typing a number in the 'Weight Criteria' text field, press the 'Log Criterion' button after each entry.
![criteria-in](https://github.com/CS2613-WI24-FR01B/exploration-activity-2-alexgroomUNB/assets/151641485/0c7527df-793a-4382-802b-b037a55f302a)

#### Input Several Project Options
The user would then go to the Project page and input all desired project's. They can optionally add a description and they are to press the 'Add Project' button after each entry. The running list of project names will be displayed below. For my example I used solar, nuclear, and win as project options. 
![projects](https://github.com/CS2613-WI24-FR01B/exploration-activity-2-alexgroomUNB/assets/151641485/a2e2bae6-8daa-4bce-83c1-bfb8bfaaf60d)

#### Rank Projects
Then go to the Rank page to rank each project by clicking on their respective drop down. Criteria are to be ranked on a scale of 1-10 for each project using the sliders in each drop down. Press 'Confirm Rankings' when all of the rankings for all projects is complete.
![Ranking](https://github.com/CS2613-WI24-FR01B/exploration-activity-2-alexgroomUNB/assets/151641485/ce9b49ee-bec5-4c5f-8d6d-bf9c4fb682eb)

#### View Chart
Go to the Charts page to view the generate chart and the best project option.
![charts](https://github.com/CS2613-WI24-FR01B/exploration-activity-2-alexgroomUNB/assets/151641485/8b73ed48-002e-48a1-b47f-fd92685d1f3b)


