def apply_behavioral_bias(prior_belief, trust_score):
    # If trust is 1.0, the farmer believes everything.
    # If trust is 0.5, the farmer is skeptical.
    # This formula mixes the two together.
    return (trust_score * prior_belief) + ((1 - trust_score) * 0.5)