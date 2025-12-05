# Render Environment Variables

When deploying to Render, you need to set the following environment variables in your Render dashboard:

## Required Environment Variables

| Variable Name | Description | Example Value |
|---------------|-------------|---------------|
| `TWILIO_ACCOUNT_SID` | Your Twilio Account SID | ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| `TWILIO_AUTH_TOKEN` | Your Twilio Auth Token | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| `TWILIO_FROM_PHONE` | Your Twilio phone number | +12345678901 |
| `SECRET_KEY` | Django secret key (generate a secure one) | your-super-secret-key-here |
| `DATABASE_URL` | PostgreSQL database URL (provided by Render) | postgres://user:pass@host:port/dbname |
| `RENDER` | Flag to indicate Render deployment | true |
| `DEBUG` | Django debug mode | false |
| `EMAIL_HOST_USER` | Your email address for sending emails | your-email@gmail.com |
| `EMAIL_HOST_PASSWORD` | Your email password or app password | your-email-password |

## Optional Environment Variables

| Variable Name | Description | Example Value |
|---------------|-------------|---------------|
| `DJANGO_SETTINGS_MODULE` | Django settings module | credit.settings |

## How to Set Environment Variables in Render

1. Go to your Render dashboard
2. Select your web service
3. Click on "Environment" in the sidebar
4. Add each variable with its corresponding value
5. Click "Save Changes"

## Security Notes

- Never commit secrets to your repository
- Always use environment variables for sensitive information
- Generate a new SECRET_KEY for production
- Use app passwords for Gmail instead of your regular password