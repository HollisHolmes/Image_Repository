# Dynamic Image Repository

## Languages and Framework
This web application was built using Python and the Django Web Framework. Logic and models handled with Python, and SQL database queries abstracted to model classes via Django's functionality. Initial items to populate the site were scraped off of Amazon.com using the Beautiful Soup library and converted to JSON format. These items were then migrated to a SQLite3 database using a Fixture Migration within Django. Web page designed using HTML and styled with CSS. The project's functionality is split between two apps, a repository-app to handle items, and a users-app to handle user authentication and permissions. 

## Functionality

### Authentication
To have any functionaly on the site, users must register for an account and then be authenticated throught the login portal. Once an account is registered their use information is stored within a Users database within the User app.

### Add
Once the users have been authenticated they are able to add items to the items-app which will remain registered to their user-id. The user to item relationship is managed via a foreign key in the items table realting each item to a user (one to many relationship)

### Remove
Once the users have been authenticated they are able to remove items that belong to them (that they have previously added. This can be anaged through a page that queries the database for all items belonging to this user.

### Search
Once a user have been authenticated they can search for any item in the database. The search prioritizes item 'tags' that can be added by users, then searches for the keyword in item names. These items are returned visually, including an image, to the user on the dynamic homepage.

### Web Scraping
I learned how to use Beautiful Soup to scrape thousands of clothing items from Amazon.com through searching the web page's document object model (DOM). These items were converted to JSON format so they could be migrated to a SQLite3 database via a fixture migration.

### Pricing
Each user is started with 10000, and may purchase any set of items whos price sums to less than their current balance.

### Future Improvements
Although I am very proud of my work to learn web-programming, and two new frameworks (Django and Beautifull Soup) which provide the core functinality of the site, there is stull much to be desired.
1) **Unit Testing** Unit testing is imperative when developing a web application particularly in a production environment. I wrote small tests for my functions that handle the main logic of the code, however these could be significantly improved. Furthermore, to test the functionality of my site, I have been learning Selenium (more documentation!). This testing framework allows a script to interface with the document object model of a web page (selcting, typing, clicking etc.). Ideally I would further improve my skill with Selenium and develop rigorous tests.
2) **Design** The aesthetics of the project could be significantly improved. I will work to improve my CSS and SASS.
