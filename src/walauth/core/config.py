"""
config.py -> single Python class that represents every configuration value your app needs to run,
typed and validated, pulled from environment variables, but doesn't include all env variables,
only the ones you explicitly declare as class attributes
"""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# BaseSettings is a special subclass of Pydantic's normal BaseModel. 
# A regular BaseModel validates data you pass into it manually (User(name="Sam")). 
# BaseSettings does something different: it automatically looks at environment variables 
# (and .env files) to fill in the fields, without you passing anything in.

class Settings(BaseSettings):
    PROJECT_NAME: str = "WalAuth"

    PORT: int = 7007

    DATABASE_URL: str

    JWT_SECRET: SecretStr
    ACCESS_TOKEN_EXPIRY: int = 30
    REFRESH_TOKEN_EXPIRY: int = 7

    ENVIRONMENT: str = "prod"

    @property
    def IS_DEV_ENV(self) -> bool:
        return self.ENVIRONMENT.lower() in ("dev", "development", "local")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    # extra="ignore" -> ignore any environment variables that are not 
    # defined in the Settings class, necessary to pass it here. Without it,
    # Pydantic's default behavior is extra="forbid"  meaning if your .env has 
    # a variable that isn't declared in the class, Pydantic raises a validation error and refuses to start the app

settings = Settings()