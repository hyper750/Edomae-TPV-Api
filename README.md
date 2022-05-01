# TPV Api

## Environment variables
- `SECRET_KEY` str: Provides cryptographic signing, and should be set to a unique, unpredictable value, eg: `L>YT=UK\YQK/:UxGdev^5/xM_SvHCY\f;%H#R!zpku{{?9[2CHJMK%PA(48Bs(Q$`
- `DEBUG` bool: Run on debug or production, default `False`, eg `True`
- `DATABASE_URI` str: Uri to access the database, eg `postgresql://user:password@127.0.0.1:5432/dbname`
- `REDIS_HOST` str: Host/Ip for the redis service, default `127.0.0.1`
- `REDIS_PORT` int: Port for the redis service, default `6379`
- `REDIS_PASSWORD` str: Password for the redis service
- `RECAPTCHA_SERVER_KEY` str: Google recaptcha server key
- `AVAILABLE_LANGUAGES` List[str]: List of available languages

### Tickets
- `SOCIETY_NAME` str: Society name, eg: `Bla Menorca S.L`
- `SOCIETY_CIF` str: Society nif, eg: `B12345678`
- `SOCIETY_QUARTERS` str: Society quarter/address, eg: `C/Bona tramuntana 26`

## Run
```bash
python app.py
```

## Run/Deploy using nginx docker
https://github.com/hyper750/EdomaeDeploy/tree/main/api
