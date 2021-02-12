"""
This is a python lambda function to start a conversation with alexa so she can 
Daily Snow reports to you as they are specified.
"""

from __future__ import print_function
import random
import requests
from bs4 import BeautifulSoup

class Forecast:
    def __init__(self, url, css_selector='.post > p:nth-child(3)', css_selector_detail='.all-access-content'):
        self.url = url
        self.css_selector = css_selector
        self.css_selector_detail = css_selector_detail
    def get_forecast(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        return elems_summary[0].text
    def get_forecast_detailed(self):
        get_summary = requests.get(self.url)
        soup_text = BeautifulSoup(get_summary.text, 'html.parser')
        elems_summary = soup_text.select(self.css_selector)
        elems_details = soup_text.select(self.css_selector_detail)
        return f'{elems_summary[0].text} {elems_details[0].text}'


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_test_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Test"
    speech_output = "This is a test message"
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome, which daily snow would you like to hear?"
    reprompt_text = "Which daily snow would you like me to read to you?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_forecast_response():
    session_attributes = {}
    card_title = "Forecast"
    
    # Gathering the daily snow forecast summary
    co_daily = Forecast('https://opensnow.com/dailysnow/colorado', '.post > p:nth-child(3)')
    co_daily_forecast = Forecast.get_forecast(co_daily)
    
    speech_output = f'Here is your Colorado Daily Snow. {co_daily_forecast}'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Would you like me to read that again?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_detailed_forecast_response():
    session_attributes = {}
    card_title = "Detailed Forecast"
    
    # Gathering the daily snow forecast summary
    co_daily_detailed = Forecast('https://opensnow.com/dailysnow/colorado', '.post > p:nth-child(3)', '.all-access-content')
    co_daily_forecast_detailed = Forecast.get_forecast_detailed(co_daily_detailed)
    
    speech_output = f'Here is your detailed Colorado Daily Snow. {co_daily_forecast_detailed}'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Would you like me to read that again?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_uscanada_forecast_response():
    session_attributes = {}
    card_title = "U.S. Canada Forecast"
    
    # Gathering the daily snow forecast summary
    uscanada = Forecast('https://opensnow.com/dailysnow/usandcanada', '.post > p:nth-child(3)')
    uscanada_forecast = Forecast.get_forecast(uscanada)
    
    speech_output = f'Here is the U.S. and Canada daily snow. {uscanada_forecast}'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Would you like me to read that again?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_detailed_uscanada_forecast_response():
    session_attributes = {}
    card_title = "U.S. Canada Forecast"
    
    # Gathering the daily snow forecast summary
    uscanada = Forecast('https://opensnow.com/dailysnow/usandcanada', '.post > p:nth-child(3)')
    uscanada_forecast = Forecast.get_forecast(uscanada)
    
    speech_output = f'Here is the U.S. and Canada daily snow. {uscanada_forecast}'
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Would you like me to read that again?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    # Dispatch to your skill's intent handlers
    if intent_name == "test":
        return get_test_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "forecast":
        return get_forecast_response()
    elif intent_name == "detailedforecast":
        return get_detailed_forecast_response()
    elif intent_name == "uscanadaforecast":
        return get_uscanada_forecast_response()
    elif intent_name == "detaileduscanadaforecast":
        return get_detailed_uscanada_forecast_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    if (event['session']['application']['applicationId'] !=
            "amzn1.ask.skill.2994421a-75ef-4502-9d4a-bf83f20a7ade"):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])