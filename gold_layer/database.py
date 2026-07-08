"""
Database Connection

Purpose
-------
Creates a reusable SQLAlchemy engine for connecting
to the SQL Server data warehouse.

Other modules import get_engine()
whenever they need to interact with SQL Server.
"""

from sqlalchemy import create_engine

SERVER_NAME = "DESKTOP-UITS5AM"      # Change if your server name is different
DATABASE_NAME = "AirbnbDW"
DRIVER = "ODBC Driver 17 for SQL Server"


def get_engine():
    """
    Return a SQLAlchemy engine connected to SQL Server.
    """

    connection_string = (
        f"mssql+pyodbc://@{SERVER_NAME}/{DATABASE_NAME}"
        f"?driver={DRIVER.replace(' ', '+')}"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)