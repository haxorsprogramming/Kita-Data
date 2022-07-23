import unittest
import numpy as np
from numpy import inf
# import time
import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)


from tqdm import tqdm
import time

bar = tqdm(range(10), desc="Testing process - Jenkins | Perhitungan ANP")

d = np.array([[3, 5, 3, 6, 9], [8, 1, 2, 4, 2], [3, 6, 9, 8, 3],
             [1, 2, 4, 2, 3], [3, 5, 2, 4, 2], [1, 9, 1, 7, 9]])

iteration = 100
n_ants = 5
n_citys = 5

m = n_ants
n = n_citys
e = .5
alpha = 1
beta = 2

visibility = 1 / d
visibility[visibility == inf] = 0

pheromne = .1 * np.ones((m, n))

rute = np.ones((m, n + 1))


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    ord = 0
    for ite in range(iteration):
        logging.debug("Testing iterasi ke : "+str(ord)+" hasil : SUCCESS")
        ord += 1
        rute[:, 0] = 1

        for i in range(m):

            temp_visibility = np.array(visibility)

            for j in range(n - 1):
                combine_feature = np.zeros(5)
                cum_prob = np.zeros(5)

                cur_loc = int(rute[i, j] - 1)

                temp_visibility[:, cur_loc] = 0

                p_feature = np.power(pheromne[cur_loc, :], beta)
                v_feature = np.power(temp_visibility[cur_loc, :], alpha)

                p_feature = p_feature[:, np.newaxis]
                v_feature = v_feature[:, np.newaxis]

                combine_feature = np.multiply(p_feature, v_feature)

                total = np.sum(combine_feature)

                probs = combine_feature / total

                cum_prob = np.cumsum(probs)
                r = np.random.random_sample()
                city = np.nonzero(cum_prob > r)[0][0] + 1

                rute[i, j + 1] = city

            left = list(set([i for i in range(1, n + 1)]) - set(rute[i, :-2]))[0]

            rute[i, -2] = left

    rute_opt = np.array(rute)

    dist_cost = np.zeros((m, 1))

    for i in range(m):

        s = 0
        for j in range(n - 1):
            s = s + d[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1]

        dist_cost[i] = s

    dist_min_loc = np.argmin(dist_cost)
    dist_min_cost = dist_cost[dist_min_loc]

    best_route = rute[dist_min_loc, :]
    pheromne = (1 - e) * pheromne

    for i in range(m):
        for j in range(n - 1):
            dt = 1 / dist_cost[i]
            pheromne[int(rute_opt[i, j]) - 1, int(rute_opt[i, j + 1]) - 1] = pheromne[int(rute_opt[i, j]) - 1, int(
                rute_opt[i, j + 1]) - 1] + dt


for i in bar:
  time.sleep(1)

if __name__ == '__main__':
    unittest.main()
