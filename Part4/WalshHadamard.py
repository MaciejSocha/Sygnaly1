from scipy.linalg import hadamard

print(hadamard(256))


def calc(tab):
    nb = tab.__sizeof__()
    print(nb)
