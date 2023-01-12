import os
import sys
import uuid
import ui.ui
import random
from time import sleep
from faker import Faker
from pathlib import Path
from rich.progress import track
from guide import init_conn, init_db_conn


# Initialise faker
Faker.seed(0)

# Initialise some uuids
reg_id = uuid.uuid1().int
country_usa_id = uuid.uuid1().int
country_de_id = uuid.uuid1().int
country_at_id = uuid.uuid1().int
country_fr_id = uuid.uuid1().int
province_id = uuid.uuid1().int

MAGIC_NUMBER = 1000000

# Initialise some arrays
MIN_SAL_CONST = [1000, 2000, 1500, 2500, 3000, 4500, 5000, 5000]
MAX_SAL_CONST = [10000, 20000, 10500, 25000, 30000, 45000, 15000]
# list of countries selected to fake data
locale_ = ["de_DE", "fr_FR", "en_US", "de_AT"]


# Storage class of an Employee
class Person:
    """A simple storage class that stores all the variable needed during fake data generation"""

    def __init__(self):
        pass


def generate_data(dbnm, num) -> None:
    """A simple function that generates all data and stores them in the database"""

    dbname = dbnm
    conn = init_db_conn(dbname)
    cursor = conn.cursor()

    dict_tmp_jobs = {}

    for _ in track(range(int(num)), description=f"Generating: "):

        locale = random.choice(locale_)

        if locale == "en_US":

            fake = Faker(locale)
            r1 = random.randint(10, 150) * 1000
            tmp_person = Person()
            tmp_person.employee_id = uuid.uuid1().int
            tmp_person.region_name = "K/A"
            tmp_person.region_id = reg_id
            tmp_person.state_province = "K/A"
            tmp_person.state_province_id = province_id
            tmp_person.first_name = fake.first_name()
            tmp_person.last_name = fake.last_name()
            tmp_person.email = fake.profile()["mail"]
            tmp_person.phone_number = fake.phone_number()
            # TODO: date_start=datetime(2015, 1, 1)
            tmp_person.hire_date = fake.date_between()
            tmp_person.min_salary = r1 - random.choice(MIN_SAL_CONST)
            tmp_person.max_salary = r1 + random.choice(MAX_SAL_CONST)
            tmp_person.salary = int(random.randint(
                tmp_person.min_salary, tmp_person.max_salary) / 1000) * 1000
            tmp = fake.profile()['job']

            found = False
            for k, v in dict_tmp_jobs.items():
                if v == tmp:
                    found = True
                    tmp_person.job_title = tmp
                    tmp_person.job_id = k
                    break

            if not found:
                tmp_person.job_title = tmp
                tmp_person.job_id = uuid.uuid1().int
                dict_tmp_jobs[tmp_person.job_id] = tmp_person.job_title

            tmp_person.country_name = "USA"
            tmp_person.country_id = country_usa_id
            tmp_person.relationship = random.choice(
                ["Sigle", "Married", "Divorced"])
            tmp_person.street_address = fake.street_address()
            tmp_person.plz = fake.postalcode_in_state()
            tmp_person.city = fake.city()
            # TODO: Make sure during inserting request in Postgre, check for redundancy
            tmp_person.location_id = uuid.uuid1().int

        elif locale == "fr_FR":

            fake = Faker(locale)
            r1 = random.randint(10, 150) * 1000
            tmp_person = Person()
            tmp_person.employee_id = uuid.uuid1().int
            tmp_person.region_name = "K/A"
            tmp_person.region_id = reg_id
            tmp_person.state_province = "K/A"
            tmp_person.state_province_id = province_id
            tmp_person.first_name = fake.first_name()
            tmp_person.last_name = fake.last_name()
            tmp_person.email = fake.profile()["mail"]
            tmp_person.phone_number = fake.phone_number()
            # TODO: date_start=datetime(2015, 1, 1)
            tmp_person.hire_date = fake.date_between()
            tmp_person.min_salary = r1 - random.choice(MIN_SAL_CONST)
            tmp_person.max_salary = r1 + random.choice(MAX_SAL_CONST)
            tmp_person.salary = int(random.randint(
                tmp_person.min_salary, tmp_person.max_salary) / 1000) * 1000
            tmp = fake.profile()['job']

            found = False
            for k, v in dict_tmp_jobs.items():
                if v == tmp:
                    found = True
                    tmp_person.job_title = tmp
                    tmp_person.job_id = k
                    break

            if not found:
                tmp_person.job_title = tmp
                tmp_person.job_id = uuid.uuid1().int
                dict_tmp_jobs[tmp_person.job_id] = tmp_person.job_title

            tmp_person.country_name = "Frankreich"
            tmp_person.country_id = country_fr_id
            tmp_person.relationship = random.choice(
                ["Célibataire", "Marié", "Devorcé"])
            tmp_person.street_address = fake.street_address()
            tmp_person.plz = fake.postcode()
            tmp_person.city = fake.city()
            # TODO: Make sure during inserting request in Postgre, check for redundancy
            tmp_person.location_id = uuid.uuid1().int

        elif locale == "de_DE":

            fake = Faker(locale)
            r1 = random.randint(10, 150) * 1000
            tmp_person = Person()
            tmp_person.employee_id = uuid.uuid1().int
            tmp_person.region_name = "K/A"
            tmp_person.region_id = reg_id
            tmp_person.state_province = "K/A"
            tmp_person.state_province_id = province_id
            tmp_person.first_name = fake.first_name()
            tmp_person.last_name = fake.last_name()
            tmp_person.email = fake.profile()["mail"]
            tmp_person.phone_number = fake.phone_number()
            # TODO: date_start=datetime(2015, 1, 1)
            tmp_person.hire_date = fake.date_between()
            tmp_person.min_salary = r1 - random.choice(MIN_SAL_CONST)
            tmp_person.max_salary = r1 + random.choice(MAX_SAL_CONST)
            tmp_person.salary = int(random.randint(
                tmp_person.min_salary, tmp_person.max_salary) / 1000) * 1000
            tmp = fake.profile()['job']

            found = False
            for k, v in dict_tmp_jobs.items():
                if v == tmp:
                    found = True
                    tmp_person.job_title = tmp
                    tmp_person.job_id = k
                    break

            if not found:
                tmp_person.job_title = tmp
                tmp_person.job_id = uuid.uuid1().int
                dict_tmp_jobs[tmp_person.job_id] = tmp_person.job_title

            tmp_person.country_name = "Deutschland"
            tmp_person.country_id = country_de_id
            tmp_person.relationship = random.choice(
                ["ledig", "verheiratet", "geschieden"])
            tmp_person.street_address = fake.street_address()
            tmp_person.plz = fake.postcode()
            tmp_person.city = fake.city()
            # TODO: Make sure during inserting request in Postgres, check for redundancy
            tmp_person.location_id = uuid.uuid1().int

        elif locale == "de_AT":

            fake = Faker(locale)
            r1 = random.randint(10, 150) * 1000
            tmp_person = Person()
            tmp_person.employee_id = uuid.uuid1().int
            tmp_person.region_name = "K/A"
            tmp_person.region_id = reg_id
            tmp_person.state_province = "K/A"
            tmp_person.state_province_id = province_id
            tmp_person.first_name = fake.first_name()
            tmp_person.last_name = fake.last_name()
            tmp_person.email = fake.profile()["mail"]
            tmp_person.phone_number = fake.phone_number()
            # TODO: date_start=datetime(2015, 1, 1)
            tmp_person.hire_date = fake.date_between()
            tmp_person.min_salary = r1 - random.choice(MIN_SAL_CONST)
            tmp_person.max_salary = r1 + random.choice(MAX_SAL_CONST)
            tmp_person.salary = int(random.randint(
                tmp_person.min_salary, tmp_person.max_salary) / 1000) * 1000
            tmp = fake.profile()['job']

            found = False
            for k, v in dict_tmp_jobs.items():
                if v == tmp:
                    found = True
                    tmp_person.job_title = tmp
                    tmp_person.job_id = k
                    break

            if not found:
                tmp_person.job_title = tmp
                tmp_person.job_id = uuid.uuid1().int
                dict_tmp_jobs[tmp_person.job_id] = tmp_person.job_title

            tmp_person.country_name = "Oesterreich"
            tmp_person.country_id = country_at_id
            tmp_person.relationship = random.choice(
                ["ledig", "verheiratet", "geschieden"])
            tmp_person.street_address = fake.street_address()
            tmp_person.plz = fake.postcode()
            tmp_person.city = fake.city()
            # TODO: Make sure during inserting request in Postgres, check for redundancy
            tmp_person.location_id = uuid.uuid1().int

        insert_data_into_job_table_query = f"""
        INSERT INTO public.job (job_id, job_title, min_salary, max_salary) VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(insert_data_into_job_table_query, (tmp_person.job_id, tmp_person.job_title,
                           tmp_person.min_salary, tmp_person.max_salary))  # print("[+] vals inserted into jobs tables")
        except Exception as e:
            pass

        insert_data_into_region_table = f"""
        INSERT INTO public.region  (region_id, region_name) VALUES (%s, %s)
        """
        try:
            # print("[+] vals inserted into regions tables")
            cursor.execute(insert_data_into_region_table,
                           (tmp_person.region_id, tmp_person.region_name))
        except Exception as e:
            pass

        insert_into_country_table_query = f"""
        INSERT INTO public.country (country_id, country_name, region_id) VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(insert_into_country_table_query, (tmp_person.country_id, tmp_person.country_name,
                           tmp_person.region_id))  # print("[+] vals inserted into country tables")
        except Exception as e:
            pass

        insert_into_locatoin_table_query = f"""
        INSERT INTO public.location (location_id, street_address, state_province, city, plz, country_id) VALUES (%s, %s, %s, %s, %s, %s);
        """
        try:
            cursor.execute(insert_into_locatoin_table_query, (tmp_person.location_id, tmp_person.street_address, tmp_person.state_province,
                           tmp_person.city, tmp_person.plz, tmp_person.country_id))  # print("[+] vals inserted into country tables")
        except Exception as e:
            pass

        insert_into_employee_table_query = f"""
        INSERT INTO public.employee (employee_id, first_name, last_name, email, phone_number, hire_date, salary, job_id, location_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        try:
            cursor.execute(insert_into_employee_table_query, (tmp_person.employee_id, tmp_person.first_name, tmp_person.last_name, tmp_person.email, tmp_person.phone_number,
                           tmp_person.hire_date, tmp_person.salary, tmp_person.job_id, tmp_person.location_id))  # print("[+] vals inserted into employee tables")
        except Exception as e:
            pass

    conn.close()


def get_file(filenm) -> str:
    """A simple function that returns the filepath independent of the platform"""

    if not sys.platform == "win32":
        path = Path(os.path.realpath(os.path.dirname(__file__)))
        return path.parent.absolute().__str__() + "/ui/" + filenm
    else:
        path = Path(os.path.realpath(os.path.dirname(__file__)))
        return path.parent.absolute().__str__() + "\\ui\\" + filenm


def create_db(dbnm):
    """A simple function that create the database with the given name"""
    conn = init_conn()
    curs = conn.cursor()

    dbname = dbnm

    # query to create a database
    sql = f'''CREATE database {dbname}'''

    # executing above query
    curs.execute(sql)

    conn.close()


def create_tables0(dbnm):
    """A simple function that creates all the necessary tables"""

    dbname = dbnm
    conn = init_db_conn(dbname)
    cursor = conn.cursor()

    create_job_table_query = f"""
        CREATE TABLE public.job(
          job_id       varchar(40) PRIMARY KEY NOT NULL,

          job_title    varchar(255) NOT NULL,
          min_salary   INT,
          max_salary   INT 
        );
      """
    cursor.execute(create_job_table_query)
    print("TABLE Jobs      has been created successfully !!")

    create_region_table_query = f"""
            CREATE TABLE public.region(
              region_id      varchar(40) PRIMARY KEY NOT NULL,
              
              region_name    varchar(255) NOT NULL
            );
          """
    cursor.execute(create_region_table_query)
    print("TABLE Region    has been created successfully !!")

    create_country_table_query = f"""
        CREATE TABLE public.country(
          country_id     varchar(40) PRIMARY KEY NOT NULL,

          country_name   varchar(255) NOT NULL,

          region_id      varchar(39),

          FOREIGN KEY(region_id) REFERENCES public.region(region_id)
        );
      """
    cursor.execute(create_country_table_query)
    print("TABLE Country   has been created successfully !!")

    create_location_table_query = f"""
        CREATE TABLE public.location(
          location_id     varchar(40) PRIMARY KEY NOT NULL,

          street_address  varchar(255) NOT NULL,
          state_province  varchar(255) NOT NULL,
          city            varchar(255) NOT NULL,
          plz             INT,

          country_id      varchar(39),

          FOREIGN KEY(country_id) REFERENCES public.country(country_id)
        );
      """
    cursor.execute(create_location_table_query)
    print("TABLE Loctions  has been created successfully !!")

    create_employee_table_query = f"""
        CREATE TABLE public.employee(
          employee_id  varchar(40) PRIMARY KEY NOT NULL,

          first_name   varchar(255) NOT NULL,
          last_name    varchar(255) NOT NULL,
          email        varchar(255) NOT NULL,
          phone_number varchar(255) NOT NULL,
          hire_date    timestamp NOT NULL,
          salary       INT,

          job_id       varchar(39),
          location_id  varchar(39),
          
          FOREIGN KEY(job_id) REFERENCES public.job(job_id),
          FOREIGN KEY(location_id) REFERENCES public.location(location_id)
        );
      """
    cursor.execute(create_employee_table_query)
    print("TABLE employees has been created successfully !!")

    conn.close()


def genrate_all_tables(consl, dbnm, entries_nm):
    """A simple function that init the generation of tables """
    load_arr = []
    console = consl
    dbname = dbnm
    entries_num = entries_nm
    ui.ui.init_tables(consl=console, dbname=dbname)

    generate_data(dbnm=dbname, num=entries_num)
    sleep(5)


def del_db(dbname):
    """A simple function that deletes the given database"""
    conn = init_db_conn(dbname)
    cursor = conn.cursor()

    delete_database_query = f"""
    DROP DATABASE {dbname} WITH (FORCE);
    """

    try:
        cursor.execute(delete_database_query)
    except Exception as e:
        pass

    conn.close()
