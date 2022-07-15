def distribute_balls_in_bins(balls_num: int, bins_num: int, max_balls_per_bin: list) -> list[list]:
    """
    Return all the possible ways to distribute balls into separate bins.
    Each bin has a different maximum capacity.

    :param balls_num: The amount of balls to distribute into bins.
    :param bins_num: The amount of bins that contain balls.
    :param max_balls_per_bin: The maximum amount of balls each bin can contain.
    :return: List of possible distributions. Each distribution is a list of balls-per-bin (distribution[bin]=balls).
    """
    assert bins_num == len(max_balls_per_bin)

    # If the total number of balls is more than the bins can contain, there's no solution.
    max_balls_to_distribute = sum(max_balls_per_bin)
    if balls_num > max_balls_to_distribute:
        return []

    # If the number of balls to distribute is 0, the solution is a list of zeroes.
    # (For 0 bins - an empty list is a correct solution)
    if balls_num == 0:
        return [[0] * bins_num]

    # If there's one bin, put the rest of the balls in it.
    if bins_num == 1:
        return [[balls_num]]

    # There's more than one bin to distribute the balls into. Let's start recursion fun.
    distributions = []
    possibilities_for_balls_in_first_bin = range(min(max_balls_per_bin[0], balls_num) + 1)
    bins_left = bins_num - 1
    max_balls_per_bin_left = max_balls_per_bin[1:]

    # For every possible way to put balls in the first bin,
    # we'll check the possible ways to distribute the rest of the balls.
    for balls_in_first_bin in possibilities_for_balls_in_first_bin:
        balls_left_to_distribute = balls_num - balls_in_first_bin

        distributions_after_first_bin = distribute_balls_in_bins(balls_left_to_distribute,
                                                                 bins_left,
                                                                 max_balls_per_bin_left)

        if not distributions_after_first_bin:
            continue

        for distribution in distributions_after_first_bin:
            possible_distribution = [balls_in_first_bin] + distribution
            distributions.append(possible_distribution)

    return distributions
