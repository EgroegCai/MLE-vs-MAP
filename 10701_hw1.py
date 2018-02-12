import matplotlib.pyplot as plt
from scipy.stats import beta
import numpy as np
import math


def plotMLE(X,Theta):
    X_s = sum(X)
    n = len(X)
    P = map(lambda theta: math.log(math.pow(1.0-theta,X_s)*math.pow(theta,float(n))), Theta)
    max_p = max(P)
    max_theta = Theta[P.index(max_p)]

    plt.plot(Theta,P,label="%d data points (MLE)"% n)
    plt.plot(max_theta,max_p,marker='o')
    plt.title(r"log-likelihood function $l(\theta)$ vs $\theta$")
    plt.legend(loc="lower left")
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$l(\theta)$")

def plotMAP(X,Theta,a,b):
    X_s = sum(X)
    n = len(X)
    P = map(lambda theta: math.log(math.pow(1.0-theta,X_s)*math.pow(theta,float(n))*beta.pdf(theta,a,b)), Theta)
    max_p = max(P)
    max_theta = Theta[P.index(max_p)]

    plt.plot(Theta,P,label="%d data points (MAP)" % n)
    plt.plot(max_theta,max_p,marker='o')
    plt.title(r"log-posterior function $l(\theta)$ vs $\theta$")
    plt.legend(loc="lower left")
    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$l(\theta)$")



def main():
    Theta = np.linspace(0.001,1.0,100,endpoint=False)
    plotMLE(x1,Theta)
    plotMLE(x2,Theta)
    plotMLE(x3,Theta)
    plt.savefig("MLE")
    plotMAP(x1,Theta,1,2)
    plotMAP(x2,Theta,1,2)
    plotMAP(x3,Theta,1,2)
    plt.savefig("MAP")

    return 0

# input
x1 = [0,21,23,8,9]
x2 = [0,21,23,8,9,2,9,0,7,8]
x3 = [0,21,23,8,9,2,9,0,7,8,20,9,7,4,17]

main()
