
# Django Auto Container


This repository contains a GitHub Actions workflow that automatically builds a Django-based container application and pushes it to Docker Hub using Buildpacks.

The purpose of this repo is to help Django devs use containers without having to learn Docker. 

## Getting Started

### 1. Copy the Build Container Workflow this Repository

Navigate to your Django project directory and copy the build container workflow from this repository.

```bash
mkdir -p .github/workflows
curl https://raw.githubusercontent.com/codingforentrepreneurs/django-auto-container/main/.github/workflows/build-container.yaml > .github/workflows/build-container.yaml
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
- project.toml
- requirements.txt

This files are needed to ensure the auto-container workflow runs correctly, review `src/` for working examples or use the following samples:

`project.toml`
```toml
[[build.env]]
name = "DISABLE_COLLECTSTATIC"
value = "1"

[[build.env]]
name =  "GOOGLE_RUNTIME_VERSION"
value = "3.11.7"

[[build.env]]
name = "GOOGLE_ENTRYPOINT"
value = "gunicorn cfehome.wsgi:application --bind \"0.0.0.0:$PORT\""
```
The `GOOGLE_ENTRYPOINT` is the command that will be run when the container is started. In this case, it's the production version of running `python manage.py runserver` but with `gunicorn` instead of `runserver`.


`requirements.txt`
```
Django
gunicorn
```
`gunicorn` is required as it's what is recommended to run Django in production.

### 4. Push

Push your code to GitHub and watch the magic happen. You can view the workflow in the "Actions" tab of your GitHub repo.

### 5. Run

If you have Docker installed locally, you can run your application with:

```
docker run -e PORT=8888 -p 8888:8888 <your-docker-hub-username>/<your-docker-hub-repo>:<your-docker-hub-image-tag>
```
Open [http://localhost:8888](http://localhost:8888) to view your application.

If you don't have Docker installed locally, you can run your application on any container host such as:

- Kubernetes
- Knative
- Hashicorp Nomad
- Any managed container hosting service