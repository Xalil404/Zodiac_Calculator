# Zodiac Calculator
The Zodiac calculator is a python terminal command line program which runs in the Code institute mock terminal on Heroku.

Upon the program initiating, the user is requested to enter their name and date of birth and based on the values provided, the program generates their astrological zodiac sign, qualities of the zodiac and the zodiac’s horoscope description based on three calendars: the western Gregorian calendar, the Mezo-American Mayan calendar and the Chinese calendar.

The data for the three astrological calendars was stored in a [Google Sheet](https://docs.google.com/spreadsheets/d/1bG8l2obMFN8uQB-j_ZrjLPf8L3HAkBQEZ17xwcD636I/edit?usp=sharing) through the enablement of Google’s APIs for Gdrive and Google sheets and the relevant data was pulled from it and presented to the user based on the date of birth information that they provided.
<p align="center">
<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695550743/Project%201/Screenshot_2023-09-24_at_11.16.52_AM_kcwqfq.png" width="auto" height="auto" alt="image of the Zodiac calculator program start screen on all devices"></p>

## UML Diagram
Prior to initiating the development, a UML diagram was created to understand the flow of the application, steps taken during the program from beginning to end and any possible edge case scenario’s which should produce the relevant error messages for the user to understand what they did wrong. 

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551348/Project%201/Screenshot_2023-09-23_at_11.03.26_AM_claegz.png" width="auto" height="auto" alt="image of the Zodiac calculator UML diagram">

## Features
Upon the program starting, the welcome screen displays the program name and instruction texts on what the program does and how to use it, with the first step being for the user to enter their name for personalised statements in the program.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551513/Project%201/Screenshot_2023-09-24_at_11.31.25_AM_ylwsvw.png" width="auto" height="auto" alt="image of the Zodiac calculator start screen">

After the user has entered their name, they are asked to provide 3 more pieces of data:
* Day of birth
* Month of birth
* Year of birth

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551681/Project%201/Screenshot_2023-09-24_at_11.34.22_AM_sg9bp3.png" width="auto" height="auto" alt="image of the required input data for the Zodiac calculator program to run">

Once the user has been provided with the initial 3 pieces of information (Zodiac sign, qualities & horoscope) based on the first Gregorian calendar, they are asked whether they would like to regenerate the same information based on the next two calendars.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695551833/Project%201/Screenshot_2023-09-24_at_11.36.27_AM_mswoy2.png" width="auto" height="auto" alt="image of the the Zodiac calculator output">

Errors; the program has three error messages.  An error message when the user enters the wrong date of birth.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695552068/Project%201/Screenshot_2023-09-24_at_11.40.44_AM_qqmmun.png" width="auto" height="auto" alt="Zodiac calculator DOB error message">

An error message when the user doesn’t provide the correct values to generate more astrological information.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695552173/Project%201/Screenshot_2023-09-24_at_11.42.40_AM_dnx6sd.png" width="auto" height="auto" alt="Zodiac calculator question error message">

And a final error message when the user doesn’t end the program properly.

<img src="https://res.cloudinary.com/dugcwv1mf/image/upload/v1695552274/Project%201/Screenshot_2023-09-24_at_11.44.17_AM_law28r.png" width="auto" height="auto" alt="Zodiac calculator end of program error message">

## Future Features
* It would be a logical idea to expand the program to provide more astrological information based on more calendars beyond just the initial three calendars. 

* Display the elements associated with each zodiac sign (e.g., Fire, Earth,etc…)

* Generate a lucky number associated with each zodiac sign.

* Astrological compatibility checker that lets the user know with with zodiac signs they will get along with well and which zodiac signs they should stay away from.

* Save the astrological information provided through generating a share link or save it in PDF, Word, etc.. file format.

## Testing

I have manually tested the project through the following methods:

* Responsive testing on various device sizes through Chrome tools of the deployed site on Heroku.

* Browser testing on Firefox, Safari and Chrome of the deployed site on Heroku.

* 36 tests to make sure each Zodiac sign and its associated data is correctly being fetched from Google sheets and displayed in the program.

* Provided invalid data to make sure the relevant error messages are being provided.

* Tested the code via the Pep8 to make sure there are no problems. 

