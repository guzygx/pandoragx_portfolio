#!/bin/bash
trap terminate SIGINT
terminate(){
    pkill -SIGINT -P $$
    exit
}

npx @tailwindcss/cli -i ./app/static/_css/style.css -o ./app/static/_prebuild/_css/style.css --watch=always &
vite &
flask --app app.py run --debug

wait
