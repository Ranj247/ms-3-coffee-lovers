# [Coffee Lovers](https://ms-3-coffee-lovers.herokuapp.com/)

## Table of contents

-  [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Manual Testing](#manual-testing)
    - [Further Manual Testing](#further-manual-testing)
    - [Compatibility and Responsiveness](#compatibility-and-responsiveness)
    - [Validation](#validation)


***

## Demo
A live demo can be found - [here](https://ms-3-coffee-lovers.herokuapp.com/)

Main README.md file can be found - [here](https://github.com/Ranj247/ms-3-coffee-lovers/blob/main/README.md)

Project Repository can be found - [here](https://github.com/Ranj247/ms-3-coffee-lovers)


***

## Testing
### Testing User Stories
Testing User Stories from User Experience (UX) Section

As a first-time visitor to the website, I want to:
- explore all the coffee recipes on the website added by different users.
    - The landing page has heading called, All Recipes, and below that all the recipes added by other users are displayed.
    - The landing page, "Home" page is clearly visible on the Navbar which would redirect the users to the recipes page.
    - All Recipes are displayed with in the card panels which enhances and provides clear recipe information.
- use the search functionality to narrow down favourite recipes using the keywords.
    - The landing page has heading called, All Recipes, and under that there is a "Search Recipes" field which is clearly visible.
    - The search field can be used to search keywords relating to coffee recipes and click "Search" button. 
    - For the next search, the search field can be easily cleared by clicking "Reset" button.
- contribute to the website by adding own favourite coffee recipes. 
    - The "Register" button is clearly visible on the landing page and as well as on all pages on the Navbar.
    - The users are prompted to register an account by creating a unique username and password via a registration form on the "Register" page.
    - After registering an account, the "New Recipe" page will be visible to the user which would allow to add new recipes. 
- experience easier registration process.
    - The registration process is quite straightforward which only requires creating a unique username and password.<br><br>

As a returning visitor to the website, I want to:
- explore all the coffee recipes on the website added by different users.
    - The landing page has heading called, All Recipes, and below that all the recipes added by other users are displayed.
    - The landing page, "Home" page is clearly visible on the Navbar which would redirect the users to the recipes page.
    - All Recipes are displayed with in the card panels which enhances and provides clear recipe information.
- use the search functionality to narrow down favourite recipes using the keywords.
    - The landing page has heading called, All Recipes, and under that there is a "Search Recipes" field which is clearly visible.
    - The search field can be used to search keywords relating to coffee recipes and click "Search" button. 
    - For the next search, the search field can be easily cleared by clicking "Reset" button.
- Login to my account to see recipes I have added:
    - The "Log In" button is clearly visible on the landing page and as well as on all pages on the Navbar.
    - On the Login page, users are prompted to log in to their account with their username and password.
    - After logging in, the user can go to the Profile page to view all their added recipes.
- Edit and Delete recipes that I have added.
    - Each recipe is displayed on a card panel with an Edit and Delete icon on the top right corner.
    - A conditional check is implemented where Edit and Delete icons only appear on the recipes added by the current user.
    - Edit icon is wired up to open an Edit Recipe page, a form is presented to the user, pre-filled with the current recipe information.
    - The user can edit the pre-filled information and click the "Save" button or "Clear" button to cancel the changes. After saving the changes, the user is redirected to the Home page, with a flash message confirming that the recipe has been updated.
    - Delete icon is wired up to a delete recipe functionality, which would require confirmation from the user by showing a pop message at the top of the window before deleting the recipe. 
    - The user can confirm their choice by clicking "Ok" or "Cancel" button and then they are redirected to Home page, and a flash message is populated confirming that the recipe has been deleted.
- Contact the site admin to request the addition of new brew methods:
    - Admin's email address has been provided in the Footer section for the user's potential queries.<br><br>

As the site owner, I want to:
- Log in to the website as an admin account:
    - On the Login page, if an admin account exists, the admin can log in to their admin account with the username "admin" & their existing password.
- Create, Edit, and Delete coffee brewing recipes.
    - The admin as a user is able to create, read, edit, and delete their own recipes. 
    - Currently, on the Home page under All Recipes, the recipe cards don't show the conditional checks, Edit and Delete icons for recipes added by other users, this functionality was missed out as these features can be implement when skills develop.
- Create, Edit, and Delete coffee brew method categories.
    - The admin only has the access to see the additional page "Manage Brew Methods" which allows the admin to be able to create, read, edit, and delete Coffee Brew Methods.
    - The "Manage Brew Methods" button is clearly visible on the landing page and as well as on all pages on the Navbar.
    - On the Manage Brew Methods page, the admin is presented with a list of currently added brew methods from the MongoDB database. 
    - On the Manage Brew Methods page, the "Add Brew Method" button is immediately visible. When clicked, this button opens the "Add Brew Method" page.
    - On the Add Brew Method page, the admin is presented with a input field which prompts them to enter the name of the brew method.
    - After saving the brew method, the admin is redirected to the Manage Brew Methods page, with a flash message shown to confirm that the brew method has been added.
    - Each Brew Method is shown on a card with an Edit and Delete buttons displayed at the bottom.
    - Edit icon is wired up to open an edit brew method page, a form is presented to the user, pre-filled with the current brew method information.
    - The admin can edit the pre-filled information and click the "Save" button or "Clear" button to cancel the changes. After saving the changes, the admin is redirected to the Manage Brew Methods page, with a flash message confirming that the brew method has been updated.
    - Delete icon is wired up to a delete brew method functionality, which would require confirmation from the user by showing a pop message at the top of the window before deleting the brew method. 
    - The admin can confirm their choice by clicking "Ok" or "Cancel" button and then they are redirected to Manage Brew Methods page, and a flash message is populated confirming that the brew method has been deleted.<br><br>


### Manual Testing
Manual testing was performed on the following elements that appear across all pages on the site, to ensure that all are working as expected;

#### All Pages
- Navbar
    - Test carried on the **Website Logo** which appears on the left of the menu bar to ensure it points to the Home page.
    - Test carried on the website pages such as  **Home, login, Register, Profile, New Recipe, Manage Brew Methods** pages to ensure each point to respective page.
    - Collapsible sidebar button opens the sidebar navigation element on mobile devices.
    - All navigation links within the collapsible sidebar correctly direct the user to the corresponding site page.
    - Test carried on the Login & Register navigation links which only appear when the user is unregistered.
    - Test carried on the Profile and Logout navigation links correctly appear only when a user is already logged in and the logout button logs the user out.
    - Test carried on the Manage Brew Methods navigation link which appears only when the "admin" user is logged in. 
    - Test carried on the links and action buttons such as **Search, Reset, Add, Edit, Delete, Save, Clear** to ensure specific action takes place.
    - Test carried by hovering the mouse over the navigation links which triggers the expected hover effect color.
- Footer
    - Test carried on the **Social Media icons** in the Footer to ensure the specific link opens the correct pages, and in the new tab.
    - Test carried by hovering the mouse over the footer links which triggers the expected hover effect color.<br><br>

#### Recipes Page (Home Page)
Manual testing was performed on the following elements that appear on the Recipes/Home page;
    - Test carried on the website pages such as  **Home, login, Register, Profile, New Recipe, Manage Brew Methods** pages to ensure each point to respective page.
- Hero Section:
    - Test carried on the Hero image which is appropriately responsive across all device sizes.
    - Test carried on the Login & Register buttons which appear when the user is unregisetered.
    - Test carried on the Profile button which correctly appears only when a user is already logged in.
    - Test carried on the Manage Brew Methods button which appears only when the "admin" user is logged in.
- Search Section:
    - Test carried on the Search functionality which validates whitespace and min/max input lengths.
    - An error message is surfaced when no database documents match the search term.
    - Reset button reloads the page to clear search terms & re-populate all recipe cards.
- Recipe Cards:
    - Recipe info is correctly iterated over to create a card for each recipe.
    - Edit & Delete icons only appear for registered users, and only on recipes that match the current user.<br><br>

#### Login Page
Manual testing was performed on the following elements that appear on the Login page:
- Test carried on the "Register Here" link which correctly directs to the Register page for users who are not yet registered.
- Test carried on the Login form input field which validate whitespace, minlength, maxlength, and required patterns.
- Login functionality correctly performs validation checks to ensure that the username exists, and that the password is correct for that user.
- An error message is displayed if the username does not exist, or if the user's password is incorrect.
- After successfully logging in, the user is directed to the Home page, with a flash message to confirm that they are logged in.<br><br>

#### Register Page
Manual testing was performed on the following elements that appear on the Registration page:
- Test carried on the "Log In Here" link which correctly directs to the login page for users who already have an account.
- Test carried on the Username input field which validates that the input value does not match an existing username.
- Username & password inputs validate whitespace, minlength, maxlength, and required patterns.
- Test carried on the Register button which correctly triggers a User document to be created in the MongoDB database.
- After successful registration, the user is automatically logged in and directed to the Home page, with a flash message populated to confirm that their registration was successful.<br><br>

#### Profile Page
Manual testing was performed on the following aspects of the Profile page:
- After logging in, a flash message displays the correct user name to confirm that the login was successful.
- Test carried on the "Add Recipe" button which correctly directs the user to the Add Recipe page.
- Test carried by adding a recipe, and only the recipes added by the user appears on their profile.<br><br>

#### Add, Edit, Delete Recipe Pages
Manual testing was performed on the following aspects of the Add, Edit, Delete Recipe Pages:
- Test carried out by adding a recipe, the form correctly populate the lists for coffee brew methods, coffee roast levels, and coffee grind of beans, quantity of coffee, brew time in the dropdown menus.
- Test carried out by editing a recipe, the form correctly pre-populates the existing values for each field of the existing recipe.
- The "Clear" button correctly redirects back to the Home page without submitting the form.
- When deleting a recipe, the delete icon is wired up to a delete recipe functionality, which would require confirmation from the user by showing a pop message at the top of the window before deleting the recipe. 
- The user can confirm their choice by clicking "Ok" or "Cancel" button and then they are redirected to Home page, and a flash message is populated confirming that the recipe has been deleted.<br><br>

#### Manage Brew Methods Page (ADMIN)
Manual testing was performed on the following aspects of the Manage Brew Methods Page:
- The "Manage Brew Methods" button is clearly visible, correctly directs to the Add Brew Method page.
- Brew methods list is correctly iterated over to create a card for each brew method.<br><br>

#### Add, Edit, Delete Brew Method (ADMIN)
Manual testing was performed on the following aspects of the Add, Edit, Delete Brew Method Pages:
- Test carried out by adding a brew method, the form correctly validates whitespace in brew method name.
- Test carried out by editing a brew method, the form correctly pre-populates the existing value of the brew method.
- Save button correctly triggers functionality to add brew method to database, and after successfully adding a brew method, directs the admin back to the Manage Brew Methods page with a success message populated.
- The "Clear" button correctly redirects back to the Manage Brew Methods page as expected without submitting the form.
- When deleting a brew method, the delete icon is wired up to a delete brew method functionality, which would require confirmation from the admin by showing a pop message at the top of the window before deleting the brew method. 
- The admin can confirm their choice by clicking "Ok" or "Cancel" button and then they are redirected to back to the Manage Brew Methods page, and a flash message is populated confirming that the brew method has been deleted.<br><br>


### Further Manual Testing
- Checked grammar and spelling throughout document.
- Ran README text through [Online-Spellcheck](https://www.online-spellcheck.com/) to double-check on grammar and spelling.
- Ran CSS through [Autoprefixer](https://autoprefixer.github.io/) and copied the resulted CSS codes back into style.css file.

- Test carried on grounds of Performance, Accessibility, Best Practices and SEO using [Lighthouse Report Viewer](https://googlechrome.github.io/lighthouse/viewer/).<br><br>
    ![Image](readme-assets/images/lighthouse-report.PNG)<br><br>
    [Result](https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2F8080-tan-hippopotamus-ptxfv8r3.ws-eu15.gitpod.io%2F&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo&category=pwa&utm_source=lh-chrome-ext)<br><br>

- Test carried on the overall site colours on [a11y](https://color.a11y.com/), a Color Contrast Accessibility Validator.<br><br>
    ![Image](readme-assets/images/website-color-contrast-report.PNG)<br><br>

### Compatibility and Responsiveness
The website has been tested on different browsers and electronic device, no compatibility issues noted. The site was found to be fully responsive on device sizes ranging from 320px X 480px to 1920px X 1080px.

- Browsers tested:
    - Chrome 
    - Safari 
    - Firefox 

- Devices tested:
    - iPhone 6
    - Samsung A20
    - Desktop PC
    - Laptop
    - Tablet

- Test carried on the Responsiveness of all pages using [Responsive Design Checker](https://responsivedesignchecker.com/).

- Test carried on the Responsiveness of all pages using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly).<br><br>
    ![Image](readme-assets/images/Mobile-friendliness-test.PNG)<br><br>

### Validation
- Tested [HTML Validation](https://validator.w3.org/) No errors or warnings to show. This validator does not recognise Jinja templates & scripting, so returns errors for the lines of code where Jinja is used - this is to be expected. No errors are present in the HTML code otherwise.
- Tested [CSS Validation](https://jigsaw.w3.org/css-validator/) No errors found.<br><br>
    ![Image](readme-assets/images/CSS-validation-report.PNG)<br><br>

- [JSHint](https://jshint.com/) was used to validate the JavaScript code in the script.js file. No errors are present.
- [PEP8 Online](http://pep8online.com/) was used to validate that the Python code in app.py is PEP8 compliant. No errors are present.<br><br>
    ![Image](readme-assets/images/PEP8-report.PNG)<br><br>

***

