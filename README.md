# Unsigned Ireland

Unsigned Ireland is a website which allows users to add a profile of their band to the site's database, to be seen by all visitors to the site. The user, once registered, can upload an image of their band along with a biography and information on their next live performance. This information once approved, can be edited or deleted by the user who created it.

You can view the live site here https://ci-pp4-unsigned-ireland.herokuapp.com/

![responsive-image](https://user-images.githubusercontent.com/55660566/187290399-6a6b4085-6dd7-4e2c-bf9c-7839b6ed496e.png)

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

If the user chooses to register an account they are presented with a form where they can provide a user name, an email - which will be used to match them to the profiles they have created in order to allow them to edit a previously added band profile, or delete it if the so choose, and lastly a password. A note is displayed above the form fields instructing the user that when creating a band profile on the site, they must use the same email address they are about to register with. If the user already has an account, the option to login is built into the form to save the user returning to the home page to select login from the menu, and vice versa, that if a use trys to login without an account the option to navigate to the register page is also in the login form.

![sign up](https://user-images.githubusercontent.com/55660566/187558438-d9b6dc84-1b2e-4a2c-8f46-66bbdef3b367.png)
![log in](https://user-images.githubusercontent.com/55660566/185745743-6d5fb1e1-ea0f-419a-a2b4-47fa94951d55.png)

*I have setup profiles under two fictitious users to test with if an assessor wishes to use them, and also so that an assessor can attempt to edit and delete the profiles they did not create themselves in order to test the authentication functionality when logged in as there own created user.

The details should they be needed are as follows:
+ username: testuser1, email: user1@gmail.com, password: testpassword1

+ username: testuser2, email: user2@gmail.com, password: testpassword2

+ Admin/superuser details to view/approve band entries: username: bandadmin1, email: fitzer99@gmail.com, password: passwordband1

Once the user has registered, a message is displayed to the user informing them they have successfully logged in, this same message appears for all user login's.

![login message](https://user-images.githubusercontent.com/55660566/185745525-3c8b2e11-82ae-4b61-809d-98b8b15c623c.png)

The user's login status is displayed in the top right on full screen format, and on smaller screens, the status is found in the drop down menu.

![logged in as](https://user-images.githubusercontent.com/55660566/185764029-ad4839c3-71f4-46fc-9bf9-752fbe8cbb7a.png)

![logged in as mobile](https://user-images.githubusercontent.com/55660566/185764032-21557868-4e70-41ea-bd09-cd7c01b60e55.png)

When the user is logged in and navigates to their chosen genre of the six provided on the home page, there they will find a link/button that will bring them to a form to fill in their band's details which includes a date picker widget for the bands next live performance, and the option to upload a photo, if a photo is not provided by the user, a default image will be displayed in its place. If the chosen genre has no other band profiles, a message is displayed saying 'Be the first to add a band!', this message is removed once a band proflie is added and approved.
The link/button to add a band does not display if a user is not logged in.

![add band page](https://user-images.githubusercontent.com/55660566/185764418-8ce44fcf-c04f-4764-a203-4b12448873fd.png)
![not logged in-no add band](https://user-images.githubusercontent.com/55660566/187291937-df825ca9-47e3-4510-bac1-f4a9900dba01.png)

Once the user clicks the 'Click here to add your band' button, they are brought to the bottom of the page to the form to be filled out, all fields are required to be filled.

![add band form](https://user-images.githubusercontent.com/55660566/185764500-ff3de277-9148-42fd-805d-dc25c33308a2.png)

When the user has finished filling out the form and the 'add my band' button is clicked, the form is submitted for approval by the admin and the user is shown a message telling them their form must be reviewed before it is displayed in the chosen genre section.To prevent a duplicate form being submitted on refresh of the page, the user is prompted to click a link in the message which is simply an empty anchor tag with an empty href, when clicked the message disappears and if the user should eventually refresh the page, the form is not re-submitted.

![add band pending](https://user-images.githubusercontent.com/55660566/185765710-ca88a5d3-c3eb-401c-b815-3dc988cb85f8.png)

In the Admin panel, accessed by adding '/admin' to the end of the home page url, eg. 'https://ci-pp4-unsigned-ireland.herokuapp.com/admin' and once logged in as the admin/superuser, the admin can by navigate to the 'bands' tab to view the details added , including the image if provided, in the submitted form. If all details are found to be okay to be displayed on the site, the admin can change the band's status from draft to published, and tick the 'approve' check box.

![admin form detail 1](https://user-images.githubusercontent.com/55660566/185765955-3de878b8-b897-4058-8411-0da92190dd78.png)
![admin form detail 2](https://user-images.githubusercontent.com/55660566/185765958-972ef756-3d8a-434c-a47d-4ed33bfa24a5.png)
![admin form detail 3](https://user-images.githubusercontent.com/55660566/185765959-b2074da3-b177-43ab-a27b-e10873500570.png)
![admin approve band ](https://user-images.githubusercontent.com/55660566/185765962-bb3d8d32-6ed9-44a8-bf0d-4727595d0965.png)

On return to the webpage, the profile is displayed in the chosen genre section, and if logged in as user who created the band profile , two buttons, 'edit band' and 'delete band' will be displayed under the profile.

![testband 1profile example](https://user-images.githubusercontent.com/55660566/185766198-183059c2-5e45-4988-abe7-b6cf199bd353.png)

To edit a bands details, only the user who created the profile can click the 'edit band' button which will bring them to a new page where they can see a form prepopulated with the information they origanally inputted, along with a link to view their current band photo.

![edit form](https://user-images.githubusercontent.com/55660566/185779258-6f31d6e0-b0a9-4d7e-bb6e-6c48c12ff2ae.png)

Link when follewed to current band image.

![band image link](https://user-images.githubusercontent.com/55660566/185779514-dc397182-7012-40f5-9afd-27b23356befa.png)

The user can then change one or all fields as required, not all are required as before. (in this example the biography, next gig date and image have been edited.)

![edit form edited](https://user-images.githubusercontent.com/55660566/185779332-d4e5c9fe-61b9-41b5-b9bc-4284b92072b0.png)

Once the user is finished making changes and clicks 'edit my band', the form is submitted and a message is displayed to the user informing them their details have been edited and they should return to the profile location to view the changes.

![edit success message](https://user-images.githubusercontent.com/55660566/185779446-e8661c08-2c33-485f-bb09-7dc14688f6f3.png)

Once back in the genre section the user added their profile in, they can see the updated profile.

![edited band](https://user-images.githubusercontent.com/55660566/185779536-9570c76e-fb2e-44a9-9c66-284fbd689daa.png)

If the user chooses to delete their profile, they can click the 'delete band' button beneath their profile.
upon clicking the button, a modal will open asking the user 'Are you sure you want to delete your band?' and a warning 'This action cannot be undone.' The user can then either cancel the action by clicking cancel or proceed withe the deletion and click 'delete'.

![delete modal](https://user-images.githubusercontent.com/55660566/187296690-69238cd4-16e8-4cb7-a12b-d347852a56f2.png)

When the user is finished using the site and clicks 'log out' for the top menu, they are logged out straight away. After logging out, a message is displayed to tell the user they are now logged out.

![log out](https://user-images.githubusercontent.com/55660566/187297621-69531848-009d-4d1c-9442-4bf47dbf998d.png)

![log out message](https://user-images.githubusercontent.com/55660566/187297634-cc85d559-bb42-44dd-ba14-f9bec6898224.png)

### Authentication
If a another user is logged in, for example testuser2, and trys to edit the band profile created by testuser1, upon clicking the edit buttton, testuser2 is redirected to the home page, if 'delete band' is clicked, the delete modal will open as the first 'delete band' button is only a link to the modal, but if the 'delete band' button is clicked inside the modal to confirm deletion, testuser2 is redirected to the home page and no deletion occurs.

## User Story Testing

+ The site is made and layed out in a way that is easy to use and does not bombard the user with too many or needless details.
+ The login/ log out status messages are displayed cleary and the user is made aware they are logged in at the top right of the screen on all pages. 
+ Adding a profile is made easy with a large button prompting the user to the form to input their details on their genre page of choice.
+ Uploading an image is made easy in that the user does not need to worry about the size of the image they upload, as it will automatically be set to a percentage in relation to the screen size the site is being viewed on.
+ The user can easily add a band profile in their chosen genre using the add band form, which can be easily and immediately edited once approved.
+ The users profile can be permanantly deleted from the database once they have confirmed deletion of the profile.


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


## HTML validation

HTML validated at https://validator.w3.org/

![log in](https://user-images.githubusercontent.com/55660566/187303587-b88e4c63-36ef-40f8-b238-363a4fae2f83.png)

![register](https://user-images.githubusercontent.com/55660566/187303590-90e29a86-89e5-46fe-9c6b-871023207576.png)

![index and base](https://user-images.githubusercontent.com/55660566/187303592-6840600b-1ba4-479e-8bb5-783e847848fc.png)

![genre detail](https://user-images.githubusercontent.com/55660566/187303591-3cff04ca-4caa-4a7b-856d-f3c38d3747ff.png)

The above url (https://ci-pp4-unsigned-ireland.herokuapp.com/Instrumental/) tests the same code for /metal, /rock, /pop etc.

## CSS validation
Css validated with jigsaw W3C CSS Validator

![css 1](https://user-images.githubusercontent.com/55660566/187304676-c1e04272-eb83-4bf0-8607-1d3fffc31fb4.png)

![css2](https://user-images.githubusercontent.com/55660566/187304677-c3d53235-9e04-4a3b-81e1-440fd1eec064.png)

![css3](https://user-images.githubusercontent.com/55660566/187304678-929199c7-07e3-4d84-b5eb-bda96b8c68ca.png)

![css4](https://user-images.githubusercontent.com/55660566/187304679-70408476-405f-4d2a-808f-0f691aa189c3.png)

![css5](https://user-images.githubusercontent.com/55660566/187304680-f924fdc1-68af-4920-921b-39ebb6eea57d.png)


## Javascript validation 
validated at https://jshint.com/

![js test](https://user-images.githubusercontent.com/55660566/187523340-c8a9f252-327e-43f3-af4b-33efffac2efc.png)

## Accessibility
I tested the sites accessibility through lighthouse, the intial performance was 73, changing the image file from jpeg's to .avif format increase this to 97, the image below shows the results.

![lighthouse](https://user-images.githubusercontent.com/55660566/185743809-a3a65569-0b3f-4152-8d55-d792a1979eef.png)

# original mock up sketches

![pp4 mock-up 1](https://user-images.githubusercontent.com/55660566/185733612-aba8a2cc-ef7e-4ac3-a70e-095992512d98.jpg)
![pp4 mock-up 2](https://user-images.githubusercontent.com/55660566/185733816-06c8c9f6-5bcd-4459-a33f-b2e99a30b1ba.jpg)
![pp4 mock-up 3](https://user-images.githubusercontent.com/55660566/185733819-4ca6197e-3f29-4810-a21e-5fd995851bb6.jpg)

+ The third mockup/sketch was intended to be a separate page with only live performance information from all added bands, but I decided to keep the live preformance on each bands profile so the user doesn't need to leave a bands profile to find more information on them in another location.


## Credits
+ All photos where taken from pexels.com and are then hosted on my cloundiary.com account.

+ The code for the navbar was taken from the 'I think therefore I blog' walkthrough navbar section of the base.html file and only changed very slightly.

+ The javascript for the timing out of the messages displayed to the user was also taken from the 'blog' walkthrough project.

+ Also from the walkthrough I used as a template from the 'class PostDetail', the 'def get' and 'def post' functions as I want to mimic how a comment is related to a particular post, that a band profile could be related to a particular genre/catagory. The code was changed to suit my sites needs, a quick comparison is of each is shown below, my code being that on the left in both screen shots.

![class compare](https://user-images.githubusercontent.com/55660566/186520286-5e55abf0-bdce-4e85-8f27-eb272e6a0441.png)

![def genre-post](https://user-images.githubusercontent.com/55660566/186520297-c6627bed-7b13-4a2a-9909-a76dc21da60e.png)


## Deployment 
To deploy the project:
+ In settings.py I set DEBUG to 'False' and added the code "X_FRAME_OPTIONS = 'SAMEORIGIN'"
+ I then pushed my work to github in the the gitpod terminal using the commands: 'git add .', git commit -m "commit message"', 'git push'.
+ In heroku settings I removed the config variable 'DISABLE_COLLECTSTATIC'
+ In the heroku deploy tab I connected my github repository for the project to the heroku app.
+ I enabled automatic deploys then clicked 'deploy branch' to build the live app.