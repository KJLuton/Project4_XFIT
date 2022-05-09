# XFIT - Crossfit Gym
## Full Stack Frameworks with Django Milestone Project 4

![homepage mock up](.image)

The [XFIT.com](link) website was built by Kirstyn Luton as part of the Full Stack Frameworks with Django Milestone Project 4, with Code Institute. The website presents an online space for the crossfit company XFIT to allow the company to sell memberships to the crossfit gym, sell merchandise and generally market their brand. 

The website uses Django and allauth to create secure accounts for XFIT members to log in to their personal profiles in order to see historic payments and book classes according to their class credit. 

Disclaimer: This website has been built for entertainment and education purposes. It does not represent an actual company. The website is build with HTML and CSS with imported Bootstrap, Python, Django and Heroku frameworks. The website is responsive for multiple screen types.

## [View live website on Heroku App](link)
---

# Table of Contents

1. [UX](#ux)
    - [Website owner business goals](#website-owner-business-goals)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Wireframes](#wireframes)
        - [Homepage - Wireframe](###homepage-wireframe)
        - [All cocktails - Wireframe](###join-us-page-wireframe)
        - [Log in - Wireframe](###members-page-wireframe)
        - [Register - Wireframe](###contact-us-page-wireframe)
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

The website owner is a crossfit gym called XFIT.

## User goals


## User stories



## Wireframes

### Homepage - Wireframe
![Homepage-Wireframe](imagelink)

### Login/Register Page - Wireframe
![Log-in-Wireframe](imagelink)

### Profile Page - Wireframe
![Log-in-Wireframe](imagelink)

XFIT Members only:
### Profile Page - Wireframe
![Log-in-Wireframe](imagelink)

### Merchandise Page - Wireframe
![Merchandise-Wireframe](imagelink)

### Payment Page - Wireframe
![Payment-Wireframe](imagelink)

### Classes Page - Wireframe
![Classes-Wireframe](imagelink)

## Surface

### Colours

The main colours used in this project are: 

### Fonts

The fonts are installed from [Google Fonts](https://fonts.google.com/):

* h1, h2, h5: 
* h3, h4: 

### Images

[Back to table of contents](#table-of-contents)

_______
# Features and functions

## Existing Features

csrf_token - security 

### Page 

![page mock up](image.url)

#### 


## Future implementations

- Add sales category
- Add links to images 


[Back to table of contents](#table-of-contents)
_______

# Technologies Used

## Languages Used

* #### [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
   Python is an interpreted high-level general-purpose programming language. Python was used to write..... 

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

* #### [Django]()    
* #### [Javascript]()   


[Back to table of contents](#table-of-contents)
_______

# Testing

* Tested the site was linked to django by typing "python3 manage.py runserver" into the terminal once the initial django installation had been made. The django confirmation screen confirmed the installation had work and the site was connected. 
* Tested the initial allauth account set up by setting the LOGIN_REDIRECT_URL to '/sucess'. Even though the final url path hadn't been set up, the error message was for the url, '/success', which confirms that the authentication is working properly. 

* compressed images using tinypng.com to ensure images dont take up to much space and slow the site down. tinypng keeps the image quality qhilst reducing te size. 

* Started with 'checkout' teminology for the 'bag' app. Updated it to bag so a checkout could be created and not confused. 
* Used print statements to confirm bag contents were being added and it was set up correctly ahead of rendering the items into the shopping bag template. 



* The website testing was a continouse process throughout the project build. I continously tested the functions and pages before every commit to ensure they were working properly. 

### Functionality Testing


### User Stories Testing


### Code Validation

* #### W3C Markup Validation Service - Confirmed results 


* #### W3C CSS Validation Service


### Issues Found During Site Development

{% load bag_tools %} wouldn't work. Read django documentation https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/ but everything was set up correctly. Restarted the server and it worked. 


[Back to table of contents](#table-of-contents)
_______
# Deployment


[Back to table of contents](#table-of-contents)
_______
# Credits

## Content


## Media


#### Images: 

Photo by <a href="https://unsplash.com/@ricardohenri?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ricardo Henri</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@johnarano?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">John Arano</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@karsten116?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Karsten Winegeart</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@victorfreitas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Victor Freitas</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@aggergakker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jesper Aggergaard</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@rdehamer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Ryan De Hamer</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@victorfreitas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Victor Freitas</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@bastien_plu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bastien Plu</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@victorfreitas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Victor Freitas</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@alonsoreyes?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Alonso Reyes</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@corey_untitled?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Corey Young</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Photo by <a href="https://unsplash.com/@bastien_plu?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Bastien Plu</a> on <a href="https://unsplash.com/s/photos/crossfit?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

#### README.md File Assistance

I used the following README.md files for assistance in structure and guidance on how to write a README.md file: 

* [README.md 1](https://github.com/KJLuton/RiversideRowingClub/blob/master/README.md)

#### Code:

To write the code I used tutorials from the Code Institute lessons (Backend Development).

Base.html boiler template - bootstrap (https://getbootstrap.com/docs/4.4/getting-started/introduction/#starter-template)
Homepage overlay : (https://codepen.io/zemchuks/pen/VwZjywr?html-preprocessor=pug)


https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#set-up-stripe


# Acknowledgements



[Back to Table of contents](#table-of-contents)
