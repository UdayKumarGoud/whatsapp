# # from django.test import TestCase
# import sys
# import logging
# import psycopg2
# import json
# import os
# # from Paysitters import settings

# # env_config = settings.env_config
# # Create your tests here.


# rds_host  = 'aurora-paysitters-dev.cluster-crkc2iyxl4hr.us-east-2.rds.amazonaws.com'
# rds_username = 'gruntwork'
# rds_user_pwd = 'xz451b*TwmyGe~e62MOf'
# rds_db_name = 'paysitters'
# rds_port = '5432'

# # print(DOTENV_FILE)

# # rds_host = env_config('DB_HOST'),
# # rds_username = env_config('DB_USER')
# # rds_user_pwd = env_config('DB_PASSWORD')
# # rds_db_name = env_config('DB_NAME')
# # rds_port = env_config('DB_PORT')

# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# try:
#     conn_string = "host=%s user=%s password=%s dbname=%s port=%s" % \
#                     (rds_host, rds_username, rds_user_pwd, rds_db_name, rds_port)
#     conn = psycopg2.connect(conn_string)
#     print(conn)
#     cursor = conn.cursor()
#     query = "SELECT version() AS version"
#     cursor.execute(query)
#     results = cursor.fetchone()
#     query1 = "SELECT * FROM admin_dashboard_adminuser"
#     print(query1)
#     cursor.execute(query1)
#     results = cursor.fetchall()
#     cursor.close()
#     conn.commit()
#     print(results)
# except:
#     logger.error("ERROR: Could not connect to Postgres instance.")
#     sys.exit()

# logger.info("SUCCESS: Connection to RDS Postgres instance succeeded")
