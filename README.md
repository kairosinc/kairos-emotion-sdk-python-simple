# Kairos Simple Emotion SDK

This SDK includes simple scripts to get your Kairos application up and running quickly. 

## Get your keys
===========

1. [Create your free developer account](https://www.kairos.com/signup)
2. Log into the Kairos Developer Dashboard
3. Create an application and copy your **App Id** & **App Key**

## How To Use:
===========

Run the scripts in the root directory using Python 2.7.  To POST a local file to the Kairos API, use:

` python local_file_post.py`

This will return a JSON object containing an emotion analysis of your image or video file.  Test files are provided in the media directory.

Sample JSON response:

` {u'status_code': 4, u'length': 0, u'frames': [DATA], u'media_info': {u'height': 720, u'width': 1280, u'length': 21, u'file': u'9ca99076cdec369d140fb046.mp4', u'type': u'video', u'mime_type': u'video/mp4'}, u'status_message': u'Complete', u'id': u'9ca99076cdec369d140fb046'}`


The timeout for the API request is set for 60 seconds.  If an analysis is not available within that time, you can do a GET request using the 'id' of your POST response above.

` python media_get.py`

If necessary, keep running this request until a successful response is obtained.

## Support 
===========
Have an issue? Visit our [Support page](http://www.kairos.com/support) or [create an issue on GitHub](https://github.com/kairosinc/Kairos-SDK-PHP)





    