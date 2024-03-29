# Owery Joinery

<img src="media/mockup-header.jpg" style="margin: 0;">

Owery have designed and hand-crafted kitchens, furniture, doors, windows for decades, however through the pandemic their users have been increasingly asking them to create home finishing products, skirting, architrave etc. This led them to opening their own online eBay shop fronted by their own static website.

<img src="media/owery-menu.png" style="margin: 0;">

>
> The purpose of this project was to create a functional e-commerce site to replace the current static site.
>

# User Experience (UX)

## User Stories

Working with the owner of Owery Joinery the following personas and user stories have been identified:

>
> First Time Visitor
>

- As a first time visitor to the Owery website, I want to be able to…
    - View a list of products. So that I can select something to buy.
    - View a list of specific products of my choosing based their category. So that I can select a particular category of product from a specific list to buy.
    - View a list of specific products of my choosing based their category and style. So that I can select something from a specific list, where it is easy to compare like for like, to buy.
    - View the details of a product. So that I can understand the details, price and dimensions of a product and also see and image of the product.
    - See if there are any special offers. So that I can make an informed purchased based on price.
    - Sort the view of products by price low to high. So that I can make an informed purchased based on price.
    - Sort the view of products by price high to low. So that I can make an informed purchased based on price.
    - Easily register for an account. So that I can have a personalised account to view my profile.
    - Receive and email once I have registered to verify my account was set up.
    - Easily view the value of my shopping cart anywhere on the website. So that I can understand how much I have selected.
    - Easily view a summary of what's in my shopping cart, including all prices such as delivery and grand total price before I purchase. So that I can see how much I will be spending.
    - Check out and purchase my items without having to log in. So that I can conveniently purchase items quickly.
    - Receive confirmation of an order via email. So that I can easily reference my order.
    - Easily view the contact details for the company. So I can contact Owery about my orders or requirements.

>
> Registered Users
>
- As someone who is registered with the Owery website, I want to be able to…
    - Be able to effortlessly log in to the site. So that I can access my profile to view my orders.
    - Be able to effortlessly log out of the site, to keep my account secure.
    - Easily recover my password if I forget it. So that I can recover my access to my profile.
    - Have a personalised profile so that I can view my order history.
    - Checkout and add for the order to be added to my profile. So that I can review my purchases at a later date.
    - Track the status of my order. So that I can check the progress or my order.
    
>
> Business Owner
>
- As a superuser of Owery, I want to be able to...
    - Add new products. So that I can add new items to the product catalogue myself.
    - Amend current products details. So that I can change products in the catalogue myself.
    - Remove products from the catalogue. So that I can keep the product catalogue current.
    - Set a product to discontinued. So that I can keep the product catalogue current without deleting the product.
    - Set a product to on offer. So I can highlight products where the price has been reduced.
    - Set the job status of an order based on business processes. So that the user and workshop can see the work schedule and progress.
    - Print off an order. So that I can pass this to the workshop to progress the order.

>
> Workshop Worker
>
- As a workshop worker, I want to be able to...
    - View all orders of a specific status so I can see my workload
    - Change the status of an order, to pass the order to the next business process step

# Wireframing

 <img src="media/wireframe.jpg" >

 <img src="media/google.jpg" style="margin: 0;">

Google Ads information reports that the current Owery website's traffic is almost 70% mobile devices. This informed the design and therefore wireframes to be built around a mobile experience and this would scale to accommodate desktop.

The wireframes can be accessed here https://www.figma.com/file/PLCjxfbqNyHkBnTBQhETnF/Owery?node-id=3%3A109

# Architecture

## Database

The Owery Joinery website is run on a relational database.

<img src="media/database.jpg" style="margin: 0;">

For this project the Heroku PostgreSQL add-on was used.

## Application

The Django framework provided the application structure that the website was built on to enable an MVC design pattern approach to the application.

### IAM

One of the great advantages of Django is the Identity and Access Management capability that it come with out of the box. This was extended by utilising the Allauth app.

