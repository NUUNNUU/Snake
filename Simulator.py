import numpy as np


class Simulator:
    def __init__(self, *args, **kwargs):
        """
        Parameters
        ----------
        time : Maximum simulation time (min 0, max 60) (unit: sec)
        time_stp : Simulation time step (min 0.0001, max 0.1) (unit: sec)
        nlink : The number of links in simulation model (min 1)
        """
        self.time = args[0]
        self.time_stp = args[1]
        self.nlink = args[2]

        # parameters error check
        if type(self.time) is not float and type(self.time) is not int:
            raise TypeError("func <__init__> param <time> parameter type should be float")
        if self.time < 1 or self.time > 60:
            raise ValueError("func <__init__> param <time> parameter out of max/min range (min 1, max 60)")
        
        if type(self.time_stp) is not float and type(self.time_stp) is not int:
            raise TypeError("func <__init__> param <timestp> parameter type should be float")
        if self.time_stp < 0.0001 or self.time_stp > 0.1:
            raise ValueError("func <__init__> param <timestp> parameter out of max/min range (min 0.0001, max 0.1)")

        if type(self.nlink) is not int:
            raise TypeError("func <__init__> param <nlink> parameter type should be int")
        if self.nlink < 1:
            raise ValueError("func <__init__> param <nlink> parameter out of min range (min 1)")

        # records current simulation time
        self.sim_time = 0

    def calc(self, soln_0, force_func):
        """This function Calculates trajectory for given initial condition.

        Parameters
        ----------
        soln_0 : ndarray of size (12, nlink)
            Initial condition
        force_func : function
            Function which accepts current positions, derivatives of positions as inputs
            and returns corresponding acceleration values.
        """

        # check whether initial solution is valid or not
        if type(soln_0) is not np.ndarray:
            raise TypeError("func <calc> param <soln_0> parameter type should be np.ndarray")
        else:
            if soln_0.shape != (12, self.nlink):
                raise ValueError("func <calc> param <soln_0> parameter size should be (12, nlink)")
            if soln_0.dtype is not np.float64:
                soln_0.astype(np.float64)
        
        # check whether force function is valid or not

        # soln_all array for saving all the solution for every time step
        num_time_stp = int(self.time / self.time_stp) + 1
        soln_all = np.ndarray((num_time_stp, 12, self.nlink), dtype=np.float64)

        # set initial condition and iteration counter
        iter = 0
        soln_all[iter, :, :] = soln_0

        while iter < num_time_stp - 1:
            # update iter
            iter += 1

            # calculate accelerations
            acc = force_func(soln_all[iter, :, :]) # acceleration vector of shape (6, nlink)
            
            # modify positions and derivatives
            delta_vel = acc * self.time_stp
            delta_pos = delta_vel * self.time_stp
            soln_delta = np.vstack((delta_pos, delta_vel))

            # save new solution to soln_all array
            soln_all[iter, :, :] = soln_all[iter - 1, :, :] + soln_delta

        return soln_all

    def __str__(self):
        sum_str = "Simulation time: %.4g \nSimulation time step: %.4g \nNumber of links: %d" \
                  % (self.time, self.time_stp, self.nlink)

        return sum_str


def dummy(a):
    return np.zeros((6, 1))


if __name__ == "__main__":
    sim = Simulator(1, 0.01, 1)
    print(sim)

    soln_0 = np.zeros((12, 1))
    soln = sim.calc(soln_0, dummy)
    print(soln.shape)
    print(soln.dtype)