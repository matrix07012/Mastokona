## Twitter Screenshot Bot
This is a python script that runs as the back end of a twitter 'screenshot' bot. It works by first parsing through a directory and selecting a video. It then generates a screenshot at a random time from that video, and uploads it to twitter.

The bot also has the ability to parse through multiple directories, so you can give it a larger organized selection of videos to choose from. 

Take note that if you have a directory in the same hierarchical level as video files, it is significantly more likely that you will pull from the videos rather than parse the directory, since the bot stops parsing once it finds a video.

![Explanation](/help_diagram.png)

Additionally, rather than a screenshot, the bot can also generate videos from the source material.

Currently, the bot is capable of finding and parsing MKV, MP4, and AVI video files. 

Other filetypes can be manually added in the function **get_random_video_filepath** at your own risk.

### How To Use

First, get the requirements with:
`pip install -r requirements.txt`

I personally run the bot as a cronjob on my home server. There are other solutions to do this, but I simply have the bot run every 30 minutes with the cronjob. The job config looks something like this.\

**On Linux:**
`*/30 * * * * python3 run.py`

**TODO:**
Windows/Mac

### Configuration
In the same directory as the run.py script is a configuration file, **settings.cfg**. You will need to modify this file in order for the bot to function.
#### Config Variables
The settings.cfg file contains a JSON-like structure of variables. Of these variables, please note:

*directory* - Located in the 'settings.general' tree. String. The path to your videos, or your folder of (folders of...) videos. Should end with a '/'.

*length* - Located in the 'settings.general.video' tree. Integer. This is what the length of an outputted video clip will be, in seconds.

*chance* - Located in the 'settings.general.video' tree. A number between 0 and 1, representing the percentage of the time the bot will produce a video instead of producing a screenshot. Set to 0 to never produce a video. Set to 1 to produce a video every time.

#### API Keys
There are also API keys that you must fill out. You will need to sign up for a twitter developer account in order to gain access to these. For more info, see Twitter's website. https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api

These keys & secrets should be placed in the corresponding variables in the 'settings.keys.consumer' and 'settings.keys.access' trees.

### Future Enhancements
* Burn in subtitles. (Currently soft-subtitles are not supported).
 
### Licensing
This software is free and open-source software, licensed under the GPLv3. For more information, see the LICENSE file in the repository, or check out https://www.fsf.org/
