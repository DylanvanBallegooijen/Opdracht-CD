# Setting up a Flask application with CI/CD using Github Actions and a Digital Ocean Droplet.
---

*First of all I want to say that I really liked this assigned, I knew a very tiny bit about CI/CD and Linux, it seemed always daunting to me. As I worked through the assigment I learned that is not daunting at all, but it's just a matter of experience .*

Before starting this assigment I promised myself to do this as perfect as possible and use this assignment as a set-up for my self created and hosted portfolio! That's why (I think) I took some steps that weren't necessary for the assignment, but would help to achieve my goal.

First I bought/created a Digital Ocean Droplet that is running a Ubuntu server. I opted to follow the [server set-up](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04) closely and made an user account with sudo permissions. After that I followed [a guide provided by Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) to get a Flask application running using Nginx & Gunicorn. This all went quite smoothely and in no-time I had the application running on the IP address provided by Digital Ocean which I could view by entering it in the browser. This was all done by logging into the server using a Secure Shell.

After that I wanted to take a look into Github Actions. I followed the Github Actions documentation and learned about YAML files and what they do and mean for Github actions (or any other CI/CD provider). The information was quite overwhelming at first and I wasn't really sure where to start to set everything up properly. I found a [guide on Youtube](https://www.youtube.com/watch?v=X3F3El_yvFg) which contains a tutorial on how to set-up automatic deployments for a React project. For this tutorial I made a new project/repo on Github/locally. From the settings of the repo I created a self-hosted linux runner on my VPS. I created a pytest file, which I changed constantly to pass/fail, so I could figure out how the YAML file, Github Actions and my self hosted runner worked and interacted with each other. 

Now I stumbled upon some problems.. I had a folder on my VPS that served an application from one guide which showed actual content on the Droplets' IP address  (this folder was created in the home directory). And a folder that stored an application that was automatically updated by pushing changes to the repository on Github (this folder was nested deeper because of the Github Runner set-up). Now I needed to figure out how to configure the server in such a way that it would display the content updated by Github Actions. This ended up in me finding myself in a "research rabbit hole" where I read too much and tried too little.

After reading a lot about Linux Commands, Nginx, Gunicorn and Github Runners I tried a couple of things and came to the conclusion that I should do a total restart with my new knowledge. I destroyed and rebuilt the droplet and redid al the server settings. I also bought and correctly set-up a Domain name (https://lumax-portfolio.nl which you can view now :D).
I knew with this run I should configure Github Actions first and point the server to the folder that the Github Actions already created for me. This eventually worked and the address would display the content from my Github repo!

However, disaster struck.. After the set-up was done I ran the Github Action and it overwrote all the files created during the server set-up. As you might imagine, this wasn't good for my website status. Luckily the culprit was also the solution. The site wasn't reachable anymore, because the virtual environment was removed by the Github Action. I was able to configure my YAML file in such a way that it would rebuild the virtual environment where my site was served.

```
run: |
          python3.6 -m venv lumax-portfolio-env
          source lumax-portfolio-env/bin/activate
          pip install wheel
          pip install gunicorn flask
          sudo systemctl daemon-reload
          sudo systemctl restart lumax_portfolio
```

These command should've been the final solution, but when I ran the action, I stumbled on the next problem: 
```sudo: no tty present and no askpass program specified```

The last two commands basically asked the Github Runner for a password to execute the sudo commands, but with nobody answering that question the runner got stuck. After some reading online I found that I could disable the sudo passwords for certain commands. So I did just that by giving the command "sudo visudo" and altering the "sudoers file".

![](/sudo_img.png?raw=true)
### The Results

Finally I was able to do a full run! I adjusted the text of the /cow page to display "MOoooOo! Im a COooooOW", and staged/committed the changes to Github. This fired the GitHub Action and ran the first job from the YAML file which 'tested' the changes using pytest in the folder. This test succeeded and thus the second job was able to launch as well. This job would update the code, reinstall the virtual python environment and finally would restart the server. Then the changes could and still can be seen on my [website](https://lumax-portfolio.nl/cow) :)!

![](/jobu_run.png?raw=true)

As a final touch, I also applied and got a SSL certification for the site using Certbot.