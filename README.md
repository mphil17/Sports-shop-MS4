
## Strategy

### Rationale

I was required to produce an e-commerce application. This project is an online second hand sports shop. There has been a growth in online sports shops over the last decade and the marketplace has begin to get saturated. There has also been the beginnings of growth in second hand shops, which started was initially dominated by eBay. Facebook Marketplace has taken off along with Depop- a specialist online second hand clothes shop. Putting these ideas together, I have created a second hand sports shop- which as far as I can tell is unique. Many times, I have had people who I play sport with trying to sell their old equipment. It would make their lives easier if there was a website dedicated to that. It would also allow those looking for cheaper alternatives to new sports equipment, a convenient place to find second hand equipment. Maybe they might be trying out a sport or it might be a child who will likely grow out of equipment quickly. I have not put a transaction cost on the sales as the sales are likely to be low anyway. I will make money through advertising on the site.

## UX

## Planes

### Design

I have used Bootswatch design- Litera. This is a sub-library of Bootstrap. This means that the website is responsive using the Bootstrap grid system.

### Scope

I have used only four of the most popular sports to start with. More sports can be added in the future.

## User Stories

### Buyer
-	To create an account/ login
-	To have a profile page to track orders and history
-	To search for equipment
-	To see details of equipment
-	To put multiple items into a shopping bag
-	To edit the shopping bag
-	To buy equipment securely
-	To receive confirmation of order
-	To contact the business with any issues
-   To navigate the website easily

### Seller
-	To create an account/ login
-	To have a profile page to track items they are selling and history
-	To be able to add items to the site
-	To receive the money from sales
-	To contact the business with any issues
-   To navigate the website easily

### Admin
-	To be able to access admin account
-	To be able to control equipment on the site
-	To be able to control users on the site
-	To make money through advertising

## Skeleton

### Wireframes

I created the wireframes on [Balsamiq](https://balsamiq.com/). I decided to add a profile page later in the project.

- [Home page](/media/wireframes/home.png)
- [Equipment page](/media/wireframes/equipment.png)
- [Individual Equipment View](/media/wireframes/ind-equip-view.png)
- [Sign-Up Page](/media/wireframes/sign-up.png)
- [Checkout Page](/media/wireframes/checkout.png)

### Features

#### Navbar
-	Navbar is reduced to hamburger menu on smaller devices
-	Functioning search bar to search equipment database
-	Links to key pages of the site
#### Equipment
-	List view of most current equipment on the database
-	Sorting of equipment based on name, price, category
-	User can click on a piece of equipment and view more details (and the full description which may have been cut off in the list view if too long) 
#### Account
-	Users can sign-up for the website
-	Users can login to their account and logout.
-	Users can access their own account where they can see their order history, selling history and details
-	Users can change their email, password and details
#### Checkout/ bag
-	Users can add items to their bag
-	Users can go to the checkout page to see their current order
-	Users can amend their current order by deleting items or changing the quantity of each object
-	Users can pay for their items using Stripe and enter their delivery address
#### Seller
-	Users with an account have the ability to sell items by adding them to the store
#### Admin
-	Admin has the ability to add items to the store
-	Admin can delete or edit details for each piece of equipment
#### Toasts
-	Users are aided by messages popping up with information

### Future Features 
-	Terms of service on the footer
-	Real email to users
-	Real Stripe payments
-	Address for delivery pre-populated

## Surface

### Colour Scheme

I initially used blue on the navbar as per the wireframes as this matched the logo. However, the blue was slightly different and clashed with the logo and would have drowned out the logo if it was the same colour. I went for a grey to black diagonal gradient colour instead. This I felt added a professional look to the website.

### Footer
The footer is from bootstrap. The default colour of grey worked well as a contrast from the green background image and complements the black navbar. On the footer are social media links (which are not linked currently), a link to a contact page and a copyright sign showing that the page is up to date.

### Buttons
The buttons are mostly the default Bootswatch Litera buttons with the primary colour. Blue is the colour of the logo so having some blue throughout the app makes sense. It makes them stand out as well. The edges are curved which gives a more friendly feel to them. The secure checkout button is black as it is more important and should be less gimmicky. The sell link is a button even though it is in the navbar as it is not just a link- it is leading to an action as well- similar to the upload button on Youtube.

### Font
I have used 'Kiwi Maru' throughout the project. The font is a modern style without being too gimmicky. The colour changes in order to make it stand out- generally black or off-white.

### Media
The main image on the site is a cricket field with a cricket ball resting on it. The picture deliberately has a lot of green in as that is a common colour in the sports that are being used. The picture is quite serene as well which reassures visitors to the website. On the equipment page, I have used a no image jpeg if the equipment doesn't have an image as a placeholder.


## Testing

#### User Story
- To navigate the website easily

#### Feature
- Navbar Links

#### Tests
- Check each link takes you to where you need to go.
- Check links change depending upon user logged in/ not/ superuser

#### Outcome
- Most links take you where you need to go. Issues with profile.html but now resolved.
- Links are correctly changed for account holder/ not account holder
- 

### Issues
-	App successfully building but showing an error when opening. The Procfile was pointing to the wrong app. Also, settings.py did not have the full Heroku address as the allowed hosts.
-	After setting up AWS, the development environment was not accessing the static files. Fixed by adding ‘development = true’ in the environment variables. 
-	Images not showing
-	‘Stripe’ not being recognised. Reason was the order of the Javascript files.

## Technologies Used
- This project uses HTML5, CSS3, Javascript and Django Framework.
- This project uses [Google Fonts](https://fonts.google.com) for more interesting fonts
- This project uses [Github](https://github.com) 