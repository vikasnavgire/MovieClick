# MovieClick
This is sample Python API application using SQLalchemy and Mysql database used for python backend-engine.

This example demonstrait the Python backend API to serve the request for  Movie, Actor tables query.
This API's support json input and return json output.
Someone may use form data to process and serv the request from Frontend.

1. get all movies details
2. get all actor details
3. get movie by id.
4. get movie by actor id.
5. Add movie details
6. Add actore details.

Example.
API support POST, GET methos :
  1.1 http://127.0.0.1:5000/ 
  
  1.2     http:/.<localhost/ip>:5000/showActorById
        i/p : 
            {
             "id":1
            }
  1.3  http://127.0.0.1:5000/addActor
         i/p:
              {
                 "actorName":"dram"
                }
  1.4 http://127.0.0.1:5000/showActor
  1.5 http://127.0.0.1:5000/addmovie
        {
	        "movie_name":"Niks hits",
         	"movie_actor_id": 2,
	        "rating": 8,
	        "createdon": "2017-02-08"
        }
   
   
 Its open to add new exmple and demonstration purpose.
 
   
