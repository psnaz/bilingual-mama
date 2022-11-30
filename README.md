# BILINGUAL MAMA


This is my 4th project for my Diploma in Software Dev Course and it’s been built for educational purposes only. 

The purpose of the website is to inspire bilingual mums (and dads!) to raise fully bilingual and multicultural children that are used to “live and learn” in two languages simultaneously. 

This website is designed to be responsive and accessible on a range of devices, making it easy to navigate for the audience.

![bm-mockup.png](./docs/images/bm-mockup.png)

## Showcase

A deployed link to the website can be found [here.](https://bilingual-mama.herokuapp.com/)


## Features

Bilingual Mama is a personal blog that includes several pages: Home/ Blog, About, Contact, Register and  Login.

### Navigation Bar

The responsive navigation bar includes links to Home page/Blog, About, Contact, Register and Login. Once a registered user loggs in the login link is replaces a Logout link in the navbar.
This section is linked to other relevant sections of this blog which allows the user to navigate through the page easily.


### The landing Page Image

The landing page includes an outdoor family photograph of the blogger with her children.


### About Section

This section tells an authentic personal story and creates connection with a reader that is being introduced to hands-on bilingual parenting practices that have been tried out by the blogger and other multilingual parents to teach their children their native (minority) language. 
As this is a blog the main focus is the content shared rather than the images, however, the images are used to entice readers and create know-like-trust factor.

### Contact page

### Register

### Login

### Logout
 


## User Experience (UX)

### Strategy

#### **User Stories**

The target audience (end users) of this project are bilingual females (but also males) from the age of 25+ who live abroad and are looking for hands-on information about raising bilingual children in an environment where the minority (their own) language is not spoken readily. It is aimed at this type of audience as my personal story (“bilingual mum of two trying to bring up her children bilingual so that they can understand and speak her language as natives”) can resonate with them.

The end user is looking for inspiration and hands-on advice and how-tos, not scientific theories.

The benefit of this project is to highlight that bilingual parenting can be a very tricky and time-consuming task however, if you have a sound ‘strategy and you persist, you will “bear the fruit of your labour” eventually, as long as you’re patient and consistent.

Other features that are not to be missed is that the users can, if they wish, get in touch to obtain more parenting advice by sending a contact form and also asking questions when commenting on the relevant blog posts. They can also easily navigate to the social links.

#### **Site user/ Blog reader Goals**
- As a site user/blog reader I can view a paginated list of posts so that I can easily select a post to view
- As a Site User/blog reader I can view a list of posts so that I can select one to read
- As a Site User/blog reader I can click on a post so that I can read the full text
- As a Site User/ Blog reader I can register an account so that I can comment and like
- As a Site User/ Blog reader I can leave comments on a post so that I can be involved in the conversation
- As a Site User/ Blog reader I can like or unlike a post so that I can interact with the content
- As a Site User/ Blog reader I can navigate easily through the website so that I can find the information I am looking for
- As a Site User / Blog reader I can view the About page so that I can find out more about the blogger and the purpose of her blog
- As a Site User/ Blog reader I can get in touch with the blogger so that I can submit my questions to her
- As a Site User/ Blog reader I can check the blogger’s social media accounts so that I can be a part of her community and get updates on her content

#### **Site owner/ Blogger / Admin Goals**
- As a Site Owner/ Blogger / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
- As a Site Owner/ Blogger / Admin I can view comments on an individual post so that I can read the conversation
- As a Site Owner/ Blogger / AdminI can create, read, update and delete posts so that I can manage my blog content
- As a Site Owner/ Blogger / AdminI can create draft posts so that I can finish writing the content later
- As a Site Owner/ Blogger / AdminI can approve or disapprove comments so that I can filter out objectionable comments

### Scope

To achieve the above goals I have implemented the following features:


## Technologies Used

### Languages Used
- HTML5, Boostrap framework
- CSS3
- JavaScript
- Python, Django library
- SQLLite/Postgress

### Frameworks, Libraries and Programs Used

- Canva.com: Canva Color Palette Generator was used to create a color palette and Canva was used to create a mock-up design, and for resizing and editing images.
- Git: Git was used for version control by utilizing the Gitpod terminal - to commit to Git and push to GitHub
- GitHub: Github is used to store the project's code after being pushed from Git.
- GoogleDev Tools used to see the element positioning and responsiveness
- [Google Fonts](https://fonts.google.com/): Google fonts ‘Lato’ and 'Roboto' were used. 
- favicon.io was used to create the favicon
- FontAwesome used for social media icons: FB, IG, YT
- Coudinary: for storing images
- [amiresponsive](http://ami.responsivedesign.is/) was used to create the mockup for Readme


## Credits

### Code

- The majority of the code came from the Django Walkthrough project and the Diploma in Software Development study materials, my notes taken during going through the materials and by working with Google DevTools - trial and error approach.

- [MDN Web Docs](https://developer.mozilla.org/en-US/): Used extensively to deepen my knowledge and understanding of HTML and CSS, and chek for ideas and solutions, specifically:  

- For Contact form/ Query model: Youtube [Django Tutorial #9: A More Complex Form (2022) by Django tutorials](https://www.youtube.com/watch?v=-qAf_Qx6Ygg)

- [Djangoproject documentation](https://docs.djangoproject.com/en/4.1/)

- Stackoverflow

- For 404 and 500 Error pages [this youtube tutorial](https://www.youtube.com/watch?v=zSEexM0GspU) and [this article](https://freefrontend.com/html-funny-404-pages/)

-  Mentor’s advice, especially when creating the template and urls for the Query model to render correctly.





======== ALL BELOW TO BE DELETED!!!! ======


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome psnaz,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
