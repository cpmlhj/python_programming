# 创建 Django环境

$ django-admin startproject <name>
$ cd <name>

$ python manage.py startapp <app_name>



# 建立默认的admin 数据模型 并访问admin页面

# 修改setting.py

mysql > create datebase django;

$ python manage.py migrate
$ python manage.py runserver localhost:<port>


# 建立管理页面的用户密码
python manage.py createsuperuser



# 更新model, 并同步数据
python manage.py makemigrations
python manage.py migrate