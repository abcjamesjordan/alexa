# About

This repository contains a lambda_function.py that can be used along with **Alexa** and **AWS Lambda** to download the OpenSnow daily snow forecasts and have them read aloud on your Alexa device. Process involves invoking a conversation with Alexa and using python to download the daily snow forecast that the user requests. Other files included python files and data files that are involved with the future work for this project.

# Motivation
Motivation and help for this project comes from the Alexa series videos from youtuber and github member Keith Galli. His Youtube and GitHub can be found below.

Alexa Tutorial Pt 1: https://www.youtube.com/watch?v=sj7NqS7yytw \
Alexa Tutorial Pt 2: https://www.youtube.com/watch?v=-MOvJ3eklr0&t=162s \
Youtube: https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw \
GitHub: https://github.com/KeithGalli

# Libraries
Required libraries include **requests** and **beautifulsoup** to web scrape the text and format it in the correct output. If they are not installed already you can install them with: 

Requests: pip install requests \
Beautifulsoup: pip install beautifulsoup4

# Supported Intents
So far the only supported Alexa intents (daily snow forecasts) are as follows:
- forecast: Colorado Daily Snow Summary
- detailedforecast: Colorado Daily Snow Full Report
- uscanada: U.S. & Canada Daily Snow Summary
- detaileduscanada: U.S. & Canada Daily Snow Full Report

# Future Work
I would like to at some point streamline this process and have a seperate lambda function for downloading the daily snow forecasts and storing them seperate from the lambda function for the alexa development skills. I envision using either AWS **S3** or **DynamoDB** for this. Additional help for implementing this can be found here: https://lumigo.io/learn/aws-lambda-boto3/

Another future work includes modifying the lambda_function to enable the text to scroll as it is read aloud with Alexa. When the detail reports are pulled, often the text is far to long to fit onto an Alexa enable display. Link to help with this can be found here: https://developer.amazon.com/en-US/docs/alexa/alexa-presentation-language/display-text-on-the-screen.html
