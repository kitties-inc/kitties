## Kitties

### quick start:
```bash
git clone git@github.com:kitties-inc/kitties.git
pip install poetry
poetry lock
poetry shell
poetry install --no-root
python3 manage.py runserver
```
then visit http://127.0.0.1:8000/

### troubleshooting
Если poetry будет ругаться на несовместимую версию питона,
то из вариантов можно: 
- установить питон версии 3.11 и выше
- поменять версию python на свою текущую версию в файле [pyproject.toml](pyproject.toml) 

