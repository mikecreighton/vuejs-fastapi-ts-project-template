# Vue.js FastAPI TypeScript Project Template

This is a simple project template for a Vue.js (TypeScript) and FastAPI project, set up to be a monorepo. It is intended for fast prototyping of web apps that use LLMs.

> [!IMPORTANT]
> This project is opinionated and uses OpenRouter's API instead of OpenAI's. However, because the OpenRouter API is compatible with the OpenAI API, we're able to use the OpenAI Python SDK with it.

## Project Structure

The project is divided into two main components:

1. Backend (Python/FastAPI)
2. Frontend (Vue.js/Vite/TypeScript/Tailwind CSS)

## Backend

The backend includes boilerplate libraries for interacting with remote LLM models and serving up static or templated pages as needed.

### Tech stack:

- Python
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI SDK](https://github.com/openai/openai-python)
- [Jinja2](https://jinja.palletsprojects.com/en/stable/)
- [Pydantic](https://docs.pydantic.dev/)
- [Gunicorn](https://gunicorn.org/) (for the web server and its process manager) + [Uvicorn](https://www.uvicorn.org/) (as async workers)

## Frontend

The frontend is a Vue.js application that provides the user interface/ It's located in the `frontend` directory and uses Vite as the build tool.

### Tech stack:

- [Vue.js](https://vuejs.org/)
- [Vite](https://vite.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [shadcn-vue](https://www.shadcn-vue.com/)
- [GSAP](https://gsap.com/)

> [!IMPORTANT]
> Because this project template is intended for prototyping, it uses [shadcn-vue](https://www.shadcn-vue.com/) for the UI components so that we can quickly put together UI / UX. Shadcn-vue isn't a package, so you need to install components individually via the command line. Be sure to view their docs for more information. But ultimately, installation of components is very easy, usually with a command that looks like `npx shadcn-vue@latest add [component]`.

## Creating a new project

This is a template project, so you'll want to start by clicking the "Use this template" button in the upper-right and creating a new repository from it.

1. Create a new repository from this template.

2. Set up the backend:
   ```
   cd backend
   python -m venv .venv # Create a virtual environment
   source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Copy the `backend/.env.template` file to a new file called `.env`. Update the `.env` file with your OpenRouter API key.

4. Set up the frontend:
   ```
   cd frontend
   npm install
   ```

5. Copy the `frontend/.env.template` file to a new file called `.env`. For local development, you can keep the default value for `VITE_API_URL`. This will be overridden by CapRover at runtime if you deploy publicly. The `VITE_API_URL` refers to the backend server URL.

## Running the Application

1. Start the backend server:
   ```
   cd backend
   source .venv/bin/activate
   python app.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173` (or the URL provided by Vite).


## Intended Deployment Infrastructure

This is ready to be deployed to a VPS (such as DigitalOcean's [Droplets](https://www.digitalocean.com/products/droplets)) using [CapRover](https://caprover.com/).

You'll see two [Captain definition files](https://caprover.com/docs/captain-definition-file.html) for deployment:

- `captain-definition-backend`: For deploying the backend
- `captain-definition-frontend`: For deploying the frontend

> [!NOTE]
> The frontend uses an accompanying `nginx.conf` file (in this project's root folder) for serving the frontend and respecting dynamic routing with Vue Router. 

> [!IMPORTANT]
> Because CapRover defaults to a definition file called `captain-definition`, you'll need to manually change that at the bottom of your app's Deployment tab. It's a field called "captain-definition Relative Path".

## Other Deployment Notes

The frontend doesn't have any default favicons or other related icons (like the ones specified in the `site.webmanifest` file). You'll need to add those manually. They should be placed in the `frontend/public` directory. Take a look at the `frontend/index.html` file for the default names of the files.

## Cursor IDE

I use the Cursor IDE for all my development. You'll find a `.cursorrules` file in the root of the project.

## License

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2024-present, Mike Creighton
