
# Django Auto Container


This repository contains a GitHub Actions workflow that automatically builds a Django-based container application and pushes it to Docker Hub using Buildpacks.

The purpose of this repo is to help Django devs use containers without having to learn Docker. 

## Getting Started

### 1. Copy the Build Container Workflow this Repository

Navigate to your Django project directory and copy the build container workflow from this repository.

```bash
curl https://raw.githubusercontent.com/codingforentrepreneurs/django-auto-container/main/.github/workflows/build-container.yml > .github/workflows/build-container.yml
```

### 2. Github Actions Secrets
In your GitHub Repo, add the following Secrets:
#### Required Secrets:
If you do not include these secrets, the container will be built but not hosted anywhere.

- `DOCKER_HUB_USERNAME`: Your Docker Hub username.
- `DOCKER_HUB_TOKEN`: Your Docker Hub access token; create a new token [here](https://hub.docker.com/settings/security).


#### Recommended Secrets:

These secrets are highly recommended to add for your specific project.
- `DOCKER_HUB_REPO`: The Docker repository to push to, in the format `username/repository`. Defaults to the format of your GitHub repo if not set -- this is where you will store your container.
- `BASE_DIR`: The default Django project location is `src/` as you see in this repo. If you have a different location, you can set it here.

#### Optional Secrets:
If you need more advanced usage, consider adding these secrets to modify how your project works.
- `BUILDPACK_BUILDER`: The buildpack builder to use. Defaults to 'heroku/buildpacks:22' if not set. Review various Heroku buildpacks [here](https://devcenter.heroku.com/articles/stack#stack-support-details)
- `DOCKER_HUB_IMAGE_TAG`: The tag to use for the Docker image. Defaults to the commit SHA (recommended) or you can set this value yourself.

### 3. Required Files

In my `BASE_DIR` (defaults to `src/`), I have the following files:
- requirements.txt
- runtime.txt
- Procfile

This files are needed to ensure the project runs correctly, review `src/` for working examples or use the following samples:

`Profile`
```
web: gunicorn myproject.wsgi --log-file -
```

`runtime.txt`
```
python-3.12.1
```

`requirements.txt`
```
Django
gunicorn
```
`gunicorn` is required as it's what is recommended to run Django in production.

