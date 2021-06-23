import os
from autoattack import AutoAttack
import torch

from fp_net_after_jov.models import model_getter
from DLBio.pt_training import set_device
from TRADES import train_trades_cifar10
import helper


model_types = ["CifarJOVFPNet"]  # ["CifarResNet", "CifarPyrResNet", "CifarJOVFPNet"]
Ns = [5, 7]

for model_type in model_types:
    for N in Ns:
        parser = helper.get_parser()
        options = parser.parse_args()
        options.model_dir = f"./Experiments/CIFAR10/{model_type}_N{N}"
        set_device(options.device)

        model = model_getter.get_model(
            model_type=model_type,
            input_dim=3,
            output_dim=10,
            device="cuda:0",
            N=[N],
            q=[2],
        )

        model = train_trades_cifar10.main(model, options)

        _, test_loader = train_trades_cifar10.get_loader(
            options, {"num_workers": 1, "pin_memory": True}
        )
        l = [x for (x, y) in test_loader]
        x_test = torch.cat(l, 0)
        l = [y for (x, y) in test_loader]
        y_test = torch.cat(l, 0)
        print(x_test.shape)

        adversary_linf = AutoAttack(
            model,
            norm="Linf",
            eps=8.0 / 255.0,
            version="standard",
            log_path=options.model_dir + "/log_file_Linf.txt",
        )
        x_adv = adversary_linf.run_standard_evaluation(x_test, y_test, bs=128)