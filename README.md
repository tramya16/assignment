Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd <repository-folder>

2. Build and Run Docker Containers
docker-compose up --build
This command will build the Docker images and start the Django, MySQL, and MongoDB containers.

3. Access Django API
Visit http://localhost:8000/api/ to access the Django API.

4. Stopping the Containers
To stop the containers, use the following command:
docker-compose down

Project Structure
backend: Django project files.
mysql: MySQL database container.
mongodb: MongoDB database container.
Additional Notes
The Django development server will be accessible at http://localhost:8000/.
