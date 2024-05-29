# Creamy Cones

Creamy Cones is a famous icecream store that wants to expand their already successful business onto the online market. 

Therefore I have built a programme which allows the user to place an order online which gives Creamy Cones another avenue of making money.

This fully python written programme is run on a mock terminal.

![Am I responsive](/assets/Am_i_responsive.png)

Live app: [Creamy Cones](https://creamy-cones-bcfe661bc605.herokuapp.com/)

# User experience

## User stories

As a user 
* I want to add colors to easy to identify if its a n error message or confirmation meassge
* I want to add a ascii image as a welcome message
* I want to easily navigate my way through the programme to select my order
* Follow a chronological order that makes sense to order an icecream
* Tell me exactly what keys to enter and if I make a mistake, tell me what I done wrong
* Have simple instruction to follow 
* I want to know the prices of all options at every step not just at the end of the order
* I want a selection and variety of flavours
* I want the options of ordering number of icecreams
* I want a selection of toppings on my icecream cone
* Give me options to re-start my order before confirming if I selected anything wrong
* I want to know exactly how long it will take for my order to be made
* I want to recieve a receipt of excatly what I ordered

As the owner

* I want to provide a simple and easy way of ordering online
* I want a clear, easy to read spreadsheet of the data from the orders recieved

# Flow chart

I used [lucid flowcharts](https://lucid.app/users/login#/login) to help design the flow and outcomes of the project that the user while face depending on their decisions

![Lucid flowchart](/assets/lucidchart.png)

# Features

All inputs have error messages that informs the user that their input was incorrect and what they should enter

### Welcome message
* The user recives a ASCII art as a welcome message
![Ascii image ](/assets/ASCII..png)

* The user recieves a welcome message and an option if they would like to place an order

![Welcome message](/assets/welcome.png)

### Menu
* The user is able to see the menu
* They can select which flavour of icecream cone  they would like to order 

![Menu](/assets/menu.png)

### Cone size
* The user then can select which size of cone they would like to order

![Size](/assets/size.png)

### Quantity
* The user then gets their cone size option written back to them
* The user can then select how many icecreams they would like to order

![Quantity](/assets/quantity.png)

### Toppings
* The user then gets their icecream quantity option written back to them
* The user can then select if they would like to add toppings to their order

![Toppings](/assets/topping.png)

### Select Toppings
* The user then gets an option to add toppings
* The user can select the toppings from the toppings menu
![Topping_menu](/assets/topping_menu.png)

### Confirm order
* The user gets their entire order written back to them including the total cost
* The user then has a choice to confirm their order or not and restart the order process

![Confirm](/assets/confirm.png)

### User details
* The user then is asked for their details of their first name 

![Details](/assets/details.png)

### Receipt
* The user then recieves a thank you message from Creamy cones and how long it will take for it to be ready
* The user is then presented with their receipt of the order which includes:
    * Order number
    * Order
    * Cost
    * Time

![Receipt](/assets/receipt.png)

### Google spreadsheet
* The user's data is then updated to the spreadsheet for the owner to see and start making their order

![Spreadsheet](/assets/spreadsheet.png)
 
### Order again
* The user can order again after getting receipt
* It will will display the menu if user select yes

![again](/assets/again.png)

## Future features

* To allow the user to order multiple different icecreams at the same time

# Data model

I have based the model on functions used as the steps to request, validate and return data from the user. As each function is executed, return values are collated and confirmed back to the user before sending to the Google spreadsheet.

The Google spreadsheet is used to recieve the data from the user and allow the owner to clearly read and understand what the user has ordered.

# Technology used

* Python to write my programme
* JavaScript provided in the Code Institute template
* CSS provided in the Code Institute template
* HTML provided in the Code Institute template
* Google sheets to store the information
* [Heroku](https://dashboard.heroku.com/apps) to deploy the project
* [Am I responsive](https://ui.dev/amiresponsive) to show a mock up of the terminals
* [ASCII](https://fsymbols.com/generators/carty/)

# Python libraries used

* [Datetime](https://docs.python.org/3/library/datetime.html) to add the time to the receipt and spreadsheet of when the order was placed
* [UUID](https://thewebdev.info/2021/10/24/how-to-create-a-guid-or-uuid-in-python/?fbclid=IwAR16O6f7oQc62Uo-lG0VW7wzm-_6GxAsuMkFnzIb-5_cKQlTXUveOWsXGgg) to generate a random code to use as an order number
* [Sys](https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python) to allow the user to exit the function
* [Gspread](https://docs.gspread.org/en/latest/) to link my google sheet for the owner to see the data of the orders 
* [Colorama](https://pypi.org/project/colorama/) to add colors to the text

# Testing

I have manually tested thi sproject by doing the following:

* Passed the code through a PEP8 linter and confirmed there are now no bugs at the time of this test
* Given invalid inputs to all input choices and made sure they allow the user to carry on with their order
* Tested in my local terminal and the Code Institute Heroku terminal

![PEP8 No errors](/assets/pep8.png)

## User Input Validation  
User input validation was carried out throughout the project build. It was very important that the user could navigate easily through the program and that their entered name, soze,quanity,order number and price  appropriately into the respective Google Sheets. 
  
| Feature                    | Tested?  | User Feedback Provided      |
|----------------------------|----------|-----------------------------|
| Order                      | Yes      | Invalid!, Your choice sholud be Y or N|
| Menu                       | Yes      | Invalid!, Please enter number between 1-6 or E |
| Size                       | Yes      | Invalid!, Enter either S or L|
| Quantity                   | Yes      | Invalid!, You can select upto 8 |
| Toppings                   | Yes      | That's not right, Please enter Y or N |
| select Toppings            | Yes      | Invalid!, Enter C,M or N |
| Cofirm Order               | Yes      | That's not right, Please enter Y or N |
| Name                       | Yes      | Try again!, Please check you entered correct name |
| Order again                | Yes      | That's not right, Please enter Y or N |
----- 


## Browser Testing  

Creamy cones was tested through the Heroku app website on the following browsers with no issues arising:  
- Google Chrome 
- Mozilla Firefox 
- Microsoft Edge 
- safari


## Manual Testing  

### Testing User Stories 

  
  
  1. As a User, I want an attractive, engaging application.  

    - Colorama library used to produce text with engaging colours and meaning  
    - GREEN for confirmation 
    - RED for invalid input
    - Purple for welcome meaasages
    - CYAN for input meassages
  
  2. As a User, I want to be provided with clear instructions throughout the application.  

    - All sections requiring user input are signposted with clear instructions on how to proceed
    - User is prompted with instructions when input provided is invalid
    - require user to confirm the data before it is updated to the worksheet
  
  3. As a user, I want to able to upload the data to google sheets

  4. As a User, I want to be able to navigate back to the Main Menu.  
    
    - User wants to order again

  
    
# Unfixed bugs

* There are no unfixed bugs at the time of the last testing

# Deployment

This project was developed through Gitpod, using Code Institue's mock terminal for Heroku and their way of linking to Google Sheet API.

## Deploy from GitHub

* Log into your GitHub repository
* Click 'Settings' in the main Repository menu
* Click 'Pages' from the left-hand side navigation menu
* Within the Source section, click the "Branch" button and change from 'None' to 'Main'
* The page should automatically refresh with a url displayed
* Test the link by clicking on the url

## Forking

* Navigate to the [Creamy Cones](https://github.com/Meghanarajvinakota/creamy-cones)
* Click the 'Fork' button on the upper right part of the page.
* You will now have a fork of the Fred's pizzas repository added to your GitHub profile.

## Cloning

* Login to Github and go to my [Creamy Cones](https://github.com/Meghanarajvinakota/creamy-cones)
* Above the list of files click the green ‘code’ button.
* This will bring up a few options as to how you would like to clone. You can 4. select HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
* Open git bash
* Type ‘git clone’ and then paste the URL you copied. Press Enter.

## Create Data model spreadsheet

* Login to your Google account, create an account if necessary
* Navigate to Sheets, Googles version of Microsoft Excel
* Start a new spreadsheet, amend the title at the top i.e., Creamy Cones
* Create 1 Sheet titling it 'Orders' 
* In the first row of the Orders sheet, add the following column headers:
* Name,Icecream,Size,Quantity,Toppings,Price,Time,Id

## Set up API

Credit to [Jorgen Brattang](https://github.com/JorgenBrattang/daily-math) for the description

* Head to [Google cloud platform](https://console.cloud.google.com/) and sign in or create a free google account
* From the google cloud platform dashboard click 'Select a new project'. Then select 'New project'.
* Create a name for your project under 'Project name' then click 'Create'.
* This should bring up a box with your project in. Underneath click 'SELECT PROJECT'.
* From the sidebar navigate to 'APIs and services', 'Library'.
* In the search bar search for google drive.
* Select 'Google drive API' and click 'ENABLE'.
* Click the 'CREATE CREDENTIALS' button located to the top right of the page.
* From the dropdown menu under 'Which API are you using?' select 'Google drive API'.
* Under 'What data will you be accessing' choose 'Application data'.
* Under 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine or Cloud Functions?' select 'No, i'm not using them' and click 'NEXT'.
* Enter a Service Account Name. You can name it whatever you like. I would suggest naming it the same as what you named your project. Then click 'CREATE AND CONTINUE'.
* In the 'Role' dropdown menu select 'Basic', 'Editor', then click 'Continue'.
* The next page can be left blank so just click 'DONE'.
* Under 'Service Accounts' find the account you just created and click it.
* Navigate to the 'KEYS' tab and click 'ADD KEY', 'Create new key'. Select 'JSON' and click 'CREATE'.
* This will download a json file to your machine. This normally downloads into your 'downloads' folder but if you're unsure you can right click the file once it's downloaded and click 'show in folder' to locate it.
* Next we will have to link the Google Sheets API. To do this navigate back to the library by clicking on the burger icon in the top left hand corner and selecting 'APIs and services', 'Library' from the dropdown menu.
* In the search bar search for 'Google Sheets' and select 'Google Sheets API' and click 'ENABLE'.
* Now, using a programme like Gitpod open or create a repository.
* Drag and drop the json file that you downloaded earlier into your workspace. Rename this file to 'creds.json'.
* Open the file and copy the email address under 'client_email' without the quotation marks.
* Open up the google sheet you want to use and click the 'Share' button.
* Paste in the client email. Make sure 'Editor' is selected, untick 'Notify people' and then click 'Share'.
* To protect sensitive information be sure to add your creds.json file to your .gitignore file inside your editor.
* In order to use our google sheets API you need to install two additional dependencies into your project.
* Copy the following code on the first two lines of your workspace

![gspread](/assets/gspread.png)

* Below this, add the following code:

![scope](/assets/scope.png)

