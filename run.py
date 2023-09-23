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

wks_western = SHEET.worksheet('western')
wks_mayan = SHEET.worksheet('mayan')
wks_chinese = SHEET.worksheet('chinese')

def zodiac_sign(day, month):
   if month == 12:
      astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
   elif month == 1:
      astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
   elif month == 2:
      astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
   elif month == 3:
      astro_sign = 'Pisces' if (day < 21) else 'Aries'
   elif month == 4:
      astro_sign = 'Aries' if (day < 20) else 'Taurus'
   elif month == 5:
      astro_sign = 'Taurus' if (day < 21) else 'Gemini'
   elif month == 6:
      astro_sign = 'Gemini' if (day < 21) else 'Cancer'
   elif month == 7:
      astro_sign = 'Cancer' if (day < 23) else 'Leo'
   elif month == 8:
      astro_sign = 'Leo' if (day < 23) else 'Virgo'
   elif month == 9:
      astro_sign = 'Virgo' if (day < 23) else 'Libra'
   elif month == 10:
      astro_sign = 'Libra' if (day < 23) else 'Scorpio'
   elif month == 11:
      astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
   else:
        print("\033[1;31;40m WARNING: Only Months 1 through 12, days 1 through 31 & Years after 1924 are accepted")
        return None
   return astro_sign

def zodiac_sign_mayan(day, month):
    if month == 12:
      astro_sign = 'ALLIGATOR' if (day < 22) else 'FALCON'
    elif month == 1:
        astro_sign = 'FALCON' if (day < 20) else 'JAGUAR'
    elif month == 2:
        astro_sign = 'JAGUAR' if (day < 19) else 'FOX'
    elif month == 3:
        astro_sign = 'FOX' if (day < 21) else 'SNAKE'
    elif month == 4:
        astro_sign = 'SNAKE' if (day < 20) else 'SQUIRREL'
    elif month == 5:
        astro_sign = 'SQUIRREL' if (day < 21) else 'TURTLE'
    elif month == 6:
        astro_sign = 'TURTLE' if (day < 21) else 'BAT'
    elif month == 7:
        astro_sign = 'BAT' if (day < 23) else 'SCORPION'
    elif month == 8:
        astro_sign = 'SCORPION' if (day < 23) else 'DEER'
    elif month == 9:
        astro_sign = 'DEER' if (day < 23) else 'OWL'
    elif month == 10:
        astro_sign = 'OWL' if (day < 23) else 'PEACOCK'
    elif month == 11:
        astro_sign = 'PEACOCK' if (day < 22) else 'ALLIGATOR'
    else:
        print("Error")
    
    return astro_sign


def zodiac_sign_chinese(y):
    first_year = 1923
    diff = y - first_year
    if y < 1924 or y > 2043:
        print("The time frame doesn't fit.")
    else:
        zodiac_num = (diff % 12)
        return zodiac_num
        
main_loop = True
while main_loop:

    
    print (
        """\033[0m
        
                    .___.     .            
                      _/  _  _|* _. _.     
                    ./__.(_)(_]|(_](_.     
                                           
                 __    .      .    ,       
                /  ` _.| _.. .| _.-+- _ ._.
                \__.(_]|(_.(_||(_] | (_)[  
                                           

        """
    )

    print("Welcome to Zodiac Calculator!\n\nThis Program Will determine Your Horoscope & Zodiac Signs in the Gregorian, Mayan and Chinese calendars.\n\nEnter your name & date of birth below to get started!\n\n")
    Name=input("Enter Your Name:")
    print ("Hello",str(Name))

    d = int(input("Enter Day (1 through 31) ::>"))
    m = int(input("Enter the Month (1 through 12) ::>"))
    y = int(input("Enter the Year (From 1924 & onwards) ::>"))



    df_western = pd.DataFrame({"Zodiac Sign": wks_western.row_values(1), "Qualities": wks_western.row_values(2), "Horoscope": wks_western.row_values(3)})

    df_mayan = pd.DataFrame({"Zodiac Sign": wks_mayan.row_values(1), "Qualities": wks_mayan.row_values(2), "Horoscope": wks_mayan.row_values(3)})

    df_chinese = pd.DataFrame({"Zodiac Sign": wks_chinese.row_values(1), "Qualities": wks_chinese.row_values(2), "Horoscope": wks_chinese.row_values(3)})




    zodiac = zodiac_sign(d, m)


    if zodiac:
        

        ### Pandas Filtering
        zodiac_df_western = df_western[df_western["Zodiac Sign"] == zodiac]
        qualities_western = zodiac_df_western["Qualities"].values[0]
        horoscope_western = zodiac_df_western["Horoscope"].values[0]
        
        print(f"\033[1;32;40m Hey {Name}, your zodiac sign is: {zodiac}.\n\n")
        print(f"\033[1;32;40m Your qualties are: {qualities_western}.\n\n")
        print(f"\033[1;32;40m Your horoscope is: {horoscope_western}\n\n")

        while True:

            mayan_choice = input("Would you like to receive your Mayan Zodiac sign & horoscope? (y/n)").lower()

            if mayan_choice == 'y' or mayan_choice == 'yes':
                # mayan logic
                zodiac_mayan = zodiac_sign_mayan(d, m)

                zodiac_df_mayan = df_mayan[df_mayan["Zodiac Sign"] == zodiac_mayan]
                qualities_mayan = zodiac_df_mayan["Qualities"].values[0]
                horoscope_mayan = zodiac_df_mayan["Horoscope"].values[0]

                print(f"\033[1;32;40m {Name}, your Mayan zodiac sign is: {zodiac_mayan}.\n\n")
                print(f"\033[1;32;40m Your qualties are: {qualities_mayan}.\n\n")
                print(f"\033[1;32;40m Your Mayan horoscope is: {horoscope_mayan}.\n\n")

                while True:

                    chinese_choice = input("Would you like to receive your Chinese Zodiac sign & horoscope? (y/n)").lower()

                    if chinese_choice == 'y' or chinese_choice == 'yes':
                        
                        zodiac_df_chinese = df_chinese.iloc[zodiac_sign_chinese(y)]

                        zodiac_chinese = zodiac_df_chinese["Zodiac Sign"]
                        qualities_chinese = zodiac_df_chinese["Qualities"]
                        horoscope_chinese = zodiac_df_chinese["Horoscope"]

                        print(f"\033[1;32;40m {Name}, your Chinese zodiac sign is: {zodiac_chinese}.\n\n")
                        print(f"\033[1;32;40m Your qualties are: {qualities_chinese}.\n\n")
                        print(f"\033[1;32;40m Your Chinese horoscope is: {horoscope_chinese}.\n\n")

                        while True:

                            continue_choice = input("Enter 'end' to end the program: ").lower()

                            if continue_choice == 'end':
                                main_loop = True
                                break
                            else:
                                print("\033[1;31;40m WARNING: Only the word 'end' is accepted! Please try again")
                                continue

                        break
                    
                    elif chinese_choice == 'n' or chinese_choice == 'no':
                        break
                    else:
                        print("\033[1;31;40m WARNING: Only Y or N or yes or no are accepted. Please try again!")
                        continue

                break
            
            elif mayan_choice == 'n' or mayan_choice == "no":
                break

            else:
                print("\033[1;31;40m WARNING: Only Y or N or yes or no are accepted. Please try again!")
                continue



