# HOW TO USE APP

### There are 2 ways (with docker and manual)

### Manual commands
### This path assumes you have installed poetry and postgresql
###### clone project 

    $ git clone https://github.com/zxc322/parse_real_estate.git


###### Create user with the same name as postgeres user ( it needed to run dump_psql script)

    $ sudo adduser zxc 
    $ sudo usermod -aG sudo zxc
    $ su zxc

###### Change const 'USE_DOCKER' to 'False' in parse_app/settings.py ( Default=True)

    USE_DOCKER = False


###### Create database (postgresql)
###### You always can change it in src/settings.py

    postgresql = {
    'pguser': 'zxc',
    'pgpswd': 'zxc',
    'pghost': 'localhost',
    'pgport': 5432,
    'pgdb': 'async_db'
    }

###### Postgers commands

    $ sudo -i -u postgres
    $ psql  
    $ CREATE database async_db;
    $ CREATE user zxc with encrypted password 'zxc';
    $ grant all privileges on database real_estate to zxc;

###### Install dependencies and run app


    $ poetry install
    $ poetry run python src/main.py

###### After finish script will create dump.gz file localy 


### Docker commands
### This path assumes you have installed docker and docker-compose


###### clone project and install poetry if u don't have it on your local machine

    $ git clone https://github.com/zxc322/parse_real_estate.git
    
###### From directory wirh 'docker-compose.yml' run:

    $ docker-compose up --build
    
###### This command will start pulling data from site
###### When its done you can dump postgers data from docker (but container with db must be runing)

    # dump data
    $ docker exec postgres_db pg_dump -U zxc -F t async_db | gzip > docker_async_db.gz