### Forms

Another advantage of Django is the quantity and quality of 3rd party apps that can be used. For form styling out of the box Crispy Forms was used https://django-crispy-forms.readthedocs.io/en/latest/ 

### Static File Delivery

Amazon Web Services was used to facilitate the delivery of application's Static content. An S3 Bucket was configured for this purpose.

### Email

A Gmail account has been configured to facilitate the ability to send emails

# Design Choices

Owery Joinery supplied their corporate colour scheme and logo for this project.

| Description | Hex Colour Value |
| --- | ----------- |
| Owery dark brown/grey  | ##383533 |
| Owery yellow | #F0AE0E |
| Lighter yellow for the main content areas | #FFDD8B |

A mobile first approach defined the layout of the site. Bootstrap was used extensively for layout control.

A sticky menu was chosen to ensure easy access to navigate the website.

I chose the term cart over bag as research suggests humans identify a cart as something you put items in temporarily as opposed to a bag which is what you take items away in.

The Admin Tools were designed for a desktop view.

Google font 'Poppins' was used as the sites default font because it complemented the Company’s logo font. 

Google font 'Nothing You Could Do' was used to bring a more casual tone with a craft vibe.

# Testing

## User Story Testing

>
> As a first time visitor to the Owery website, I want to be able to…
>

<img src="media/UST1.jpg" style="margin: 0;">

<img src="media/UST1-1.jpg" style="margin: 0;">

<img src="media/UST1-2.jpg" style="margin: 0;">

 - View a list of products. So that I can select something to buy.
    - Upon navigating to the website the user is presented with a clean site containing imagery and text that indicates that this is a site that sells wood crafted products.
    - The 6 categories that contain the products each have a card containing an image with a shop now button. This highlights what type of products are available.
    - The user can also navigate to the Product menu item and then see links to All Products
    - When the user has seen a product they wish to purchase they simply click on the Add to Cart button.
    - Or if the user is in the details of the product they can click on an Add to Cart button there too.
 - View a list of specific products of my choosing based their category. So that I can select a particular category of product from a specific list to buy.
    - The category cards on the home page make it easy to navigate to product list filtered to the category specified.
    - On the top navigation there is also a menu item to Products. When this is clicked the list of categories is also viewed.

<img src="media/UST2.jpg" style="margin: 0;">

 - View a list of specific products of my choosing based their category and style. So that I can select something from a specific list, where it is easy to compare like for like.
    - On any product page there is a filter and sort component.
    - The user can specifically tailor a search to their requirements.

<img src="media/UST3.jpg" style="margin: 0;">

 - View the details of a product. So that I can understand the details, price and dimensions of a product and also see and image of the product.
    - Take make this a little quicker, when listed each product has some details available to view without needing to look at further details.
    - However each product also has an obvious View Details button. When clicked this takes the user to a dedicated product details page that contains the items specific details.

<img src="media/UST4.jpg" style="margin: 0;">

<img src="media/UST5.jpg" style="margin: 0;">

 - See if there are any special offers. So that I can make an informed purchased based on price.
    - Any items that are on special offer highlight this by stating that it is a Special Offer! and to View Details in a red button that is distinctive from other products not on offer.

<img src="media/UST6.jpg" style="margin: 0;">

 - Sort the view of products by price low to high. So that I can make an informed purchased based on price.
    - All pages showing lists of products can be order on price of which an option is low to high.
 - Sort the view of products by price high to low. So that I can make an informed purchased based on price.
     - All pages showing lists of products can be order on price of which an option is high to low.

<img src="media/UST7.jpg" style="margin: 0;">

 - Easily register for an account. So that I can have a personalised account to view my profile.
    - If the user wishes to create an account by clicking the Account item on the menu they are presented with an option to register.
    - The sign in process is very simple.
 - Receive and email once I have registered to verify my account was set up.
    - An email is sent to the newly registered user so they can be assured the account is set up correctly.

