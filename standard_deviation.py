class StandardDeviation:
    n_values = 0
    def __init__(self, *values):
        self.values = values
        for i in values:
            self.n_values += 1

    def __compute_mean(self):
        total = 0
        for i in self.values:
            total += i
        
        return total/self.n_values
 
    def population_standard_deviation(self):
        total = 0
        mean = self.__compute_mean()
        for v in self.values:
            total += (v - mean) ** 2

        return (total/ self.n_values) ** (0.5)




    




