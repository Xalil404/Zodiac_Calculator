# Zodiac Calculator
The Zodiac calculator is a python terminal command line program which runs in the Code institute mock terminal on Heroku.

Upon the program initiating, the user is requested to enter their name and date of birth and based on the values provided, the program generates their astrological zodiac sign, qualities of the zodiac and the zodiac’s horoscope description based on three calendars: the western Gregorian calendar, the Mezo-American Mayan calendar and the Chinese calendar.

The data for the three astrological calendars is stored in a [Google Sheet](https://docs.google.com/spreadsheets/d/1bG8l2obMFN8uQB-j_ZrjLPf8L3HAkBQEZ17xwcD636I/edit?usp=sharing) being used as the database and through the enablement of Google’s APIs for Gdrive and Google sheets, the relevant data is pulled from it and presented to the user based on the date of birth information that they provided.

[Click here](https://zodiac-calculator-93d5e86df08c.herokuapp.com/) to view the deployed project.
<p align="center">
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695550743/Project%201/Screenshot_2023-09-24_at_11.16.52_AM_kcwqfq.png" width="auto" height="auto" alt="image of the Zodiac calculator program start screen on all devices"></p>

## UML Diagram
Prior to initiating the development, a UML diagram was created to understand the flow of the application, i.e. the steps taken during the program from beginning to end and in the process foresee any possible edge case scenario’s which should produce the relevant error messages for the user in order for them to understand what they did wrong. 

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551348/Project%201/Screenshot_2023-09-23_at_11.03.26_AM_claegz.png" width="auto" height="auto" alt="image of the Zodiac calculator UML diagram">

## Features
Upon the program starting, the welcome screen displays the program name and instruction texts on what the program does and how to use it, with the first step being for the user to enter their name for personalised statements in the program.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695650856/Project%201/Screenshot_2023-09-25_at_3.06.38_PM_ulnete.png" width="auto" height="auto" alt="image of the Zodiac calculator start screen">

After the user has entered their name, they are asked to provide 3 more pieces of data:
* Day of birth
* Month of birth
* Year of birth

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551681/Project%201/Screenshot_2023-09-24_at_11.34.22_AM_sg9bp3.png" width="auto" height="auto" alt="image of the required input data for the Zodiac calculator program to run">

Once the user has been provided with the initial 3 pieces of information (their Zodiac sign, qualities & horoscope) based on the first Gregorian calendar, they are asked whether they would like to regenerate the same information based on the next two calendars.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551833/Project%201/Screenshot_2023-09-24_at_11.36.27_AM_mswoy2.png" width="auto" height="auto" alt="image of the the Zodiac calculator output">

* Errors; the program has four error messages.  An error message when the user enters the wrong day or month.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695650989/Project%201/Screenshot_2023-09-25_at_3.09.33_PM_wutf22.png" width="auto" height="auto" alt="Zodiac calculator DOB error message">

* An error message when the user enters the wrong year.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695651081/Project%201/Screenshot_2023-09-25_at_3.11.08_PM_kiel1p.png" width="auto" height="auto" alt="Zodiac calculator DOB error message">

* An error message when the user doesn’t provide the correct values to generate more astrological information.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695552173/Project%201/Screenshot_2023-09-24_at_11.42.40_AM_dnx6sd.png" width="auto" height="auto" alt="Zodiac calculator question error message">

* And a final error message when the user doesn’t end the program properly.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695552274/Project%201/Screenshot_2023-09-24_at_11.44.17_AM_law28r.png" width="auto" height="auto" alt="Zodiac calculator end of program error message">

## Future Features
* It would be a logical idea to expand the program to provide more astrological information based on more calendars beyond just the initial three calendars. 

* Display the elements associated with each zodiac sign (i.e. Fire, Earth,etc…)

* Generate a lucky number associated with each zodiac sign.

* Astrological compatibility checker that lets the user know with which zodiac signs they will get along with well and which zodiac signs they should stay away from.

* Save the astrological information provided through generating a share link or save it in a PDF, Word, etc.. file format for future reference or sharing.

## Testing

I have manually tested the project through the following methods:

* Responsive testing on various device sizes through Chrome tools of the deployed site on Heroku.

* Browser compatibility testing on Firefox, Safari and Chrome of the deployed site on Heroku.

* Tests to make sure each Zodiac sign and its associated data is correctly being fetched from Google sheets and displayed in the program.

* Provided invalid data to make sure the relevant error messages are being provided.

* Tested the code via the [Pep8](https://pep8ci.herokuapp.com/) to make sure there are no critical problems. 
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695655465/Project%201/Screenshot_2023-09-25_at_4.22.34_PM_wfuega.png" width="auto" height="auto" alt="Zodiac calculator pip eight errors">

## Deployment

In order to deploy the project on Heroku, the following steps were taken:

* Activate Dyno points in the billing section of the Heroku account settings.

* In the Heroku dashboard create a new project and give it a name.

* In the project settings add 2 config vars (kEY: Creds VALUE: Copy and paste the credentials from the creds.json file and a second configuration KEY: PORT with VALUE: 8000).

* Also in the project settings add two build packs (A python build pack and a node.js build pack in that order).

* Then go to the deploy tab of the project and connect the project's Github repository. 

* After the Github repository has been connected, select the manual deploy option which will deploy the project if no errors arise.  

## Credits

* Gregorian horoscope data was provided by [Allure](https://www.allure.com/story/zodiac-sign-personality-traits-dates).

* Mayan horoscope data was provided by [AZULIK](https://www.newsroom.azulik.com/healing/discover-what-sign-of-the-mayan-horoscope-you-are/).

* Chinese horoscope data was provided by [travel-china-guide](https://www.travelchinaguide.com/intro/social_customs/zodiac/).

* Welcome banner ASCII text art provided by [Patorjik](https://patorjk.com/software/taag/#p=display&f=Bloody&t=Food%20Thing).

* For code and syntax references: Code Academy python materials/lessons, Python documentation on the internet and the Love Sandwiches practice project.

* Google APIs for Gdrive & Google sheets to communicate with the Google sheet document.

* Many project tutorials on the web of similar projects.