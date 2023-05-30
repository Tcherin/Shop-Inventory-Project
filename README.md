# shop_inventory solo_project

## Project description:
### What does the application do?
This is my first full-stack app project. The brief I chose required me to build a shop inventory app that can add products and manufacturers seperately.
I chose to make this shop a video shop, which buys videos from suppliers.

The app had to meet the following criteria:
* app needed to have CRUD functionality.
* The inventory should be able to track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should be able to track manufacturers, including a name and any other appropriate details.
* The shop could sell anything you like, but you should be able to create and edit manufacturers and products separately.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should be able to visually highlight "low stock" and "out of stock" items to the user.

Extensions were also suggested, such as:
* Calculate the markup on items in the store, and display it in the inventory
* Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
* Provide the ability to filter items by a particular attribute, e.g genre for books.
* Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

### Technologies used and why?
I have used Python, HTML, CSS, Flask framework, Djinja, PostgreSQL, psycopg2 to build this full stack web application. 
The aim of this project was to use these languages and framework, learned over the previous 4 weeks, in one program to solidify my knowledge.

### Challenges faced and features I hope to implement in the future:
In the future I would like to include:
* A customer class and table that would allow me to factor in transactions made with various customers.
* A till feature that would allow me to see a running total of money coming in, in exchange for videos rented to customers.

## How to install and run the project:
1. Open files in editor e.g. Visual Studio Code
2. Create database: 'video_shop.sql' - Run `dropdb video_shop` then `createdb video_shop`
3. Run psql in the terminal to initiate the database `psql -d video_shop -f db/video_shop.sql`
4. Run console.py file using command `python3 console.py`
5. Run Flask using command `flask run`
6. Access webpage using url: http://localhost:4999
7. To exit Flask, use CTRL + C in the terminal
