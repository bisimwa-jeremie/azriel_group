## Installation

1. Cloner le dépôt :
   ```bash
   git clone git@github.com:bisimwa-jeremie/azriel_group.git
   cd AZRIEL_GROUP


Voici un guide complet pour intégrer Tailwind CSS avec Webpack dans votre projet Django avancé, en utilisant python-webpack (ou plus précisément django-webpack-loader), avec une configuration optimisée pour le déploiement et la collaboration via GitHub.
1. Installation
— Python and Nodejs should be installed into your system.

2. Setting up django project and application
— Create the virtual enviroment with: python -m venv .venv
— Activate the virtual enviroment: source .venv/bin/activate
— Install the django package: pip install django
— Create a django project: django-admin startproject djangotailwind
— Create django application: cd djangotailwind and python manage.py startapp blog

3. Activate django app and setup static,template directory
— Add the templates and static directory inside blog application
— Inside `settings.py` file of djangotailwind project, add

INSTALLED_APPS = [
 ‘blog’, #updated
]

4. Installing Tailwind CSS
— Install tailwind and @tailwindcss/cli via npm or yarn
npm install tailwindcss @tailwindcss/cli

5. Add tailwind directives
— Create a style.css as static/css/style.css and add

@import “tailwindcss” ; 

while using tailwind version 4 , there is no need to create tailwind configuration file just like we did on v3 as tailwind.config.js. tailwind automatically detect html file and it’s content. you can add own custom styling directly on style.css file.

6. Build Tailwind CSS
— Use the Tailwind CLI to build your CSS

npx @tailwindcss/cli -i blog/static/css/style.css -o blog/static/css/tailwind.css

To run above command as script, add it inside package.json file as

{
  "name": "djangotailwind",
  "version": "1.0.0",
  "description": "this is django tailwind",
  "license": "ISC",
  "author": "",
  "type": "commonjs",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "watch": "npx @tailwindcss/cli -i blog/static/css/style.css -o blog/static/css/tailwind.css --minify --watch"
  },
  "dependencies": {
    "@tailwindcss/cli": "^4.1.4",
    "tailwindcss": "^4.1.4"
  }
}

Now, you can run as
`npm run watch` # which auto generate styling into tailwind.css.

7. Create html files
— Create home.html file inside templates as blog/templates/home.html

{% load static %}
<!DOCTYPE html>
<html lang="en">
 <head>
    <title>Django Tailwind</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="{% static 'css/tailwind.css' %}">
 </head>

 <body class="bg-gray-50 font-serif leading-normal tracking-normal">
  <div class="container mx-auto">
   <section class="flex items-center justify-center h-screen">
    <h1 class="text-5xl">Django + Tailwind = ❤️</h1>
   </section>
  </div>
 </body>
</html>

et en cas d'erreurs, il y a autres choses de nécéssaire à installer:
   -python -m pip install Pillow : en cas d'une erreur de migrations après modifications du models