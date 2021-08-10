# [Coffee Lovers](https://ms-3-coffee-lovers.herokuapp.com/)

Coffee Lovers is a website where users can view coffee brewing recipes and contribute by sharing their own recipes on the website for other users. This website has been created for my third milestone project as part of the Diploma in Full Stack Software Development course with Code Institute. The website is responsive on all device sizes.

***

## Table of contents

-  [Demo](#demo)
-  [Overview](#overview)
-  [User Experience (UX)](#user-experience)
-  [Technologies used](#technologies-used)
-  [Resources](#resources)
-  [Testing](#testing)
-  [Code validity](#code-validity)
-  [Version Control](#version-control)
-  [Deployment](#deployment)
-  [Credits](#credits)
-  [Acknowledgments](#acknowledgements)

***

## Demo
Please click on the image to open link in a new browser window.

![Image](https://res.cloudinary.com/dvsb7k8tp/image/upload/v1628563391/MS3/AmiResponsive-mockup-image_hjacki.png) 

A live demo can be found - [here](https://ms-3-coffee-lovers.herokuapp.com/)

***

## Overview
This is a Coffee Lovers page, which has been designed solely for coffee lovers who would like to find and share their own coffee brewing recipes with other members of the community. This website has been built for my third milestone project which is part of the Code Isntitute's FullStack Software Development Diploma Course, and the main focus is to build a full-stack website allowing users to manage a common dataset. This project demonstrates the skills and knowledge of using the HTML5, CSS3, JavaScript, Python,the Flask framework, Jinja templating language and MongoDB in Back-End development which I have learned recently on the course.

The aim of the project is to create a coffee brewing recipes website keeping in mind the CRUD functionalities: Create, Read, Update, and Delete recipes from the database. Upon registration, the user will be able to view their profile, create new recipes, update and delete their own recipes at any time. The website is created using the Materialize CSS responsive designing which provide a better user experience from mobile devices to tablets or larger screens.The website was created for educational purposes.

***

## User Experience
This website would advance the user's goals by providing CRUD functionality to the coffee recipes database. It advances the site owner's goals by being a regular user of the site themselves.

The User Experience for this site was planned & developed using the [5 Planes of UX Design](https://www.geeksinux.com/the-elements-of-user-experience-design/): Strategy, Scope, Structure, Skeleton, Surface.

### Strategy
#### User Stories

- As a first-time visitor to the website, I want to:
    - explore all the coffee recipes on the website added by different users.
    - use the search functionality to narrow down favourite recipes using the keywords.
    - contribute to the website by adding own favourite coffee recipes. 
    - experience easier registration process.

- As a returning visitor to the website, I want to:
    - explore all the coffee recipes on the website added by different users.
    - Search for recipes by keyword.
    - Login to my account to see recipes I have added.
    - Edit recipes that I have added.
    - Delete recipes that I have added.
    - Contact the site owner/admin to request the addition of new brew methods.

- As the site owner, I want to be able to:
    - Log in to the website as an admin account.
    - Create, Edit, and Delete coffee brew method categories.
    - Create, Edit, and Delete coffee brewing recipes.

### Scope
#### Existing Features
- **Hero Image:**
    - The hero image of coffee being extracted from the coffee machine hints user that the site content relates to a coffee website.
- **Search Functionality:**
    - The search functionality allows all users, registered or unregistered to search for coffee recipes by keywords.
- **Register:**
    - Users can very simply create an account on the website, the user input is validated, a new "user" document in the site's database is created, and hashing is used for password security. After an account is created, a flash message appears on the screen to showcase that the registration being successful and now the new user would be able to contribute by adding their favourite coffee brewing recipes. 
- **Login/Logout:**
    - The Login/Logout functionality adds authentication for registered users, allowing them to access, edit and delete their own recipes. Allows users to logout by clearing the "session" cookie.
- **Profile:**
    - The Profile provides functionality for registered & logged in users to see their own recipes (if any recipe created), add more recipes, edit or delete their existing recipes.
- **Add Recipe:**
    - The Add Recipe provides functionality for registered users to add their own recipes via a form.
- **Edit Recipe:**
    - The Edit Recipe provides functionality for registered users to edit recipes that they've added. Extra checks are in place here to ensure the current user matches the username of the user who created the recipe.
- **Delete Recipe:**
    - The Delete Recipe provides functionality for registered users to delete recipes that they've added. Extra authentication steps are also in place in this feature to ensure that the current username matches that of the recipe's creator.
- **Manage Brew Methods:**
    - The Manage Brew Methods functionality provides the Admin of the site to view all of the coffee brew methods.
- **Add Brew Method:**
    - The Add Brew Method functionality provides a form where the site admin can add new coffee brew method.
- **Delete Brew Method:**
    - The Delete Brew Method functionality provides functionality for the site admin to remove brew methods from the site.

#### Future Planned Features

### Structure
#### Flowchart

### Skeleton
#### Wireframes


### Surface


***

## Technologies Used

### Tools
- [GitPod](https://www.gitpod.io/)
    - Used as the preferred IDE for development.
- [Git](https://git-scm.com/)
    - Used via the Gitpod terminal for version control, with regular commits, and to push to GitHub & Heroku.
- [GitHub](https://github.com/)
    - Used to store the site's code repository.
- [Heroku](https://www.heroku.com/)
    - Used to host the deployed site.
- [Lucidchart](https://www.lucidchart.com)
    - To create the site's structural flowchart.
- [Balsamiq](https://balsamiq.com/)
    - To create the site's wireframes.
- [Google Fonts](https://fonts.google.com/)
    - Used to import the site's fonts.
- [Compress JPEG](https://compressjpeg.com/)
    - Used to compress the site's hero image.
- [Cloudinary](https://cloudinary.com/)
    - Used to link image files to the README.md file.

### Front-End Technologies
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [JQuery 3.6.0](https://jquery.com/)
    - Used as the primary JavaScript library.
- [Materialize 1.0.0](https://materializecss.com/)
    - Used as a responsive front-end framework.

### Back-End Technologies
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Used with Python as the primary web microframework.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Used for creating templates with Flask.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    - Used for password hashing & authentication on the site.
- [MongoDB Atlas](https://www.mongodb.com/)
    - Used to store the site's database.
- [PyMongo](https://pypi.org/project/pymongo/)
    - Used to interact with the MongoDB database from Python.

***

## Resources

- [Code Institute Course Content](https://courses.codeinstitute.net/login) -Main source of fundamental knowledge.
- [Stack Overflow](https://stackoverflow.com/) -General resource.
- [Google chrome developer tools](https://developer.chrome.com/docs/devtools/) - used to check page elements, help debug issues with the site layout and test different CSS styles and console JS.
- [w3schools](https://www.w3schools.com/default.asp)-General resource.
- [Balsamic](https://balsamiq.com/wireframes/) - Wireframing design tool to create wireframes.
- [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator.
- [Imagecolorpicker](https://imagecolorpicker.com/en) - color schemes generator.
- [a11y](https://color.a11y.com/Contrast/) - Website color contrast checker
- [Lighthouse Report Viewer](https://googlechrome.github.io/lighthouse/viewer/) - used as part of testing website on grounds of Performance, Accessibility, Best Practices and SEO.


***

## Testing

***

## Code validity
- HTML - [Markup Validation W3C Service](https://validator.w3.org/)
- CSS - [Jigsaw  Validation W3C Service](https://jigsaw.w3.org/css-validator/)

***

## Version Control
- Used Git for version control.

***

## Deployment
### Local Deployment

The following dependencies will need to be installed in order to run this application locally:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install app requirements.
- [GitPod](https://www.gitpod.io/) or any preferred IDE, such as [VSCode](https://code.visualstudio.com/).
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for cloning and version control.
- [MongoDB](https://www.mongodb.com/) to create a database using MongoDB Atlas.

Follow the below steps for local deployment:

1. Clone the GitHub repository by entering the following command into the Git terminal:
    - `git clone https://github.com/Ranj247/ms-3-coffee-lovers.git`
2. After cloning the project, create an `env.py` file that includes the below code, replacing the `SECRET_KEY`, `MONGO_URI`, `MONGO_DBNAME` with your own credentials:
```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGO_URI")
os.environ.setdefault("MONGO_DBNAME", "coffee_lovers")
```
3. Create a `.gitignore` file, and add the `env.py` file to the list of files.
4. Install all requirements from the [requirements.txt](https://github.com/Ranj247/ms-3-coffee-lovers/blob/main/requirements.txt) file using this command:
    - `pip3 -r requirements.txt`
5. Sign up for a [MongoDB](https://www.mongodb.com) account, and create a new Database called `coffee_lovers`. The collections in that database should be structured as follows:

**coffee_brew_methods**
```
_id: <ObjectId>
method_name: <string>
```

**recipes**
```
_id: <ObjectId>
recipe_method: <string>
roast_level: <string>
grind_of_bean: <string>
quantity_of_coffee: <string>
brew_time: <string>
recipe_description: <string>
created_by: <string>
```

**users**
```
_id: <ObjectId>
username: <string>
password: <string>
```

6. Run the app using the following command in the terminal:
    - `python3 app.py`

### Remote Deployment

To deploy this app on Heroku, the following steps were taken:

1. Create a `requirements.txt` file so Heroku can install the required dependencies.
    - `pip3 freeze --local > requirements.txt`
    - This project's requirements.txt file can be seen [here](https://github.com/Ranj247/ms-3-coffee-lovers/blob/main/requirements.txt).
2. Create a `Procfile` with information about the type of app that will be deployed.
    - `echo web: python app.py > Procfile`
    - This project's Procfile file can be seen [here](https://github.com/Ranj247/ms-3-coffee-lovers/blob/main/Procfile).
    - Make sure to delete the blank line at the end of the Profile, as this can cause issues when deploying to Heroku later.
3. Create a Heroku account, create a project app, and click the "Deploy" tab. 
4. "Connect GitHub" as the Deployment Method, and select "Enable Automatic Deployment".
4. In the "Settings" tab, click the "Reveal Config Vars" button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `5000`
    - **SECRET_KEY** : `<YOUR_SECRET_KEY>`
    - **MONGO_URI** : `<YOUR_MONGO_DB_URI>`
    - **MONGO_DBNAME**: `coffee_lovers`    
    
5. The app should now be deployed to Heroku - click the "Open App" button to view the deployed site.

***

## Credits

### Media
- [favicon.io](https://favicon.io/) was used to generate the site's favicon image.
- [Pexels](https://www.pexels.com/) used to source Hero image and customised to be used for the website.

### Content
- [6 Popular Methods for Brewing Coffee at Home](https://treescoffee.com/blog/2016/04/6-popular-methods-for-brewing-coffee-at-home/) - inspiration for website content.

### Code Snippets
- Hero Image functionality adapted from [W3Schools Example](https://www.w3schools.com/howto/howto_css_hero_image.asp).
- Fixed Navbar functionality adapted from [W3Schools Example](https://www.w3schools.com/howto/howto_css_fixed_menu.asp).
- Sticky Footer functionality adapted from [Materialize CSS Example](https://materializecss.com/footer.html).
- Code Institute coursework mini project: 
- [Stack overflow](https://stackoverflow.com)

***

## Acknowledgements
I would like to thank:
- My mentor, **Caleb Mbakwe**, for his guidance, valuable feedbacks, and encouragement through out the project.
- Tutor support at Code Institute, for funtastic support and help with my technical questions.
- Slack community for their suggestions and support.

***
