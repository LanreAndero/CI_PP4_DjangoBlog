# Christian Youth Blog

![Am I Responsive](docs/amiresponsive.png)

**Developer: Lanre James Andero**

💻 [Visit live website](https://cy-django-blog-486df1fc929f.herokuapp.com/)  
(Ctrl + click to open in new tab)


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Christian Youth Blog is a platform aims to provide a space for Christian youth to explore, share, and engage with content that aligns with their faith and values. Discover articles, stories, and discussions that inspire and connect the Christian youth community.
<hr>

### User Goals

- Access content that aligns with Christian values.
- Engage with a community of like-minded Christian youth.
- Find inspiration, guidance, and encouragement through blog articles.

### Site Owner Goals

- Establish a platform for Christian youth to share and explore content.
- Foster a sense of community and connection among Christian youth.
- Provide valuable and uplifting content that resonates with the target audience.
<hr>


## User Experience

### Target Audience
- Teenagers and young adults who are exploring their faith and seeking guidance in their spiritual journey. They may have 
  questions, doubts, and uncertainties about their beliefs and are looking for resources to help them navigate these challenges.
- Youth who are actively involved in their local church community or youth group. They may be seeking content that helps them 
  deepen their understanding of Christian teachings, engage with Scripture, and live out their faith in their daily lives.
- Christian youth who are looking for encouragement, inspiration, and practical advice to help them overcome obstacles, grow 
  spiritually, and live out their faith authentically in today's world.
- As digital natives, this audience is accustomed to consuming content online. They are likely to engage with multimedia content 
  such as blog posts, videos, and social media updates that resonate with their interests and address their spiritual needs.
- Christian youth who are interested in connecting with like-minded peers, sharing experiences, and building a supportive online 
  community where they can discuss faith, ask questions, and encourage one another on their journey of faith.

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Social media
- Contact information

##### Back to [top](#table-of-contents)<hr>


## User Stories


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details>
<img src="docs/heroku/heroku-deployment-01.png">
</details>

2. Create an app, give it a name for such as cy-django-blog, and select a region
<details>
<img src="docs/heroku/heroku-deployment-02.png">
<img src="docs/heroku/heroku-deployment-03.png">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details>
<img src="docs/heroku/heroku-deployment-04.png">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details>
<img src="docs/heroku/heroku-deployment-18.png">
<img src="docs/heroku/heroku-deployment-17.png">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details>
<img src="docs/heroku/heroku-deployment-05.png">
</details>

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi
<details>
<img src="docs/heroku/heroku-deployment-06.png">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py
<details>
<img src="docs/heroku/heroku-deployment-07.png">
<img src="docs/heroku/heroku-deployment-08.png">
</details>

6. Ensure debug is set to false in the settings.py file
<details>
<img src="docs/heroku/heroku-deployment-09.png">
</details>

7. Add localhost, and cy-django-blog.herokuapp.com to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a cy-django-blog
<details>
<img src="docs/heroku/heroku-deployment-19.png">
<img src="docs/heroku/heroku-deployment-10.png">
</details>


15. Ensure the following environment variables are set in Heroku
<details>
<img src="docs/heroku/heroku-deployment-11.png">
</details>

16. Connect the app to GitHub, and enable automatic deploys from main if you wish
<details>
<img src="docs/heroku/heroku-deployment-13.png">
<img src="docs/heroku/heroku-deployment-14.png">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images

Images used were free and sourced from Pinterest.o.uk

### Code

Bootstrap dark navigation theme was used alongside boostrap classes and carousel

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- Code Institute
- My Mentor Mo Shami