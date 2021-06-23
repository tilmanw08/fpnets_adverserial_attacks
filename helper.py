import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="PyTorch CIFAR TRADES Adversarial Training"
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=128,
        metavar="N",
        help="input batch size for training (default: 128)",
    )
    parser.add_argument(
        "--test-batch-size",
        type=int,
        default=128,
        metavar="N",
        help="input batch size for testing (default: 128)",
    )
    parser.add_argument(
        "--epochs", type=int, default=76, metavar="N", help="number of epochs to train"
    )
    parser.add_argument("--weight-decay", "--wd", default=2e-4, type=float, metavar="W")
    parser.add_argument(
        "--lr", type=float, default=0.1, metavar="LR", help="learning rate"
    )
    parser.add_argument(
        "--momentum", type=float, default=0.9, metavar="M", help="SGD momentum"
    )
    parser.add_argument(
        "--no-cuda", action="store_true", default=False, help="disables CUDA training"
    )
    parser.add_argument("--epsilon", default=0.031, help="perturbation")
    parser.add_argument("--num-steps", default=10, help="perturb number of steps")
    parser.add_argument("--step-size", default=0.007, help="perturb step size")
    parser.add_argument(
        "--beta", default=6.0, help="regularization, i.e., 1/lambda in TRADES"
    )
    parser.add_argument(
        "--seed", type=int, default=1, metavar="S", help="random seed (default: 1)"
    )
    parser.add_argument(
        "--log-interval",
        type=int,
        default=100,
        metavar="N",
        help="how many batches to wait before logging training status",
    )
    parser.add_argument(
        "--model-dir",
        default="./model-cifar-wideResNet",
        help="directory of model for saving checkpoint",
    )
    parser.add_argument(
        "--save-freq", "-s", default=100, type=int, metavar="N", help="save frequency"
    )
    parser.add_argument("--device", type=int, default=None)

    return parser