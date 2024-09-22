## Backend
  * play.py
    *  Where FastAPI is located
  * mancala.py
    *  Handles different player moves
    *  Entry point for the game in checkMove
  * board.py
    *  Where all the game logic is handled
  * test_board.py
    *  Unit tests for the board class
  * test_mancala.py
    *  Unit tests for the mancala class
  * requirements.txt and Procfile
    *  Needed for deployment 
## Frontend 
  * node modules
    *  All the packages and dependencies we used
  * src
    *  App.css
        * All of the styling for our game
    *  App.js
        * Holds Routes to all other pages 
    *  Instructions.js
        * List of instructions for users 
    *  Mancala.js
        * Game board, responsible for sending out API calls 
    *  Welcome.js
        * Intro page 
    *  Winloss.js
        * Ending page 
  * build folder
    *  Needed for deployment

## To run the game locally:
  * Clone the repository
     * Make sure your device has up to date versions of Python and Node.  
  * For the backend API, please run the following  
     * pip install fastapi
     * pip install uvicorn 
        * FastAPI is a web framework for building APIs with Python, and Uvicorn is an Asynchronous Server Gateway Interface between Python web servers and frameworks.  
     * After cloning the repository, navigate to the backend folder and run the following command to start up the backend server.
       * python3 -m uvicorn play:app –reload
  * In another terminal, navigate into the “mancala-frontend” folder and run the following to install any additional packages. Do not terminate the backend.
    * npm install
       * Note: Sometimes certain machines might not install all packages. If you run into an issue where the error says a certain package cannot be found, directly install the package.
       * Npm install [package]
    * npm start  
   
