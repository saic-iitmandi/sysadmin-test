<h2>Dockerizing a fullstack app</h2>
It was quiet familier with docker but still faced many issues in this question

I first made the necessary Frontend(using nginx:alpine) , Backend Dockerfiles and then in the root directory made a docker-compose.yml to define services.(using llms ofc)
The frontend was in js but the backend was in Go.
I script made 4 containers for database(PostgreSql) ,frontend , backend , Redis.

<img src="Screenshot 2025-01-27 213501.png" alt="Example Image" width="600">

For sequre network
1- made a app-network for all services to communicate securely defined a custom bridge network app-network in the docker-compose.yml
2-each service (frontend, backend, db, and redis) i attched explicitly to app-network
3- used .env file in the root to manage sensitive configs(made fake once if does not exists)

Restricted database access to the backend service by using the internal Docker network

I faced many issues in the build and like npm install gave many issues mostly the frontend gave problems...

but somehow after some time i was able to succesfully build and run the app

<img src="Screenshot 2025-01-28 003130.png" alt="Example Image" width="600">
<img src="Screenshot 2025-01-28 003252.png" alt="Example Image" width="600">
<img src="Screenshot 2025-01-28 003338.png" alt="Example Image" width="600">
<img src="Screenshot 2025-01-28 003348.png" alt="Example Image" width="600">

Everything was working fine but the request was not going properly to backend api.
<img src="Screenshot 2025-01-28 003358.png" alt="Example Image" width="600">

I checked the ping thing where i pinged frontend with the backend and it was pinging .

I checked more and found that the api request is being sent to the same url in the network in the inspect element

<img src="Screenshot 2025-01-28 003405.png" alt="Example Image" width="600">
<img src="Screenshot 2025-01-28 003358.png" alt="Example Image" width="600">

To tackle this problem and assuming we cannot make changes to the main code base I thought of using a proxy for the frontend to the backend Api i want

I made an ngnix.config file tried to implement the proxy but was not able to do it with the time contraint so i left the problem till here only
