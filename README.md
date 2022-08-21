# Unsigned Ireland

Unsigned Ireland is a website which allows users to add a profile of their band or solo act to the site's database, to be seen by all visitors to the site. The user, once registered, can upload an image of their band along with a biography and information on their next live performance. This information once approved, can be edited or deleted by the user who created it.

------------------AM I REPONSIVE IMAGE-------------------------

## User Storys
Github user storys url: https://github.com/users/paulfitzpatrick85/projects/9
+ As a user I want to register for an account with the website
+ As a user I want to see my logged or logged out in status
+ As a user I want to add a profile with a short biography 
+ As a user I want to be able to upload a photo for my profile
+ As a user I want to update my text/bio and photo
+ As a user I want to be able to delete my profile

## How To Use The Website
 When a user visits the page, they can navigate to the menu in the top left of the page where they can attempt to log in if they have an account or register for account if they have yet to create one.
+ Full screen

 ![nav bar](https://user-images.githubusercontent.com/55660566/185744300-1a5da294-1b97-4805-b162-5b15da566773.png)

 + Mobile view

![nar bar mobile](https://user-images.githubusercontent.com/55660566/185744303-dfc02fbd-98a8-4414-bab4-093bb934d307.png)

If the user chooses to register an account they are required to provide a user name, an email which will be used to match them to the profiles they have created if they try to edit a previously added band profile, and lastly a password. If the user already has an account, the option to login is built into the form to save the user returning to the home page to select login from the menu, and vice versa, that if a use trys to login without an account the option to navigate to the register page is also in the login form.

![signup](https://user-images.githubusercontent.com/55660566/185745664-7b43f1bd-deab-4f6e-a6ea-90911c6ef0c0.png)
![log in](https://user-images.githubusercontent.com/55660566/185745743-6d5fb1e1-ea0f-419a-a2b4-47fa94951d55.png)

*I have setup profiles under two fictitious users to test with if an assessor wishes to use them and also for attemptiing to edit and delete the profiles they did not create themselves in order to test the authentication functionality when logged in as there own created user.

The details should they be needed are as follows:
+ username: testuser1, email: user1@gmail.com, password: testpassword1

+ username: testuser2, email: user2@gmail.com, password: testpassword2

+ Admin/superuser details to view/approve band entries: username: bandadmin1, email: fitzer99@gmail.com, password: passwordband1

Once the user has registered, a message is displayed to the user informing them they have successfully logged in, this same message appears for all user login's.

![login message](https://user-images.githubusercontent.com/55660566/185745525-3c8b2e11-82ae-4b61-809d-98b8b15c623c.png)

The user's login status is displayed in the top right on full screen format, and on smaller screens, the status is found it the drop down menu.

![logged in as](https://user-images.githubusercontent.com/55660566/185764029-ad4839c3-71f4-46fc-9bf9-752fbe8cbb7a.png)

![logged in as mobile](https://user-images.githubusercontent.com/55660566/185764032-21557868-4e70-41ea-bd09-cd7c01b60e55.png)

When the user is logged in and navigates to their chosen genre of the six provided on the home page, there they will find a link/button that will bring them to a form to fill in their band's details which includes a date picker widget for the bands next live performance, and the option to upload a photo, if a photo is not provided by the user, a default image will be displayed in its place. If the chosen genre has no other band profiles, a message is displayed saying 'Be the first to add a band!', this message is removed once a band proflie is added and approved.

![add band page](https://user-images.githubusercontent.com/55660566/185764418-8ce44fcf-c04f-4764-a203-4b12448873fd.png)

Once the user click the 'Click here to add your band' button, they are brought to the bottom of the page to the form to be filled out, all fields are required to be filled.

![add band form](https://user-images.githubusercontent.com/55660566/185764500-ff3de277-9148-42fd-805d-dc25c33308a2.png)

When the 'add my band' button is click the form is submitted for approval by the admin and the user is shown a message telling them their form must be reviewed before it is displayed in the chosen genre section.To prevent a duplicate form being submitted on refresh of the page, the user is prompted to click a link in the message which is simply an empty anchor tag with an empty href, when clicked the message disappears and if the user should eventually refresh the page, the form is not re-submitted.

![add band pending](https://user-images.githubusercontent.com/55660566/185765710-ca88a5d3-c3eb-401c-b815-3dc988cb85f8.png)

In the Admin panel, accessed by adding '/admin' to the end of the home page url, and once logged in as the admin/superuser, the admin can view the details added, including the image if provided, in the submitted form. If all details are found to be okay to be displayed on the site, the admin can change the band's status from draft to published, and tick the 'approve' check box.

![admin form detail 1](https://user-images.githubusercontent.com/55660566/185765955-3de878b8-b897-4058-8411-0da92190dd78.png)
![admin form detail 2](https://user-images.githubusercontent.com/55660566/185765958-972ef756-3d8a-434c-a47d-4ed33bfa24a5.png)
![admin form detail 3](https://user-images.githubusercontent.com/55660566/185765959-b2074da3-b177-43ab-a27b-e10873500570.png)
![admin approve band ](https://user-images.githubusercontent.com/55660566/185765962-bb3d8d32-6ed9-44a8-bf0d-4727595d0965.png)

On return to the webpage, logged in as the band profile creator, the profile is displayed in the chosen genre page along with two buttons, 'edit band' and 'delete band'.

![testband 1profile example](https://user-images.githubusercontent.com/55660566/185766198-183059c2-5e45-4988-abe7-b6cf199bd353.png)

To edit a bands details, only the user and creator of the profile, can click the 'edit band' button which will bring them to a new page where they can see a form prepopulated with the information they origanally inputted, along with a link to view their current band photo.

![edit form](https://user-images.githubusercontent.com/55660566/185779258-6f31d6e0-b0a9-4d7e-bb6e-6c48c12ff2ae.png)

Link when follewed to current band image.

![band image link](https://user-images.githubusercontent.com/55660566/185779514-dc397182-7012-40f5-9afd-27b23356befa.png)

The user can then change one or all fields as required, not all are required as before. (in this example the biography, next gig date and image have been edited.)

![edit form edited](https://user-images.githubusercontent.com/55660566/185779332-d4e5c9fe-61b9-41b5-b9bc-4284b92072b0.png)

Once the user is finished making changes and clicks 'edit my band', the form is submitted and a message is displayed to the user informing them their details have been edited and they should return to the profile location to view the changes.

![edit success message](https://user-images.githubusercontent.com/55660566/185779446-e8661c08-2c33-485f-bb09-7dc14688f6f3.png)

Once back in the genre section the user added their in, they can see the updated profile.

![edited band](https://user-images.githubusercontent.com/55660566/185779536-9570c76e-fb2e-44a9-9c66-284fbd689daa.png)




### Authentication
If a another user is logged in, for example testuser2, and trys to edit the band profile created by testuser1, upon clicking the edit buttton, testuser2 is redirected to the home page, if 'delete band' is clicked, the delete modal will open as the first 'delete band' button is only a link to the modal, but if the 'delete band' button is clicked in the modal to confirm deletion, testuser2 is redirected to the home page and no deletion occurs.

## Code Validation
### Files for PEP8 validation checked through http://pep8online.com/
Although Gitpod displayed errors in the terminal for code that was working as intended (the same errors that where seen is some of the walkthrough projects), these errors where not picked up by the pep8 validator. 
Although I did attempt to remove/edit the code which was underlined in red, this only resulted in errors and the website not functioning.  
All files passed without errors with only a warning 'no new line at end of file', which when a new line is added only creates new warnings of 'blank line at end of file' and 'blank line contains whitespace', so all files where left with this one warning of no new line.

Any other warnings that occured in individual files are mentioned below their image.

+ admin.py

![admin-pep](https://user-images.githubusercontent.com/55660566/185734593-eae5fdf5-1510-446e-80a3-9d60477f06b0.png)

+ forms.py

![forms-pep](https://user-images.githubusercontent.com/55660566/185734753-f72c62fb-99df-4f88-bf16-b9d62cf80a61.png)

+ models.py

![models-pep](https://user-images.githubusercontent.com/55660566/185734943-7a05eb65-e1b5-4bbc-9932-4d28209b0202.png)

+ genres - urls.py

![genre-urls-pep](https://user-images.githubusercontent.com/55660566/185735006-b285cb8f-59f2-40c2-b5ae-e35feb9feb26.png)

+ views.py

![views1-pep](https://user-images.githubusercontent.com/55660566/185735322-7ef310ab-2665-419b-8c54-8d835939e61f.png)
![views2-pep](https://user-images.githubusercontent.com/55660566/185735324-20cb4c43-ac05-44c4-b512-701d513ca9fa.png)

This file displayed a number of warnings regarding 'trailing whitespace', though it seems to be the white space left by the indentation that is being picked up, so any attempt to resolve the warnings only results in incorrect indentation and produces legitimate errors, so the code was left as is.

+ unsigned ireland - urls.py

![un-irel-urls-pep](https://user-images.githubusercontent.com/55660566/185740361-22a10c0c-3387-4c52-ac2d-fa167a23d4a0.png)


## Files for HTML validation
+ base.html
+ edit_band.html
+ genre_detail.html
+ index.html.html
+ login.html
+ logout.html
+ signup.html

## CSS validation



## 
+ I tested the sites accessibility through lighthouse, the intial performance was 73, changing the image file from jpeg's to .avif format increase this to 97, the image below shows the results.

![lighthouse](https://user-images.githubusercontent.com/55660566/185743809-a3a65569-0b3f-4152-8d55-d792a1979eef.png)


credits

I used the walkthrough 'I think thereforew I blog as a template for my site, using its structure to suits my sites needs and changing the code to get what i needed done'. the following code was taken and unchanged: nav section of base.html

post function in views.py -  if statement based on same in blog project

all photos from pexels.com

# original mock up sketches

![pp4 mock-up 1](https://user-images.githubusercontent.com/55660566/185733612-aba8a2cc-ef7e-4ac3-a70e-095992512d98.jpg)
![pp4 mock-up 2](https://user-images.githubusercontent.com/55660566/185733816-06c8c9f6-5bcd-4459-a33f-b2e99a30b1ba.jpg)
![pp4 mock-up 3](https://user-images.githubusercontent.com/55660566/185733819-4ca6197e-3f29-4810-a21e-5fd995851bb6.jpg)

ongoing bugs:
after adding band, user has to navagate to home then back to genre page to check for added profile.
edit form not prepopulating