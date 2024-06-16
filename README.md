# Roll and Resin

By Melody Lisa.

[View the live project here.](https://blissboost-079490cc3274.herokuapp.com)

This is the documentation for Roll & Resin - an ecommerce site aimed towards selling tabletop accessories. The site has been built using HTML5, CSS3 with bootstrap templating, Python and Django with a relational database stored with ElephantSQL.

******

## Contents

* [User Experience (UX)](#user-experience---ux)
  * [Strategy](#strategy)
    * [User Goals](#user-goals)
    * [Site Admin Goals](#site-admin-goals)
    * [User Stories](#user-stories)
  * [Scope](#scope)
  * [Structure](#structure)
    * [Site Structure](#site-structure)
    * [Database Structure](#database-structure)
  * [Skeleton](#skeleton)
    * [Wireframes](#wireframes)
* [User Interface (UI) Design](#user-interface---design)
  * [Surface](#surface)
    * [Typography](#typography)
    * [Colours](#colours)
* [Features](#features)
    * [Site Features](#site-features)
      * [Favicon](#favicon)
      * [Navbar](#navbar)
      * [Footer](#footer)
      * [Home](#home)
      * [Register](#register)
      * [Log In](#log-in)
      * [Profile](#profile)
      * [Community](#community)
      * [Admin Pages](#admin-pages)
      * [404 Page](#404-page)
    * [Defensive Programming](#defensive-programming)
* [Future Implementations](#future-implementations)
* [Accessibility](#accessibility)
  * [Alt Text](#alt-text)
  * [Aria Labels](#aria-labels)
  * [Colours](#colours-1)
  * [Fonts](#fonts)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Libraries](#libraries)
  * [Programs](#programs)
  * [Testing and Validation Tools](#testing-and-validation-tools)
* [Deployment & Local Development](#deployment--local-development)
  * [MongoDB Non-Relational Database](#mongodb-non-relational-database)
  * [Heroku Deployment](#heroku-deployment)
  * [Local Deployment](#local-deployment)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## User Experience - UX

### Strategy

This project was built as a milestone project on my Diploma in Web Application Development with Code Institute as a learning tool for Full Stack Frameworks with Django. The aim was to create an ecommerce website with login functionality and Stripe implementation for users to pay for goods.


#### User Stories

### New Site Users

- As a new site user, I would like to easily navigate to the main categories of products, so that I can see what the site offers.
- As a new site user, I would like to see my purchase total at all times, so that I don't overspend.
- As a new site user, I would like to view the site's latest news, so that I can understand the company better.
- As a new site user, I would like a clear and straightforward checkout process, so that I can finalize my purchase smoothly.
- As a new site user, I would like to see social media icons prominently displayed, so that I can follow the company on my preferred platforms for updates.

### Returning Site Users

- As a returning site user, I would like to receive email confirmation when I register, so that I can verify my account easily.
- As a returning site user, I would like a secure login and registration process, so that I can protect my personal information.
- As a returning site user, I would like a dashboard where I can view and manage my orders, so that I can track my purchases and manage my account.
- As a returning site user, I would like to easily edit my personal information, so that I can update my details as needed.
- As a returning site user, I would like to view the company's latest news, so that I can keep up to date with their products.
- As a returning site user, I would like to be able to save products to buy later, without having to add them to my basket.

### Site Admin

- As a site administrator, I should be able to add new products.
- As a site administrator, I should be able to edit existing products.
- As a site administrator, I should be able to remove products.
- As a site administrator, I should be able to add news articles.
- As a site administrator, I should be able to edit existing news articles.
- As a site administrator, I should be able to remove news articles.


<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Scope

Taking all of the above into account I decided I would need 14 main pages for the content of the site, outside of the Django allauth account pages. These would be included in templates across 6 Django apps:

- __Home App__:
  - __Home Page__: When users first navigate to the site they are taken to the `index.html` page, where they can view the navigation at the top of the page, along with a call to action button that sends them to the main products page.

- __Products App__:
  - __Products__: This page lists all the products available on the site. Users can browse, search, and filter products based on various criteria.
  - __Product Description__: This page provides detailed information about a specific product. It includes images, descriptions, prices, and ratings. Users can also add the product to their cart or wishlist from this page.
  - __Add Product__: This page is used by administrators or authorized users to add a new product to the site. It includes fields for the product name, description, price, images, and other relevant details.
  - __Edit Product__: This page allows administrators or authorized users to edit the details of an existing product. It is similar to the add product page but pre-populates the fields with the current product information.
  - __Wishlist__: This page displays a list of products that the user has added to their wishlist. Users can view, remove, or move items to their cart from this page.

- __Bag App__:
  - __Bag__: This page shows the contents of the user's shopping bag. Users can view the products they have added, update quantities, remove items, and see the total price before proceeding to checkout.

- __Checkout App__:
  - __Checkout__: This page is where users enter their shipping and payment information to complete their purchase. It includes fields for address, payment details, and order summary.
  - __Checkout Success__: This page is displayed after a successful checkout process. It thanks the user for their purchase and provides an order summary and confirmation number.

- __Profiles App__:
  - __Profile__: This page allows users to view and edit their personal information, such as name, email, and address. It also displays the user's order history and other account-related details.

- __News App__:
  - __News__: This page lists all news articles or blog posts on the site. Users can browse through the latest news and updates. Admin or authorized users can choose to edit or delete individual news items from here.
  - __News Item__: This page provides detailed information about a specific news article or blog post. It includes the full text, images, publication date, and author information. Admin or authorized users can choose to edit or delete news items from here.
  - __Add News Item__: This page is used by administrators or authorized users to add a new news article or blog post. It includes fields for the title, content, images, and publication date.
  - __Edit News Item__: This page allows administrators or authorized users to edit the details of an existing news article or blog post. It is similar to the add news item page but pre-populates the fields with the current information.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Structure

#### Site Structure

| **Navbar?** | **Page**            | **Logged Out** | **Logged In (non-admin)** | **Logged In (admin)** |
|-------------|---------------------|----------------|---------------------------|-----------------------|
| ✔           | Home Page           | ✔              | ✔                         | ✔                     |
| ✔           | Products            | ✔              | ✔                         | ✔                     |
| -           | Product Description | ✔              | ✔                         | ✔                     |
| -           | Add Product         | -              | -                         | ✔                     |
| -           | Edit Product        | -              | -                         | ✔                     |
| ✔           | Wishlist            | -              | ✔                         | ✔                     |
| ✔           | Bag                 | ✔              | ✔                         | ✔                     |
| (In messages)           | Checkout            | ✔              | ✔                         | ✔                     |
| -           | Checkout Success    | ✔              | ✔                         | ✔                     |
| ✔           | Profile             | -              | ✔                         | ✔                     |
| ✔           | News                | ✔              | ✔                         | ✔                     |
| -           | News Item           | ✔              | ✔                         | ✔                     |
| -           | Add News Item       | -              | -                         | ✔                     |
| -           | Edit News Item      | -              | -                         | ✔                     |


#### Database Structure



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Skeleton

#### Wireframes



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## User Interface - Design

### Surface

For the user interface design of the website, dark mode Bootstrap stylings have been chosen to create an aesthetically pleasing and user-friendly experience that aligns with the thematic elements of the content.

1. __Dark Mode Benefits__:
   - __Visual Comfort__: Dark mode reduces eye strain, especially in low-light environments. This makes it easier for users to interact with the site for extended periods.
   - __Battery Efficiency__: For users on mobile devices, dark mode can help conserve battery life, enhancing the overall user experience.
   - __Modern Aesthetic__: Dark mode has gained popularity and is often associated with modern, sleek, and professional designs. This can make the site feel more up-to-date and appealing.

2. __Color Scheme__:
   - __Red and Green__: These colors are chosen to align with the official Dungeons and Dragons branding, providing a familiar yet distinct look.
     - __Red__: This color has been used for main headings and call to action buttons.
     - __Green__: This colour has been used for secondary headings, muted text and hover effects over call to action buttons, turning them green from red to encourage them to go!
   - __Balancing the Colors__: While integrating red and green, care will be taken to avoid overwhelming the user with too many contrasting colors. The primary focus will be on creating a harmonious balance that enhances readability and usability with the main content text being white for maximum readability.

3. __Alignment with Dungeons and Dragons Branding__:
   - __Similar, Not Identical__: The design aims to capture the essence of Dungeons and Dragons without directly copying their branding. This ensures a unique identity for the site while still appealing to fans of the game.
   - __Subtle References__: Using colors and design elements inspired by Dungeons and Dragons helps in creating a thematic connection.

By using dark mode Bootstrap stylings with strategically chosen red and green colors, the website will not only look appealing and professional but will also provide a user experience that resonates with the target audience. This approach ensures that the site stands out while maintaining an intuitive and enjoyable interface for users.


#### Typography

Fonts have been imported from [Google Fonts](https://fonts.google.com/).

- [Sedan](https://fonts.google.com/specimen/Sedan?query=sedan): This is the font across the whole site. The font has been kept simple for readability and so as not to make the page look too busy along with the bold colours and imagery across the site.

#### Colours



<sup><sub>[*Back to top*](#contents)</sup></sub>

-------

## Features

### Site Features

#### Favicon

![Roll & Resin Favicon](media/rollresinfavicon.png)

#### Navbar



#### Footer



#### Home



## Defensive Programming

Defensive programming is crucial for ensuring the reliability, security, and robustness of our Django application. Here's how defensive strategies have been implemented across the app:

### User Authentication and Authorization

To safeguard sensitive areas and ensure proper user access:

#### `@login_required` Decorator

The `@login_required` decorator is used extensively throughout the views to restrict access to authenticated users only. This ensures that unauthorized users cannot access sensitive pages.

Example:
```python
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
```

#### Superuser and Staff Checks
Conditional checks within views determine user roles and provide appropriate access:

Example:

```python
@login_required
def edit_news_item(request, news_item_id):
    """ Edit a news item """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
```

### Superuser Checks in Templates

In addition to backend views, checks have been implemented within the templates to facilitate easy access for superusers to specific pages or features. These template checks ensure that only users with superuser privileges can view and interact with designated elements.

#### Example:

```html
{% if request.user.is_superuser %}
    <a href="{% url 'add_news_item' %}" class="btn-up text-red">Add Article</a>
{% endif %}
```

```html
<div class="dropdown-menu border-0 bg-dark shade-invert text-saria-labelledby="user-options">
  {% if request.user.is_authenticated %}
  {% if request.user.is_superuser %}
  <a href="{% url 'add_product' %}" class="dropdown-item hover-underline-animation">Product Management</a>
  <a href="{% url 'news_items' %}" class="dropdown-item hover-underline-animation">News Management</a>
  {% endif %}
  <a href="{% url 'profile' %}" class="dropdown-item hover-underline-animation">My Profile</a>
  <a href="{% url 'view_product_wishlist' %}" class="dropdown-item hover-underline-animation">Wishlist</a>
  <a href="{% url 'account_logout' %}" class="dropdown-item hover-underline-animation">Logout</a>
  {% else %}
  <a href="{% url 'account_signup' %}" class="dropdown-item hover-underline-animation">Register</a>
  <a href="{% url 'account_login' %}" class="dropdown-item hover-underline-animation">Login</a>
  {% endif %}
</div>
```


<sup><sub>[*Back to top*](#contents)</sup></sub>

------

## Future Implementations

### Reviews and Ratings

Enhancing the current review functionality to allow user contributions will foster greater engagement and provide valuable feedback on products or services offered by the application. Key enhancements will include:

- __User Contributions__: Allowing authenticated users to submit reviews and ratings for products or services they have experienced.
- __Review Moderation__: Providing moderation tools to manage and ensure the authenticity and appropriateness of user-contributed reviews.

### Improved Navigation Bar Styling

Enhancing the navigation bar styling will improve the overall aesthetics and usability of the application, making it easier for users to navigate and access different sections. Key improvements will include:

- __Visual Design__: Enhancing the visual appeal of the navigation bar with modern styling and clear, intuitive icons or labels.
- __Responsive Design__: Ensuring the navigation bar remains functional and visually appealing across various devices and screen sizes.
- __Accessibility__: Optimizing navigation bar elements for accessibility standards to ensure all users can easily navigate the application.
- __Dropdown Menus__: Implementing hierarchical dropdown menus where necessary to organize and categorize navigation options effectively.

### Frontend Admin to Replace Django Admin Panel

Implementing a frontend admin interface offers a more intuitive and customizable alternative to Django's default admin panel, enhancing administrative capabilities and user experience. Key features will include:

- __Dashboard Overview__: Providing administrators with a comprehensive dashboard displaying key metrics and insights.
- __CRUD Operations__: Enabling administrators to perform Create, Read, Update, and Delete operations on application data directly from the frontend.
- __Customization__: Tailoring the frontend admin interface to match the application's branding and workflow requirements.
- __Security__: Implementing robust security measures to safeguard sensitive administrative functions and data.
- __Integration__: Seamlessly integrating with existing backend functionalities while enhancing usability and accessibility for administrators.

These future implementations aim to enhance user engagement, improve usability, and streamline administrative tasks within your Django application.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Accessibility

### Alt Text

Alt text has been implemented across the site, with template syntax to ensure any image that appears via for loop displays the correct alternative.

Example:

```html
{% if product.image %}
<a href="{% url 'product_detail' product.id %}">
  <img class="card-img-top img-fluid" src="{{ product.image.url }}"
                                    alt="{{ product.name }}">
</a>
{% else %}
<a href="{% url 'product_detail' product.id %}">
  <img class="card-img-top img-fluid" src="{{ MEDIA_URL }}noimage.png"
                                    alt="{{ product.name }}">
</a>
{% endif %}
```

### Aria Labels

Aria labels have been implemented across the site where applicable.

### Colours

Contrasting colors are strategically employed throughout the site to enhance readability, complemented by the implementation of text shadows for further clarity.

### Fonts

The site maintains a professional and uniform appearance by using a simple font, ensuring maximum readability.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-------

## Technologies Used

### Languages

- HTML
- CSS
- Jquery
- Javascript
- Python

### Frameworks

- [Django](https://www.djangoproject.com/) - Used as the primary web framework for backend development.

- [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Implemented for frontend styling and layout.

### Libraries

- [Font Awesome](https://fontawesome.com/) - For the iconography on the website.
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.
- [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

### Programs

- [Flaticon](https://www.flaticon.com/free-icon/d20_6545894) - To create the favicon for the site.
- [Figma](https://figma.com/) - For wireframes and other graphics in readme.
- [Git](https://git-scm.com/) - For version control.
- [Google Dev Tools](https://developers.google.com/web/tools/chrome-devtools) - To troubleshoot and test features, solve issues with responsiveness and styling.
- [Heroku](https://www.heroku.com) - For website deployment.
- [ElephantSQL]() - The database used for storing information for the site.
- [Pip](https://pypi.org/project/pip/) - To install Python packages.
- [Red Ketchup](https://redketchup.io/image-resizer) - To convert background image to webp format.

### Testing and Validation Tools

- Samsung Talkback - To test accessibility.
- [JS Hint](https://jshint.com/) - To check the JavaScript code for errors.
- [UI.dev](https://ui.dev/amiresponsive) - To show the site on a range of screen sizes.
- [W3C Markup Validation Service](https://validator.w3.org/) - To validate HTML and CSS code.
- [CI Python Linter](https://pep8ci.herokuapp.com) - To Validate python code.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-------

## Deployment & Local Development

The live deployed application can be found deployed on [Heroku](https://roll-and-resin-60438760f385.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click __Create New Instance__ to start a new database.
- Provide a name (this is commonly the name of the project: tech-treasures).
- Select the __Tiny Turtle (Free)__ plan.
- You can leave the __Tags__ blank.
- Select the __Region__ and __Data Center__ closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the __AWS Management Console__ page.

#### S3 Bucket

- Search for __S3__.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck __Block all public access__, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From __Object Ownership__, make sure to have __ACLs enabled__, and __Bucket owner preferred__ selected.
- From the __Properties__ tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click __Save__.
- From the __Permissions__ tab, paste in the following CORS configuration:

  ```shell
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
- Copy your __ARN__ string.
- From the __Bucket Policy__ tab, select the __Policy Generator__ link, and use the following steps:

  - Policy Type: __S3 Bucket Policy__
  - Effect: __Allow__
  - Principal: `*`
  - Actions: __GetObject__
  - Amazon Resource Name (ARN): __paste-your-ARN-here__
  - Click __Add Statement__
  - Click __Generate Policy__
  - Copy the entire Policy, and paste it into the __Bucket Policy Editor__

    ```shell
    {
    	"Id": "Policy1234567890",
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    			"Sid": "Stmt1234567890",
    			"Action": [
    				"s3:GetObject"
    			],
    			"Effect": "Allow",
    			"Resource": "arn:aws:s3:::your-bucket-name/*"
    			"Principal": "*",
    		}
    	]
    }
    ```
  - Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
  - Click __Save__.
- From the __Access Control List (ACL)__ section, click "Edit" and enable __List__ for __Everyone (public access)__, and accept the warning box.

  - If the edit button is disabled, you need to change the __Object Ownership__ section above to __ACLs enabled__ (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open __IAM__ (Identity and Access Management).
Once on the IAM page, follow these steps:

- From __User Groups__, click __Create New Group__.
  - Suggested Name: `group-roll-resin` (group + the project name)
- Tags are optional, but you must click it to get to the __review policy__ page.
- From __User Groups__, select your newly created group, and go to the __Permissions__ tab.
- Open the __Add Permissions__ dropdown, and click __Attach Policies__.
- Select the policy, then click __Add Permissions__ at the bottom when finished.
- From the __JSON__ tab, select the __Import Managed Policy__ link.
  - Search for __S3__, select the `AmazonS3FullAccess` policy, and then __Import__.
  - You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

    ```shell
    {
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    			"Effect": "Allow",
    			"Action": "s3:*",
    			"Resource": [
    				"arn:aws:s3:::your-bucket-name",
    				"arn:aws:s3:::your-bucket-name/*"
    			]
    		}
    	]
    }
    ```
  - Click __Review Policy__.
  - Suggested Name: `policy-roll-resin` (policy + the project name)
  - Provide a description:

    - "Access to S3 Bucket for tech-treasures static files."
  - Click __Create Policy__.
- From __User Groups__, click your "group-tech-treasures".
- Click __Attach Policy__.
- Search for the policy you've just created ("policy-tech-treasures") and select it, then __Attach Policy__.
- From __User Groups__, click __Add User__.
  - Suggested Name: `user-tech-treasures` (user + the project name)
- For "Select AWS Access Type", select __Programmatic Access__.
- Select the group to add your new user to: `group-tech-treasures`
- Tags are optional, but you must click it to get to the __review user__ page.
- Click __Create User__ once done.
- You should see a button to __Download .csv__, so click it to save a copy on your system.
  - __IMPORTANT__: once you pass this page, you cannot come back to download it again, so do it immediately!
  - This contains the user's __Access key ID__ and __Secret access key__.
  - `AWS_ACCESS_KEY_ID` = __Access key ID__
  - `AWS_SECRET_ACCESS_KEY` = __Secret access key__

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within __S3__, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under __Manage Public Permissions__, select __Grant public read access to this object(s)__.
- No further settings are required, so click __Upload__.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
  - `STRIPE_PUBLIC_KEY` = Publishable Key (starts with __pk__)
  - `STRIPE_SECRET_KEY` = Secret Key (starts with __sk__)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click __Developers__, and select __Webhooks__.
- From there, click __Add Endpoint__.
  - `https://roll-and-resin-60438760f385.herokuapp.com/checkout/wh/`
- Click __receive all events__.
- Click __Add Endpoint__ to complete the process.
- You'll have a new key here:
  - `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with __wh__)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select __New__ in the top-right corner of your Heroku Dashboard, and select __Create new app__ from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select __Create App__.
- From the new app __Settings__, click __Reveal Config Vars__, and set your environment variables.

| Key                       | Value                                                                  |
| ------------------------- | ---------------------------------------------------------------------- |
| `AWS_ACCESS_KEY_ID`     | user's own value                                                       |
| `AWS_SECRET_ACCESS_KEY` | user's own value                                                       |
| `DATABASE_URL`          | user's own value                                                       |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS`       | user's own value                                                       |
| `EMAIL_HOST_USER`       | user's own value                                                       |
| `SECRET_KEY`            | user's own value                                                       |
| `STRIPE_PUBLIC_KEY`     | user's own value                                                       |
| `STRIPE_SECRET_KEY`     | user's own value                                                       |
| `STRIPE_WH_SECRET`      | user's own value                                                       |
| `USE_AWS`               | True                                                                   |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's __requirements__ (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The __Procfile__ can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace __app_name__ with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select __Automatic Deployment__ from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

#### How to Fork

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Melody-Lisa/roll-and-resin)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

#### How to Clone

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Melody-Lisa/roll-and-resin) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Melody-Lisa/roll-and-resin.git`
7. Press Enter to create your local clone.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps. If you are using gitpod, you can add these variables under the __variables__ section of your __user settings__.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Testing

Please see [TESTING.md](TESTING.md) for all testing elements of this site.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Credits

### Code Used



### Content



### Media



### Acknowledgements

* Amy Richardson - Cohort Facilitator: For providing great resources to help with everyone's projects through weekly stand ups.
 
* Class of June 2023: Everyone in my class channel on slack who is involved with the stand ups and group chat for contributing to the great atmosphere and supportive environment.
 
* The wider slack community: For quick responses to various issues and questions I had at all stages of the project.
 
* Friends and Family: For helping me to test my site on various devices and provide feedback.

<sup><sub>[*Back to top*](#contents)</sup></sub>