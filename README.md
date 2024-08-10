About: Fun project that I use as a tool for the Puzzles and Dragons game. The tool offers a more refined and useful monster search capability than what the game offers. The project uses django with the djongo framework to work with a MongoDB backend where all the monsters are stored.

Installation: 
  Clone the repository and then install all the modules in the requirements.txt file. 
  To populate the database with your monsters, you need to capture http responses from the game, and dowload the json from the body of the responses with monster information.
  Run python raw/populate_json.py and then raw/populate_db.py from the PadSearch directory
  Run python manage.py runserver to run the server
