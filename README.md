# Games

## Install Python for Windows

- Go to www.python.org and click on Downloads. 
- Click on the latest version of Python for Windows. _It should start with the number 3_.
- Select executable installer from the options that appear.

We used Python 3.6.4 to make our stuff.
Also we used an IDE but Python comes with IDLE. Just saying IDE is better.

## Install dependencies

- From the command prompt, enter:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

## Run the game

- From the command prompt, enter the following command:
    ```
    cd invadedhouse
    python3 run.py
    ```
