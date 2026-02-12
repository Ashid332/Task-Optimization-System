# Deployment Guide

This guide explains how to deploy the Task Optimization System to various platforms.

## Local Development

### Prerequisites
- Python 3.9+
- pip or conda
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/Ashid332/Task-Optimization-System.git
cd Task-Optimization-System

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run application
python app.py
```

Application runs on `http://localhost:5000`

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed
- Git repository

### Steps

1. **Login to Heroku**
```bash
heroku login
```

2. **Create Heroku app**
```bash
heroku create your-app-name
```

3. **Add PostgreSQL addon**
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. **Set environment variables**
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DATABASE_URL=<auto-set by addon>
```

5. **Deploy**
```bash
git push heroku main
```

6. **Check logs**
```bash
heroku logs --tail
```

7. **Visit application**
```bash
heroku open
```

### Heroku Configuration

- **Procfile**: Specifies how to run the application
- **runtime.txt**: Specifies Python version (3.9.16)
- **requirements.txt**: Python dependencies

## Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Build & Run
```bash
# Build image
docker build -t task-optimizer:latest .

# Run container
docker run -p 5000:5000 task-optimizer:latest
```

## AWS Deployment (Elastic Beanstalk)

### Prerequisites
- AWS account
- AWS CLI
- EB CLI

### Steps
```bash
# Initialize EB
eb init -p python-3.9 task-optimizer

# Create environment
eb create task-optimizer-env

# Deploy
eb deploy

# Open application
eb open
```

## Google Cloud Deployment (App Engine)

### app.yaml
```yaml
runtime: python39

env: standard

entrypoint: gunicorn -b :$PORT app:app
```

### Deploy
```bash
gcloud app deploy
```

## Performance Optimization

### Production Settings
- Set `FLASK_ENV=production`
- Disable `DEBUG=False`
- Use `gunicorn` instead of Flask dev server
- Configure proper logging
- Enable caching

### Scaling
- **Vertical**: Increase dyno size on Heroku
- **Horizontal**: Use multiple worker processes
  ```bash
  heroku ps:scale web=2  # Scale to 2 dynos
  ```

## Database Setup

### PostgreSQL
```bash
# Connection string format
postgresql://user:password@host:port/database
```

### Database Migrations (if using SQLAlchemy)
```bash
flask db upgrade
```

## Monitoring & Logging

### Heroku Logs
```bash
heroku logs --tail
heroku logs --dyno web
```

### Application Monitoring
- Monitor endpoint: `/api/health`
- Status endpoint: `/api/metrics`
- Configure alerts for error rates

## Security Checklist

- [ ] Set strong `SECRET_KEY`
- [ ] Use HTTPS (auto-enabled on Heroku)
- [ ] Store sensitive keys in environment variables
- [ ] Enable database encryption
- [ ] Configure firewall rules
- [ ] Enable audit logging
- [ ] Regular security updates
- [ ] Use API authentication tokens

## Troubleshooting

### Application won't start
```bash
heroku logs --tail
# Check for missing dependencies
# Verify environment variables
```

### Database connection errors
```bash
heroku config  # Check DATABASE_URL
heroku pg:info  # Check PostgreSQL status
```

### Memory issues
```bash
heroku ps
heroku restart  # Restart dynos
```

## Backup & Recovery

### Database Backup
```bash
heroku pg:backups capture
heroku pg:backups download
```

### Restore from Backup
```bash
heroku pg:backups restore b001 DATABASE_URL
```

## Cost Optimization

### Heroku
- Free tier: Limited to hobby-dev database
- Standard-0: $7/month per dyno
- Production: Use 2+ dynos for high availability
- Database: Evaluate data size needs

## CI/CD Pipeline

### GitHub Actions Example
```yaml
name: Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        run: git push https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/${{ secrets.HEROKU_APP_NAME }}.git main
```

## Maintenance

### Regular Tasks
- Monitor application logs
- Check database size
- Update dependencies
- Security patches
- Performance monitoring
- Backup verification

### Version Management
- Keep Python updated
- Test upgrades in staging
- Update dependencies monthly
- Document breaking changes

## Production Readiness Checklist

- [ ] Environment variables configured
- [ ] Database setup and initialized
- [ ] Logging configured
- [ ] Error handling tested
- [ ] Performance optimized
- [ ] Security measures in place
- [ ] Monitoring and alerts enabled
- [ ] Backup strategy implemented
- [ ] Disaster recovery plan
- [ ] Documentation complete

---

**Last Updated**: 2024
**Supported Platforms**: Heroku, AWS, Google Cloud, Docker
**Python Version**: 3.9+
