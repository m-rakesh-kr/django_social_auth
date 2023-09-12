# Features and Dependencies of `social-auth-app-django`

```markdown
# Django Social Authentication Example

This is an example Django project that demonstrates how to implement social authentication using the `social-auth-app-django` library. Social authentication allows users to sign in to your application using their social media accounts, such as Google, Facebook, GitHub, Twitter, etc.

## Features

- User registration and login with social media accounts (Google, Facebook, GitHub, Twitter, etc.).
- Password reset and account activation via email.
- User profile management.
- Deactivate user accounts.
- Integration with Django Rest Framework for API endpoints.
- Integration with Celery for asynchronous task processing.

## Requirements/Dependencies

- Python 3.7+
- Django 4.0+
- social-auth-app-django 5.0.0
- social-auth-core 4.3.0
- PostgreSQL (or any other compatible database)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/django-social-auth.git
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS**:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:

   Create a `.env` file in the project root directory and configure the following environment variables:

   ```
   SECRET_KEY=your_secret_key
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASS=your_database_password
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_email_password
   GITHUB_CLIENT_ID=your_github_client_id
   GITHUB_CLIENT_SECRET=your_github_client_secret
   FACEBOOK_CLIENT_ID=your_facebook_client_id
   FACEBOOK_CLIENT_SECRET=your_facebook_client_secret
   TWITTER_CLIENT_ID=your_twitter_client_id
   TWITTER_CLIENT_SECRET=your_twitter_client_secret
   GOOGLE_OAUTH2_CLIENT_ID=your_google_oauth2_client_id
   GOOGLE_OAUTH2_CLIENT_SECRET=your_google_oauth2_client_secret
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000/`

## Usage

- Visit the registration page to create a new user account or use social authentication to sign in.
- Access the account settings to manage your profile and change the password.
- Use the provided API endpoints for advanced integration.


---
# Thank You!

---