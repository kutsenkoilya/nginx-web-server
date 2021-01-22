# nginx-web-server

Use <sudo nginx -t> for test runs and detailed error output <br>

How to run: <br>

sudo rm -r /home/box/web
git clone https://github.com/kutsenkoilya/nginx-web-server.git /home/box/web
bash /home/box/web/init.sh

cd /home/box/web/ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
cd ../../home/box/web
gunicorn --bind='0.0.0.0:8080' hello:application