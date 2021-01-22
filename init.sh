sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ask/ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
cd /home/box/web
gunicorn --bind='0.0.0.0:8080' hello:application
