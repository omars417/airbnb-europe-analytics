from pathlib import Path #Instead of writing "C:/Users/Ahmed/Desktop/project/data/raw"  we let Python automatically find the project.

# ==========================
# Project Paths
# ==========================

# Root project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
BRONZE_DATA_PATH = PROJECT_ROOT / "data" / "bronze"
SILVER_DATA_PATH = PROJECT_ROOT / "data"  / "silver"
GOLD_DATA_PATH =PROJECT_ROOT / "data"  / "gold"
SCRAPED_DATA_PATH = PROJECT_ROOT / "data" / "scraped"
# Metadata & Logs
METADATA_FILE = BRONZE_DATA_PATH / "metadata.json"
LOG_FILE = BRONZE_DATA_PATH / "pipeline.log"

# Expected schema (will be updated later if needed)
#could hardcode those inside validate.py prefer keeping them in config.py because It keeps validate.py focused only on checking, not defining, the schema.
EXPECTED_COLUMNS = [
    "realSum",
    "room_type",
    "room_shared",
    "room_private",
    "person_capacity",
    "host_is_superhost",
    "multi",
    "biz",
    "cleanliness_rating",
    "guest_satisfaction_overall",
    "bedrooms",
    "dist",
    "metro_dist",
    "attr_index",
    "attr_index_norm",
    "rest_index",
    "rest_index_norm",
    "lng",
    "lat"
]