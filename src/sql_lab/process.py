import os
import logging
import pandas as pd
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def read_data(filename):
    """Read a CSV file and return a pandas DataFrame."""
    logging.info("Reading data from %s", filename)
    data = pd.read_csv(filename)
    logging.info("Read %d rows", len(data))
    return data


def clean_data(data):
    """Remove rows with missing values and return cleaned data."""
    logging.info("Cleaning data")
    cleaned_data = data.dropna().copy()
    logging.info(
        "Removed %d rows with missing values",
        len(data) - len(cleaned_data)
    )
    return cleaned_data


def load_data(data, table):
    """Create the destination table and upload data to MySQL."""
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )

        cursor = connection.cursor()

        logging.info("Connected to database")

        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS `{table}` (
            id BIGINT PRIMARY KEY,
            `group` VARCHAR(255),
            name VARCHAR(255),
            age BIGINT,
            city VARCHAR(255),
            score DOUBLE
        )
        """

        cursor.execute(create_table_sql)

        insert_sql = f"""
        INSERT INTO `{table}`
        (id, `group`, name, age, city, score)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for _, row in data.iterrows():
            values = (
                int(row["id"]),
                row["group"],
                row["name"],
                int(row["age"]),
                row["city"],
                float(row["score"])
            )

            cursor.execute(insert_sql, values)

        connection.commit()

        logging.info(
            "Uploaded %d rows to %s",
            len(data),
            table
        )

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

        logging.info("Database connection closed")


def main():
    """Run the complete data upload workflow."""
    data = read_data("MOCK_DATA.csv")
    cleaned_data = clean_data(data)
    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()
