#!/bin/bash
trap terminate SIGINT
terminate(){
    pkill -SIGINT -P $$
    exit
}

npx @tailwindcss/cli -i ./app/static/_css/style.css -o ./app/static/_css/prebuild/style.css --watch=always > logs/tailwind.txt &
vite > logs/vite.txt &
flask --app app.py run --debug > logs/flask.txt

wait
