Setup Instructions
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd <repository-folder>
2. Build and Run Docker Containers
bash
Copy code
docker-compose up --build
This command will build the Docker images and start the Django, MySQL, and MongoDB containers.

3. Create Django Superuser (Optional)
If you want to access the Django admin interface, you can create a superuser:

bash
Copy code
docker-compose exec backend python manage.py createsuperuser
Follow the prompts to set up a superuser account.

4. Access Django Admin
Visit http://localhost:8000/admin/ to access the Django admin interface.

5. Access Django API
Visit http://localhost:8000/api/ to access the Django API.

6. Stopping the Containers
To stop the containers, use the following command:

bash
Copy code
docker-compose down
Project Structure
backend: Django project files.
mysql: MySQL database container.
mongodb: MongoDB database container.
Additional Notes
The Django development server will be accessible at http://localhost:8000/.
