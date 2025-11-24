from utils.math_ops import compute_weighted_avg

def process_scores(scores, weights):
    return compute_weighted_avg(scores, weights)
