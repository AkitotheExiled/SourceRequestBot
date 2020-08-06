* [Getting started](#installing-script)
    * [Installing Python](#installing-python)
    * [Installing requirements.txt](#installing-requirements.txt)
    * [Setting your config](#setting-up-config.ini)
        * [username and password](#username-and-password)
        * [secret and client_id](#secret-and-client_id)
        * [flair](#flair)
        * [wait timer](#recheck_wait)
        * [removal reason](#removal_reason)
        * [Putting it all together](#putting-it-together)
* [Running your script](#running-your-script)
* [Bug tracking](#contributing)
* [Contact me](#contact)
- - - -
# Installing Script
* Download the zip file for this repo.
* Extract the contents to your desktop.
- - - -

## Installing Python
* Download [Python 3.7](https://www.python.org/downloads/release/python-370/)
* Add Python to Path by selecting box during installation or [manually adding to Path](https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.
```
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
- - - -
## Installing requirements.txt
* Open up the command prompt.  You may type cmd or command prompt in the windows search bar.  Your command prompt should look like below
```
Microsoft Windows [Version 10.0.18362.959]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\AkitotheExiled>

```
* Now lets navigate to our directory where we downloaded the script.  In the command prompt, type, **cd desktop/SourceRequestBot-master** Now your command prompt should look like
```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>
```

* Installing requirements.txt so our script can be ran.  In the command prompt, type **python pip install requirements.txt**.  Press enter and wait for the command to finish.  
```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>python pip install requirements.txt
```
- - - -
## Setting up config.ini
### username and password
* Enter your username and password for the account you will be using for the program
```
USER= user123
PASSWORD= myultrasecretpassword
```
### Secret and Client_ID
* Go to reddit.com and login to your account. Now select your account name in the top right and select user settings
* Select Privacy & Security
* At the very bottom, select Manage third-party app authorization
* At the very bottom again, select create another app..
* In the name, type "SourceRequestBot by ScoopJr"
* Select the radio button: script
* In description, type "Request sources from specific flaired posts on my subreddit."
* For about url, type "http://localhost"
* For redirect url, type "http://localhost"
* Select create app

**Secret**
* look next to the text, "Secret", and copy this text down somewhere

```
SECRET= daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at SourceRequestBot by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

```
CLIENT_ID= ddMaksjJsuyeb
```

**Delay**
* The time in seconds between full runs.  One full run is a full pass through your subreddit.
```
DELAY = 60
```

**Subreddit**
* The subreddit you will be running the program in!
```
mysubredditexample
```

**Flair**
* The flair the bot will search for when looking for posts that need sources
```
FLAIR= Fan Art
```

**Recheck_wait**
* The time in minutes to wait before checking up on the post.
```
RECHECK_WAIT= 10
```

**Removal_reason**
* The reason added to the post when it gets removed for OP not providing a source.
```
REMOVAL_REASON= Your post was removed because you failed to provide a source!
```
- - - -
### Putting it together
* On your desktop, navigate to the extracted folder, SourceRequestBot-master and open it. 
* Open config.ini and it should look something like this.
* Enter in your information from before and select save!

**It should now look like this!**

```
[main]
USER =user123
PASSWORD=myultrasecretpassword
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
DELAY=60
SUBREDDIT=mysubredditexample
FLAIR=Fan Art
RECHECK_WAIT=10
REMOVAL_REASON=Your post was removed because you failed to provide a source!
```
- - - -

## Running your script
* **Make sure your account is a moderator in the subreddit you will be running in!!**
* Time to run your script!  In the command prompt, type, **python sourceordelete.py**.  Your command prompt should match the below text

```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>python sourceordelete.py
```
* Press the enter key on your keyboard.  The script should be running now :)


### Contributing
Issue Tracker: https://github.com/AkitotheExiled/SourceRequestBot/issues

### Contact
https://www.reddit.com/user/ScoopJr

