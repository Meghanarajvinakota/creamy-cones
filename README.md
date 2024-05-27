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
![Ascii image ](/assets/ascii.png)

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
* [ASCII](https://ascii-generator.site)

# Python libraries used

* [Datetime](https://docs.python.org/3/library/datetime.html) to add the time to the receipt and spreadsheet of when the order was placed
* [UUID](https://thewebdev.info/2021/10/24/how-to-create-a-guid-or-uuid-in-python/?fbclid=IwAR16O6f7oQc62Uo-lG0VW7wzm-_6GxAsuMkFnzIb-5_cKQlTXUveOWsXGgg) to generate a random code to use as an order number
* [Sys](https://stackoverflow.com/questions/14639077/how-to-use-sys-exit-in-python) to allow the user to exit the function
* [Gspread](https://docs.gspread.org/en/latest/) to link my google sheet for the owner to see the data of the orders 
* [Colorama](https://pypi.org/project/colorama/) to add colors to the text