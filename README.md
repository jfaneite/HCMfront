# HCMfront

Clona el proyecto en la ruta donde vas a crear el virtualenv

Creando VirtualEvn...

```sh
$ cd ~/repositories/hcmfront
$ virtualenv venv-salas
$ . venv/bin/activate
$ pip install -r requirements.txt 
$ 
```

luego corre el servidor y prueba...

```sh
$ cd salas
$ ./manage.py migrate
$ ./manage.py createsuperuser
$ ./manage.py runserver
$ 
```

la ruta para administrar la app...
http://127.0.0.1:8000/admin/