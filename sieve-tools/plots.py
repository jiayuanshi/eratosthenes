from matplotlip import pyplot as plt

def plot_sieve(all_nmax, all_propotions, log_scale = False):
    plt.plot(all_nmax, all_proportions)
    plt.xlabel("N")
    plt.ylabel("Proportion of primer numbers")