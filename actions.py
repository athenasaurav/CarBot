# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
class ActionSaveName(Action):
#
    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("tutorial").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        name = tracker.get_slot("PERSON")
        insertRow = ["none"]
        sheet.insert_row(insertRow, 2)
        sheet.update_cell(2,1, name) 
        dispatcher.utter_message("Okay")

        return []

class ActionSaveEmail(Action):
#
    def name(self) -> Text:
        return "action_save_email"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("tutorial").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        email = tracker.get_slot("email")
        
        sheet.update_cell(2, 2, email) 
        dispatcher.utter_message("Done")

        return []

class ActionCar(Action):
#
    def name(self) -> Text:
        return "action_car"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("tutorial").sheet1  # Open the spreadhseet
        data = sheet.get_all_records()  # Get a list of all records
        
        car = tracker.get_slot("car")
        
        sheet.update_cell(2, 3, car) 
        dispatcher.utter_message("Okay. Let me get details for {}.". format(car))

        return []

class ActionCarSearch(Action):
#
    def name(self) -> Text:
        return "action_car_search"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        from pprint import pprint
        import pandas as pd
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("tutorial") # Open the spreadhseet
        worksheet = sheet.get_worksheet(1)
        data = pd.DataFrame(worksheet.get_all_records()) 
        car = tracker.get_slot("car")
        mpg = int(tracker.get_slot("mpg"))
        city_mpg_data = data[data['city mpg'] == mpg]
        car_city_mpg_data = city_mpg_data[city_mpg_data['Make'] == car]
        car_city_mpg_data = car_city_mpg_data.reset_index()        
        dispatcher.utter_message("We found following car with your inputs")
        for i in range(1,5):
            get = city_mpg_data.iloc[i]
            dispatcher.utter_message("Okay. You are looking for {} {}. Here are the details of the car: The car make is {} and has a Engine Fuel Type of {}. It has Engine of {} Hp with {} cylinders. The Transmission is {} & is {} driven. The no of doors are{}. Its market cateogory is {}. The size and style of car is {} & {} respecitively. It has milage on highway of {} MPG and in city is {} MPG. Its popularity according to company is {} and MSRP is ${}.".format(get[6], get[8], get[14], get[3], get[4], get[2], get[11], get[1], get[9], get[7], get[12], get[13], get[17], get[16], get[10], get[5]))
        
        return []