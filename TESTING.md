# BlissBoost Testing

<div style="text-align: right;">

[Back to README.md](README.md)

</div>

<img src="static/documents/blissboost_responsive.png" alt="An image representing how the site looks across different devices of varying size.">

[View the live project here.](https://blissboost-079490cc3274.herokuapp.com)

Manual testing was conducted continuously throughout the development process to ensure the functionality of various features across the site.

- - -

## CONTENTS

* [AUTOMATED TESTING](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [JavaScript Validator](#javascript-validation)
  * [Python Validator](#python-validation)
  * [Lighthouse](#lighthouse)
  * [WAVE Testing](#wave-testing)
* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)
    * [Site Wide](#site-wide)
    * [Index Home](#index-home)
    * [Register Page](#register-page)
    * [Log In Page](#log-in-page)
    * [Profile](#profile)
    * [Edit Profile](#edit-profile)
    * [Community Posts](#community-posts)
    * [Add Post](#add-post)
    * [Edit Post](#edit-post)
    * [Get Themes](#get-themes)
    * [Add Theme](#add-theme)
    * [Edit Theme](#edit-theme)
    * [404 Page](#404-page)
  * [Accessibility Testing](#accessibility-testing)
* [BUGS](#bugs)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site along with validation of CSS. I have checked the HTML via url input of the deployed site, so as not to flag errors within the templating, and the CSS has been tested by direct input.



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Javascript Validation

[JS Hint](https://jshint.com) 


<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Python Validation

Flake8 command within the gitpod terminal has been used to validate all python code on the site and ensure it is pep8 compliant. This has flagged no errors with the current code, except for code within migrations and other unused files.



<details><summary>Python</summary>
<img src="static/documents/blissboost_pythonvalidation.png" alt="Javascript Validation with js hint">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Lighthouse

The lighthouse tool within the chrome developer tools has been used to test performance, best practices, accessibility, and SEO. Desktop and mobile tests have been run for each page.

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop |  |  |  |  |
| Mobile |  |  |  |  |



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### WAVE Testing

Parts of the site have been tested for accessibility with [WAVE](https://wave.webaim.org),

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Manual Testing

### Testing User Stories

>#### New User Goals
>
>
>#### Returning User Goals
>
>
>#### Site Admin Goals
>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Full Testing

Full testing was performed on the following devices:

* Laptop
  * Lenovo IDEAPAD Flex 5i

* Mobile
  * Samsung Galaxy S20 FE 5G
 
 Desktop device tested the site using the following browsers:
 
 * Google Chrome
 * Mozilla Firefox
 * Opera
 * Microsoft Edge

Additional testing has been carried out by friends and colleagues including on apple devices and safari.

#### Site-Wide

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Navbar Links | View Different navbar links based on logged out/logged in user/logged in admin | Viewed site based on different logged in status | Links appear based on each status | __PASS__ |
| Brand Logo | Takes you to index or profile home depending on whether you are logged in | Clicked logo | Redirected accordingly | __PASS__ |
| Footer Links | Links open in new tabs to github and linked in | Clicked links | Links open in new tabs to github and linked in | __PASS__ |

#### Index Home

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Shop now Button in call to action | To be taken to the products page | Clicked button | Taken to products page | __PASS__ |

#### Register Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


#### Log In Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |


#### Profile

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |




#### 404 Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Appears when incorrect url entered | View 404 page | Input incorrect url path | Page appears |  |
| Home button | User is returned to index if logged out or their profile if logged in | Click Home button | Redirected accordingly |  |

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Accessibility Testing

Accessibility has been tested via narrator for windows and talkback on android. 

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

## Bugs

### Solved Bugs

| # | Issue | Details | What was done | Fixed? |
| --- | --- | --- | --- | --- |
 

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Known Bugs



<sup><sub>[*Back to top*](#contents)</sup></sub>

-----