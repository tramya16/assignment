Setup Instructions
Clone the Repository :

      git clone <repository-url>
      cd assignment
      cd admin

Build and Run Docker Containers, This command will build the Docker images and start the Django, MySQL, and MongoDB containers.

      docker-compose up --build
      

Access Django APIs on swagger documentations via
   
     http://127.0.0.1:8000/doc/

Stopping the Containers, To stop the containers, use the following command:
   
       docker-compose down

Project Structure

      backend: Django project files.
      mysql: MySQL database container.
      mongodb: MongoDB database container.

Additional Notes

      The Django development server will be accessible at http://localhost:8000/.
