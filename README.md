# Credit Scoring Backend

This is a Django backend application for credit scoring and loan processing.

## Project Structure

```
.
├── manage.py
├── requirements.txt
├── build.sh
├── railway.json
├── .gitignore
├── README.md
├── credit/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── tests.py
│   ├── beneficiary_json.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   └── templates/
│       └── case2_add_loan.html
└── templates/
    ├── base.html
    ├── login.html
    ├── home.html
    ├── beneficiary_register.html
    ├── beneficiary_verify_otp.html
    ├── beneficiary_home.html
    ├── beneficiary_edit.html
    ├── beneficiary_documents.html
    ├── beneficiary_apply_loan.html
    ├── beneficiary_loan_submitted.html
    ├── beneficiary_score.html
    ├── officer_upload.html
    ├── officer_beneficiaries.html
    ├── officer_beneficiary_details.html
    ├── officer_beneficiary_documents.html
    ├── officer_dashboard.html
    ├── officer_ai_explanation.html
    ├── case_details.html
    ├── case1_input.html
    ├── case1_result.html
    ├── case2_add_loan.html
    ├── income_scoring_result.html
    └── officer_loan_applications.html
```

## Environment Variables

For deployment, set the following environment variables:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to "False" for production
- `DATABASE_URL` - PostgreSQL database URL
- `RAILWAY` - Set to "true" when deploying on Railway
- `RENDER` - Set to "true" when deploying on Render
- `TWILIO_ACCOUNT_SID` - Twilio account SID
- `TWILIO_AUTH_TOKEN` - Twilio auth token
- `TWILIO_FROM_PHONE` - Twilio phone number
- `EMAIL_HOST_USER` - Email address for sending notifications
- `EMAIL_HOST_PASSWORD` - Email password or app password

## Deployment

### Railway

1. Connect your GitHub repository to Railway
2. Set the environment variables
3. Railway will automatically detect the Django app and deploy it

### Render

1. Connect your GitHub repository to Render
2. Set the build command to `./build.sh`
3. Set the start command to `gunicorn credit.wsgi:application`
4. Set the environment variables

## Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```