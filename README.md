# Waze50 — Harvard CS50 Web — Final Project


## Distinctiveness and Complexity:
I made an interactive 'Google Maps'/'Waze'-like website using Django on the back-end and JavaScript on the front-end. This project uses a JavaScript library called Mapbox GL JS for map rendering, tracking current location, search for places, providing directions, and reporting traffic. This website has seven main features:
1. Real-time location tracking.
2. Search for places in the input that has auto-suggestions(When you start typing in the query, then it displays suggestions of what you might be looking for) and marker display at the location you selected.
3. For signed-in users, the search history is displayed when the search input is cleared. Clicking a history item takes you to that location with a marker (up to five searches are saved).
4. The 'Direction' feature shows routes between two places with suggestions(similar to the search) for both 'from' and 'to' inputs(Depending on which input you have selected, it will display the suggestion in that input). After searching, it displays the route, distance, and travel time by car.
5. Signed-in users have a direction history that autofills both inputs when clicked. The history is displayed when the input is empty (up to five directions are saved).
6. Signed-in users can report traffic by clicking on a street, which displays a red line and a popup with the street name and reporter's name (linked to their profile). Users can remove their own traffic reports, which stays after reload until manually removed.
7. Each authenticated user has a profile with a reputation system showing their name, good and bad reviews, and a trustworthiness rating based on review percentages. Users can review others posts once, with comments displaying the review type, date, and content. Users cannot review their own posts.
Finally, the non-main/less distinct features:
*  The search submit button is enabled after typing begins. The directions submit button is enabled when both inputs have more than one character.
*  There is also a login and register feature.

---

## Why I did this project?
One day, my dad told me that he might want me to make a Lazada-like website, where after someone has ordered a package, it shows a live map of the delivery driver delivering to the consumer. So, I thought of making this website to have at least some sort of idea of how maps can be used in a website. The reason I used Mapbox over Google's API was that I didn't know how to use Google, and I couldn't either way because I only had a Touch 'n Go card to subscribe for free. Mapbox accepts that card.

---

## Additional information
There are two thinks I think you should know about. 1. I was coding for this project less than two weeks ago. I initially made profiles for users with a like and unlike button instead of good or bad reviews. However, I encountered migration errors. Even after deleting the like from the models (where I gave them default values in the terminal), the errors persisted. So, I copied my code, deleted the folder, created a new one, and pasted everything back. I tried to be careful with code that required default values and avoided using them. If you wonder why there aren't many migrations, this is the reason. 2. This project does have an error I encountered: some streets do not load the red line after reporting traffic, only the popup. I found out that it has something to do with API caching (this information is what I have understood from the Mapbox FAQ). It looked like a lot of work, and I got lazy and didn't do it.

---

## What's contained in each file:
* urls.py: Contains the URL patterns for routing requests to the appropriate views.
* views.py: Contains views for login, register (creates profile when you create account), logout, search (saves search history), directions (saves direction history), profile (manages profile, comments, reviews), and index (renders search and direction histories).
* models.py: Contains all of the project's models, which are "User", "SearchHistory", "DirectionHistory", "Profile", and "Comment"
* admin.py: Registers Comment and DirectionHistory for the Django admin interface.
* forms.py: Defines CommentForm with review type choice field and comments text area with custom styling.
* index.html: Contains links for displaying the world map with interactive features, a div with the id map, and variables used in other files. Index also includes search form, search history, report button, direction form (with "from" and "where" inputs), direction history, and buttons for displaying search and direction. Also includes functions for handling text and color changes of the report traffic button, and external JavaScript files for map rendering, search logic, directions, and traffic reporting.
* layout.html: Links to Bootstrap and my CSS files, includes a meta tag for responsive design, and a navigation bar with links to index, login, logout, register, and the brand name.
* login.html: Contains the login template for the project
* register.html: Contains the register template for the project
* profile.html: Displays the username, user’s reputation based on good review percentage, counts of good and bad reviews, a comment form with review radio selection, and a comment section.
* map.js: Contains API and map rendering with default display of New York, gets the user's location, includes functions for navigating to selected locations with markers (used in search and direction files), and draws routes for directions.
* search.js: Handles search form (disables submit button if input is empty, processes form submission without reloading), updates location (updates map with new coordinates and marker, focuses on searched location), provides suggestions (using Mapbox API as the user types), displays search history (displays and allows the user to select from past searches), and shows history if input is empty or suggestions if input has more than 2 characters.
* directions.js: Validates inputs (disables submit button until both starting and ending points are not empty), fetches directions (uses Mapbox API for coordinates and Directions API for route, distance, and travel time), displays direction history (allows selection of past routes and auto-fills fields), handles events (updates suggestions and handles clicks to auto-fill inputs), and shows history if both inputs are empty or suggestions if any input has more than 2 characters.
* traffic.js: Contains traffic mode (Button toggles "Report Traffic" on/off. When on, users can click roads to report incidents), display reports (Clicked streets show as red lines with popups (street name, reporter, close button if self-reported). Clicking the close button removes the red line and popup), page load(loads previous traffic reports from localStorage, displaying them as red lines with popups), local storage (saves traffic reports in localStorage to persist after reload).
* profile.css: Conatins all the CSS design for profile.html
* LLRR.css: Contains all the CSS design for login.html, layout.html, register.html, responsive design for index.
* index.css: Contains all the CSS design for index.html

---

## How to run the application:
1. Navigate to the project directory: cd finalproject in terminal
2. Run "python manage.py runserver" in the terminal(if it doesn't work, run 'python manage.py makemigrations' and 'python manage.py migrate' first then runserver)
3.  Open your web browser and go to 'http://127.0.0.1:8000'
