class Simulator:
    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        time : Maximum simulation time (min 0, max 60) (unit: sec)
        timestp : Simulation time step (min 0.0001, max 0.1) (unit: sec)
        nlink : The number of links in simulation model (min 1)
        """
        self.time = args[0]
        self.timestp = args[1]
        self.nlink = args[2]

        # parameters error check
        if type(self.time) is not float and type(self.time) is not int:
            raise TypeError("func <__init__> param <time> parameter type should be float")
        if self.time < 1 or self.time > 60:
            raise ValueError("func <__init__> param <time> parameter out of max/min range (min 1, max 60)")
        
        if type(self.timestp) is not float and type(self.timestp) is not int:
            raise TypeError("func <__init__> param <timestp> parameter type should be float")
        if self.timestp < 0.0001 or self.timestp > 0.1:
            raise ValueError("func <__init__> param <timestp> parameter out of max/min range (min 0.0001, max 0.1)")

        if type(self.nlink) is not int:
            raise TypeError("func <__init__> param <nlink> parameter type should be int")
        if self.nlink < 1:
            raise ValueError("func <__init__> param <nlink> parameter out of min range (min 1)")

    def calc(self, soln_0):
        """This function Calculates trajectory for given initial condition.

        Parameters
        ----------
        soln_0 : Initial condition
        """

    def __str__(self):
        sum_str = "Simulation time: %.4g \nSimulation time step: %.4g \nNumber of links: %d" \
                  % (self.time, self.timestp, self.nlink)

        return sum_str


if __name__ == "__main__":
    sim = Simulator(1, 0.001, 1)
    print(sim)
