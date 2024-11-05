import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'PySTG',
    version= '1.0.0',
    author= 'Sulaiman Shamasna',
    author_email= 'suleiman.shamasneh@gmail.com',
    url= 'https://github.com/sulaiman-shamasna/PySTG',
    description= 'A complete TTS/STT App',
    packages=['pystg', 'pystg/helpers'],
    long_description=read('README.md'),
    entry_points = {
        'console_scripts': [
            'speech_generator=pystg.speech_generator:main',
            'text_generator=pystg.text_generator:main',
        ]
    },
    install_requires=[
        'fpdf==1.7.2',
        'openai==0.28.0',
        'pydub==0.25.1',
        'python-dotenv==1.0.1',
        'sounddevice==0.5.1',
        'soundfile==0.12.1',
        'gTTS==2.5.3',
        'playsound==1.3.0',
        'pyttsx3==2.98',
    ]

)