<img src="media/UST8.jpg" style="margin: 0;">

 - Easily view the value of my shopping cart anywhere on the website. So that I can understand how much I have selected.
    - The shopping cart icon is displayed on the navigation bar at all times including on a mobile device. The icon displays a running total of items in the cart. Clicking on the cart shows a full breakdown of what is in the cart. This includes the cost of item and then a total cost.
    - A sticky navigation bar ensures the shopping cart icon is accessible even when scrolling down a page.
 - Easily view a summary of what's in my shopping cart, including all prices such as delivery and grand total price before I purchase. So that I can see how much I will be spending.
    - The shopping cart icon is displayed on the navigation bar at all times including on a mobile device. The icon displays a running total of items in the cart. Clicking on the cart shows a full breakdown of what is in the cart. This includes the cost of item and then a total cost.
    - A sticky navigation bar ensures the shopping cart icon is accessible even when scrolling down a page.

<img src="media/UST9.jpg" style="margin: 0;">

 - Check out and purchase my items without having to log in. So that I can conveniently purchase items quickly.
    - The application is configured so a user does not need to register with the website
 - Receive confirmation of an order via email. So that I can easily reference my order.
    - Once an order is complete they are directed to a confirmation pages outlining the details of their order and the order number. An email is also sent to the email address they provided.

<img src="media/UST10.jpg" style="margin: 0;">

 - Easily view the contact details for the company. So I can contact Owery about my orders or requirements.
    - On the navigation bar there is a menu item called contact. Clicking this navigates the user a page that displays the various way in which the business can be contacted.

>
> As someone who is registered with the Owery website, I want to be able to…
>

<img src="media/UST11.jpg" style="margin: 0;">

 - Be able to effortlessly log in to the site. So that I can access my profile to view my orders.
    - When a user visits the site by clicking Accounts on the navigation bar they are presented with the option to login.
 - Be able to effortlessly log out of the site, to keep my account secure.
    - When the user wishes to log out of the site  by click on the Accounts item in the menu and then select Logout.
 - Easily recover my password if I forget it. So that I can recover my access to my profile.
    - If the user is unable to remember the password for their account then this can be reset by clicking on the Forgot password button.
    - A reset link is emailed to their account.
    - Clicking on this link takes them to a page that enables them to reset their password.

<img src="media/UST12.jpg" style="margin: 0;"> 

 - Have a personalised profile so that I can view my order history.
    - A user's profile is easily access by clicking on Accounts in the navigation menu then selecting profile. This shows a list of previous orders where they can quickly see the order number, the order date, the order amount and the order status
    - Clicking on the Order Details button takes them to a page where they can view all the details of the order including the individual items purchased.

<img src="media/UST13.jpg" style="margin: 0;">

 - Checkout and add for the order to be added to my profile. So that I can review my purchases at a later date.
    - As a registered user the order is automatically added to their profile.

<img src="media/UST14.jpg" style="margin: 0;">

 - Track the status of my order. So that I can check the progress or my order.
    - The reason for creating a profile is so a user can conveniently store their purchase history information. This also means they can track the status of their order through the workshop.
    
>
> Business Owner - As a superuser of Owery, I want to be able to...
>

<img src="media/UST15.jpg" style="margin: 0;">

 - Add new products. So that I can add new items to the product catalogue myself.
    - If an account is a superuser of the site they will have the facility to add products to the catalogue. This is access by clicking on the Admin Tools item in the menu then selecting Add Products.
    - A very simple for is presented that makes it simple to add a new product.

<img src="media/UST16.jpg" style="margin: 0;">

