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
- Logo was not showing on Heroku but fixed now

#### Feature
- Toasts

#### Tests
- Check that toasts appear when they should

#### Outcome
- Toasts appear to give information but disappear quite quickly

#### User Story
- To search for equipment

#### Feature
- Search

#### Tests
- Enter a search term to check it works.
- Enter nothing.

#### Outcome
- Entering nothing turns up all products


#### User Story
- To see details of equipment

#### Feature
- Equipment

#### Tests
- Check that equipment list is viewable.
- Check that equipment can be clicked on to see details.
- Check that sorting works
- Check that categories work

#### Outcome
- Equipment list is viewable. No-image url not working on Heroku. Fixed.
- Can see details when clicked on.
- Sorting works
- Clicking on categories filters only that category.


#### User Story
- To put multiple items into a shopping bag
- To edit the shopping bag

#### Feature
- Bag

#### Tests
- Click on bag when empty.
- Check bag links to checkout when something in there.
- Check ‘go to checkout’ comes up on hover.
- Check that items can be deleted and edited.

#### Outcome
- Bag goes nowhere if clicked on when empty
- Bag goes to checkout screen when got items in
- Go to checkout comes up on hover
- Update and remove work

#### User Story
- To create an account/ login

#### Feature
- Login

#### Tests
- Check logging in with genuine user.
- Check logging in with incorrect username/ password.

#### Outcome
- Can login when email is verified
- Incorrect information throws up error message

#### Feature
- Logout

#### Tests
- Check user can logout.
- Check landing page after logging out.

#### Outcome
- User can logout and gets a check before doing
- Landing page was broken but now goes to home page

#### Feature
- Signup

#### Tests
- Check validators after entering incorrect information into the form (including special characters).
- Check sign-up works.

#### Outcome
- Email verification if not email pattern/ password verification if not strong enough
- Sign-up works

#### Feature
- Change email/ password

#### Tests
- Check this works.

#### Outcome
- It works.

#### User Story
- To have a profile page to track orders and history

#### Feature
- Profile

#### Tests
- Check that an order populates on page.
- Check that users details can be updated.
- Check that users details are populated correctly. 
- Check that unsigned in users can't access profile

#### Outcome
- Orders are on page with relevant information
- User details can be updated
- User details are pre-populated
- Typing in profile in address bar gives an error

#### User Story
- To be able to add items to the site

#### Feature
- Sell

#### Tests
- Check that information is sent correctly.
- Check that correct item is assigned to user

#### Outcome
- Information is received on database and equipment shows in the view
- User is assigned with hidden field in database

#### User Story
- To be able to access admin account
- To be able to control equipment on the site

#### Feature
- Admin

#### Tests
- Check that can add, edit and delete products. 

#### Outcome
- Initially could not edit but fixed. Delete and add work.

#### User Story
- To buy equipment securely
- To receive confirmation of order


#### Feature
- Stripe

#### Tests
- Enter test card.
- Enter card with validation.
- Check information goes through correctly.
- Enter incorrect information.
- Test webhooks- fail and succeed.
- Enter incorrect card information.

#### Outcome
- Card payment works with test card
- Validation works with test card for validation
- Information sent to database
- Webhooks work when testing from Stripe
- Validators work when incorrect card information entered