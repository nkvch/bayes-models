from pomegranate import *
from random import random
from input import *


class BNGenerator:
    def __init__(self, bn):
        self.network = bn
        self.table = {}
        self.vars_num = len(bn)

    def is_independent(self):
        pass

    def generate_all_samples(self):
        samples = []
        # binary numbers generation
        for i in range(0, 2 ** self.vars_num):
            b = bin(i)[2:]
            samples.append(str(b).zfill(self.vars_num))
        return samples

    def sort_table(self):
        self.table['probabilities'] = {
          k: v for k, v in sorted(self.table['probabilities'].items(), key=lambda item: item[1])
        }

    def generate(self):
        order = []
        while len(order) < self.vars_num:
            portion = [
                node[0] for node in self.network.items()
                if
                node[0] not in order and
                all(parent in order for parent in node[1]['depends_on'])
            ]
            order.extend(portion)
        samples = self.generate_all_samples()
        table = {
            'depends_on': order,
            'probabilities': {}
        }
        for sample in samples:
            acc = 1
            values = list(sample)
            matched = dict(zip(order, values))
            for node in order:
                value = matched[node]
                if not self.network[node]['depends_on']:
                    prob = self.network[node]['probabilities']
                    acc *= prob if not not eval(value) else 1 - prob
                else:
                    case = ''.join(list(map(lambda name: matched[name], self.network[node]['depends_on'])))
                    prob = self.network[node]['probabilities'][case]
                    acc *= prob if not not eval(value) else 1 - prob
            table['probabilities'][sample] = acc
        self.table = table
        self.sort_table()

    def get_probability(self, name, value):
        index = self.table['depends_on'].index(name)
        cases = [sample_prob[1] for sample_prob in self.table['probabilities'].items() if sample_prob[0][index] == value]
        return sum(cases)
    

    def generate_sample(self):
        items = self.table['probabilities'].items()
        rand = random()
        acc = 0
        for item in items:
            sample, prob = item
            if rand <= acc + prob:
                return sample
            else:
                acc += prob

    
    def generate_samples(self, number):
        samples = {
            'headers': self.table['depends_on'],
            'values': [],
            'length': number,
        }

        for _ in range(number):
            sample = self.generate_sample()
            samples['values'].append(sample)
        return samples

    def compare_samples_with_probs(self, samples):
        print('sample'.rjust(25) + '|' + 'probability'.rjust(25) + '|' + 'frequency'.rjust(25))
        print('_'*77)
        for item in self.table['probabilities'].items():
            sample, prob = item
            frequency = samples['values'].count(sample)/samples['length']
            print(sample.rjust(25) + '|' + str(prob).rjust(25) + '|' + str(frequency).rjust(25))
            print('_'*77)

    def print_prob_table(self):
        headers = '|'.join([*[header.rjust(22) for header in self.table['depends_on']], 'probability'.rjust(22)])
        line_len = len(headers)
        print(headers)
        print('_'*line_len)
        for item in self.table['probabilities'].items():
            sample, prob = item
            
            print('|'.join([*[val.rjust(22) for val in sample], str(prob).rjust(22)]))
            print('_'*line_len)



def main():
    generator = BNGenerator(bayesian_network)

    generator.generate()

    generator.print_prob_table()

    samples = generator.generate_samples(10)
    generator.compare_samples_with_probs(samples)


if __name__ == '__main__':
    main()
