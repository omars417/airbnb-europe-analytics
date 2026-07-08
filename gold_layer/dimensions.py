import pandas as pd


def create_dim_city(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create the City dimension table.
    """

    dim_city = (df[["City"]].drop_duplicates().sort_values("City").reset_index(drop=True))
    #insert() adds a column at a specific position. 0 → insert as the first column. "CityID" → column name. range(...) → generates 1, 2, 3, ...

    dim_city.insert(0,"CityID",range(1, len(dim_city) + 1))
    # CityID | City
    return dim_city

def create_dim_room(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create the Room dimension table.
    """

    dim_room = (
        df[["room_type"]]
        .drop_duplicates()
        .sort_values("room_type")
        .reset_index(drop=True)
    )

    dim_room.insert(
        0,
        "RoomID",
        range(1, len(dim_room) + 1)
    )

    dim_room.rename(
        columns={
            "room_type": "RoomType"
        },
        inplace=True
    )
            #| RoomID | RoomType |
    return dim_room

def create_dim_day_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create the Day Type dimension table.
    """

    dim_day = (
        df[["Day Type"]]
        .drop_duplicates()
        .sort_values("Day Type")
        .reset_index(drop=True)
    )

    dim_day.insert(
        0,
        "DayTypeID",
        range(1, len(dim_day) + 1)
    )

    dim_day.rename(
        columns={
            "Day Type": "DayType"
        },
        inplace=True
    )
            #| DayTypeID | DayType |
    return dim_day