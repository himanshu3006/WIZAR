

# Install python-pip::	
	sudo apt-get install python-pip

# Install robotFramework:: 
	sudo pip install robotframework

# Install selenium2library::  
	sudo pip install robotframework-selenium2library

# Taking screenshot ::for linux gtk(means graphic libraries) package 
	#Ubuntu 
	sudo apt-get install libgtk-3-dev
	sudo apt-get install python-gtk2

	#Window for window PIL package or wx python 
	#Download and install  PIL or wxpython packages

# Install chrome::
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
	sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
	sudo apt-get install -f

# Install ChromeDriver::
	wget -N http://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip -P ~/
	unzip ~/chromedriver_linux64.zip -d ~/
	sudo mv -f ~/chromedriver /usr/local/share/
	sudo chmod +x /usr/local/share/chromedriver
	sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

# Install robotframework-pageobject::
	sudo pip install robotframework-pageobjects

# Checkout git clone and run the command from the folder 
	python runner.py



# Folder Structure for reference
    .
     └── README.md
    ├── lib
    │   ├── WizrHomePage.py
    │   └── WizrHomePage.pyc
    ├── logs
    ├── resource
    │   ├── forget_passwordlink.robot
    │   ├── login_logoutPage.robot
    │   ├── Relogin_loginPage.robot
    │   ├── Verify_Camera.robot
    │   ├── Verify_DashboardPage.robot
    │   └── Wrong_Email.robot
    └── runner.py



