# [Blacktooth Coffee]()



[View the live project here](https://blacktooth-coffee.herokuapp.com/)



![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\homepage-readme-image.jpg)



The aim of my fourth project for the Code Institute was to create a full stack e-commerce website for a premium coffee delivery service using Python, Django, PostgreSQL, AWS, Stripe Payments API, jQuery,  JavaScript, CSS, Bootstrap and HTML.



The website will incorporate all CRUD (Create, Read, Update Delete) functions and be responsive across all devices from 320px up.



### <u>** NOTE **</u>

* This website is for educational purposes only and is part of a Full Stack Development Course

* No commercial revenue is generated from this project

  

* PLEASE USE THE TEST STRIPE CARD DETAILS TO MAKE PAYMENTS, MORE INFORMATION ABOUT TESTING CAN BE FOUND - [HERE](https://stripe.com/docs/testing):

  * Card Number - 4242 4242 4242 4242
  * End Date - 04/24
  * CVC - 242
  * ZIP - 42424



## Contents:

* [Description](#description)
* [User Stories](#user-stories)
* [Market Research](#market-research)
* [UX and Features](#ux-and-features)
* [Future Improvements](#future-improvements)
* [Changes](#changes)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)
* [Support](#support)



## <a name="description">Description</a>

Blacktooth Coffee is a premium coffee delivery service where users are able to purchase different varieties of coffee from around the world and have them delivered straight to their door.



## <a name="user-stories">User Stories</a>

* "I want to be able to purchase coffee and have it delivered to my home"
* "I want to understand where in the world my coffee is coming from"
* "I want to know details about the coffee such as taste notes and process before I purchase the item"
* "I want to know that my coffee is being sourced responsibly and the farmers are being paid fairly"
* "I want to be able to search for products using different criteria such as region or name"
* "I want to be able to contact the store owner if necessary"



## <a name="market-research">Market Research</a>

I decided to carry out some research into different companies that offered a similar service in order to ensure the website had all the necessary information and features.



All this information was used when designing the layout, colour scheme, typography, images and features that were deployed to the final website and contributed to the above User Stories.



## <a name="ux-and-features">UX and Features</a>

The website was designed as an easy to use e-commerce store where users would be able to find out detailed information about a particular type of coffee and order it directly to their door.



#### 1. Strategy

The aim of the project was to create a full stack e-commerce store for a premium coffee delivery service using Python, Django, PostgreSQL, AWS, Stripe Payments API, jQuery,  JavaScript, CSS, Bootstrap and HTML that could be built upon in the future to include more features.



##### Customer Goals

* Easy to register an account and sign in
* Easy to search for specific products using a few different methods
* Easy to find information about the company
* Easy to find method to contact the store owner
* Easy to understand checkout process
* Easy to see feedback being provided to the user when different actions are being made
* Easy to find reviews on various products being offered



##### Business Goals

- Easy to create new products and add it to the website
- Easy to edit products already on the website
- Easy to delete products already on the website
- Easy to use CRUD function for all reviews on the website
- Easy to use admin interface where all essential information can be found



#### 2. Scope

The scope of the project and features to include were influenced by the market research carried out. It should be a mobile-first website that is responsive on all devices from 320px upwards.



##### Current Features

* ###### Home Page

  * Large font used to make finding and distinguishing different pages and sections easy

  * Responsive navigation bar that condenses down to an icon on smaller devices

  * Large hero image of coffee to draw the user in

  * h1 tag that is clickable across all pages to allow the user to easily navigate back to the home page

  * Easy to read description of what the website and business does

  * Link at the top of the page that goes directly to the products

  * Footer with links to other website pages for easy navigation and also social links that open in a new tab

    

* ###### Products Page

  * Search bar appears at the top of the screen where users are able to search for products using different methods including name, origin, region, taste notes, process and variety
  * Clear essential information displayed for each product including name, price and category it belongs to
  * Edit and delete buttons appear for super users to make changes if necessary
  * Sort by section at the top of the page so users are able to filter the products how they want
  * Selected filters and product numbers at the top to easily show users what is selected

  

* ###### Product Details Page

  * Large picture of product to draw the user in

  * Key information about the product is displayed to the customer so they are able to see what they are buying

  * Edit and delete buttons appear for super users to make changes if necessary

  * Large section for creating an order to make it clear to the customer how to proceed

  * Large add to bag and keep shopping buttons to direct users

  * Feedback/toast message in the top right of the page to provide feedback to users on what they actions they are taking across the entire website

  * Review form where logged in users can leave a review on the specific product

  * Review section where everyone can read reviews of the specific product

  * Edit and delete buttons appear for super users to make changes if necessary

  * Edit button appears for users so they can edit their own review only

    

* ###### Shopping Bag Page

  * Small image of the product in the bag to show the user what they have purchased

  * Essential information is displayed to users including the name of the product, SKU, price, quantity and subtotal

  * Delivery costs/information is displayed to clearly show the user what they are paying/need to add to bag in order to get free delivery

    

* ###### Checkout Page

  * Easy to see order summary displaying the product image, quantity and subtotal

  * Summarised delivery information showing total, delivery and grand total to the user

  * Easy to fill out payment form so the user is able to complete their order

  * Checkbox so user is able to save their payment information to their account

    

* ###### Checkout Success Page

  * Confirmation to the user that their order is complete and what email address the confirmation will be sent to

  * Toast message to again show the user their order is completed

  * Summary of complete order shows to customer including order information, order details, delivery information, billing information and grand total

  * Back to home page button so the user is able to return to the home page after completing an order

    

* ###### About Page

  * Large hero image at the top of the page to engage the user
  * Clear and easy to read paragraphs explain the history of the business and what their goals are
  * Link to products page so the user is able to easily find products after reading more about the business



- ###### Contact Page

  - Easy to see contact details with appropriate tags to open a new email/start a call if someone needs to contact the store owner



- ###### Brewtorials Page

  - Own section in the menu so users are able to easily find the section
  - Clear h3 title tags with bold font weight so the user can easily see the title of the post
  - Date and time of when the posts were created are visible to users
  - Create New Post button appears at the top for super users so they are able to create new articles quickly
  - Read more link so users are able to view the specific post in more detail



- ###### Brewtorials Details Page

  - Clear h3 title tags with bold font weight so the user can easily see the title of the post
  - Date and time of when the posts were created are visible to users
  - Clear numbered instructions for users to follow a step by step process easily
  - Edit and Delete buttons appear for super users so they can easily edit/delete posts



#### 3. Structure

The site was designed to have essential pages which are Home, Products, Brewtorials, About Us, Contact Us, Account and various Sign In/Register pages. 



The same navigation bar and footer was used across all pages for consistency and better UX.



Short and easy to read paragraphs were used to easily get essential information across to users.



A selection of quality images were used to be engaging and draw users in and show what they could potentially purchase. These images were paired with descriptions about the product to provide information to the customer.



###### Data Schema

[dbdiagram](https://dbdiagram.io/home) was used to help design the relational database. The original design is below:



![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\original-db-schema.jpg)



#### 4. Skeleton

* Wireframes was created using [Balsamiq](https://balsamiq.com/)

  

###### Home Page

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-home-page.jpg)



###### Home Page - Scrolled

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-home-page-scrolled.jpg)



###### Home Page - Bottom

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-home-page-bottom.jpg)



###### Products Page

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-products-page.jpg)



###### Profile Page

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-profile-page.jpg)



###### About Us Page

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-about-us-page.jpg)



###### Contact Us Page

![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\wireframes\wireframe-contact-us-page.jpg)



#### 5. Surface

##### Design

* ###### Colour Scheme

  * The main colours used throughout the website were Black Olive (#3A413A), Yellow (#FFD966), Grey (#EEE) White (#FFF) and Black (#000). These were chosen as they felt professional and had good contrast to each other

    

* ###### Typography

  * Roboto was used as the main text across the entire website as it was clear to read and felt smooth
  * Sans Serif was the back up font should the primary one not load



* ###### Imagery

  * All  hero images were sourced from [Unsplash](https://unsplash.com/)




## <a name="future-improvements">Future Improvements</a>

* Ability to sort products by rating
* More types of coffee and products available to customers
* Subscription service so customers are able to set up a recurring order rather than having to make a purchase every week
* More searching and filter options
* Pagination for products pages when more are added
* A proper contact form to contact the site owner



## <a name="changes">Changes</a>

* The original idea was to create a subscription service, however this was later changed to just buying items at once to begin with - subscription service is something that will be added at a later date
* There was a point where the secret keys were available to the public due to an error, however these were all changed to secure the application
* A contact form was originally going to be used to contact the store owner, however this was changed and various tags were implemented to immediately open a new email/start a call
* There were some additional models that needed to be added from the original Wireframes design due to project requirements, this meant adding in a Reviews app and Brewtorials/Blog app
* There were a number of changes to the original DB schema due to evolving circumstance of the project and the need for additional applications within the project



## <a name="technologies-used">Technologies Used</a>

##### Languages Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  The following Python modules were used within this project:

  * asgiref==3.3.4

  * boto3==1.17.88

  * botocore==1.20.88

  * dj-database-url==0.5.0

  * Django==3.2

  * django-allauth==0.44.0

  * django-countries==7.1

  * django-crispy-forms==1.11.2

  * django-storages==1.11.1

  * gunicorn==20.1.0

  * jmespath==0.10.0

  * oauthlib==3.1.0

  * Pillow==8.2.0

  * psycopg2-binary==2.8.6

  * PyJWT==2.0.1

  * python3-openid==3.2.0

  * pytz==2021.1

  * requests-oauthlib==1.3.0

  * s3transfer==0.4.2

  * sqlparse==0.4.1

  * stripe==2.56.0

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

* [CSS3](https://en.wikipedia.org/wiki/CSS)

  

##### Frameworks, Libraries, Programs and Websites Used

* [Bootstrap](https://getbootstrap.com/)

* [Hover.css](https://ianlunn.github.io/Hover/)

* [Google Fonts](https://fonts.google.com/)

* [Django](https://en.wikipedia.org/wiki/Django_(web_framework))

* [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL)

* [Amazon Web Services](https://en.wikipedia.org/wiki/Amazon_Web_Services)

* [Heroku](https://en.wikipedia.org/wiki/Heroku)

* [Git](https://git-scm.com/)

* [GitHub](https://github.com/)

* [Balsamiq](https://balsamiq.com/)

* [Microsoft Paint](https://en.wikipedia.org/wiki/Microsoft_Paint)

* [Typora](https://typora.io/)

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

* [TinyPNG](https://tinypng.com/)

* [Autoprefixer CSS](https://autoprefixer.github.io/)

* [Favicon.cc](https://www.favicon.cc/)

* [dbdiagram](https://dbdiagram.io/home)

  

## <a name="testing">Testing</a>

##### User Story Testing

* "I want to be able to purchase coffee and have it delivered to my home"

  * A user is able to browse various products and make an order

  

* "I want to understand where in the world my coffee is coming from"

  * Clear descriptions on each product detail page explain where the coffee is coming from
  * Information and guarantees are provided on various pages to state the coffee is sustainably sourced and fair for the farmers

  

* "I want to know details about the coffee such as taste notes and process before I purchase the item"

  * Clear descriptions on each product detail page explain taste notes and process



* "I want to know that my coffee is being sourced responsibly and the farmers are being paid fairly"

  * Information and guarantees are provided on various pages to state the coffee is sustainably sourced and fair for the farmers

  

* "I want to be able to search for products using different criteria such as region or name"

  * Search bar appears at the top of the products page with the ability to search using different methods including name, origin, region, taste notes etc.

  

* "I want to be able to contact the store owner if necessary"

  * Contact us page provided for customers to contact the site owner



##### General Testing





##### Validation

The W3C Markup Validator, W3C CSS Validator, JSHint and PEP8 Online services were used to validate every page of the project to ensure there were no syntax errors in the project.



[W3C Markup Validator](https://validator.w3.org/) 



[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)



[JSHint](https://jshint.com/)



[PEP8 Online](http://pep8online.com/)





##### Devices

The website was initially tested on different types of devices using Chrome DevTools to see if there were any immediate issues. 



The website works well on all mobile devices from 320px and upwards.



[Google's Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) was used and the results were that the 'Page is mobile friendly - this page is easy to use on a mobile device'.



![](C:\Users\Scott\Documents\Coding\CI-MS4\readme_docs\google-mobile-friendly-test.jpg)



The website was then sent via email to a number of family and friends of all ages to test on different devices to see how easy it was to use and how responsive it was.



The following devices were used:

* iPhone X - Chrome Browser
* iPad Air - Safari Browser
* iPad Mini - Safari Browser
* Samsung Galaxy S9 - Samsung Internet Browser
* iMac - OS X Yosemite - Safari Browser
* iPhone 11 Pro Max - Safari Browser
* Sony Vaio Laptop - Windows 8 - Chrome Browser
* Apple Macbook Pro 16 - Chrome Browser



##### Errors/Bugs During Device Testing

* iPhone X - Chrome Browser
  * 



* iPad Mini / iPad Air - Safari Browser
  * 



* Samsung Galaxy S9 - Samsung Internet Browser
  * 



* iMac - OS X Yosemite - Safari Browser
  * 



* iPhone 11 Pro Max - Safari Browser
  * 



* Sony Vaio Laptop - Windows 8 - Chrome Browser
  * 



* Apple MacBook Pro 16 - Chrome Browser



##### Errors During Testing

[W3C Markup Validator](https://validator.w3.org/) 

* 



[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

* 



##### Known Bugs

* 



## <a name="deployment">Deployment</a>

The master branch of this repository is the most current version and has been used for the deployed version of the site.



The Code Institute student template was used to create this project.



[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.

- Give your repository a name, and description if you wish.

- Click the *Create Repository from Template* to create your repository.

- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.

- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one. Use the following commands to commit your work,

- `git add . `- adds all modified files to a staging area.

- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.

- `git push` - pushes all your commited changes to your Github repository.

  

**Requirements**

- [Python 3](https://www.python.org/downloads/)

- [Pip](https://pypi.org/project/pip/)

- [Git](https://git-scm.com/)

- [AWS S3](https://aws.amazon.com/)

  

**Creating a Clone**

1. From the repository, click *Code*
2. In the *Clone >> HTTPS* section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2 - `git clone https://github.com/scottsimpson91/CI-MS4-Blacktooth-Coffee`
6. Set the following values in a `env.py` file.

```
import os

os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_WH_SECRET', '<key generated by Stripe>')
```

- Stripe keys are generated by Stripe, each individual have their own unique key values.
- *PLEASE MAKE SURE NEVER TO PUBLISH THESE KEYS, ADD THE `env.py` TO A `.gitignore` TO AVOID PUSHING KEYS TO GITHUB.*

1. Install the project requirements - `pip3 install requirements.txt`

2. Apply database migrations - `python manage.py migrate`

3. Create a superuser - `python manage.py createsuperuser`

4. The project can be run with the following - `python manage.py runserver`

   

**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.

```
pip3 install dj_database_url
pip3 install psycopg2
```

1. Login to the Heroku CLI - `heroku login -i`
2. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
3. Create a superuser - `python manage.py createsuperuser`
4. Install `gunicorn` - `pip3 install gunicorn`
5. Create a requirements.txt file - `pip3 freeze > requirements.txt`
6. Create a `Procfile` (note the capital P), and add the following,

```
web: gunicorn moose_juice.wsgi:application
```

1. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
2. Add the hostname to project settings.py file

```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']
```

1. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
2. In Heroku, within settings, under config vars select `Reveal config vars`
3. Add the following,

```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```

1. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
2. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app

```
git add .
git commit -m "Initial commit"
git push
```

1. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

   

**AWS S3 Bucket setup**

1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
   - Allow public access
3. Under Properties > Static website hosting
   - Enable
   - index.html as index.html
   - save
4. Under Permissions > CORS use the following:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

1. Under Permissions > Bucket Policy:

   - Generate Bucket Policy and take note of Bucket ARN
   - Chose S3 Bucket Policy as Type of Policy
   - For Principal, enter *
   - Enter ARN noted above
   - Add Statement
   - Generate Policy
   - Copy Policy JSON Document
   - Paste policy into Edit Bucket policy on the previous tab
   - Save changes

2. Under Access Control List (ACL):

   - For Everyone (public access), tick List

   - Accept that everyone in the world may access the Bucket

   - Save changes

     

**AWS IAM (Identity and Access Management) setup**

1. From the IAM dashboard within AWS, select User Groups:

   - Create a new group
   - Click through and Create Group

2. Select Policies:

   - Create policy
   - Under JSON tab, click Import managed policy
   - Choose AmazongS3FullAccess
   - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
   - Click next step and go to Review policy
   - Give the policy a name and description of your choice
   - Create policy

3. Go back to User Groups and choose the group created earlier

   - Under Permissions > Add permissions, choose Attach Policies and select the one just created
   - Add permissions

4. Under Users:

   - Choose a user name
   - Select Programmatic access as the Access type
   - Click Next
   - Add the user to the Group just created
   - Click Next and Create User

5. Download the

   ```
   .csv
   ```

   containing the access key and secret access key.

   - **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.**

     

**Connecting Heroku to AWS S3**

1. Install boto3 and django-storages

```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```

1. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:

2. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app

3. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.

   - **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**

     

## <a name="credits">Credits</a>

##### Media

* Favicon was generated from [Favicon.cc](https://www.favicon.cc/)
* [TinyPNG](https://tinypng.com/) was used to reduce the overall total image size
* Home hero image was sourced from [Unsplash](https://unsplash.com/photos/Am2kjOEKADs)
* Secondary Home hero image was sourced from [Unsplash](https://unsplash.com/photos/QLkjP_W4d7c)
* About Us image was sourced from [Unsplash](https://unsplash.com/photos/UvWlksgZGPE)
* Product images were sourced from:
  * [Unsplash](https://unsplash.com/photos/lcfH0p6emhw)
  * [Unsplash](https://unsplash.com/photos/QSUbfuscL3s)
  * [Unsplash](https://unsplash.com/photos/fmc-tFMMiBs)
  * [Unsplash](https://unsplash.com/photos/TD4DBagg2wE)



##### Code Snippets


* ###### [Stack Overflow](https://stackoverflow.com/)

  * Guidance on how to get line breaks to appear in the Blog application - [Here](https://stackoverflow.com/questions/59048154/i-can-not-use-django-template-tag-linebreak-and-justify)
  * Guidance on issues surrounding migrations - [Here](https://stackoverflow.com/questions/42613536/django-programming-error-column-does-not-exist-even-after-running-migrations)

* ###### [Code Institute](https://codeinstitute.net/)

    * The main elements of the project were taken from the Boutique Ado Walkthrough and adapted to suit the requirements of this project

* ###### [YouTube](https://www.youtube.com/)

    * Guidance on how to build a blog application in Django - [Here](https://www.youtube.com/watch?v=m3hhLE1KR5Q)

* ###### [Django](https://docs.djangoproject.com/en/3.2/)

  * Guidance on how to use template tags and filters - [Here](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)

* ###### Other

  * Guidance on how to remove the last tag in a loop - [Here](https://processwire.com/talk/topic/4456-help-how-to-remove-the-last-tag-in-a-loop/)



**Content**

* Information on the coffees and home/about us page were sourced from [Ozone Coffee](https://ozonecoffee.co.uk/)
* All other text content was written by the developer



## <a name="acknowledgements">Acknowledgements</a>

I would like to thank the following:

* My mentor, **Spencer Barriball**, for his guidance, wisdom and encouragement throughout the project

* **CI Staff** and **Slack Community** for their assistance with minor coding issues

* **Benjamin Kavanagh** for his help working through various minor coding issues

* **Harry Dhillon** for his help working through various minor coding issues and for helping me with the deployment section of this README

  

## <a name="support">Support</a>

Thanks for taking the time to view my README. I hope you enjoyed your visit to my page.