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

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site along with validation of CSS. I have checked the HTML via url input of the deployed site, so as not to flag errors within the templating, and the CSS has been tested by direct input. All pages return with no errors or warnings.

#### HTML Validation

<details>
<summary>Home Page Validation</summary>
<img width="866" alt="rollresinhtmlhome" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/45c4e4ba-d36f-4999-ae4a-a317990622b4">
</details>

<details>
<summary>Products Page Validation</summary>
<img width="874" alt="rollresinhtmlproducts" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/ab415aad-c11a-4821-be78-b23fecfeaff2">
</details>

<details>
<summary>Product Details Page Validation</summary>
<img width="868" alt="rollresinhtmlproductdetails" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/d035d6fc-6b56-43e5-9eaa-f96de8892a07">
</details>

<details>
<summary>Wishlist Page Validation</summary>
<img width="872" alt="rollresinhtmlwishlist" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/1e65e734-edde-4eff-a0f9-0593d0a82333">
</details>

<details>
<summary>Profile Page Validation</summary>
<img width="869" alt="rollresinhtmlprofile" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/405ea2c8-fd16-4f90-90fe-cac8dc9f5445">
</details>

<details>
<summary>Bag Page Validation</summary>
<img width="868" alt="rollresinhtmlbag" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/0a91fa8a-de6f-4bba-87cf-7b98055639a9">
</details>

<details>
<summary>Checkout Page Validation</summary>
<img width="867" alt="rollresinhtmlcheckout" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/0f5c9036-e8d9-4447-a76d-09606330e802">
</details>

<details>
<summary>Checkout Success Page Validation</summary>
<img width="866" alt="rollresinhtmlcheckoutsuccess" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e7d55fdb-30f1-4049-b2a7-7ede724248c3">
</details>

<details>
<summary>Add Product Page Validation</summary>
<img width="862" alt="rollresinhtmladdproduct" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/a05fd164-f702-4c42-8557-ce2d7219ba4a">
</details>

<details>
<summary>Edit Product Page Validation</summary>
<img width="870" alt="rollresinhtmleditproduct" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/9cf2c673-1a09-4d4a-a56e-57073a0060f6">
</details>

<details>
<summary>News Page Validation</summary>
<img width="866" alt="rollresinhtmlnews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/2d464709-0638-4c82-b7f9-b49b2617c59c">
</details>

<details>
<summary>News Item Page Validation</summary>
<img width="865" alt="rollresinhtmlnewsitem" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/30b9c957-d4c6-4bc9-bd06-78a40c138616">
</details>

<details>
<summary>Add News Item Page Validation</summary>
<img width="863" alt="rollresinhtmladdnewsitem" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/14d3a1b6-f7fa-4afa-91e8-520136a6a0c1">
</details>

<details>
<summary>Edit News Page Validation</summary>
<img width="864" alt="rollresinhtmleditnews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/1f05807e-f914-47a5-9ecb-1e76b0efcada">
</details>

<details>
<summary>Sign Up Page Validation</summary>
<img width="861" alt="rollresinhtmlsignup" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/28a2f1b0-3030-43b8-b70c-60173a146014">
</details>

<details>
<summary>Log In Page Validation</summary>
<img width="863" alt="rollresinhtmllogin" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/7313051f-3f1b-4ad0-8e57-ce9fd1c1149e">
</details>

<details>
<summary>Log Out Page Validation</summary>
<img width="863" alt="rollresinhtmllogout" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/9fa76737-c4fb-4e22-affb-6dd9186fd39d">
</details>

#### CSS Validation

<details>
<summary>Base CSS Validation</summary>
<img width="863" alt="rollresincssbase" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/402d8448-ba91-4ff0-bede-edff5e511949">
</details>

<details>
<summary>Products CSS Validation</summary>
<img width="874" alt="rollresincssproducts" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/06ecac30-2eb4-466b-ba50-312f90d56bba">
</details>

<details>
<summary>Profile CSS Validation</summary>
<img width="874" alt="rollresincssprofile" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/3aaa3afc-41e4-4412-942b-526fbcc97163">
</details>

<details>
<summary>Checkout CSS Validation</summary>
<img width="868" alt="rollresincsscheckout" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/6eee8988-91b2-4b24-ba11-51839416d55c">
</details>

<details>
<summary>Sign Up CSS Validation</summary>
<img width="863" alt="rollresincsssignup" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/1d96a92f-4a98-4203-b916-71ad38e0d336">
</details>