<img src="media/UST17.jpg" style="margin: 0;">

 - Amend current products details. So that I can change products in the catalogue myself.
    - A superuser can easily amend a product by simple finding it in on of the product catalogue views be that filtered or all products and clicking on the Edit button.
    - They will then be presented with the Edit Product form. From here they can amend and save the product's details.
 - Remove products from the catalogue. So that I can keep the product catalogue current.
    - A superuser can easily delete a product item from the database by finding it in one of the product views be that filtered or all products and clicking on the Edit button.
    They will then be presented with the Edit Product form. From here they can click Delete Product button to delete the product from the database. 
 - Set a product to discontinued. So that I can keep the product catalogue current without deleting the product.
    - If the superuser wishes to just set the product to discontinued instead of deleting the product they can by editing the product and ticking is_discontinued.
 - Set a product to on offer. So I can highlight products where the price has been reduced.
    - If the superuser wishes to set the product as being on offer they can by editing the product and ticking is_discontinued.

<img src="media/UST18.jpg" style="margin: 0;">

 - Set the job status of an order based on business processes. So that the user and workshop can see the work schedule and progress.
    - A super user can easily set the status of an order by simply navigating to it through the Admin Tools' Orders page. From here they can click to view the details of the order. The status of the order is a dropdown and the superuser is able to click and change this status to the required status.
    - The orders page can be searched for by either first name or last name.
    - The orders can also be filtered by current order status.

<img src="media/UST19.jpg" style="margin: 0;">

 - Print off an order. So that I can pass this to the workshop to progress the order.
    - Whilst in the details of an order a Superuser can print off the order by clicking on the Print button.

>
> As a workshop worker, I want to be able to...
>
 - View all orders of a specific status so I can see my workload.
    - As a staff member they are able navigate to the Orders page via the Admin Tool link in the site navigation menu.
    - Here they have a view of all orders. Using the Search bar at the top of the orders the job status can be filtered to show the status required.
 - Change the status of an order, to pass the order to the next business process step.
    - As a staff member they are able to view the details of an order and from there change the status of the order by clicking on the status which opens a drop-down box containing the available status categories. Selecting the one they want and saving the changes.

## Automated URL Testing

Django SimpleTestCase was used to automate the testing of the Django URLS used in this application.

## Functional Testing

The remained of the functional testing was carried out manually.

The was done extensively and throught the build to ensure that the funtionality met the expected outcomes.
The testing sheet can be view here [Functional Testing](Testing.xlsx)

A code review was completed with my course mentor.

## User Testing

A code review was posted in the Code Institute peer-code-review channel.

A group of friends and family took part in user testing.

## HTML
All pages have been tested through https://validator.w3.org/ without issue

## CSS
CSS was validated through https://jigsaw.w3.org/css-validator without issues

## Python
No errors were highlighted through http://pep8online.com/

# Deployment

## To contribute to the project

- Navigate to the Owery Joinery repository page in GitHub https://github.com/PaulWheatcroft/owery-joinery
- In the top right corner click Fork
- This creates a copy in your GitHub repository
- From here you could open in Gitpod or make changes directly in GitHub. Once completed click New Push Request to submit your changes to be merged with the master branch

## Clone and Run Locally

You can find the clone string for the repository in Code button above the project’s files. Most IDE applications have a GUI interface for cloning a GitHub repository from this string.

Alternatively the repository can be cloned from the terminal of your IDE
- Open the terminal
- Change the current working directory to the location where you want the cloned directory
- Type git clone, and then paste the URL you copied earlier. git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
- Press Enter to create the local clone
Once the clone has completed (through either method) you should see a requirements.txt file in the route of the directory.
- In the terminal run pip install -r requirements.txt

The inbuilt Django sqlite3 database will run as a default until you reconfigure this once deployed to Heroku.

It’s advisable to set up the DJANGO_SECRET_KEY as an environment variable rather than leave it exposed in settings.py.

## Stripe

You will need to configure your payment service provider. This project has been set up using Stripe and that will have installed as part of requirements.txt. This project has used the following environment variables to store the keys necessary to run Stripe and make use of their webhook capability. Further documentation of

