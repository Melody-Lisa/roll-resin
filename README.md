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



### Frameworks



### Libraries



### Programs



### Testing and Validation Tools



<sup><sub>[*Back to top*](#contents)</sup></sub>

-------

## Deployment & Local Development



### Heroku Deployment



### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

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