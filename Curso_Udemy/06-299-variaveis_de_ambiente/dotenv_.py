from pathlib import Path
import os
from dotenv import load_dotenv

env_path = Path().absolute() / '.env'
load_dotenv(env_path)

print(os.getenv('DB_PASSWORD'))
