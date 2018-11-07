

КАК ЗАПУСТИТЬ НА ЛОКАЛЬНОМ СЕРВЕРЕ:


1. Создать дирректорию и перейти в нее:
cd ~/
mkdir chart && cd chart

2. Создать виртуальное окружение и активировать его:

virtualenv -p python3 .

 # activate on Mac/Linux
source bin/activate

# activate on Windows
.\Scripts\activate

3.Разархивировать архив chart-master.zip

4.Переименовать полученную папку в src и войти в нее
 # on Mac/Linux
mv chart-master src && cd src

5.Установить в полученной папке зависимости

pip install -r requirements.txt

6.Запустить проект:

python manage.py runserver

7.Открыть проект в браузере по адресу:

http://127.0.0.1:8000/


