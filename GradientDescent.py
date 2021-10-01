import pandas
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class GradientDescent:

    def __init__(self, pathData, iterations=2000, learningRate=0.1):
        self.theta0 = 0
        self.theta1 = 0
        self.normalizedTheta0 = 0
        self.normalizedTheta1 = 0
        self.x = 0
        self.y = 0
        self.normalizedX = 0
        self.normalizedY = 0
        self.lenData = 0
        self.data = self.processData(pathData)
        self.iterations = iterations
        self.learningRate = learningRate

    def processData(self, pathData):
        # TO DO : to protect
        self.data = pandas.read_csv(pathData)
        self.x = self.data['km'].values
        self.y = self.data['price'].values
        self.normalizedX = self.normalizer(self.x)
        self.normalizedY = self.normalizer(self.y)
        self.lenData = len(self.x)      # TO DO : PROTECT !!!

    def normalizer(self, values):

        normalizedValues = (values - min(values)) / (max(values) - min(values))

        return normalizedValues

    def denormalizer(self):
        # TO DO : take off useless bracket
        self.theta1 = (max(self.y) - min(self.y)) * self.normalizedTheta1 / (max(self.x) - min(self.x))
        self.theta0 = min(self.y) + ((max(self.y) - min(self.y)) * self.normalizedTheta0) + self.theta1 * (1 - min(self.x))

    def estimatePrice(self, x, theta0, theta1):

        y = theta0 + theta1 * x

        return y

    def doGradientDescent(self):

        for i in range(self.iterations):
            total1 = 0
            total2 = 0

            for i in range(self.lenData):
                
                # TO DO : take off useless bracket
                total1 -= self.estimatePrice(self.normalizedX[i], self.normalizedTheta0, self.normalizedTheta1) \
                    - self.normalizedY[i]
                total2 -= (self.estimatePrice(self.normalizedX[i], self.normalizedTheta0, self.normalizedTheta1) \
                    - self.normalizedY[i]) * self.normalizedX[i]

            self.normalizedTheta0 += self.learningRate * (total1 / self.lenData)
            self.normalizedTheta1 += self.learningRate * (total2 / self.lenData)


            if(i < 500) or (i > 500 and i % 10 == 0):
                plt.plot(self.normalizedX, self.estimatePrice(self.normalizedX, self.normalizedTheta0, self.normalizedTheta1))

        self.denormalizer()

if __name__ == "__main__":

    fig = figure(figsize=(20, 15), dpi=80)
    fig.add_subplot(221)

    learn = GradientDescent('files/data.csv')
    learn.doGradientDescent()
    
    print(f'\ntheta0 = {learn.theta0} and theta1 = {learn.theta1}\n')

    plt.plot(learn.normalizedX, learn.normalizedY, 'bo')
    plt.ylabel('normalized price')
    plt.xlabel('normalized mileage')

    fig.add_subplot(222)
    plt.plot(learn.x, learn.y, 'bo')
    plt.plot(learn.x, learn.estimatePrice(learn.x, learn.theta0, learn.theta1))
    plt.ylabel('price')
    plt.xlabel('mileage (Km)')

    # fig.add_subplot(212)
    # plt.plot(learn.normalizedX, learn.normalizedY, 'bo')

    plt.show()