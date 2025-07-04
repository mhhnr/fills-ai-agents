from pydantic_settings import BaseSettings


class AgentSettings(BaseSettings):
    """Agent settings that can be set using environment variables.

    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    gpt_4_mini: str = "gpt-4o-mini"
    gpt_4: str = "gpt-4o"
    
    # Amazon Nova Lite configuration
    nova_lite: str = "amazon.nova-lite-v1:0"
    aws_region: str = "us-east-1"
    
    embedding_model: str = "text-embedding-3-small"
    default_max_completion_tokens: int = 16000
    default_temperature: float = 0


# Create an TeamSettings object
agent_settings = AgentSettings()
