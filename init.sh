sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gun_hello.py  /etc/gunicorn.d/gun_hello.py
sudo ln -sf /home/box/web/etc/gun_task.py /etc/gunicorn.d/task.py
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepik_web;"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
python3 /home/box/web/ask/manage.py syncdb




