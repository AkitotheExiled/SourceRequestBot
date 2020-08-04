# SourceRequestBot
Uses a moderator account on reddit to request users to post sources for specific flairs.

### Installing Python
* Download Python 3.7: https://www.python.org/downloads/release/python-370/
* Add Python to Path by selecting box during installation or manually adding to Path(https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.

### Setting up config.ini
* Download the zip file for this repo.
* Extract the contents to your desktop.
* Move on to Secret and Client_ID section.

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

*mysecret*
```
daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at SourceRequestBot by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

*myclient_id*
```
ddMaksjJsuyeb
```

**FLAIR**
* The flair the bot will search for when looking for posts that need sources
```
Fan Art
```

*RECHECK_WAIT*
* The time in minutes to wait before checking up on the post.
```
10
```

*REMOVAL_REASON*
* The reason added to the post when it gets removed for OP not providing a source.
```
Your post was removed because you failed to provide a source!
```

#### Lets put our gathered information into our config.ini file.
* On your desktop, navigate to the extracted folder, SourceRequestBot-master and open it. 
* Open config.ini and it should look something like this.

**Default config.ini**

```
[main]
USER= username
PASSWORD=password
CLIENT_ID=yourclientid
SECRET=yoursecret
DELAY=60
SUBREDDIT=yoursubreddit
FLAIR=Fan Art
RECHECK_WAIT=10
REMOVAL_REASON=Your post was removed because you failed to provide a source!
```

* Now lets enter in our gathered information.  Once you've added all the required information, USER, PASSWORD, CLIENT_ID, SECRET, SUBREDDIT, FLAIR, REMOVAL_REASON, RECHECK_WAIT.  Select file in notepad, and select save.  Now your file should look like this below.

```
[main]
USER =user123
PASSWORD=myultrasecretpassword
CLIENT_ID=ddMaksjJsuyeb
SECRET=daklfanlfkanl392r29neorfjs
RSSURL=https://n4g.com/rss/news?channel=next-gen&sort=latest
DELAY=60
SUBREDDIT=mysubredditexample
FLAIR=Fan Art
RECHECK_WAIT=10
REMOVAL_REASON=Your post was removed because you failed to provide a source!
```
* Now lets move on to the Running your script section.

### PREQ BEFORE RUNNING THE SCRIPT
1. Make sure the account you will run the script on is a moderator of the subreddit it will be posting in.
2. We need to install requirements.txt before continuing.  Please follow the steps below in Running your script section to get started.
*I.E. ScoopJr is a moderator of Kgamers, where I test all my scripts.*

### Running your script
1. Open up the command prompt.  You may type cmd or command prompt in the windows search bar.  Your command prompt should look like below
```
Microsoft Windows [Version 10.0.18362.959]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\AkitotheExiled>

```
2. Now lets navigate to our directory where we downloaded the script.  In the command prompt, type, **cd desktop/SourceRequestBot-master** Now your command prompt should look like
```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>
```

3. Installing requirements.txt so our script can be ran.  In the command prompt, type **python pip install requirements.txt**.  Press enter and wait for the command to finish.  
```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>python pip install requirements.txt
```
4. Time to run our script!  In the command prompt, type, **python sourceordelete.py**.  Your command prompt should match the below text

```
C:\Users\AkitotheExiled\Desktop\SourceRequestBot-master>python parsereplybot.py
```
5. Press the enter key on your keyboard.  The script should run now.


### Contributing
Issue Tracker: https://github.com/AkitotheExiled/SourceRequestBot/issues

### Contact
https://www.reddit.com/user/ScoopJr

