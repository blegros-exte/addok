# Just to test that keys from a local file are loaded.
import os

COMMON_THRESHOLD = 1000

REDIS = {
    "host": os.environ.get("REDIS_HOST") or "localhost",
    "port": os.environ.get("REDIS_PORT") or 6379
}
