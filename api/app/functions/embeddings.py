import json

from app.dependencies.bedrock import get_bedrock_client

_EMBED_MODEL_ID = "amazon.titan-embed-text-v2:0"


def embed_text(text: str) -> list[float]:
    client = get_bedrock_client()
    response = client.invoke_model(
        modelId=_EMBED_MODEL_ID,
        body=json.dumps({"inputText": text}),
        contentType="application/json",
        accept="application/json",
    )
    return json.loads(response["body"].read())["embedding"]
