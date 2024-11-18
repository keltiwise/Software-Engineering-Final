# Software Engineering Final
## Overview 
Using Azure DevOps and Python, my team and I developed a website to showcase breweries all throughout the United States from pulling a public REST API. Through this website, we encorporated a map with pin-points to each brewery, as well as a review page where customers can leave reviews. Through Azure DevOps, we used sentiment analysis to automatically categorize each review into postiive, negative, or neutral and keep a running score of the category each brewery falls under. 

## Azure SQL Connector
This file connects SQL to our server
[SQL Connector file found here](azuresqlconnect.py)

## Python Script
Flask is a required dependency, used to link our Python script with Azure DevOps. Through Python, we developed our file, app.py, where we scritped how our app would run, including the Azure DevOps sentiment analysis. 

[Python script found here](https://github.com/keltiwise/Software-Engineering-Final/blob/main/app.py)

## Templates
This branch includes all HTML files that corresponds to the website. Each HTML file corresponds to an individual page on the website: About page, Chat page (can interact with other members that use this website), Database page, Home page, and the Review page.

[Template branch found here](https://github.com/keltiwise/Software-Engineering-Final/blob/templates/README.md)

## Static/CSS
This branch includes a CSS script to personalize the website. This script allowed us to change different features on the website, including font, margins, background color, etc. 

[CSS branch found here]()




Link to the website: 
https://cs188breweryflaskapp.azurewebsites.net/
