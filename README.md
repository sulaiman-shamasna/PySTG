# PySTG
A complete TTS/STT App


## Setup Environment
---
To use this package, follow the following stepps:
1. Clone the following repository using the command:
    ```bash
    git clone git@github.com:sulaiman-shamasna/PySTG.git && cd PySTG
    ```
2. Create a ```.env``` file and put there your *OPENAI_API_KEY*, it should look like:
    ```python
    ## .env
    OPENAI_API_KEY='sh-...'
    ```
3. create a virtual environment:
    ```bash
    python -m venv env
    ```
    and activate it via:
    ```bash
    source env/Scripts/activate     # for Windows Machine
    ```
    or
    ```bash
    source env/bin/activate         # For Linux or Mac
    ```

4. Install the package using the command:
    ```bash
    pip install -e .
    ```

## Usage
---
Once the package is sucessfully created and installed, you can use its features, it has tow main features:
- ```speech_generator```: Converts a text (.txt loaded file or directly written) into speech.
- ```text_generator```: Convert a pre-recorded or live recorded audio/ speech into text.

**You can use them as follows**
Make sure you are in the source directory ```../PySTG```, and simply type ```speech_generator``` or ```text_generator```, simply without using ```python``` before the command or ```.py``` after. This is due to the feature of ```console entry points```.

For further detailes on the documentation, please refer to the git repos:
- [Speech Generator](https://github.com/sulaiman-shamasna/Speech-Generator)
- [Text generation](https://github.com/sulaiman-shamasna/Text-Generator)

***Well Done!***