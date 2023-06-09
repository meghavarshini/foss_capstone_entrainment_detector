from ecdc import *
import argparse
import pdb
import numpy as np
import random
import os

os.getcwd()

SEED=448

def make_argument_parser():
    parser = argparse.ArgumentParser(description='entrainment testing')
    parser.add_argument('--no-cuda', action='store_true',
                        default=False,
                        help='enables CUDA training')
    parser.add_argument('--seed', type=int,
                        default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--hff', default= '../baseline_1_h5/test_ASIST3_nonorm.h5',
                        help='location of h5 file with the test data')
    parser.add_argument('--model_name',
                        default= "../baseline_1_models/trained_VAE_nonorm_nopre_l1.pt",
                        help='name associated with the trained model')
    # args = parser.parse_args()
    return parser



def load_h5(file):
    print("loading h5 file: ", file)
    file = h5py.File(file, 'r')
    test = np.array(file['dataset'])
    print("loading complete!")
    return test

def model_testing(model_name, X_test,cuda):

    model = VAE().double()
    model = torch.load(model_name)
    model.eval()
    if cuda:
        model.cuda()
    if 'l1' in model_name:
        p=1
    elif 'l2' in model_name:
        p=2
    else:
        print("need better model name")
        p=2

        pdb
    test_loss = 0
    fake_test_loss = 0
    Loss=[]
    Fake_loss = []

    for idx, data in enumerate(X_test):
        print("working on instance: ", idx)


        print("length of test set list: ", len(data))


        x_data = data[:228]
        y_data = data[228:-1]


        idx_same_spk =list(np.where(X_test[:,-1]==data[-1]))[0]

        ll = random.choice(list(set(idx_same_spk) - set([idx])))
        spk = int(data[-1])

        x_data = torch.from_numpy(x_data)
        y_data = torch.from_numpy(y_data)


        y_fake_data = X_test[ll,228:-1]

        y_fake_data = torch.from_numpy(y_fake_data)
        print("data loaded!")

        if cuda:
            x_data = x_data.cuda()
            y_data = y_data.cuda()
            y_fake_data = y_fake_data.cuda()

        recon_batch = model(x_data)


        z_x = model.embedding(x_data)
        z_y = model.embedding(y_data)

        loss_real = lp_distance(z_x, z_y, p).data
        # loss_real = loss_function(z_x, z_y, mu, logvar)

      
        z_y_fake = model.embedding(y_fake_data)

        loss_fake = lp_distance(z_x, z_y_fake, p).data

        test_loss += loss_real
        fake_test_loss += loss_fake
        print("model run complete!")

        Loss.append(loss_real.cpu())
        Fake_loss.append(loss_fake.cpu())

    # print loss_real, loss_fake
    test_loss /= X_test.shape[0]
    fake_test_loss /= X_test.shape[0]
    Loss = np.array(Loss)
    Fake_loss = np.array(Fake_loss)

    print("Total Real Loss: "+ str(test_loss))
    print("Total Fake Loss: " + str(fake_test_loss))

    print(float(np.sum(Loss < Fake_loss))/Loss.shape[0])
    return None


if __name__ == "__main__":
    os.getcwd()
    parser = make_argument_parser()
    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()

    torch.manual_seed(args.seed)

    if not args.no_cuda and torch.cuda.is_available():
        torch.cuda.manual_seed(args.seed)

    X_test1 = load_h5(args.hff)
    test_run = model_testing(args.model_name, X_test1, args.cuda)
