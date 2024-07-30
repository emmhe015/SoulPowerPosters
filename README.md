# SoulPower Posters

![Mockup of Soul Power Posters](./media/mockupSoulPowerPosters.jpg)

Welcome to Soul Power Poste! This application is designed to show posters of different zodiac signs and affirmations to remind you of who you are. 

## Table of Contents

- [Introduction](#introduction)
- [User Stories](#user-stories)
- [Design Features](#design-features)
- [Functions](#functions)
- [Marketing](#marketing)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)


## Introduction
 - This application is designed to show posters as wall art of different zodiac signs and affirmations to remind you of who you are. The concept is a e-commerce store for buyers to add posters to a cart and buy the posters thru a secure checkout. The buyer has a profile to save all the user profile information. 

## User Stories
 - [Go to this project on github to review the user stories](https://github.com/users/emmhe015/projects/2/views/1)


 ## Design Features

- **Homepage Gallery:** The homepage features a gallery showcasing all posters. This allows users to quickly browse through the available products and find items of interest at a glance. The gallery is visually appealing and easy to navigate, enhancing the user experience.

- **Product Page:** The product page lists all the available posters with brief descriptions and prices. Users can filter and sort the products based on various criteria such as popularity, price, and newest arrivals. This helps users to find the specific posters they are looking for more efficiently.

- **Product Detail Page:** Each poster has a dedicated product detail page that provides comprehensive information, including a high-resolution image, detailed description, price, and available sizes. Users can also see customer reviews and ratings, which aid in making informed purchase decisions.

- **Shopping Cart Icon in Navbar:** A shopping cart icon is conveniently located in the navigation bar, allowing users to quickly view and manage their cart items. The icon shows the number of items in the cart, providing a constant reminder and easy access to the cart for a smoother shopping experience.

## Functions

### Homepage
- **Gallery Display:** Shows a gallery of all available posters, allowing users to quickly browse through the offerings.
- **Search Bar:** Users can search for specific posters by entering keywords.
- **Navigation Bar:** Provides links to different sections of the site, including the product page, cart, and user account.

### Product Page
- **Product Listings:** Displays all products with thumbnail images, titles, and prices.
- **Filter Options:** Users can filter products by categories such as zodiac signs, affirmations, and new arrivals.
- **Sort Options:** Allows users to sort products by price, popularity, or newest arrivals.

### Product Detail Page
- **High-Resolution Images:** Provides detailed images of the posters.
- **Product Descriptions:** Includes detailed descriptions, sizes available, and price.
- **Customer Reviews:** Displays customer ratings and reviews to help users make informed decisions.
- **Add to Cart:** Users can add the product to their shopping cart from this page.

### Shopping Cart
- **Cart Overview:** Displays all items added to the cart with their quantities and prices.
- **Update Quantities:** Users can update the quantity of each item in the cart.
- **Remove Items:** Allows users to remove items from the cart.
- **Proceed to Checkout:** Users can proceed to the checkout process from the cart.

### User Account
- **Login/Signup:** Users can create an account or log in to an existing account.
- **Order History:** Displays the user's past orders and their statuses.
- **Account Details:** Allows users to update their personal information and password.

### Checkout Process
- **Billing Information:** Users enter their billing details.
- **Shipping Information:** Users enter their shipping address.
- **Payment Gateway:** Secure payment processing through a payment gateway.
- **Order Confirmation:** Provides a summary of the order and confirmation message once the payment is processed.

### Admin Panel
- **Product Management:** Admins can add, update, or remove products from the store.
- **Order Management:** Admins can view and manage customer orders.
- **User Management:** Admins can manage user accounts, including viewing account details and order history.



## Marketing

![Facebook of Soul Power Posters](./media/facebookSoulPowerPosters.png)

To connect with us and stay updated on the latest news and updates, follow our Facebook page:

- [Soul Power Poster on Facebook](https://www.facebook.com/profile.php?id=61563281967004)

We regularly post updates, feature announcements, and other important information about Soul Power Poste. Engage with us to get the most out of your experience with our application!

- Optimize SEO meta tags. 

## Deployment

### Deploying to GitHub

To deploy your project to GitHub:

1. Initialize a new Git repository if you haven't already:
    ```bash
    git init
    ```
2. Add your files to the repository:
    ```bash
    git add .
    ```
3. Commit your changes:
    ```bash
    git commit -m "Initial commit"
    ```
4. Create a new repository on GitHub.
5. Add the remote repository URL:
    ```bash
    git remote add origin https://github.com/yourusername/your-repository.git
    ```
6. Push your code to GitHub:
    ```bash
    git push -u origin master
    ```

### Deploying to Heroku

To deploy your project to Heroku:

1. Make sure you have the Heroku CLI installed. If not, install it from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

2. Log in to your Heroku account:
    ```bash
    heroku login
    ```

3. Create a new Heroku application:
    ```bash
    heroku create your-app-name
    ```

4. Add a `Procfile` to your project root directory to specify the command that should be run to start your app. For example:
    ```bash
    echo "web: python app.py" > Procfile
    ```

5. Ensure your application has a `requirements.txt` file that lists all dependencies.

6. Commit your changes:
    ```bash
    git add Procfile
    git commit -m "Added Procfile for Heroku"
    ```

7. Push your code to Heroku:
    ```bash
    git push heroku master
    ```

8. Set up your configuration variables on Heroku if needed (e.g., database URL, secret keys):
    ```bash
    heroku config:set KEY=VALUE
    ```

9. Open your application in the browser:
    ```bash
    heroku open
    ```

Your application should now be live on Heroku!

## Testing

The table below outlines the testing functions available in the project and their purposes:

| **Test Function**      | **Description**                                          |
|------------------------|----------------------------------------------------------|
| `test_login_function`  | Tests user login functionality and validation.           |
| `test_signup_function` | Tests user registration and input validation.            |
| `test_data_retrieval`  | Validates data retrieval from the database.              |
| `test_api_endpoints`   | Checks the correctness of API responses.                 |
| `test_ui_elements`     | Ensures that UI components render correctly.             |
| `test_checkout`        | Ensures that checkout is successfull.                    |

All tests have been executed and passed successfully.

## Credits
- Followed the walkthrough of Boutique Ado (Thru Code institute), most of the structure code is from that project. 
- Images is from www.canva.com. 
