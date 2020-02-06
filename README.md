# SpeechRecognition

- Hello world examples using speech recognition library with python
- How to easly handle audio messages from facebook messenger and whatsapp without having to create additional files on the server

## How to install:

1. Create a virtualenv
   1. $ virtualenv venv -p python3
   1. $ source venv/bin/activate
1. Install Speech Recognition and PyAudio
   1. $ pip install SpeechRecognition
   1. $ sudo apt install portaudio19-dev python-all-dev
   1. $ pip install pyaudio
1. Run file
   1. $ python speech.py
   
## Code example:

``` python
from Speech import Speech
url = "https://cdn.fbsbx.com/v/t59.3654-21/82553223_796445640872741_8263787187997245440_n.mp4/audioclip-1580956656-5155.mp4?_nc_cat=108&_nc_ohc=3JEUqiAi2-4AX_GpxB2&_nc_ht=cdn.fbsbx.com&oh=0934fe24d7e106658ddebbe1066fb001&oe=5E3D856A"
speech = Speech('messenger')
print(speech.process(url))
```