To set up an account got to https://stripe.com/
- Click start now
- Create your stripe account
- Log in and click on Developers
- Click on API Keys
- •Create two following variables both in settings.py and the same two variable names in your environment variables.
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
- Store the Stripe Publishable key in STRIPE_PUBLIC_KEY in the environment variables and link this to your variable in settings.py: STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '') While strictly speaking this isn’t necessary as the key is public it’s still good practice.
- Store the Stripe Secret key in STRIPE_SECRET_KEY in the environment variables and link this to your variable in settings.py: STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
- Now click on Webhooks in Stripe
- Click Add an endpoint
- When you have configured the endpoint get the Signing secret and store this in another variable STRIPE_WH_SECRET. Again create an environment variable to store the key and link this to the variable in settings.py: STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

The application has been configured for the UK market. Also in settings.py add the following STRIPE_CURRENCY = 'gbp'

At this point content delivery does not need to be configured as this will be served locally through the standard Django file structure.
You should now be able to run the website from your local environment.

# Deploying to Heroku

- To deploy to Heroku https://www.heroku.com/
- Log in with your account
- Select New
- Then Create new app
- Give your app a unique name and choose your local region
- Then click Create app

Once created for the following steps you will need to have access to Settings and to Reveal Config Vars section of your app

## Postgres

This project has been configured using the Heroku Postgres add-on. If you plan on also using this add-on…
- Go to the resources tab in Heroku.
- In the Add-ons search bar look for Heroku Postgres and then click on it to select it
- Choose the Hobby Dev-Free option in plans.
- Click submit order form.

