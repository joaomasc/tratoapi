from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da aplicação carregadas de variáveis de ambiente"""
    
    # api config
    API_TITLE: str
    API_VERSION: str
    API_DESCRIPTION: str = "API DESENVOLVIDA COM FASTAPI"

    # server config
    HOST: str
    PORT: int
    DEBUG: bool

    # database config
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    
    # pool config
    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    
    @property
    def DATABASE_URL(self) -> str:
        """Gera a URL de conexão com o PostgreSQL"""
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
