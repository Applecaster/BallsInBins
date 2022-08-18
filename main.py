import argparse
import sys
from balls_in_bins import distribute_balls_in_bins


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prints all the possible ways to distribute N balls into M bins, "
                                                 "where each bin i has a maximum Mi capacity.")
    parser.add_argument('--balls', metavar='N', required=True, type=int,
                        help='Number of balls to distribute into bins')
    parser.add_argument('--max_balls_per_bin', metavar=('m1', 'm2'), required=True, nargs='+', type=int,
                        help="Maximum balls that each bin can contain. "
                             "This variable also represents the amount of bins used")

    args = parser.parse_args()

    print(distribute_balls_in_bins(args.balls, len(args.max_balls_per_bin), args.max_balls_per_bin))