By clicking on the add-on when displayed on the Resources page you will be taken to the datastores page for the database. Click on settings then View Credentials to get the URI path that will be added to the DATABASE_URL variable (see below

## AWS S3 Bucket

An AWS S3 Bucket is used to store the projects static files. Because of how Django works you will also need to configure external storage when deploying to Heroku. To use AWS
- Sign up for an AWS account at https://portal.aws.amazon.com/
- Unless otherwise set this up as a personal account
- Navigate to the AWS Management Console as Root user
- Search and click on S3
- Create a bucket
- Give your bucket a name and choose a region based on your geographical requirements
- Uncheck Block all public access to enable public access
- Acknowledge the current settings
- Click to create the bucket
- Open the bucket you created
- Select Properties tab and turn on static website hosting (bottom of the page)
    - Edit
    - Enable
    - Set Index document to index.html
    - Set Error document to error.html
    - Save changes
- Copy the Amazon Resource Name (ARN)
- Click on the Permissions tab and navigate to Cross-origin resource sharing (CORS) and add the following
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
- In the Bucket Policy click Edit then Policy Generator
    - This open a separate window
- Step 1: is S3 Bucket Policy
- Step 2: add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: The Amazon Resource Name (ARN)
- Click on Add Statement.
- Click on Generate Policy
- Copy the policy from the popup that appears
- Paste the generated policy into the Bucket Policy
- Add '/*' at the end of the Resource key, and save.
- Navigate to the Access control list (ACL) and select List next to Everyone

## AWS IAM

- Search and click on IAM
- Staring on the left of the screen navigate to User Groups
- Create group
- Give your group a name and click create group
- Again on the left of the navigate Policies
    - Create New Policy
    - JSON tab
    - Import Managed Policy and search for S3
    - Select AmazonS3FullAccess and click Import
- Within "Resource" replace * with your [ARN address and ARN address/]
"Resource": [
    "ARN",
    "ARN/*"
]

- Click Next: Tags
- Click Next: Review and provide a name
- Click create policy
- Back on the left-hand side go to User Groups
    - Open your group
    - Permissions
    - Add Permissions
    - Attach Policies
    - Search for your policy and add it
- Back on the left-hand side click Users
    - Add user
    - Add a user name
    - Select Access key - Programmatic access
    - Click Next
    - Select your user group
    - Click Next: Tags then Next: Review then Create User
    - IMPORTANT THIS IS THE ONLY TIME YOU CAN COMPLETE THIS STEP. Download tHE Download.CSV which contains the information you need for the variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. Create both of these environment variables.
You can now configure the following in settings.py
AWS_STORAGE_BUCKET_NAME = 'your bucket name'
AWS_S3_REGION_NAME = ‘your region’
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# Static and media files
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Gmail

Email will print to the console unless you set up your own email account.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'your.email@example.com'

For this project Gmail was used. To use Gmail log in to your account and go to
- All Settings
- Other Google Account settings
- Security (new tab opens)
- Ensure the 2 Step Verification is on
- Now click on App Password and log in
- Set App to Mail
- Device to Other and name it Django
- A 16-digit number will be generated. Copy this and create the following environment variables


EMAIL_HOST_PASS *with the 16-digit code*
EMAIL_HOST_USER *your Gmail account*
DEFAULT_FROM_EMAIL *your applications email address*

The following can now be configured in settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')

## Heroku Config Vars

To recap the Heroku app’s Config Vars should be

DJANGO_SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
USE_AWS
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
DEFAULT_FROM_EMAIL

You should now add

USE_AWS = True
DISABLE_COLLECTSTATIC = 0

# Deploy

You can now deploy the application from your GitHub repository. In Heroku
- Deploy and click on Connect to GitHub
- Authenticate to your GitHub repositories and select the correct GitHub repository for this project.
- Click on Deploy Branch to make the application available publicly through Heroku

This will take several  minutes as Heroku installs the components outlined in requirements.txt. Once complete the app is ready to be opened.

# Bugs
- When partway down a product page adding an item to the cart jupms you back to the top of the page. This is a limitation of the way Python and Django work. Using JavaScript would be a better experience.

# Technologies

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): Is used to structure the website
- [CSS3](https://en.wikipedia.org/wiki/CSS): Is used for the styling of the site
- [Python](https://www.python.org/): Is used to program the functionality of the application
- [Django template language](https://docs.djangoproject.com/en/3.2/ref/templates/language/) Is used to render the data passed to it in the DOM
- [JQuery](https://jquery.com/): Is used to facilitate the Stripe payment. Enabling Bootstrap toasts

### Frameworks, Libraries, Databases & Programs Used

- [Django](https://www.djangoproject.com/): Django is used as the application programming framework 
- [Bootstrap](https://getbootstrap.com/): CSS framework used to speed up design, layout and build of the website 
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Is used to extend the standard Django User class
- [Google Fonts](https://fonts.google.com/): Google fonts were used to import the 'Poppins' and 'Nothing You Could Do' fonts
- [Font Awesome](https://fontawesome.com/): Font Awesome was used icons
- [Git](https://git-scm.com/): Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub
- [GitPod](https://www.gitpod.io/): GitPod was used as the initial development environment
- [GitHub](https://github.com/): GitHub is used to store the projects code after being pushed from Git
- [DB DESIGNER](https://www.dbdesigner.net/): DB DESIGNER was used to design the database structure
- [Figma](https://www.figma.com/): Figma was used to create the wireframes during the design process

# Future Improvements
- Profiles to store addresses
- Implement social media login
- Print button captures the whole window. This could be made much neater
- Search is very crude. Would be better to implement a third party such as Haystack
- Proper layout of emails

# Acknowledgements

Thank you to Paul Gristwood at Owery Joinery for allowing me to redesign his companies website (https://www.owery.co.uk/).

- Product names
- Product SKU
- Product images
- Product descriptions
- Product prices
- Company images
- Company branding and logo information

Massive thanks to my Mentor Adegbenga Adeye for his professional view throughout the project and pushing me to to better :-)

Also a huge thanks to the tutors a Code Institute for being there when I needed them and for them being able to always point me in the right direction!

https://youtu.be/F5mRW0jo-U4 This video from freeCodeCamp.org was super useful it getting be going initially.

Thanks to https://www.goranstimac.com/ for his video tutorial on setting up Bootstrap 5 toasts https://www.goranstimac.com/blog/2021/07/how-to-add-bootstrap-5-toast-on-page-load/

https://smartmockups.com/ was used for the image in the README.

