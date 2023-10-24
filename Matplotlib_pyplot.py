import matplotlib.pyplot as plt


if __name__ == '__main__':


    x = [1, 2, 3, 4 , 5]
    y = []
    for i in x:
        el = i * 10
        y.append(el)


    fig = plt.figure()
    ax= fig.add_subplot()

    ax.plot(x, y, marker= "v", c='darkgreen')
    ax.set_facecolor("whitesmoke")
    ax.set_xlabel("years")
    ax.set_ylabel("población")
    plt.show()
