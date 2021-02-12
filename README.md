# About

This repository contains a lambda_function.py that can be used along with alexa and aws lambda to have the daily snow forecasts posted online read aloud on you alexa devices.

# Libraries
Required libraries include requests and beautifulsoup to web scrape the text and format it in the correct output.

# Future Work
I would like to at some point streamline this process and have a seperate lambda function for downloading the daily snow forecasts and storing them seperate from the lambda function for the alexa development skills. I envision using either AWS S3 or DynamoDB for this.
