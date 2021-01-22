sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gun_hello.py  /etc/gunicorn.d/gun_hello.py
sudo ln -sf /home/box/web/etc/gun_task.py /etc/gunicorn.d/task.py
sudo /etc/init.d/gunicorn restart