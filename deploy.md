# Deployment

This work-in-progress document outlines the steps necessary to deploy the site.

- [Deployment](#deployment)
  - [DigitalOcean App Platform](#digitalocean-app-platform)
    - [Example configuration](#example-configuration)
    - [Static files](#static-files)
    - [Environment variables](#environment-variables)
  - [Migrate, create a superuser, and collect static](#migrate-create-a-superuser-and-collect-static)
  - [Scaffold initial content](#scaffold-initial-content)
  - [Data prep/import](#data-prepimport)


## DigitalOcean App Platform

We are using the DigitalOcean App Platform to auto-deploy and manage the site. 

Set up the site by following the steps below. The order of steps matters. So, be careful about jumping ahead before completing any given step.

1. Create a Storage Bucket for site static media and file uploads
2. Create a new App with the following considerations during the creation process
   1. Make sure to add a database
   2. Deployment is triggered when changes are merged to the `main` branch
   3. Configure all necessary [environment variables](#environment-variables) while creating the App
   4. Edit the App Info with the following settings
      1. Give the app a meaningful name
      2. Set the Region to San Francisco, so it is closer to most WesternFriend community
3. configure a domain (or subdomain) to point to the deployed app

### Example configuration

Below is an example configuration for our staging setup.

```yaml
App
- wf-website-staging
   - wf-website: Web Service / Dockerfile
   - db: Dev Database

Environment Variables
- Global: 0 environment variables
   - wf-website: 9 environment variables

Info
   - Name: wf-website-staging
   - Region: San Francisco

Project: Western Friend
```

### Static files

We need a space to store static files. For that, we will use DO Spaces.

1. Create a Spaces Bucket
2. Edit the CORS settings with the following values

```yaml
Origin: https://<domain.TLD>
Allowed Methods: GET
Allowed Headers:
- Access-Control-Allow-Origin
- Referer
Access Control Max Age: 600
```

### Environment variables

Environment variables are added through the DigitalOcean App Platform configuration for the specific app. Make sure to define the following environment variables with corresponding values. Also, make sure to quote all of the environment variable values, to avoid potential pitfalls or unexpected behavior.

- `DJANGO_CORS_ALLOWED_ORIGINS` - each origin should begin with a protocol, e.g., `"https://..."`
- `DJANGO_ALLOWED_HOSTS` - each allowed host needs only the domain (and subdomain if relevant), no protocol
- `DJANGO_CSRF_TRUSTED_ORIGINS`- each origin should begin with a protocol, e.g., `"https://..."`
- `DJANGO_SECRET_KEY` - [random generated key](https://stackoverflow.com/a/67423892)
- `DEBUG` - "True" or "False", should be "False" for production
- `USE_SPACES` - "True" or "False", whether to use DO Spaces for static files. In this case, use "True".
- `AWS_S3_REGION_NAME` - use the region name selected when setting up the DO Spaces Storage Bucket
- `AWS_STORAGE_BUCKET_NAME` - the name of the DO Storage Bucket for static files


## Migrate, create a superuser, and collect static

Access the app console via DigitalOcean admin UI, and run the following commands.

1. run migrations
    - `python manage.py migrate`
2. create a superuser
   - `python manage.py createsuperuser`
3. collect static files
   - `python manage.py collectstatic --no-input`

At this point, make sure to check the DigitalOcean Space where static files should be stored, to ensure the app has access to the storage space.

## Scaffold initial content

We have a pre-defined content tree for the primary website structure. To save some time, run the following command in the DO App console to scaffold the initial content tree.

```py
python manage.py scaffold_initial_content
```

## Data prep/import

Refer to the [content migration](CONTENT_MIGRATION.md) guide for further details about preparing data for import. Once the data have been prepared, use the following steps to import them to the online website.

1. copy all import files (CSV format) to the DO Spaces bucket for import data
2. run the import commands via the DO App console, using the bucket location (HTTPS) as a target
