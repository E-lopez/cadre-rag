import json
from unittest.mock import MagicMock, patch

from app.services.evals import _JUDGE_MODEL_ID, run_rag_eval

_SAMPLE_VERDICT = {
    "user_query": "What does Cadre AI do?",
    "retrieved_context": "Cadre AI helps businesses implement AI strategies.",
    "generated_response": "Cadre AI provides AI strategy consulting.",
    "context_relevance": {"chain_of_thought_justification": "...", "score": 1.0},
    "groundedness": {"chain_of_thought_justification": "...", "score": 1.0},
    "answer_relevance": {"chain_of_thought_justification": "...", "score": 1.0},
    "triad_summary_verdict": "High quality RAG transaction.",
}


def _make_judge_response(verdict: dict) -> dict:
    body = MagicMock()
    body.read.return_value = json.dumps({
        "content": [{"text": f"```json\n{json.dumps(verdict)}\n```"}]
    }).encode()
    return {"body": body}


def test_run_rag_eval_logs_scores():
    mock_client = MagicMock()
    mock_client.invoke_model.return_value = _make_judge_response(_SAMPLE_VERDICT)

    with patch("app.services.evals.get_bedrock_client", return_value=mock_client):
        run_rag_eval(
            user_query="What does Cadre AI do?",
            retrieved_context="Cadre AI helps businesses implement AI strategies.",
            generated_response="Cadre AI provides AI strategy consulting.",
        )

    mock_client.invoke_model.assert_called_once()
    call_kwargs = mock_client.invoke_model.call_args.kwargs
    assert call_kwargs["modelId"] == _JUDGE_MODEL_ID


def test_run_rag_eval_handles_bedrock_error_gracefully():
    from botocore.exceptions import ClientError

    mock_client = MagicMock()
    mock_client.invoke_model.side_effect = ClientError(
        {"Error": {"Code": "ThrottlingException", "Message": "Rate exceeded"}},
        "InvokeModel",
    )

    with patch("app.services.evals.get_bedrock_client", return_value=mock_client):
        run_rag_eval(
            user_query="test",
            retrieved_context="context",
            generated_response="response",
        )
