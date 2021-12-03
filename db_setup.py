from restaurateur_functions import open_local_db_admin_connection, create_source_tables


def main():
    # The work flow to set up the tables for API data in my local restaurateur database.
    connection = open_local_db_admin_connection()
    cursor = connection.cursor()
    create_source_tables(cursor)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