<details>
<summary>Log In CSS Validation</summary>
<img width="865" alt="rollresincsslogin" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/7efab91d-0a9c-4619-a378-5dcfffb3cd1a">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Javascript Validation

[JS Hint](https://jshint.com) has been used to validate all javascript on the site. All files return no errors or warnings with `/* global $ */` and `/* jshint eversion: 6 */` added to relevant files to override jshints inability to recognise jquery, and to allow ES6 syntax and features.

<details>
<summary>Bag JS Validation</summary>
<img width="719" alt="rollresinjsbag" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/552c4f9d-5525-4df4-a094-2446df274d65">
</details>

<details>
<summary>Stripe Element JS Validation</summary>
<img width="736" alt="rollresinjsstripeelement" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/300dcdad-d8d8-4024-83ba-2505dbccfd6a">
</details>

<details>
<summary>News JS Validation</summary>
<img width="761" alt="rollresinjsnews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/c8899a05-e76c-4fd8-8bc2-928c2c534397">
</details>

<details>
<summary>Products JS Validation</summary>
<img width="763" alt="rollresinjsproducts" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/0e7cce78-b132-46b7-9347-1cb0b7947e46">
</details>

<details>
<summary>Quantity Input Script JS Validation</summary>
<img width="759" alt="rollresinjsquantityinputscript" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/26c14cad-d7b8-4661-a452-30d1f366156f">
</details>

<details>
<summary>Profile JS Validation</summary>
<img width="761" alt="rollresinjsprofile" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e10ffb48-09c5-411d-a6bc-9c0f6a57b35a">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Python Validation

Flake8 command within the gitpod terminal has been used to validate all python code on the site and ensure it is pep8 compliant as well as using the [CI Python Linter](https://pep8ci.herokuapp.com/#) to double check everything at the end of production. All files tested return no errors or warnings.

#### Roll & Resin Main

<details>
<summary>Settings</summary>
<img width="845" alt="rollresinpythonsettings" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/f023cf3d-3064-47b7-9f20-5fbfe977b6a5">
</details>

<details>
<summary>URLs</summary>
<img width="845" alt="rollresinpythonurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/9152f0ae-17bf-4500-9047-dc9ab941b67e">
</details>

#### Home

<details>
<summary>Home Apps</summary>
<img width="845" alt="rollresinpythonhomeapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/3540f8e7-52ed-475f-b1ba-35463e9ded5a">
</details>

<details>
<summary>Home URLs</summary>
<img width="842" alt="rollresinpythonhomeurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/35228bcc-d07f-49ca-b9a0-462c270dc77f">
</details>

<details>
<summary>Home Views</summary>
<img width="842" alt="rollresinpythonhomeviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e3ceb88b-15c3-4f5e-b1bc-2f71a01dfd6f">
</details>

#### Products

<details>
<summary>Products Admin</summary>
<img width="842" alt="rollresinpythonproductsadmin" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/6efbf040-9a33-4727-b515-b8e7bc244899">
</details>

<details>
<summary>Products Apps</summary>
<img width="842" alt="rollresinpythonproductsapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/f1f5db70-4d4d-4bb0-aacb-7e3963c5d9fa">
</details>

<details>
<summary>Products Forms</summary>
<img width="843" alt="rollresinpythonproductsforms" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/41ce573a-8bec-40f9-b5bf-482d9f631df2">
</details>

<details>
<summary>Products Models</summary>
<img width="842" alt="rollresinpythonproductsmodels" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/f3f309ad-b114-484f-a5e9-1167620ff545">
</details>

<details>
<summary>Products URLs</summary>
<img width="842" alt="rollresinpythonproductsurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/ba3601cb-71a8-4d12-97d5-ee2e0521a602">
</details>

<details>
<summary>Products Views</summary>
<img width="840" alt="rollresinpythonproductsviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/d9082dec-8075-49bd-8010-6430a093d030">
</details>

<details>
<summary>Products Widgets</summary>
<img width="843" alt="rollresinpythonproductswidgets" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/2cf90e7e-e2f8-4eb5-8c11-63fb8900ea73">
</details>

#### News

<details>
<summary>News Admin</summary>
<img width="844" alt="rollresinpythonnewsadmin" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/be8788d7-e2b4-4a52-9470-2305c723bb65">
</details>

<details>
<summary>News Apps</summary>
<img width="847" alt="rollresinpythonnewsapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/ffa2c9c6-e2d9-4fad-b0d9-6706f2158fb2">
</details>

<details>
<summary>News Forms</summary>
<img width="839" alt="rollresinpythonnewsforms" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e097afac-4c34-49ca-b778-b78f532ef2f7">
</details>

<details>
<summary>News Models</summary>
<img width="841" alt="rollresinpythonnewsmodels" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/85a646d9-3270-428d-8b6a-113e92e19393">
</details>

<details>
<summary>News URLs</summary>
<img width="844" alt="rollresinpythonnewsurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/db5e8ccd-d724-445d-b962-7e7fd57e994c">
</details>

<details>
<summary>News Views</summary>
<img width="842" alt="rollresinpythonnewsviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e98280ce-de0e-4870-9134-0f354bdb178e">
</details>

#### Bag

<details>
<summary>Bag Apps</summary>
<img width="857" alt="rollresinpythonbagapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/251a0e8e-9688-4ae4-bc00-ab0337bbc466">
</details>

<details>
<summary>Bag Contexts</summary>
<img width="848" alt="rollresinpythonbagcontexts" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/7f003cb4-1bdc-4814-bb88-04dc1c8ff12a">
</details>

<details>
<summary>Bag URLs</summary>
<img width="847" alt="rollresinpythonbagurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/cfd01101-0ddc-4a1d-b24d-66339fd2704c">
</details>

<details>
<summary>Bag Views</summary>
<img width="843" alt="rollresinpythonbagviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/29ec7a53-73ba-4b94-a4e2-a34622feb358">
</details>

#### Checkout

<details>
<summary>Checkout Admin</summary>
<img width="842" alt="rollresinpythoncheckoutadmin" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/5262bec7-396f-4a69-87b6-afada55d1445">
</details>

<details>
<summary>Checkout Apps</summary>
<img width="843" alt="rollresinpythoncheckoutapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/24da4761-ed1d-41cd-bbab-94311aa3da77">
</details>

<details>
<summary>Checkout Forms</summary>
<img width="842" alt="rollresinpythoncheckoutforms" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/fee8d6ce-57ab-4f0e-8415-87b791d86552">
</details>

<details>
<summary>Checkout Models</summary>
<img width="842" alt="rollresinpythoncheckoutmodels" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/6652a7c6-9e27-4b4b-887d-63dd489ec895">
</details>

<details>
<summary>Checkout Signals</summary>
<img width="841" alt="rollresinpythoncheckoutsignals" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/e1135877-7b5e-4977-b5a2-a5646bb3262f">
</details>

<details>
<summary>Checkout Views</summary>
<img width="842" alt="rollresinpythoncheckoutviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/0d2ebb8a-af2e-4db2-bff5-bafdc3c08cb2">
</details>

<details>
<summary>Checkout Webhooks</summary>
<img width="847" alt="rollresinpythoncheckoutwebhooks" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/cf9b2988-2921-4698-8a3b-909b26dcd934">
</details>

<details>
<summary>Checkout Webhook Handler</summary>
<img width="845" alt="rollresinpythoncheckoutwebhookhandler" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/5de4d33b-9193-4ee7-a825-e8c33b073bbe">
</details>

#### Profile

<details>
<summary>Profile Apps</summary>
<img width="843" alt="rollresinpythonprofileapps" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/4b737f1d-0c5a-46a3-a9b2-222fa1e2ff37">
</details>

<details>
<summary>Profile Forms</summary>
<img width="842" alt="rollresinpythonprofileforms" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/57f89054-9eef-43d1-a6cc-ad35ebba49cb">
</details>

<details>
<summary>Profile Models</summary>
<img width="843" alt="rollresinpythonprofilemodels" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/f3462369-9141-4e24-948d-db602ab17b83">
</details>

<details>
<summary>Profile URLs</summary>
<img width="843" alt="rollresinpythonprofileurls" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/fddc72fc-ab9f-4ca2-9549-058ac4275c11">
</details>

<details>
<summary>Profile Views</summary>
<img width="842" alt="rollresinpythonprofileviews" src="https://github.com/Melody-Lisa/roll-resin/assets/137832068/2486ca92-3d00-41f8-99a4-63abdbef814b">
</details>

<sup><sub>[*Back to top*](#contents)</sup></sub>

-----

### Lighthouse

The lighthouse tool within the chrome developer tools has been used to test performance, best practices, accessibility, and SEO. Desktop and mobile tests have been run for each page.

#### Home

| | Performance | Accessibility | Best Practice | SEO |
| :---: | :---: | :---: | :---: | :---: |
| Desktop | 97 | 84 | 100 | 89 |
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
