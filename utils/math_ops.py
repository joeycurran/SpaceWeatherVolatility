def compute_moving_avg(values):
    if not values:
        return 0
    return sum(values) / len(values)

def compute_weighted_avg(values, weights):
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)
