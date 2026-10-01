import os
import logging
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

DBHOST = os.getenv("DBHOST")
DBUSER = os.getenv("DBUSER")
DBPASS = os.getenv("DBPASS")
DBNAME = os.getenv("DBNAME")


def get_data_by_group(value):
    """Return all rows where the `group` column equals the given value."""
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

        query = """
        SELECT *
        FROM mock
        WHERE `group` = %s
        """

        cursor.execute(query, (value,))
        rows = cursor.fetchall()

        logging.info(
            "Retrieved %d rows for group %s",
            len(rows),
            value
        )

        return rows

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


def plot_counts(groupby):
    """Count rows for each distinct value in the selected column."""
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

        allowed_columns = {
            "id",
            "group",
            "name",
            "age",
            "city",
            "score"
        }

        if groupby not in allowed_columns:
            raise ValueError("Invalid column name")

        query = f"""
        SELECT `{groupby}`, COUNT(*)
        FROM mock
        GROUP BY `{groupby}`
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        logging.info(
            "Calculated counts grouped by %s",
            groupby
        )

        return rows

    except (mysql.connector.Error, ValueError) as error:
        logging.error("Error: %s", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


def main():
    """Demonstrate the query functions."""

    print("Rows in group Alpha:")
    print(get_data_by_group("Alpha"))

    print("\nCounts by city:")
    print(plot_counts("city"))


if __name__ == "__main__":
    main()
