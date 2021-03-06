# XFIT - Crossfit Gym
## Full Stack Frameworks with Django Milestone Project 4

![homepage mock up](/media/website-mockup.jpg)

The [XFIT Crossfit](https://xfit-crossfit-ms4.herokuapp.com/) website was built by Kirstyn Luton as part of the Full Stack Frameworks with Django Milestone Project 4, with Code Institute. The website presents an online space for a company called “XFIT Crossfit”.  It allows for merchandise sales, membership sales, class schedules and daily workouts to be shared into their community. 

The website is deployed using Heroku pages here: [XFIT Crossfit](https://xfit-crossfit-ms4.herokuapp.com/)

The GitHub repository containing the source code and assets is available here: [GitHub Repo](https://github.com/KJLuton/Project4_XFIT)
Disclaimer: This website has been built for entertainment and education purposes. It does not represent an actual company. The website is responsive for multiple screen types.

Users can be created for the website on the site. To test any payment features, please use card below:
<strong>Method:</strong> Credit card <br>
<strong>Scenario 1:</strong> The card payment succeeds and doesn’t require authentication.<br>
<strong>Testing:</strong> Fill in the credit card form using the credit card number 4242 4242 4242 4242 with any expiry, CVC, and postal code.<br>
<br>

## [View live website on Heroku App](https://xfit-crossfit-ms4.herokuapp.com/)
---

# Table of Contents

1. [UX](#ux)
    - [Website owner business goals](#website-owner-business-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Database Design](#database-design)
    - [Wireframes](#wireframes)
        - [Homepage - Wireframe](###homepage-wireframe)
        - [Shop - Wireframe](###shop-wireframe)
        - [Classes - Wireframe](###classes-wireframe)
        - [Contact - Wireframe](###contact-wireframe)
    - [Surface](#surface)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
    - [Functionality testing](#functionality-testing)
    - [Code Validation](#code-validation)
    - [User stories testing](#user-stories-testing)
    - [Issues found during site development](#issues-found-during-site-development)
5. [Deployment](#deployment)
6. [Credits](#credits)

# UX

## Website owner business goals

The website owner is the owner of a crossfit gym called XFIT Crossfit. 

## User goals

## User stories and goals

All user stories can be found here [here](https://docs.google.com/spreadsheets/d/1pOBh0FCzIuVy0o07vWA4MQvVk5BNl09HXZjQ0tReOWA/edit?usp=sharing)

## Database Design

Categories & Products
- memberships
    - 1 year membership
    - 1 month membership
- shorts_leggings
    - xfit shorts
    - xfit leggings (womans)
- xfit_essentials
    - wrist straps
    - weightlighting belt
- tshirts_hoodies
    - xfit tank top
    - xfit tshirt
    - xfit hoody

Users
- Super User 
    - Manage Products 
    - Purchase products
- Logged in & Profile Holder
    - Save personal information for faster checkout
    - Purchase products
- Website user 
    - Purchase products 


## Wireframes

### Homepage - Wireframe
[Homepage-Wireframe](/media/xfit-homepage-wireframe.png)

### Shop Page - Wireframe
[Shop-Wireframe](/media/xfit-shop-wireframe.png)

### Classes Page - Wireframe
[Classes-Wireframe](/media/xfit-classes-wireframe.png)

### Contact Page - Wireframe
[Contact-Wireframe](/media/xfit-contact-wireframe.png)

## Surface

### Colours

The main colours used in this project are: 

#FF6F61 - orange
#333 - dark grey
#fff - white

### Fonts

The fonts are installed from [Google Fonts](https://fonts.google.com/):

* h1, h2, h3, h4, h5: Orbitron with a backup of sans-serif.

[Back to table of contents](#table-of-contents)
_______
# Features and functions

General user: 

Super User: 
* Add product 
* Edit Product 

## Existing Features

## Apps

### Home App 
- The Home App welcomes the user to the website and gives clear navigational direction on where the user needs to click in order to achieve their particular goals. 

### Profiles 
- The Profiles App provides the user with a place to save default delivery information. 
- It also provides the user with a record of their order history.
- The Profile App uses a form model to capture the users details attached them to their account, should they wish to save their account for future use. 

### Shop App 
- Host the merchandise and membership items being sold by the crossfit gym. Provide a platform to search for products and see individual product views according to what the user wants to see. 
- Allows the logged in super user to create, edit and delete products on the shop. 

### Bag App 
- The bag app allows users to browse the products on the site and collect the sizes and items they want into place, before they proceed to the checkout.
- The bag app is where the calculations take place in order to understand how much the user owes for the purchase. 
- The bag app also calculates the delivery cost according to the amount that is in the bag. 

### Checkout App 
- The checkout app is connected to [Stripe](https://stripe.com/gb) and provides a payment function to take a payment from the user according to what is in their bag. 

### Contact Us App
- The contact app provides the user with a contact point via email to get in touch with the crossfit gym. 


## Future implementations

- Add an interactive calendar where members are recognised as a logged in user and can book their sessions in advance according to their membership type. This would allow for managers to limit classes to a certain number of users and allow the users to book in advance to organise themselves better. 
- Add a subscription membership type to allow for on going subscriptions.
- Include a daily workout section on the members area to allow members to see daily workouts and tips. This would encourage members to go on to the site daily and increase traffic to the site. 
- Allow members to comment on the workouts and share their session's best with other members of the gym. This would improve engagement on the site and overall XFIT community. 
- Add confirmation when deleting products. This would help the user experience of the manager as it would give an extra step to avoid accidentally deleting products. 

[Back to table of contents](#table-of-contents)
_______

# Technologies Used

## Languages Used

* #### [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
   Python is an interpreted high-level general-purpose programming language. 

* #### [HTML5](https://en.wikipedia.org/wiki/HTML5)
    HTML was used to build the website structure and overall layout. 

* #### [CSS3](https://en.wikipedia.org/wiki/CSS)
    CSS was used to style the website and build on the Bootstrap framework to customise the website. 

## Frameworks, Libraries and Programmes Used

* #### [Bootstrap](https://getbootstrap.com/)
    Bootstrap 5.0 was used to assist with a responsive design and basic structure of the website.  

* #### [jsDelivr](https://www.jsdelivr.com/)
    jsDelivr was used with Bootstrap and aided the responsive and interactive elements of the site. 

* #### [Font Awesome](https://fontawesome.com/)
    Font Awesome was used to supply icons for the social links and 'Club Facilities' section. 

* #### [Google Fonts](https://fonts.google.com/) 
    Google Fonts were used to install the 'Bebas Neue' and 'Signika Negative' fonts which were used across the site. 

* #### [GitHub](https://github.com/)
    GitHub is used to store the project code. The code is pushed from GitPod to the GitHub respository. 

* #### [GitPod](https://www.gitpod.io/)
    Gitpod was used to write the code and the Git terminal was used for version control. The code was committed to Git and pushed to GitHub via the terminal. 

* #### [Heroku App](https://www.heroku.com)
    Heroku was used to deploy the overall project to ensure the Python languages work preoperly. 

* #### [Django](https://www.djangoproject.com/)    
    Django is teh frame work used to build the application.

* #### [Javascript](https://www.javascript.com/)   
    Javascript was used with Bootstrap and aided the responsive and interactive elements of the site.

[Back to table of contents](#table-of-contents)
_______

# Testing 

The website was tested throughout the build process to ensure user stories were being checked and written code was working properly. 

### Functionality Testing

* The website was initially tested to check the connection to django by typing "python3 manage.py runserver" into the terminal once the initial django installation had been made. The django confirmation screen confirmed the installation had work and the site was connected. 
* Tested the initial allauth account set up by setting the LOGIN_REDIRECT_URL to '/sucess'. Even though the final url path hadn't been set up, the error message was for the url, '/success', which confirms that the authentication is working properly. 
* Compressed images using tinypng.com to ensure images dont take up to much space and slow the site down. tinypng keeps the image quality qhilst reducing te size. 
* Started with 'checkout' teminology for the 'bag' app. Updated it to bag so a checkout could be created and not confused. 
* Used print statements to confirm bag contents were being added and it was set up correctly ahead of rendering the items into the shopping bag template. 

By logging into the Stripe dashboard, I tested the integration and the webhook set up. I checked the events to see if the payment intent was created and processed successfully. [Stripe test payments](https://dashboard.stripe.com/test/payments)
 
<strong><u>Stripe payment testing</u></strong> <br>
<strong>Method:</strong> Credit card <br>
<strong>Scenario 1:</strong> The card payment succeeds and doesn’t require authentication.<br>
<strong>Testing:</strong> Fill in the credit card form using the credit card number 4242 4242 4242 4242 with any expiry, CVC, and postal code.<br>
<br>
<strong>Method:</strong> Credit card <br>
<strong>Scenario 2:</strong> The card payment requires authentication.<br>
<strong>Testing:</strong> Fill in the credit card form using the credit card number 4000 0025 0000 3155 with any expiry, CVC, and postal code.<br>
<br>
<strong>Method:</strong> Credit card<br>
<strong>Scenario 3:</strong> The card is declined with a decline code such as insufficient_funds.<br>
<strong>Testing:</strong> Fill in the credit card form using the credit card number 4000 0000 0000 9995 with any expiry, CVC, and postal code.<br>

<hr>

### User Stories Testing

Testing of the user stories can be found [here](https://docs.google.com/spreadsheets/d/1pOBh0FCzIuVy0o07vWA4MQvVk5BNl09HXZjQ0tReOWA/edit?usp=sharing)


### Code Validation

* #### W3C Markup Validation Service - Confirmed results 

[HTML Validator](https://validator.w3.org/)
<br>
Homepage - Pass <br>
Membership Page - Pass <br>
Classes Page - Pass <br>
Shop Page - Pass<br>
Contact Us Page - Pass<br>
Profile Page - Pass<br>
Login and All auth pages - Pass<br>
<br>
'id="user-options"' running an error on HTML checker as id is used in base.html header and mobile-nav header. <br>

* #### W3C CSS Validation Service - Confirmed result
[CSS Validator](https://jigsaw.w3.org/css-validator/)

Homepage - Pass <br>
Membership Page - Pass <br>
Classes Page - Pass <br>
Shop Page - Pass <br>
Contact Us Page - Pass <br>
Profile Page - Pass <br>
Login and All auth pages - Pass <br>
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>

<br>
I also tested my code on the following validators: 

[Accessibility](https://wave.webaim.org/) <br>
[Performance](https://developers.google.com/web/tools/lighthouse) <br>
[javaScript](https://jshint.com/) <br>
[Python](http://pep8online.com/) <br>

### Issues Found During Site Development

* {% load bag_tools %} wouldn't work. Read django documentation https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/ but everything was set up correctly. Restarted the server and it worked. 

[Back to table of contents](#table-of-contents)
_______
# Deployment

## Local deployment
To deploy this site locally, run the following steps: 
1. Enter the command git add .
2. Enter the command gid commit -m "Enter your commit message here"
3. Ener the command git push

## Heroku Deployment 

To deploy this application to Heroku, run the following steps: 

1. Create an account at heroku.com
2. Create an app, give it a name, and select a region
3. Under resources search for postgres, and add a Postgres database to the app Heroku Postgres
4. Install the plugins dj-database-url and psycopg2-binary.
5. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
6. Create a Procfile with the text: web: gunicorn rugby_shop.wsgi:application for example
7. In the settings.py ensure the connection is to the Heroku postgres database
8. Ensure debug is set to false in the settings.py file
9. Run "python3 manage.py showmigrations" to check the status of the migrations
10. Run "python3 manage.py migrate" to migrate the database
11. Run "python3 manage.py createsuperuser" to create a super/admin user
12. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories
13. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products
14. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
15. From the CLI login to Heroku using the command heroku login -i
16. Disable collectstatic in Heroku before any code is pushed using the command heroku config:unset DISABLE_COLLECTSTATIC
17. Ensure the following environment variables are set in Heroku
![heroku_config_var](/media/config_var_heroku.png)
18. Push the code to Heroku using the command git push heroku main (Due to a Heroku and GitHub current error, automatic deployments are not possible at this time.)
19. Check the build logs to confirm deployment and build successful

[Back to table of contents](#table-of-contents)
_______
# Credits

## Content

Information from for the website was take from [Wikipedia](https://en.wikipedia.org/wiki/CrossFit) and was written by myself. The website policy was created with a [policy generator](https://app.freeprivacypolicy.com/)

## Media

The merchandise products were edited by myself. The original images can be found here: 
Shirt - https://www.pngbyte.com/en/freepng-zqozx/download
Tank - https://www.redbubble.com/i/tank-top/t-shirt-mockup-free-by-davids350/96256725.B4HC7?country_code=GB&gclid=Cj0KCQjwg_iTBhDrARIsAD3Ib5jnGy3kF5IuoTTfu5_1ikoMZ9_dUrLW7RiJTe3sAxfCDhFVh5xlxfQaAmkgEALw_wcB&gclsrc=aw.ds 
Weight belt - https://www.gymreapers.com/products/gymreapers-7mm-leather-weightlifting-belt
Hoody - https://www.pngfind.com/pngs/b/351-3518660_blank-hoodie-png.png 
Shorts - https://media.endclothing.com/media/f_auto,q_auto:eco/prodmedia/media/catalog/product/0/2/02-09-2021_JD_DM4400-010_m1_1.jpg
Leggings - https://i5.walmartimages.com/asr/a83c3c4b-95de-49f3-b588-dbfeffd9dedd_1.c67be96c5fe1eaf4a03f720e1c052f3c.jpeg 

#### Images: 

Photo by <a href="https://unsplash.com/@bastien_plu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bastien Plu</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

#### README.md File Assistance

I used the following README.md files for assistance in structure and guidance on how to write a README.md file: 
* [README.md 1](https://github.com/KJLuton/RiversideRowingClub/blob/master/README.md)
* [README.md 2](https://github.com/pmeeny/CI-MS4-LOVErugby#strategy)

#### Code:

I wrote the code with the guidance of the Code Institute lessons (Boutique Ado Project).
Base.html boiler template - bootstrap (https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template)
Homepage overlay : (https://codepen.io/zemchuks/pen/VwZjywr?html-preprocessor=pug)
Assist in the contact form: https://learndjango.com/tutorials/django-email-contact-form
Stripe documentation assiatance: https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#set-up-stripe


# Acknowledgements

I would like to thank my mentor Antonija for her guidance, the tutor Ed b_alum and the students on slack for their feedback.

[Back to Table of contents](#table-of-contents)
