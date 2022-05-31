This is a coinmena test task

How to run:
1. You should populate .env file, example:
   ```
       ALPHAVANTAGE_API_KEY=supersecretkey
       SECRET_KEY=djangosecretkeyalsosupersecret
       DB_URL=postgresql://user:passwordfrompostgres@postgres:5432/coinmena
       DB_PASSWORD=passwordfrompostgres
       ```
2. Then you should run `docker-compose up`
3. Web interface will be availible at `http://localhost:8000`
4. Keep in mind that due to task's requirements i kept this project as simple as possible so there is no DRF 