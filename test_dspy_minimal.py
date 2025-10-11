# test_dspy_minimal.py
from dspy_minimal import PromptOptimizer, PromptCandidate, similarity_score, simulated_model

def test_optimizer_picks_best_on_simulated_model():
    candidates = [
        PromptCandidate("Summarize: {input}"),
        PromptCandidate("Explain in detail: {input}"),
        PromptCandidate("Answer in one word: {input}"),
    ]
    # Construct a tiny dataset where the 'Summarize' prompt achieves highest average similarity
    dataset = [
        ("Data A", "short summary"),
        ("Data B", "short summary"),
    ]
    opt = PromptOptimizer(simulated_model, similarity_score)
    best, score = opt.best_candidate(candidates, dataset)
    assert best.prompt == "Summarize: {input}"
    assert score > 0.5