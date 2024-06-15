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
  - __News__: This page lists all news articles or blog posts on the site. Users can browse through the latest news and updates.
  - __News Item__: This page provides detailed information about a specific news article or blog post. It includes the full text, images, publication date, and author information.
  - __Add News Item__: This page is used by administrators or authorized users to add a new news article or blog post. It includes fields for the title, content, images, and publication date.
  - __Edit News Item__: This page allows administrators or authorized users to edit the details of an existing news article or blog post. It is similar to the add news item page but pre-populates the fields with the current information.

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Structure

#### Site Structure



#### Database Structure



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Skeleton

#### Wireframes



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## User Interface - Design

### Surface



#### Typography



#### Colours



<sup><sub>[*Back to top*](#contents)</sup></sub>

-------

## Features

### Site Features

#### Favicon



#### Navbar



#### Footer



#### Home



### Defensive Programming



<sup><sub>[*Back to top*](#contents)</sup></sub>

------

## Future Implementations



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Accessibility

### Alt Text



### Aria Labels



### Colours



### Fonts



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