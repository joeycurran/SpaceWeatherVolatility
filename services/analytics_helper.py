from utils.math_ops import compute_moving_avg

def normalise_scores(score_list):
    avg = compute_moving_avg(score_list)
    return [s - avg for s in score_list]
