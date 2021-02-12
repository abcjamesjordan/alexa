# About

This repository contains a lambda_function.py that can be used along with **Alexa** and **AWS Lambda** to download the OpenSnow daily snow forecasts and have them read aloud on your Alexa device. Process involves invoking a conversation with Alexa and using python to download the daily snow forecast that the user requests. Other files included python files and data files that are involved with the future work for this project.

# Libraries
Required libraries include **requests** and **beautifulsoup** to web scrape the text and format it in the correct output.

# Supported Intents
- forecast: Colorado Daily Snow Summary
- detailedforecast: Colorado Daily Snow Full Report
- uscanada: U.S. & Canada Daily Snow Summary
- detaileduscanada: U.S. & Canada Daily Snow Full Report

# Future Work
I would like to at some point streamline this process and have a seperate lambda function for downloading the daily snow forecasts and storing them seperate from the lambda function for the alexa development skills. I envision using either AWS **S3** or **DynamoDB** for this.
