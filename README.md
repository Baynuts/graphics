# README - Graphicz Design Database Driven Website - Final Milestone

## Table of Contents

- [Description](#Description)
- [UX](#UX)
- [Wireframe](#Wireframe)
- [Screenshots](#Screenshots)
- [Features](#Features)
- [Technologies](#Technologies)
- [Tools](#Tools)
- [Deployment](#Deployment)
- [Testing](#Testing)
- [Credits](#Credits)

## Description

Creation of an ecommerce website which can sell and market products and services for a graphic designer. Contains database which holds user profiles, orders, products and portfolio examples.

## UX

It has been designed to be current, easy to follow and responsive for a full range of device sizes from mobile up to large desktop screens. 

- Very user friendly design with current best practice layout..
- The product list view uses a grid layout which all lines up to create a pleasing page which is easily viewable.
- All forms have been created to be easily filled in and intuitively laid out and described.
- Product detail page has well positioned elements and uses a contrasting colour for the call to action.
- Tabs have been used on the product detail page to add commonly needed information before a sale.
- Home page contains large colorful design and clear images. Product list has been replicated on base of home page to sell straight through from home.
- Search function allows users to quickly and easily find product. Contained in header it is available on every page.
- All forms have the same styling and submit button to ease transition.
- Customer retention with user profiles.
- Stripe payments contained in the site so forwarding to payment screen avoided. Keeping user on site.

#### As a site owner I want to be able to:
- Add products
- Sell products
- Take payments
- Receive customisation data for personalised products
- Showcase previous work

#### As a site user I want to be able to:
- Register
- Login
- Logout
- Save / update profile
- Buy products
- Be able to amend my cart by adding removing items.
 
## Wireframe
Wireframe (https://raw.githubusercontent.com/Baynuts/graphics/master/media/wireframe.jpg)

## Screenshots

#### Home Page
Home Page Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/home.jpg)
#### Product List page
Product List Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/product-list.jpg)
#### Product Detail page
Product Detail Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/product-detail.jpg)
#### Profile Page
Profile Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/profile.jpg)
#### Shopping Cart Page
Shopping Cart Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/cart.jpg)
#### Checkout Page
Checkout Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/checkout.jpg)

## Features

#### Low load time
All background images have been compressed to speed up site
#### Responsive design
Bootstrap4 has been incorporated in to the design as the framework. This is widely used and adds a common framework to ease construction. This has also been added to using individualy created styles.
#### User Authentication
Profiles are required to ease shopping experience. These are held in a database and users can access the site easily using these retained credentials.
#### Shopping Cart
Simple cart system which holds list of added items and calculates totals.
#### Stripe Payments
Integrated with Stripe payments. Ability to check if a payment has been received back to the server once paid. Failover system in place to clarify that paid orders are marked as such and cannot get missed and customer disgruntled.
#### Sorting
Product list pages are able to be sorted by various criteria.
#### Product Image Zoom
Product list pages have images that zoom when the mouse is hovered over. This is a slow and smooth ation and adds to the user experience.
#### AWS S3 
Images for products are stored in a designated bucket. This and the user profiles allows admin / staff users to add products and images without access to the backend admin.
#### Product Management
Super users are able to create, delete and amend products from the site using the product management section.
#### Portfolio Management
Portfolio images kept in separete storage, ensuring sections can be kept separate.
#### Product Tabs
Product detail pages have description, dimensions and shipping information separated using tabs.
#### Quantity Box
Easy to use quantity box with plus and minus to aid visual queues increase site turnover.

### Features to add in future
#### Recommended Products
Product detail page could include related or recommended items. This could be easily constructed using other items in the same category.
#### Contact Us Form
This would have been a great addition and very useful on the generic customised products such as leaflets / business cards. This would allow the upload of business details such as logos and styles and also help confirm neccessary details before payment is made.
#### File upload from customer
Unfortunately I ran out of time with this project but would have liked to add the functionality so that customers could upload their own image files. I believe that this would be a huge positive on the site as certain products on offer would alos be able to be designed by the customer and then the printing could be sold.
#### Add app for onscreen editting of products
This would be a large amount of work but would aid in the sale of goods by abling customers to create their own artwork.

## Technologies

#### HTML5
The basic layout of the page has been created using HTML5, any duplication has been reformatted and the code has been written sparingly.
#### CSS
The HTML has been styled using many separate stylesheets. This unfortunately can slow the site down but does aid it self for reuse as the separate apps can be used in other projects.
#### JavaScript 
Javascript has been used to solve any issues between database and front end. 
#### Bootrstrap4
Bootstrap4 is currently the newest version and has a vast number of features. It has aided in the responsiveness of the site and also the general layout / framework.
#### Django
Used to create the main structure of the backend
#### Django-AllAuth
Django package for user authentication.
#### Django-Crispy Forms
Using Bootstrap4 templates this helps to create user friendly forms that are functional and secure.
#### Gunicorn
Python Web Server Gateway Interface HTTP server
#### Python3
The language that Django requires for use.
#### Stripe
Payment processing technology to allow the acceptance of payments on the site. This has been set up but kept in test mode so that nobody is able to purchase products from the store.
#### AWS
IAM has been used for busket security and S3 has been used for image storage.
#### GitHub
Code base repository for implemental changes and storage
#### Heroku
The web app has been deployed to Heroku as the host, all secret keys and passwords have been hidden using the config settings available.

## Tools
* Gitpod
* Google Chrome Developer Tools
* Git
* Github
* Boostrap
* W3C Validator
* Adobe Fireworks
* Django
* Django Allauth
* Django Countries
* Django Crispy Forms
* Django Storage
* Pillow
* Amazon Webservices


## Deployment
The project has been deployed via Gitpod to the Heroku platform.

Create account and log in to Heroku  
Press 'new' button > Create New App  
Choose app name : graphicz-drb  
Choose the region closest to your physical location  
Submit to create app.  

Open console in Gitpod to connect to the new heroku app.  
Ensure that requirements.txt and Profile are up to date.  
Type in terminal:  heroku login -i   
Type in terminal:  heroku add remote heroku  
Enter app details  
Type in terminal:  git add .  
Type in terminal:  git commit -m "Commit message"  
Type in terminal:  git push heroku master  

The IDE is then connected to Heroku but you must run migrations for the models to be created and available.  
Type in terminal: heroku run python manage.py makemigrations  
Type in terminal: heroku run python manage.py migrate  

Open the Heroku site and attach the app to the Github repository  
This can be found under 'Deploy' > Connect to GitHub  
Following this each time the project is committed to Github the Heroku app will also get updated.  

Final stage is to create the environment variables directly in Heroku  
This can be found under 'Settings' > Config Vars  
All of your private keys can be entered in to here for the database (Postgres), AWS settings, Stripe keys and any other details that we will want to keep hidden from public view.  

Configuration variable created  
AWS_ACCESS_KEY_ID access to Amazons web services bucket  
AWS_SECRET_ACCESS_KEY access to Amazons web services bucket  
DATABASE_URL holds database access information  
EMAIL_HOST_PASS used for sending emails  
EMAIL_HOST_USER used for sending emails  
SECRET_KEY Djangos secret key   
STRIPE_PUBLIC_KEY used for stripe payments  
STRIPE_SECRET_KEY used for stripe payments  
STRIPE_WH_SECRET used for stripe payments  
USE_AWS boolean value to designate whether AWS is used or not  

In the settings.py update the required information to use the environment variables.  

Once details are correctly entered re commit the site, wait for Heroku to build the app and then open via Heroku dashboard > Open App.  

The code can be viewed using Heroku: https://graphicz-drb.herokuapp.com/  

## Testing

#### Testing has completed using: 
* W3C validator for both HTML and CSS
* Google Chrome Developer
All errors have been resolved and now the code validates without any errors.

#### Responsiveness
The sites responsiveness has been tested using Chrome developer tools and mimiced using each device available within the software and also reducing the screen size. Additional media queries have been added to solve various sizing issues with text and images between the standard md and lg sizes to compensate for irregular sized devices.  
Manual test have been performed on various desktop and laptop screens as well as iPhone SE, iPhone 11, iPhone 6, iPhone 8, iPhone 5, Samsung Galaxy Tab, Samsung Galaxy Ace, iPad mini.  
With the standard sizes of the font throughout the site and my want to have elements spaced but without too much white space the sizes have been adjusted at various screen sizes to guarantee that the site looks correct at every screen size.  

#### Browsers
I have tested the site using the following browsers

* Google Chrome
* Apple Safari
* Opera
* Internet Explorer
* Mozilla Firefox

Internet explorer has shown some errors which are not shown in all other browsers. I am unable to ascertain the issue after further research and it appears to be a caching issue even after the cache is cleared.

#### Cart testing
Each individul product has been added to the cart and various options have been amended and removed. I did encounter a problem with my customtext field not showing in various places of the cart and not transfering through to the checkout but this has now been resolved.

#### Checkout testing
The checkout has been manually tested using various lengths in the fields the validation has worked correctly. Stripe payments has encountered various errors and has been my steepest learning curve. Through trial and error and reading the documentation provided by Stripe the finctionality is now correct. I have tested the integration in a live setting with my own card and it worked correctly. I have now put the Stripe setting back to the test API so that it can show you the functionality but is unable to take live payments.

#### Email testing
Various orders have been placed on the site and profile created. The functionality of the emails has worked correctly throughout but some amendments were made to the design of the email templates to further increase customer experience.

#### Profile testing
Profiles have been tested but largely reflect the models showed in the Code Institute example. The models provided all of the functionality that was needed and nothing was encountered that needed to be changed. These have been tested in production using various email addresses, usernames and passwords to see if any special instructions were needed for customers but it functioned perfectly everytime.

#### Product management testing
All areas of the product management have been manually tested. The addition of products is correct, editting various fields on the form push correctly to the database and I have used the console and network functions in Chrome developer tools to diagnose the exact route of the function.

#### Final Testing
Friends, family and collegues have been used to test the functionality of the site but also to give a design specific. Two genuine graphic designers have been questioned as to how the site is represented and the portfolio app was created following their input.

#### Stripe payments testing
The stripe integration has been manually tested many times to ensure that the setup and webhooks are functioning as intended.

- Checkout Page Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/stripe-checkout.jpg)
- Loading Overlay Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/stripe-loading.jpg)
- Payment Complete Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/stripe-complete.jpg)
- Stripe Screenshot (https://raw.githubusercontent.com/Baynuts/graphics/master/media/stripe-screenshot.jpg)

## Credits

*	Images from Envato Elements have been used throughout the site.

------------------------------------------------------------