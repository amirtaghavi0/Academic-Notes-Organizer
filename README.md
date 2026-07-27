#Academic Note Organizer

این پروژه یک پروژه ی تحت وب با فریم ورک Django برای مدیریت دروس و جزوه های درسی است

##امکانات پروژه
-ثبت نام و ورود کاربران
-ایجاد ویرایش حذف و نمایش دوره ها
-ایجاد ویرایش حذف و نمایش جزوه ها
-دسته بندی یادداشت ها با تگ
-جستجو در میان یادداشت ها

##ابزار های استفاده شده
-Python
-Django
-postgreSQL
-HTML
-CSS

##ساخت محیط مجازی 
python -m venv venv

##فعال سازی محیط مجازی 
venv/Scripts/activate

##نصب وابستگی ها
pip install -r requirements

##اعمال migrate
python manage.py migrate 

##ایجاد کاربر ادمین
python manage.py createsuperuser 

##اجرای پروژه
Python manage.py runserver 
