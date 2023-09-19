import gspread
from google.oauth2.service_account import Credentials



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('zodiac_generator')

print (
    """

                   ________    ______    _______   __       ___       ______                               
                  |       /   /  __  \  |       \ |  |     /   \     /      |                              
                  `---/  /   |  |  |  | |  .--.  ||  |    /  ^  \   |  ,----'                              
                     /  /    |  |  |  | |  |  |  ||  |   /  /_\  \  |  |                                   
                    /  /----.|  `--'  | |  '--'  ||  |  /  _____  \ |  `----.                              
                   /________| \______/  |_______/ |__| /__/     \__\ \______|                              
                                                                                                           
  ______     ___       __        ______  __    __   __          ___   .___________.  ______   .______      
 /      |   /   \     |  |      /      ||  |  |  | |  |        /   \  |           | /  __  \  |   _  \     
|  ,----'  /  ^  \    |  |     |  ,----'|  |  |  | |  |       /  ^  \ `---|  |----`|  |  |  | |  |_)  |    
|  |      /  /_\  \   |  |     |  |     |  |  |  | |  |      /  /_\  \    |  |     |  |  |  | |      /     
|  `----./  _____  \  |  `----.|  `----.|  `--'  | |  `----./  _____  \   |  |     |  `--'  | |  |\  \----.
 \______/__/     \__\ |_______| \______| \______/  |_______/__/     \__\  |__|      \______/  | _| `._____|
                                                                                                           

    """
)


def get_name_data():
    """
    Get name from the user.
    """
    print("Enter your name and date of birth to generate your Gregorian calendar zodiac sign and horoscope.\n")
    print("The data entered should strictly be numbers.\n")

    name_str = input("Enter your name here: ")
    print(f"The name provided is {name_str}")

get_name_data()


