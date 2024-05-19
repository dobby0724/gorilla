from enum import Enum


class ModelStyle(Enum):
    Gorilla = "gorilla"
    OpenAI = "gpt"
    Anthropic_FC = "claude"
    Anthropic_Prompt = "claude"
    Mistral = "mistral"
    Google = "google"
    FIREWORK_AI = "firework_ai"
    NEXUS = "nexus"
    OSSMODEL = "ossmodel"
    COHERE = "cohere"
    Llama = "llama"
