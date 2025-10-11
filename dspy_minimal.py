# dspy_minimal.py
from typing import Callable, List, Tuple
from difflib import SequenceMatcher

class PromptCandidate:
    def __init__(self, prompt: str, params: dict = None):
        self.prompt = prompt
        self.params = params or {}

class PromptOptimizer:
    """
    Very small optimizer that scores candidate prompts using a provided model function
    and scorer. Strategy: evaluate all candidates (grid-like).
    """
    def __init__(self, model_fn: Callable[[str, dict], str], scorer_fn: Callable[[str, str], float]):
        """
        model_fn(prompt, params) -> model_output (str)
        scorer_fn(output, expected) -> score (higher is better)
        """
        self.model_fn = model_fn
        self.scorer_fn = scorer_fn

    def evaluate_candidates(self, candidates: List[PromptCandidate], dataset: List[Tuple[str, str]]):
        """
        dataset: list of (input_payload, expected_output) pairs. The optimizer will format/insert
        the input into candidate.prompt as needed.
        Returns mapping candidate -> avg score.
        """
        results = []
        for cand in candidates:
            scores = []
            for input_text, expected in dataset:
                # For this minimal example, we assume candidate.prompt contains {input}
                prompt_text = cand.prompt.format(input=input_text)
                out = self.model_fn(prompt_text, cand.params)
                score = self.scorer_fn(out, expected)
                scores.append(score)
            avg = sum(scores) / len(scores) if scores else 0.0
            results.append((cand, avg))
        return results

    def best_candidate(self, candidates: List[PromptCandidate], dataset: List[Tuple[str, str]]):
        scored = self.evaluate_candidates(candidates, dataset)
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0] if scored else (None, 0.0)

# Simple scoring: normalized sequence similarity
def similarity_score(output: str, expected: str) -> float:
    return SequenceMatcher(None, output.strip(), expected.strip()).ratio()

# Example simulated model function that depends on prompt wording
def simulated_model(prompt: str, params: dict):
    # Simple rule-based simulator: look for keywords to decide output
    if "Summarize" in prompt:
        return "short summary"
    if "Explain" in prompt:
        return "detailed explanation"
    if "Answer in one word" in prompt:
        # pretend model returns the single token answer extracted from input
        # For testability, we return the input's first word
        content = prompt.split("{input}")[-1] if "{input}" in prompt else prompt
        return content.strip().split()[0] if content.strip() else ""
    # fallback: echo
    return prompt

# Usage example
if __name__ == "__main__":
    candidates = [
        PromptCandidate("Summarize: {input}"),
        PromptCandidate("Explain in detail: {input}"),
        PromptCandidate("Answer in one word: {input}"),
    ]
    dataset = [
        ("This is a long paragraph that needs to be summarized.", "short summary"),
        ("Why is the sky blue?", "detailed explanation"),
        ("Hello world example", "Hello"),
    ]
    optimizer = PromptOptimizer(simulated_model, similarity_score)
    best, score = optimizer.best_candidate(candidates, dataset)
    print("Best prompt:", best.prompt, "score:", score)
    