/*
=========================================================
Airbnb Data Warehouse Schema
=========================================================

Purpose
-------
Defines the structure of the Gold Layer SQLite database.

This script creates the Star Schema used for analytics.

Responsibilities
----------------
- Create Dimension tables
- Create Fact table
- Define Primary Keys
- Define Foreign Keys

Note
----
This script ONLY creates the database structure.

It does NOT insert any data.

Data loading is handled separately by database.py.
=========================================================
*/
IF DB_ID('AirbnbDW') IS NULL
BEGIN
    CREATE DATABASE AirbnbDW;
END
GO

USE AirbnbDW;
GO

DROP TABLE IF EXISTS FactListing;
DROP TABLE IF EXISTS CityMarket;
DROP TABLE IF EXISTS DimRoom;
DROP TABLE IF EXISTS DimDayType;
DROP TABLE IF EXISTS DimCity;

CREATE TABLE DimCity (

    CityID INT PRIMARY KEY,

    City NVARCHAR(100) NOT NULL UNIQUE

);

CREATE TABLE DimRoom (

    RoomID INTEGER PRIMARY KEY,

    RoomType NVARCHAR(100) NOT NULL UNIQUE

);

CREATE TABLE DimDayType (

    DayTypeID INTEGER PRIMARY KEY,

    DayType NVARCHAR(100) NOT NULL UNIQUE

);

CREATE TABLE CityMarket (

    City NVARCHAR(100) PRIMARY KEY,

    CityAveragePrice FLOAT,

    CityMedianPrice FLOAT,

    CityAverageRating FLOAT,

    CityAverageReviews FLOAT,

    SuperhostRate FLOAT,

    GuestFavoriteRate FLOAT,

    ListingCount INT

);

CREATE TABLE FactListing (

    ListingID INTEGER PRIMARY KEY,

    CityID INTEGER NOT NULL,

    RoomID INTEGER NOT NULL,

    DayTypeID INTEGER NOT NULL,

    realSum FLOAT,

    room_shared INTEGER,

    room_private INTEGER,

    person_capacity INTEGER,

    host_is_superhost INTEGER,

    multi INTEGER,

    biz INTEGER,

    cleanliness_rating INTEGER,

    guest_satisfaction_overall INTEGER,

    bedrooms FLOAT,

    dist FLOAT,

    metro_dist FLOAT,

    attr_index FLOAT,

    attr_index_norm FLOAT,

    rest_index FLOAT,

    rest_index_norm FLOAT,

    lng FLOAT,

    lat FLOAT,

    -- =====================================
    -- Engineered Features
    -- =====================================

    price_per_guest FLOAT,

    price_per_bedroom FLOAT,

    distance_category NVARCHAR(50),

    metro_accessibility NVARCHAR(50),

    luxury_listing BIT,

    city_price_tier NVARCHAR(50),

    PricePerPerson FLOAT,

    -- =====================================
    -- Market Intelligence
    -- =====================================

    CityAveragePrice FLOAT,

    CityMedianPrice FLOAT,

    CityAverageRating FLOAT,

    CityAverageReviews FLOAT,

    SuperhostRate FLOAT,

    GuestFavoriteRate FLOAT,

    ListingCount INTEGER,

    -- =====================================
    -- Relationships
    -- =====================================

    FOREIGN KEY (CityID)
        REFERENCES DimCity (CityID),

    FOREIGN KEY (RoomID)
        REFERENCES DimRoom (RoomID),

    FOREIGN KEY (DayTypeID)
        REFERENCES DimDayType (DayTypeID)

);