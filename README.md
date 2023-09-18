
---

# Django Social Auth Project: django_social_auth

This is a Django project that demonstrates how to implement social authentication using the "social_auth" library. The project includes integration with various social authentication providers such as Google, Github, Facebook, and Twitter.

## Getting Started

Follow these steps to set up the project and configure social authentication providers.

### Prerequisites

- Python (3.6 or higher)
- Django (3.0 or higher)
- `social-auth-app-django` library
- Development environment with a database (e.g., SQLite for local development)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/django_social_auth.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django_social_auth
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

#### Social Authentication Credentials

To enable social authentication, you need to obtain credentials (Client ID and Client Secret) from various social authentication providers. Here's how to do it for each provider:

##### Google

1. Go to the [Google Developers Console](https://console.developers.google.com/).

2. Create a new project or select an existing one.

3. In the left sidebar, navigate to "Credentials."

4. Click on "Create Credentials" and select "OAuth client ID."

5. Choose "Web application" as the application type.

6. Set the authorized JavaScript origins and redirect URIs for your development environment. For local development, you can use `http://localhost:8000` for both.

7. Note the generated Client ID and Client Secret.

##### Github

1. Go to [GitHub Developer Settings](https://github.com/settings/developers).

2. Click on "New OAuth App."

3. Fill in the required details, including the callback URL for your local development environment (e.g., `http://localhost:8000/accounts/github/login/callback/`).

4. Note the generated Client ID and Client Secret.

##### Facebook

1. Go to the [Facebook Developers](https://developers.facebook.com/) portal.

2. Create a new app and select "For Everything Else."

3. In the app dashboard, go to "Settings" > "Basic."

4. Note the App ID and App Secret.

##### Twitter

1. Go to the [Twitter Developer Portal](https://developer.twitter.com/en/apps).

2. Create a new Twitter Developer App.

3. Note the generated API Key (Client ID) and API Secret Key (Client Secret).

#### Project Settings

In your Django project's settings.py file, configure the social authentication providers using the obtained credentials:

```python
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your Google Client ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Your Google Client Secret'

SOCIAL_AUTH_GITHUB_KEY = 'Your GitHub Client ID'
SOCIAL_AUTH_GITHUB_SECRET = 'Your GitHub Client Secret'

SOCIAL_AUTH_FACEBOOK_KEY = 'Your Facebook App ID'
SOCIAL_AUTH_FACEBOOK_SECRET = 'Your Facebook App Secret'

SOCIAL_AUTH_TWITTER_KEY = 'Your Twitter API Key'
SOCIAL_AUTH_TWITTER_SECRET = 'Your Twitter API Secret Key'
```

### Usage

The project includes an "accounts" app that provides API endpoints for user operations. You can use tools like [Postman](https://www.postman.com/) to interact with the API.

#### User Registration

Use the following API endpoint to register a new user:

- **Endpoint**: `/api/register/`
- **Method**: POST
- **Parameters**:
  - `username` (string)
  - `email` (string)
  - `password` (string)

#### User Login

Use the following API endpoint to log in:

- **Endpoint**: `/api/login/`
- **Method**: POST
- **Parameters**:
  - `username` (string)
  - `password` (string)

#### User Logout

Use the following API endpoint to log out:

- **Endpoint**: `/api/logout/`
- **Method**: POST

#### Password Reset

Use the following API endpoint to initiate a password reset:

- **Endpoint**: `/api/password-reset/`
- **Method**: POST
- **Parameters**:
  - `email` (string)

#### Forgot Password

Use the following API endpoint to request a password reset email:

- **Endpoint**: `/api/forgot-password/`
- **Method**: POST
- **Parameters**:
  - `email` (string)

#### Restore Password

To restore a password after receiving a password reset email, use the following API endpoint:

- **Endpoint**: `/api/restore-password/<uidb64>/<token>/`
- **Method**: POST
- **Parameters**:
  - `uidb64` (string) - User ID in base64 format
  - `token` (string) - Token received in the password reset email

#### Account Activation

Use the following API endpoint to activate a user account:

- **Endpoint**: `/api/activate/<code>/`
- **Method**: POST
- **Parameters**:
  - `code` (string) - Activation code received in the email

#### Resend Activation Code

If the activation email is not received, you can request to resend the activation code using the following API endpoint:

- **Endpoint**: `/api/resent-activation-code/`
- **Method**: POST

#### Deactivate Account

To deactivate a user account, use the following API endpoint:

- **Endpoint**: `/api/deactivate/`
- **Method**: POST

---

### Contributions

Contributions to improve and expand this project are welcome. Feel free to create issues or submit pull requests.

---

Thank You

---
