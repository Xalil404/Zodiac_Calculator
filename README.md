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

## Future Features

* It would be a logical idea to expand the program to provide more astrological information based on more calendars beyond just the initial three calendars. 

* Display the elements associated with each zodiac sign (i.e. Fire, Earth,etc…)

* Generate a lucky number associated with each zodiac sign.

* Astrological compatibility checker that lets the user know with which zodiac signs they will get along with well and which zodiac signs they should stay away from.

* Save the astrological information provided through generating a share link or save it in a PDF, Word, etc.. file format for future reference or sharing.

## General Testing

I have manually tested the project through the following methods:

* Responsive testing on various device sizes through Chrome tools of the deployed site on Heroku.

* Browser compatibility testing on Firefox, Safari and Chrome of the deployed site on Heroku.

* Tests to make sure each Zodiac sign and its associated data is correctly being fetched from Google sheets and displayed in the program.

* Provided invalid data to make sure the relevant error messages are being provided.

* Tested the code via the [Pep8](https://pep8ci.herokuapp.com/) to make sure there are no critical problems. 
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695655465/Project%201/Screenshot_2023-09-25_at_4.22.34_PM_wfuega.png" width="auto" height="auto" alt="Zodiac calculator pip eight errors">

## Features Testing

| User Story | Screenshot | Notes |
| --- | --- | --- |
| User can enter date of birth information to generate zodiac signs and horoscopes. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699444857/Project%204/Screenshot_2023-11-08_at_12.00.34_PM_lj83nd.png) | Works as expected |
| User can generate Gregorian zodiac sign and horoscope. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699444907/Project%204/Screenshot_2023-11-08_at_12.01.25_PM_jttqdy.png) | Works as expected |
| User can continue on to generate Mayan zodiac sign and horoscope. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699444953/Project%204/Screenshot_2023-11-08_at_12.02.15_PM_uwjzxc.png) | Works as expected |
| User can continue on to generate Chinese zodiac sign and horoscope. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699444994/Project%204/Screenshot_2023-11-08_at_12.02.55_PM_dzjhvm.png) | Works as expected |
| User can end program midway and restart it. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445126/Project%204/Screenshot_2023-11-08_at_12.05.07_PM_uglyp6.png) | Works as expected |
| User can end program at the end and restart it. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445069/Project%204/Screenshot_2023-11-08_at_12.04.12_PM_sv6t2n.png) | Works as expected |

## Error Handling Testing

| Edge Case | Screenshot | Notes |
| --- | --- | --- |
| User cannot proceed without entering a name. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445196/Project%204/Screenshot_2023-11-08_at_12.06.16_PM_sxmaej.png) | Works as expected |
| Day entered must have a value; cannot be empty. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445245/Project%204/Screenshot_2023-11-08_at_12.07.07_PM_kf3efi.png) | Works as expected |
| Day entered has to be within the specified range. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445368/Project%204/Screenshot_2023-11-08_at_12.09.06_PM_gzfurq.png) | Works as expected |
| Day entered must be an integer; cannot be a letter. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445306/Project%204/Screenshot_2023-11-08_at_12.08.06_PM_vvijsg.png) | Works as expected |
| Month entered must have a value; cannot be empty. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445426/Project%204/Screenshot_2023-11-08_at_12.10.04_PM_qfrgmm.png) | Works as expected |
| Month entered has to be within the specified range. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445564/Project%204/Screenshot_2023-11-08_at_12.12.26_PM_oqn8pz.png) | Works as expected |
| Month entered must be an integer; cannot be a letter. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445505/Project%204/Screenshot_2023-11-08_at_12.11.26_PM_qgjvtv.png) | Works as expected |
| Year entered must have a value; cannot be empty. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445623/Project%204/Screenshot_2023-11-08_at_12.13.25_PM_g7agey.png) | Works as expected |
| Year entered has to be within the specified range. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445725/Project%204/Screenshot_2023-11-08_at_12.15.07_PM_wmpfqf.png) | Works as expected |
| Year entered must be an integer; cannot be a letter. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445817/Project%204/Screenshot_2023-11-08_at_12.16.39_PM_escjtz.png) | Works as expected |
| Only y, n , yes or no are acceptable commands to continue program. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699445938/Project%204/Screenshot_2023-11-08_at_12.18.36_PM_fmkbnw.png) | Works as expected |
| Only end is acceptable command to end program. | ![screenshot](https://res.cloudinary.com/dugcwv1mf/image/upload/v1699446008/Project%204/Screenshot_2023-11-08_at_12.19.49_PM_hl0bnf.png) | Works as expected |

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

* [Pandas](https://pandas.pydata.org/) Library for reading and handling Zodiac data stored in Google Sheets.

* Many project tutorials on the web of similar projects.