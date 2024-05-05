# Introduction

Melys is an e-commerce business, located in South Wales, creating honey and beeswax products. Please note some of these products are not yet created by Melys and have been created for the purpose of this project. The purpose of this website is to sell Melys’ range of products and to create a portfolio for its owner. Melys will have a personable feel to the website, emphasising that this is a small, ethical, and local business. Users can buy a range of products from the website, such as honey or candles, and users can find out more about the bees and owner that created the products. Melys also offers beekeeping workshops, presented by the owner of Melys, and users can sign up through the website if interested.

## Mock up

# User Experience, Research and Design

## Strategy

The purpose of this website is to primarily sell products and promote the site owner’s beekeeping business. For this, the website should have a beekeeping ‘feel’ to it, offering a personable service. In order to understand and create the best user experience, I looked at several honey/beekeeping related websites in order to understand best practice. Here are a couple that helped me in my research:

[Honey Bee Beautiful](https://www.honeybeebeautiful.co.uk/collections/)
gave me a good idea of how I would like my products to appear on the page, along with the language to use in regards to products and descriptions.

[Bees In The D](https://beesinthed.com/) is a NGO that has a focus on “saving the bees”, but it also sells a range of products such as honey, books, clothes, and tours. Its focus on educating audiences prior to selling is useful when creating Melys, as it’s important for users to initially know a little about the business and its owner and bees, before buying its products. Melys should build a level of reliability in order to ensure users both invest in the business through buying products, but also emotionally investing in Melys.

Melys’ target audience, then, are both potential beekeepers and people interested in buying beekeeping products. While, it’s important to entice users through promoting beekeeping, it’s important not to alienate users either by focusing only on beekeeping. The website should have a good e-commerce experience by providing an easy, efficient navigation and checkout system for all users, just like the websites listed above.

Of course, when researching this website, the most influential and important factor in the design and goals of this website was the business owner. Melys’ owner stated that her main goals for this site are the following:

“Sell my products, especially my honey and candles. To promote beekeeping as a hobby and increase interest. I’d like to position myself within the beekeeping community.” 

It is imperative, then, that these needs are considered and met when designing and implementing this website.

## Scope

The scope of this project is partly dependent on the project requirements for [Code Institute](https://learn.codeinstitute.net/courses/course-v1:codeinstitute+DIWAD_MS4+2022_Q1/courseware/5cc55f6df9fe41cc8dcb4d665a251ded/8341150079674a76b87da0143c45f6f9/) and partly dependent on the site owner’s goals as this will be used as a functional e-commerce website.

Code Institute has required the following for this website:

“
1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps..
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain.
4. Create at least 2 custom django models beyond the examples shown on the course
5. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in.
6. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend.
7. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. 
8. Structure and Navigation: Incorporate a main navigation menu and structured layout”

Therefore, the website will have a relational database with custom django models, user authentication, and a payment system. Melys gives a perfect opportunity to do this, offering beekeeping products to sell and workshops for users to apply to. Authentication becomes a necessary component as users who wish to purchase something must log in first.

## User Stories

Here are the User Stories:

![User Stories](media/docs/melysuserstories.webp)

## Structure

In order to ensure good user experience, navigating Melys is clear and easy. This ease encourages users to learn quickly about the business and navigate their way efficiently to products and workshops. Below is the User Journey for Melys:

![User Journey](media/docs/userjourney.webp)

As seen above, users are able to access home, products, about, and workshop pages without needing to log in. This offers users an opportunity to initially learn about the business and its services without expectation to invest in the business itself. However, users must sign up/ log in in order to checkout, incentivising users to create an account, further supporting Melys.

## Skeleton

## Wireframes

Here are the Wireframes:

This is the Home Page:

![Home Page](media/docs/wireframes/home.png)

This is the Log In page:

![Log in](media/docs/wireframes/login.png)

This is the About page:

![About](media/docs/wireframes/about.png)

This is the All Products page:

![All Products](media/docs/wireframes/allproducts.png)

This is the product details page:

![Product page](media/docs/wireframes/productpage.png)

This is the Workshop page:

![Workshop](media/docs/wireframes/workshop.png)

My Account page:

![My Account](media/docs/wireframes/myaccount.png)

This is the shopping bag:

![Shopping Bag](media/docs/wireframes/basket.png)

This is the Checkout page:

![Check Out](media/docs/wireframes/checkout.png)

This is the Thank you page:

![Thank you](media/docs/wireframes/thankyou.png)

## Surface

- The honey and candle images are products by Melys and were taken by the store owner

- The lip balm and soap images were taken from [Unsplash](https://unsplash.com/)

- The lip balm was taken by myself

- All photos featured on the About and Workshop page are owned by the store owner

- The logo was created by the store owner using [Canva](https://www.canva.com/en_gb/)

## Features and Testing

Melys’ features considers both the project requirements and user stories.

**Logo:**

This logo was created by the business owner. It shows a digital drawing of a Lovespoon. The title, “Melys” uses font “Parisienne”, using [Canva](https://www.canva.com/en_gb/). The italicised style of this font allows for a more relaxed approach within the branding, making the website feel more personal.

**Favicon:**

The Favicon used is the Lovespoon logo. The Lovespoon logo is a fundamental component of this site as it signifies Melys’ values: both Welshness and beekeeping. Lovespoons are a traditional Welsh gift, and this depiction of one has a honey dipper at the end of it.

![Favicon](media/docs/screenshots/favicon.png)

**Main navigation:**

The navigation is easy to use and filters products into necessary categories to make for a better user experience. Users are also able to search products or categories via the search panel.

![Main-Nav](media/docs/screenshots/header.png)

The search panel fulfills user stories "Search for a product by name or description (14)" and "See what I've searched for and the number of results (15)"

**Mobile navigation:**

On mobile devices, the navigation becomes a burger menu, ensuring users are not overwhelmed by the navigation system when trying to navigate the website.

![Mobile-nav](media/docs/screenshots/mobilenav.png)

**Sign Up/Log In:**

Users must create an account if needing to checkout. This is to incentivise the users to create an account as well as providing an efficient way for returning customers to checkout.

![Sign-up](media/docs/screenshots/signup.png)

**Shop now/Home page:**

The Shop Now page or the Home Page is the landing point for the website. When the logo is clicked on any site page, it will lead the user back to here. The Home Page shows an image of beekeeping with a small sentence about Melys, before offering users a link to “Shop Now”, leading to the All Products page.

![Home](media/docs/screenshots/landingpage.png)

This fulfills the following user stories- "Register for an account,
Login and logout of own account, Recover my passwork in case I forget it,
Have a personalized user profile"

**All Products:**

The All Products page features each product’s name, image, rating, and price. This page can be sorted by products’ name (A-Z, Z-A), Category, and price. When users click on a product, users are sent to the Product Details Page.

![AllProducts](media/docs/screenshots/allproductspage.png)

This achieves User Story ID 1 - "View a list of products".

**Product details page:**

The product details page shows a single product’s necessary details: image, name, description, rating, and price. Users are able to choose their desired quantity before adding to their shopping bag.

![ProductDetail](media/docs/screenshots/proddetail.png)

This achieves User Story ID 2 - "View individual product details" and ID 16 "Select the quantity of a product when purchasing".

**Sorting**

Users are able to sort products as seen below:

![Sorting](media/docs/screenshots/sorting.png)

This fulfills the following user stories:
"Sort the list of available products, Sort a specific category of product, Sort multiple categories of products simultaneously"

**Shopping bag:**

The shopping bag is featured on the top right of the website, regardless of device. When a product is successfully added, a notification will appear below the bag to notify the user. The shopping back includes a small image of the product(s) in the bag, product(s) name, and the total cost of the product(s).

The Shopping bag fulfils User ID 4 - "Easily view the total of my purchases", 17 - "View items in my bag to be purchased", and 18 - "Adjust the quantity of individual items in my bag".

![Bag](media/docs/screenshots/shoppingbag.png)

**Checkout:**

The Checkout Page includes a summary of the user’s order, delivery details, and payment details. Following checkout, users are taken to an Order Confirmation/Thank You page.

![Checkout](media/docs/screenshots/ordersummary.png)

**Order Confirmation Page:**

![Order-confirm](media/docs/screenshots/orderconfirmation.png)

The checkout process fulfills the following user stories: "Easily enter my payment information", "Feel my personal and payment information is safe and secure", and "View an order confirmation after checkout".

**About:**

The About Page says a little about the site owner.
This fulfils the user ID "Learn about the business and its products" and the site owner's goal "Say a little about my business and products".

**Workshops:**

The Workshop page shows available workshops hosted by Melys. This includes an image, name, description, time, date, and duration. Users click the "Apply Now" button which takes them to the Workshop Apply page.

![Workshops](media/docs/screenshots/workshops.png)

This fulfils the User ID 3 - "Learn about the business and its products" and the store owner's goal "Promote workshops for users to attend".

**Apply Now:**

The Apply Now asks users to fill our its necessary fields to express interest in their desired workshop.

![Apply](media/docs/screenshots/applynow.png)

The workshops and apply now page fulfills user story 5 - "View and apply for workshops".

**Product Management:**

Through Product Management, the site owner is able to easily and efficiently enter new products for their site. This gives the site owner ownership over their own business and allows them to update the site according to their needs.

![Management](media/docs/screenshots/prodmanagement.png)

This fulfills the user stories "Add a product", "Edit/update a product", and "Delete a product".

## Future features

- Ideally, this website would have an alternative version where all text is Welsh as this really pushes the values of the site owner.

## Database schema:

Here is the entity relationship diagram:

![Database schema](media/docs/dbdiagram.webp)

As seen above, models are included for product and category, as well as for the workshops page. Workshop models include fields such as name and description of workshops and can be altered by the store owner. This allows efficiency in presenting information to users who are interested in the workshops, as well as providing efficiency for the store owner to add key information. The WorkshopApply model allows any user to express interest and apply for a workshop, purposefully not restricting potential interest in beekeeping as promoting beekeeping is important to the store owner.

## Code validation

- No errors found in [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) 
Pep8
Jshint
lighthouse

## Deployment

This application is deployed with Heroku. Here are the steps to deploy to Heroku:

- Log in to Heroku and choose New App
Choose a name and the region closest to you.
- Open Settings. Add the config var DATABASE_URL and copy your db URL from ElephantSQL. If you do not have your db attached, you must do the following: Sign up to ElephantSQL, create a new instance, give it a name and select region closest to you, click "Create Instance". Navigate to the start page and click on your database, now you can copy the URL.
- In the terminal, type "pip3 install dj_database_url==0.5.0 psycopg2" to connect to your external db.
- Update requirements.txt through "pip freeze > requirements.txt"
- Import dj_database_url underneath import for os in settings.py
- In Settings, find the DATABASES section and update to this code: "DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }". Do not commit this file with your db in the string.
- Run "python3 manage.py showmigrations". You should see a list of all migrations, with none checked off.
- Migrate your db models using "python3 manage.py migrate"
- Load in the fixtures e.g. "python3 manage.py loaddata categories"
- Create superuser for your db "python3 manage.py createsuperuser"
- Delete the db URL from your settings once more to avoid exposing our db when pushing to Github
- Back on ElephantSQL, select "BROWSER" then click Table queries, then auth-user. If you click "Execute", your newly created superuser details should display.

Now let's run migrations:
- Create a file names "Procfile" in the root directory of your project and as "web: gunicorn projectname.wsgi"
- In settings.py add ['yourappname.heroku.com', 'localhost] to "ALLOWED_HOSTS". Commit and push these changes
- In Heroku settings, update your config vars to include your AWS_ACCESS_KEY and AWS_SECRET_ACCESS_KEY (both from AWS in CSV download). You must have your DATABASE_URL (from ElephantSQL as seen above), EMAIL_HOST_PASSWORD and EMAIL_HOST_USER, and your SECRET_KEY. If using Stripe, you must have your STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY from the Stripe dashboard, and the "STRIPE_WH_SECRET" from the Webhooks Endpoint. USE_AWS should be set to True.
- Once the project is completed, set DEBUG = FALSE in settings.py
- On Heroku, select deploy and connect to your Github. Search for your repository and connect. Click "Deploy Branch". The log will show your project building.
- Click "open app" at the top of the page to view your deployed app.


## Credits, Sources & Acknowledgements

https://fonts.google.com/selection/embed
https://fontawesome.com/
Css tricks as found in base.css
