
# TASK APPLICATION

A robust, yet user-friendly task management system is provided out of the box for personal and collaborative use via this Django project The app has been built using a minimalistic and functional design, thus making it very easy for users to cope with their newly received task lists from home. This method helps you organize what needs to be done and manage them in a scalable way, no matter if it's maintaining the series of tasks on daily basis or handling long term project.

## Description
This project is a web application designed for task management with user authentication, built using Django for the backend and a custom HTML/CSS frontend. Users can sign up and log in to create and manage their tasks. The application features a responsive design with Bootstrap modals for adding, editing, and deleting tasks, and includes dynamic message handling for user feedback. On the profile page, users can view their tasks, filter them by status (Active, Pending, Completed), and update task details. The Django backend handles user authentication, task management, and filtering, while the frontend provides a user-friendly interface with animations and responsive design. Overall, the project combines robust backend functionality with an intuitive and interactive user experience.

## Features
- Task Management
- User Authentication
- Add Task
- Edit Task
- Delete Task
- Filter and Sort Tasks
- Responsive Design
- User-Friendly Interface


## Installation

 Install Task Application

1. Clone this repository to your local machine:

```bash
  git clone https://github.com/Muhammedrazikkm/TO-DO.git

```
2. Navigate to the project directory:
 ```bash
  cd myProject
```
3. Set Up a Virtual Environment:
 ```bash
  python -m venv myVenv
```
4. Activate Virtual Environment:
 ```bash
  source myVenv/Scripts/activate
```
5. Install Django:
 ```bash
  pip install django
```
6. Set Up the Database:
 ```bash
  python manage.py migrate
```
7. Create a Superuser (Optional):
 ```bash
  python manage.py createsuperuser
```
8. Start the development server:
 ```bash
  python manage.py runserver
```
9. Open your browser and navigate to `http://localhost:8000/signup` to view the application.

## Appendix

- Code Structure

The project follows a simple and organized structure to maintain readability and ease of use. Below is a high-level overview of the code structure.

project-root/  
├── myProject/  
│   ├── myapps/  
│   │   ├── __pycache__/               // Compiled Python files   
│   │   ├── migrations/                // Database migrations  
│   │   ├── static/                    // Static files  
│   │   │   ├── js/                    // JavaScript files  
│   │   │   │   ├── script.js          // Main JavaScript file  
│   │   │   ├── css/                   // CSS files  
│   │   │   │   ├── profile.css        // CSS for profile page  
│   │   │   │   ├── style.css          // General styling    
│   │   │   ├── image/                 // Image files  
│   │   ├── templates/                 // HTML templates  
│   │   │   ├── registration/          // Registration-related templates  
│   │   │   │   ├── signup.html        // Sign-up page template  
│   │   │   │   ├── profile.html       // Profile page template  
│   │   ├── __init__.py                // Initialization file for the app  
│   │   ├── admin.py                   // Admin configuration  
│   │   ├── apps.py                    // App configuration  
│   │   ├── forms.py                   // Form classes  
│   │   ├── models.py                  // Database models  
│   │   ├── tests.py                   // Unit tests  
│   │   ├── urls.py                    // URL routing  
│   │   ├── views.py                   // View functions  
│   ├── myProject/         
│   │   ├── __pycache__/               // Compiled Python files     
│   │   ├── init.py                    // Initialization file for the app  
│   │   ├── asgi.py                    // ASGI configuration   
│   │   ├── settings.py                // Project settings  
│   │   ├── urls.py                    // URL routing for the project    
│   │   ├── wsgi.py                    // WSGI configuration  
│   ├── db.sqlite3                     // SQLite database file  
├── myVenv/                            // Python virtual environment  
├── manage.py                          // Django's command-line utility  

## Contributing

Contributions are always welcome!

- Create a new branch for your feature: ` git checkout -b feature/new-feature`.

- Commit your changes:                                    `git commit -m`  'Add new feature'.

- Push to the branch: `git push origin feature/new-feature`.

- Open a pull request.


## Screenshots
![signup](https://github.com/user-attachments/assets/81dce16a-ff56-4725-893e-6c3ff3002461)

![login](https://github.com/user-attachments/assets/2d341031-1979-4dae-8a5a-e4b976817b91)

![profile page](https://github.com/user-attachments/assets/ca554279-f64f-4966-ab74-be92814230a7)

![task addition](https://github.com/user-attachments/assets/eaaf17e2-5733-484c-9154-6282194ba07e)

![status](https://github.com/user-attachments/assets/fd7fc31f-bbe8-456f-b3d7-59d92e8e7ca0)

![edit](https://github.com/user-attachments/assets/c9b2130b-fbca-4f21-b2da-0f1ba5a1047b)

![delete](https://github.com/user-attachments/assets/73ecd1e2-2bff-4927-b1a7-ca8b490cc7ac)

![logout](https://github.com/user-attachments/assets/d3e33314-9fb8-41d3-8744-4afa728b5046)



## 🛠 Skills

- Django
- Python
- CSS
- HTML
- Javascript

## Authors

- [@Muhammed Razik](https://www.github.com/Muhammedrazikkm)


## Feedback

If you have any feedback, please reach out to us at muhdrazikkm@gmail.com


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://muhammedrazikportfolio.netlify.app/)  
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/muhammed-razik-b5b266245)  
[![Whatsapp](https://img.shields.io/badge/Whatsapp-1DA1F2?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.link/dgng9j)


## Support

For support,muhdrazikkm@gmail.com 


## Acknowledgements

 

- Django Community: https://www.djangoproject.com/community/

- Documentation: https://docs.djangoproject.com/en/5.1/





Web Development Community: https://stackoverflow.com

Thank you all for your support and contributions.





