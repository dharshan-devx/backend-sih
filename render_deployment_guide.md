# Render Deployment Workflow Guide

## Prerequisites
1. A GitHub account
2. A Render account
3. A PostgreSQL database (can be provisioned on Render)

## Step-by-Step Deployment Process

### 1. Push Project to GitHub
1. Create a new repository on GitHub
2. Push your cleaned Django project to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Render deployment"
   git remote add origin https://github.com/your-username/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

### 2. Create a New Render Web Service
1. Log in to your Render account
2. Click "New" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: Your choice
   - Runtime: Python 3
   - Build command: `./build.sh`
   - Start command: `gunicorn credit.wsgi:application`
   - Instance type: Free or paid as per your requirement

### 3. Configure Environment Variables
In the Render dashboard, add the following environment variables:
- `DB_NAME`: Your PostgreSQL database name
- `DB_USER`: Your PostgreSQL username
- `DB_PASSWORD`: Your PostgreSQL password
- `DB_HOST`: Your PostgreSQL host
- `DB_PORT`: Your PostgreSQL port (usually 5432)
- `DJANGO_SETTINGS_MODULE`: credit.settings
- `SECRET_KEY`: A secure secret key for production
- `DEBUG`: False

### 4. Add PostgreSQL Database (Optional)
1. In Render, click "New" and select "PostgreSQL"
2. Configure the database settings
3. Once created, Render will provide connection details
4. Update your environment variables with these details

### 5. Deploy
1. Click "Create Web Service"
2. Render will automatically start the build and deployment process
3. Monitor the logs for any issues

### 6. Connecting Frontend
To connect your frontend application:
1. Set the axios/baseURL to your Render app URL (e.g., https://your-app.onrender.com)
2. Ensure CORS is properly configured in your Django settings (already done in this project)
3. Test API endpoints from your frontend

## Troubleshooting Tips
- Check logs in the Render dashboard for any deployment errors
- Ensure all environment variables are correctly set
- Make sure your build.sh script has Unix line endings (LF) not Windows (CRLF)
- If you encounter static file issues, ensure DEBUG=False and STATIC_ROOT is properly configured