import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('zodiac_generator')

wks = SHEET.worksheet('western')

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


Name=input("Enter Your Name:")
print ("Hello",str(Name))
print("This Program Will determine Your Horoscope & Zodiac Signs in the Gregorian, Mayan and Chinese calendars.")

d = int(input("Enter Day ::>"))
m = input("Enter the Month ::>")

def zodiac_sign(day, month):
   if month == '12':
      astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
   elif month == '1':
      astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
   elif month == '2':
      astro_sign = 'Aquarius' if (day < 19) else 'pisces'
   elif month == '3':
      astro_sign = 'Pisces' if (day < 21) else 'aries'
   elif month == '4':
      astro_sign = 'Aries' if (day < 20) else 'taurus'
   elif month == '5':
      astro_sign = 'Taurus' if (day < 21) else 'gemini'
   elif month == '6':
      astro_sign = 'Gemini' if (day < 21) else 'cancer'
   elif month == '7':
      astro_sign = 'Cancer' if (day < 23) else 'leo'
   elif month == '8':
      astro_sign = 'Leo' if (day < 23) else 'virgo'
   elif month == '9':
      astro_sign = 'Virgo' if (day < 23) else 'libra'
   elif month == '10':
      astro_sign = 'Libra' if (day < 23) else 'scorpio'
   elif month == '11':
      astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
   else:
        print("Only Months 1 through 12 & days 1 through 31 are accepted")
        return None
   return astro_sign




#print(wks.cell(1, 1))
#print(wks.row_values(1))
#print(wks.col_values(1))

df = pd.DataFrame({"Zodiac Sign": wks.row_values(1), "Qualities": wks.row_values(2), "Horoscope": wks.row_values(3)})


zodiac = zodiac_sign(d, m)

if zodiac:
    #xprint(zodiac)

    ### Pandas Filtering
    zodiac_df = df[df["Zodiac Sign"] == zodiac]
    qualities = zodiac_df["Qualities"].values[0]
    horoscope = zodiac_df["Horoscope"].values[0]
    #print(qualities)

    #print()
    #print(horoscope)

    print(f"Hey {Name}, your zodiac sign is {zodiac}. Your qualties are {qualities}. Your horoscope is:\n{horoscope}")


