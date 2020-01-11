[![Build Status](https://travis-ci.org/pranitastudent/Milestone_5_project.svg?branch=master)](https://travis-ci.org/pranitastudent/Milestone_5_project)

[Deployed Website](https://pranita-tshirt-shop.herokuapp.com/)

# Full Stack Frameworks with Django Milestone Project- Ecommerce store - Milestone 5 Project 

## Project Entrails

<p> An e-commerce site will be built which will sell t-shirts for men, women and children. The user should be able to search for a particular T-shirt for example 'Red T-shirt. In order to buy the t-shirts the user will have to register with a username and password and login. The registration and username will be a secure application using the authentication process. The user will navigate through the site using a navbar  through : Home, Cart, Feedback. Cart, Login and Register.  The user once logged in can pay for the item using the strip authentication system. Logged in users are able to leave feedback for the site in terms of 'likes' and a feedback review on the item purchased.
Logged in users can only edit and deleted there own feedback. Users will not be able to delete items from the website or delete reviews from other users.  All users will be able to view feedback reviews.SQLite3 will be used for as a testing databases once tables are created and PostgreSQL will be used as a production database. Git and GitHub will be used for version control. The final site will be deployed and hosted on Heroku. <strong> Please note that this website is only for educational purposes to fulfil the criteria for Milestone 5 Full Stack Frameworks Django Project.</strong></p>

## UX Design - User Experience
<br>

<p> The user regardless of being logged in should be able to view all t-shirts , each with a price indicated and quantity to add to cart. The user should be able to register and login in securely using the authentication process. The user will have a limit of maximum 999 products to add to the cart. The user is able to view the item in the cart but must be registered and logged
in to pay for the item using the stripe payment system. The logged in user is able to leave reviews about a particular product, edit there review and delete there own review. Non-registered users are unable to leave a review for a product but view reviews. All users can also 'like' a review by clicking on the 'thumbs-up' icon if they like the review. 
The user must be able to filter the t-shirts according to the key words e.g 'Red T-shirt'. Users obtain at £20 discount if there orders are over £80. Pagination is added to the site and a total of six products can be viewed at any one time.

The web application should fulfil the CRUD operations as below:

### Create

The logged un user should be able to add feedback once logged in. Fill in the feedback review, select the product name and give a rating from 1 to 5 stars. 

### Read

All users can read the feedback reviews.

### Update

Logged in users can update there own feedback only using the edit button. Non-logged in users can't edit feedback.

### Delete

Logged in users can delete there own feedback only using the delete button. Non-logged in users can't edit feedback.

</p>

## User Stories
<br>
<ul>
<li> As a user to the site I should view a responsive site on ; desktop, mobile, tablet and large screens.</li> 
<li> As a user to the site I should be able to view all t-shirts available</li>
<li> As a user I should be able to register on the ecommerce site in order to purchase my product through strip authentication.</li>
<li> A a consumer I should be able to buy t-shirts for myself and others through searching the options </li>
<li> As a logged in user I should be able to leave a review for the product I purchased. </li>
<li> As a logged in user I should be able to purchase the product I wish up to a maximum quantity of 999.</li>
<li> As a user I should be able to register, login and reset my password on the website </li>
<li> The user can contact the shop using the contact form, validate through reCAPTCHA and submit</li>
</ul>

## Wireframes

<p>The wireframes for the Full Stack Frameworks with Django Milestone Project- Ecommerce store - Milestone 5 Project project were created using Balsamiq. Mocks-ups were produced for desktop and mobile versions.</p>

[Wire Frames](wireframes/ecommerce.pdf)

## Database Schema
<p> A database schema is provided so that I could visualise the tables. The relationship between tables is shown in the schema<p>

[Database_Schema](schema/databaseschema.pdf)

## Features

### Existing Features

### Non-logged in user
<p> A non-logged in user is able to access the following links on the Navbar:</p>

<ul>
<li> Home Page - Able to press 'Shop Now' button to see products. Able to view top t-shirts and google map indicating destination and address of shop </li>
<li> Contact Page- Able to send an email to the shop  and validate message through reCAPTCHA </li>
<li> Products Page - Able to view Products and add to cart </li>
<li> Cart Page - Able to view items in cart and adjust quantity but NOT checkout unless a registered and logged in user</li>
<li> Feedback Page - Able to view feedback from all users and like 'Upvote' feedback</li>
<li> Register Page - Able to Register as a user</li>
<li> Login Page - Able to login as a user once register. Ability to reset password through an email link which is sent to the registered email address. </li>
<li> Messages - Able to view success and error messages which are displayed below navigation and dismiss them by clicking on the cross icon.</li>
</ul>

### Logged- in user
</p> A logged in user is able to access the following links on the Navbar:</p>

<ul>
<li> Home Page - Able to press 'Shop Now' button to see products. Able to view top t-shirts and google map indicating destination and address of shop </li>
<li> Contact Page- Able to send an email to the shop  and validate message through reCAPTCHA </li>
<li> Products Page - Able to view Products and add to cart </li>
<li> Cart Page - Able to view items in cart  and adjust quantity </li>
<li> Checkout Page - Able to fill in  checkout form details, discount displayed if applicable and submit as necessary </li>
<li> Login Page - Able to login as a user once register. Ability to reset password through an email link which is sent to the registered email address. </li>
<li> Logout Page - Once logged in the login link on the navbar is not-visible.  Ability out logout through logout link on navbar when required </li>
<li> Feedback Page - Able to view feedback from all users and like 'Upvote' feedback</li>
<li> Add Feedback Page - Able to add feedback, edit and delete own feedback through edit and delete buttons.</li>
<li> Messages - Able to view success and error messages which are displayed below navigation and dismiss them by clicking on the cross icon.</li>
</ul>

#### Products
<p> All users can click on the products and view them in a separate window displaying a larger image of the product and dismiss on the page through the cross icon </p> 

#### Logo and Breadcrumb
<p> All users can return to the homepage by clicking on the t-shirt icon and through clicking on the home link on the breadcrumb which is displayed on each page</p>

#### Pagination
<p> A maximum of 6 products are displayed on the products page and 6 feedback responses on the feedback page using pagination. Users can move between pages 1 and 2 using the pagination tab at the bottom.</p>

#### Checkout

<p> Checkout is completed using the checkout page. Whereby users fill in personal details and use the credit card number : 4242 4242 4242 4242, CVV (three digit), expiry month and year (don't enter any real credit card information) to checkout - makes use of the STRIPE API. Success message displayed once payment is successful.</p>

### Features left to implement

Several more features could have been incorporated into the project:
<ul>
<li> A filter function could have been included whereby the user is able to filter through category and filter through a price range </li>
<li> The like button could have been restricted to users who can only like the same post once and not again </li>
<li> Users can choose different sizes and colours of t-shirts and this choice is copied through to checkout </li>
<li> Perhaps a coupon discount section could have been included as well whereby the users enters a coupon code and is able to acquire a discount </li>
</ul>

## Technologies Used

<p> The Full Stack Frameworks module requires a project to be built using: HTML, CSS, Bootstrap 4.4, JavaScript, stripe payment system, Python and Django. The project will use the Postgres relational database and will use additional libraries. The project brief indicates to build an e-commerce site. CI tested through travis integration</p>

### IDE

<ul>
<li><a href="https://code.visualstudio.com/">Visual Studio Code</a></li>Visual Studio Code was used as the chosen IDE and all code was written in Visual Studio Code.
</ul>

### Front-end Technologies and Frameworks

<ul>

<li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5"> HTML5 </a></li> HTML 5 was used to create the structure of webpage with the necessary elements.
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html"> CSS3 </a></li> CSS3 was used to write custom CSS styles the webpage with the necessary attributes.
<li><a href="https://getbootstrap.com/"> Bootstrap v 4.4 </a> </li>  The Bootstrap framework is used to style the webpage alongside custom CSS and the grid system is adhered to.
<li><a href ="https://www.javascript.com/">JavaScript</a></li> JavaScript was used to write the function for the google map and  stripe JS.
<li><a href = "https://jquery.com/">JQuery</a></li>JQuery is used to create the back-to-the top button function and date function enabling the website to contain appropriate year date. 
<li><a href="https://stripe.com/gb">Stripe</a></li> STRIPE API is used as a payment method and the STRIPE dashboard can be used by the developer to see payments displayed. 
<li><a href ="https://aws.amazon.com/">AWS S3, IAM services</a></li> Images are stored in s3 buckets on AWS, Boto3 is used as dependency and AWS passwords are stored in env.py.
<li><a href="https://fontawesome.com/">Font Awesome</a></li> Font Awesome is used to add icons to text to make it visually appealing.

</ul>

### Version Control

<ul>

<li><a href = "https://git-scm.com/">Git</a></li>Git is used as a version control system to add, commit and push files to the local repository.

</ul>

### Back-End Technologies and Frameworks

<ul>

<li><a href = "https://www.python.org/">Python</a></li> Python is used as the back-end coding language to write functions and enable 'GET' and 'POST' requests.
<li><a href = "https://www.djangoproject.com/"> Django 2.2.8</a></li>Django is the backend framework used to create URL's, models and views.
<li><a href = "https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a></li>Jinja is a templating language which works alongside python and Django to create templates.

</ul>

### Databases

<ul>

<li><a href ="https://www.sqlite.org/index.html">SQLite3</a></li>SQLite3 is used a testing database whereby tables and fields are added to test out data created.

<li><a href = "https://www.postgresql.org/">PostgreSQL</a></li>PostgreSQL is used as the production database whereby tables and fields are added in the working apps.

</ul>

### Deployment

<ul>

<li><a href = "https://www.heroku.com/">Heroku</a></li> Heroku is used to host and deploy the working app using the PostgreSQL database.

</ul>

### Testing Code

<ul>

<li><a href = "https://validator.w3.org/">WC3 Markup Validation Service</a></li> WC3 was used to validate HTML Code.
<li><a href = "https://jigsaw.w3.org/css-validator/">WC3 CSS Validation Service</a></li> WC3 CSS was used to validate CSS Code.
<li><a href ="https://pypi.org/project/autopep8/">autopep8</a></li> autopep8 was used confirm python code to the PEP8 standard. 
<li><a href = "https://jshint.com/">JS Hint</a></li>JS Hint was used to validate JavaScript and JQuery

</ul>

## Testing and Validating

### Validating Code

<p> The HTML and CSS codes were validated using the CSS validators with a few syntax errors notably extra or missing divs in the checkout.html and products.html pages. The JavaScript and JQuery codes were validated using JS Hint and no errors were found.</p>

</p> Python code was formatted using autopep8 and installed using the bash command:

`$ pip install autopep8`

Code was tested using the command below for specific file:

`$ autopep8 --in-place --aggressive --aggressive <filename>`
 

### Testing URLS, Views and Models.

Django Unit Testing was used to test URLS and Views. The URLS and views were tested to check if an response of 200 or 302 for redirect as required to see if they pass the tests. The models are tested to check they return the the correct fields inputs.

Interesting testing was completed on the testing database SQLite3 and not PostgreSQL as production testing is not required. 

The following error when trying to test in the production database: `error: \ RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when
running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
warnings.warn(
Got an error creating the test database: permission denied to create database)`

It is suspected this is due using Windows PowerShell as a terminal and Visual Studio Code as the IDE.


Tests were running using :

`python manage.py test <app name>` command 

#### URLS

Example Login Url Test :

 `def test_login_url_resolves(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login)`

<p> The code above tests that the URL for login is directed to the login URL and resolves as login URL </p>        
        
#### Views

Example Products Views Test:

`class TestProductsView(TestCase):
    def test_products_page(self):
        response = self.client.get('/products/products/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')`

<p> The code above tests that the products views renders to products.html with a status code of 200 - indicating that is the correct view and asserts to the correct template.</p>   

#### Apps

<p> Each of the apps were tested to test that they asserted to the app that was created e.g products configures to products</p>

Example Feedback App Test:

`class TestAccountsConfig(TestCase):
    def test_feedback_app(self):
        self.assertEqual("feedback", FeedbackConfig.name)
        self.assertEqual("feedback", apps.get_app_config("feedback").name)`

<p> The code above tests that the app is configures to feedback</p>   

#### Models

Example Checkout Model Test:

`class OrderTests(TestCase):
    def test_country_str_test(self):
        test_order = Order(full_name="test",
                           phone_number="test",
                           country="france",
                           postcode="test",
                           town_or_city="test",
                           street_address1="test",
                           street_address2="test",
                           county="test",
                           date="2020-01-01")
        self.assertEqual(str(test_order.country), "france")`

<p> The code above tests that the Order model fields inputs are strings and are asserted to strings for example: country, town_or city. Country is tested and self-asserts correctly to 'france'.</p>  


#### Travis CI

<p> The GitHub repository was linked to travis continuous integration testing when the project was started and CI checks were completed every time the code was pushed to GitHub using Git. The code was connected to Travis integration through creating a .travis.yml file and adding the build status markup:

`[![Build Status](https://travis-ci.org/pranitastudent/Milestone_5_project.svg?branch=master)](https://travis-ci.org/pranitastudent/Milestone_5_project)`


 Continuous integration ensured that views and URLs matched, apps created and placed in installed apps in settings.py existed and views and templates rendered. Errors were flag up if views and URLs did not match and the build would be shown as failing. Currently build has passed all integration testing and is shown as 'Build Passing'.

#### Manual Testing

##### Login

<p> Each of the links were tested. If an incorrect username or password is entered on the login page a error message  appears and indicates that error. A success message is displayed when the correct username and password is used to login. If a user tries to register and does not fill all the fields an empty fields error message is displayed.</p>

##### Stripe and Checkout

<p> The checkout form if not fully completed , an error message flags showing the empty fields.The STRIPE API payment was tested using the API credit card number: 4242 4242 4242 4242, Three digit CVV and expiry month and year (don't enter any real credit card information) and message indicating payment was found to be successful is displayed,  HTTP Response code 200 seen on Network tab of Chrome Dev Tools. If an incorrect card number is applied , the appropriate error message is shown "Your card was declined". The payment time and status code can also be checked in the Stripe Dashboard
</p>

##### Contact Form

<ul>

<li> Go to Contact page </li>
<li> Try to submit an empty form - error messages flag up to show empty fields (hence form validation)
</li>
<li> Try to submit a form without completing the reCAPTCHA task - error message for invalid reCAPTCHA flags up</li>
<li> Try to submit a form with all fields filled in and  tick reCAPTCHA - success message indicates message has been sent, HTTP Response code 200 seen on Network tab of Chrome Dev Tools</li>

</ul>

<p> An example  received message is shown below </p>

[Example_message](example/example.png)

##### Discount Testing

<li> Go to Products page </li>
<li> Add 20 products to the quantity which are £4.99</li>
<li> Click on Cart - SubTotal shown without discount (£99.80) </li>
<li> Click on Checkout - Total shown with £20 discount applied (£79.80) </li>

The discount was shown to successfully apply on order £80 and above thereby validating the checkout and cart.views code.</p>


### Responsive Design Testing

The website was tested on various screen sizes which include mobile and tablet devices. The website was found to be fully functional and has been tested on the following browsers:

<ul>
<li>Google Chrome </li>
<li> Microsoft Edge </li>
<li> Opera</li>
<li> Mozilla Firefox</li>
</ul>

The website was testing on the following devices and found to display code elements and attributes correctly without compromising pixilation of images. 

<ul>
<li> Desktop </li>
<li> Laptop with HiDPI</li>
<li> Laptop with MDPI </li>
<li> Pixel 2 </li>
<li> Pixel 2L </li>
<li> Galaxy S5 </li>
<li> iPhone 5/SE - There is a horizontal scroll bar on cart.html due to the size of small screen but the functionality and UI is not impaired.  </li>
<li> iPhone 6/7/8 </li>
<li> iPhone 6/7/8 plus </li>
<li> iPhone X </li>
<li> iPad </li>
<li> iPad Mini </li>
<li> iPad Pro </li>
</ul>

#### Responsive Design

On mobile view elements stack on top of each as required for example: products. The toggle button is functional to navigate between elements. The website if fully functional throughout all devices.

#### Interesting Bugs

<p> A SMTP Authentication Error was found on Heroku when a user tries to reset there password and submit the contact form. This was resolved by navigating to DisplayUnlockCaptcha on the google account and then a password reset link was successfully sent to the user.</p>

## Testing User Stories

<li> A potential user is able to navigate round the site, view products, register and login. The user's username is displayed top  left underneath the logo once logged in. The user is able to view 6 products/feedback reviews at a time using the pagination bar at the bottom and move between pages 1 and 2 </li>
<li> A potential user is able to reset there password using the password reset link through entering there email address, clicking on the link sent to there email address and entering the new password twice. </li>
<li> A potential user to able to views and add products to cart</li>
<li> A logged in user to able to checkout and purchase products using the stripe API and API credit card number 4242 4242 4242 4242</li>
<li> A potential user is able to view feedback and send a contact email and validate through reCAPTCHA.
</li>
<li> A potential user is able to like/vote a feedback review but clicking on the 'thumbs-up' icon.</li>

### CRUD - logged in user (Feedback)

##### CREATE

<p>The logged in user to able to add a feedback view - feedback review, rating (1-5) and product name.
</p>

##### READ

<p>All users can READ feedback reviews.</p>

##### UPDATE

<p>A user which is logged and has created a feedback can edit there own feedback only and the edit button is only displayed on there own feedback.</p>

##### DELETE    

<p>A user which is logged and has created a feedback can delete there own feedback only and the delete button is only displayed on there own feedback.</p> 


## Deployment

####  Version Control
<p> Code was pushed to GitHub using git. Git was used as version control. </p>

#### To run locally
<ol>
<li> Manually download the project from GitHub and upload to the IDE of choice</li>
<li> Install Python on your machine</li>
<li> Create a folder to store project</li>
<li> Install a virtual environment </li>
<li> Activate virtual environment <li>
<li> Install Django inside virtual environment </li>
<li> Create a Django project : 

`django-admin startproject <name>` </li>

<li> Install dependencies using the command:

`pip install -r requirements.txt` </li>

<li> Add each APP to your settings.py file under INSTALLED_APPS </li>

<li> Next run the command :

`python manage.py makemigrations`

to create a database and then run:

`python manage.py migrate ` to create the tables and fields. </li>

<li> To run the project use the command :

`python manage.py runserver` </li>

</ol>

####  Deploy To Heroku 

<ol>
<li> Created a requriements.txt file which contains all dependencies </li>
<li> Created a Heroku app on Heroku with a unique name </li>
<li> Click on Deploy tab and choose the Heroku PostgreSQL  as a add-on - store URL as an environmental variable in env.py </li>
<li> Under Config Vars in Heroku - add your SECRET KEY , AWS Keys and Stripe KEYS an an environmental variables from env.py </li>
<li> Ensure all migrations are migrated to PostgreSQL database </li>
<li> Created a Procfile- ensure Heroku knows what type of app is being created </li>
<li> Under Deploy the Deployment method- Connected to GitHub is chosen and under Manual deploy : Deploy Branch is chosen to connect the project from GitHub and deploy.
<li> Finally add the Heroku URL to ALLOWED_HOSTS in settings.py </li>
</ol>



## Credits

#### Images

<p> All Images were taken from [Unsplash](https://unsplash.com/) and [Debenhams Store Site] (https://www.debenhams.com/). If the authors wish for me to take these images them they can email on : pranitacoder12@gmail.com</p>

##### Debenhams Store Images

<ol>
<li>Women's Pink T-shirt</li>
<li>Boy White T-shirt</li>
<li>Boy Striped T-shirt</li>
<li>Men's Striped T-shirt</li>
<li>Men's Black T-shirt</li>
<li>Men's White T-shirt</li>
</ol>

##### Unsplash Images

<ol>
<li>Men's Black Skeleton T-shirt</li>
<li>Women's White T-shirt</li>
<li>Women's Black T-shirt</li>
<li>Women's Red T-shirt</li>
</ol>

#### Logo 

<p>The logo was creates using [Flat_Icon](https://www.flaticon.com/). The icon is referenced on the live website as well as required by Flat Icon regulations.</p>

#### Adapted and Taken Code

<p><strong> Where Code has been taken and adapted, references are made within that section of code.</strong></p>

The references which were used are :
<ol>
<li> Traversy Media Udemy Course - Python Django Dev to Development</li>
<li> Bootstrap examples to create product page - https://getbootstrap.com/docs/4.4/examples/album/ </li>
<li> Contact Form- Code adapted from (Django-2.2 Part-7 Django Contact Form
# with SMTP Email Backed Tutorial | By Creative web - https://www.youtube.com/watch?v=QQj561w0wt4 </li>
<li> How to Add reCAPTCHA to a Django Site- VITOR FREITAS - https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html </li> 
<li> Free Code Camp Python Django Web Framework - Full Course for Beginners - https://www.youtube.com/watch?v=F5mRW0jo-U4 </li>
<li> #4 Django Tutorial: How to allow users to login with both username or email ?- 
Jaikrishna Sharma-  https://www.youtube.com/watch?v=c7PqMsQiWKU</li>
<li> The Dumbfounds - Django Testing - URLS, Forms , Models and Views - https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM </li>
<li>Convert Ratings in stars in Django Templates- stack overflow - https://stackoverflow.com/questions/55448221/convert-ratings-in-stars-in-django-template</li>
<li>Bootstrap 4 Multiple Items Carousel (several carousel items shown at once)- stack overflow - https://stackoverflow.com/questions/40393210/bootstrap-4-multiple-items-carousel-several-carousel-items-shown-at-once</li>
<li> Code Institute Blog Lectures - https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+F101+2017_T1/course/ </li>
<li> Code Institute Mini Ecommerce Project Lectures - https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+F101+2017_T1/course/ </li>

</ol>

## Acknowledgements

<p> I received inspiration for this project from The Debenhams Store Site </p>

<p> I would like to acknowledge The Code Institute tutors for there immense help and guidance during this project. A very special thanks to Tim Nelson who aided me to debug my discount function in my cart.views and checkout.views and helped to point out what is required. A special thanks to Anna Greaves who helped me debug my Contact Form Code. A special thank-you to Xavier who taught me how to execute the logging method when trying to debug code. </p>
