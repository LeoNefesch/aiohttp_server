# Aiohttp_server
## Миграция


```commandline
alembic init migrations
```
```commandline
export PYTHONPATH=.
```
(для Linux)
```commandline
$env:PYTHONPATH = "."
```
(для Windows)
```commandline
alembic revision -m 'create table Message' --autogenerate
```
```commandline
alembic upgrade head
```
(повысим версию БД до последней)