import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    crop = np.loadtxt('./data/augWUR_crop.txt').astype(int)
    weed = np.loadtxt('./data/augWUR_weed.txt').astype(int)

    crop_true = crop[:, 0]
    crop_predicted = crop[:, 1]

    weed_true = weed[:, 0]
    weed_predicted = weed[:, 1]

    n = np.max(crop)+1
    # n = 18
    res = np.zeros((n, n))
    # res = np.zeros((26, 26))

    for i in range(0, n):

        for j, val in enumerate(crop_true):

            if val == i:
                pred = crop_predicted[j]
                res[val, pred] += 1

    np.savetxt('./results/crop.txt', res)

    plt.matshow(res)
    plt.colorbar()
    plt.xlabel('True number of crops')
    plt.ylabel('Detected number of crops')

    column_sum = np.sum(res, axis=0)

    for i, val in enumerate(column_sum):
        if val != 0:
            res[:, i] /= val

    np.savetxt('./results/crop_norm.txt', res)
    np.savetxt('./results/crop_count.txt', column_sum)

    # print(res)

    plt.matshow(res)
    plt.colorbar()
    plt.xlabel('True number of crops')
    plt.ylabel('Detected number of crops')

    crop_max = np.max(crop)+1
    n = 13
    bin = crop_max/n
    res = np.zeros((n+1, n+1))

    for gt, dt in zip(crop_true, crop_predicted):
        res[int(round(gt/bin)), int(round(dt/bin))] += 1

    #plt.matshow(res)
    #plt.colorbar()
    #plt.xlabel('True number of crops')
    #plt.ylabel('Detected number of crops')
    n = np.max(weed)+1
    n = 14
    res = np.zeros((n, n-1))

    for i in range(0, n):

        for j, val in enumerate(weed_true):
            pred = weed_predicted[j]

            if val >= 13:
                if pred >= 13:
                    res[-1, -1] += 1
                else:
                    res[-1, pred] += 1

            else:
                if val == i:
                    if pred >= 13-1:
                        res[val, -1] += 1
                    else:
                        res[val, pred] += 1

    #np.savetxt('./results/weed.txt', res)

    plt.matshow(res)
    plt.colorbar()
    plt.xlabel('True number of weeds')
    plt.ylabel('Detected number of weeds')

    column_sum = np.sum(res, axis=0)
    print(column_sum.shape)

    for i, val in enumerate(column_sum):
        if val != 0:
            res[:, i] /= val

	'''
    np.savetxt('./results/weed_norm.txt', res)
    np.savetxt('./results/weed_count.txt', column_sum)
	'''
    plt.matshow(res)
    plt.colorbar()
    plt.xlabel('True number of weeds')
    plt.ylabel('Detected number of weeds')

    weed_max = np.max(weed)+1
    n = 13
    bin = weed_max/n
    res = np.zeros((n+1, n+1))

    # for gt, dt in zip(weed_true, weed_predicted):
    #    res[int(round(gt/bin)), int(round(dt/bin))] += 1

    #plt.matshow(res)
    #plt.colorbar()
    #plt.xlabel('True number of weeds')
    #plt.ylabel('Detected number of weeds')

    plt.show()


