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
