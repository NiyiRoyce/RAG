from llm_app.rag_pipeline import run_pipeline


def test_pipeline_runs():
    try:
        run_pipeline("test_source", {"db": "mock_db"})
        assert True
    except Exception as e:
        assert False, f"Pipeline failed: {e}"
