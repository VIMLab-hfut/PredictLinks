import argparse
from seal_link_predict import *


def parse_args(data="Random29888", epoch=1, lr=0.00001, is_directed=0):
    parser = argparse.ArgumentParser(description="Link prediction with SEAL.")
    parser.add_argument("--data", type=str, default=data,help="data name." )
    parser.add_argument("--epoch", type=int, default=epoch, help="epochs of gnn")
    parser.add_argument("--learning_rate", type=float, default=lr, help="learning rate")
    parser.add_argument("--is_directed",  type=int, default=0, help="use 0, 1 stands for undirected or directed graph")
    parser.add_argument("--test_ratio", type=float, default=0.360575, help="ratio of testing set")
    parser.add_argument("--hop", default=1, help="option: 0, 1, ... or 'auto'.")
    parser.add_argument("--dimension", type=int, default=128, help="number of embedding.")
    return parser.parse_args()


def seal_for_link_predict():
    args = parse_args()
    classifier(args.data, args.is_directed, args.test_ratio, args.dimension, args.hop, args.learning_rate, epoch=args.epoch)

if __name__ == "__main__":
    seal_for_link_predict()