import simpy
import random

class DistributedSystem:
    def __init__(self, env, num_processes, num_sites=2):
        self.env = env
        self.num_processes = num_processes
        self.num_sites = num_sites

        # Wait-For Graph
        self.wait_graph = {f"P{i}": [] for i in range(num_processes)}

        # Assign processes to sites
        self.process_site = {
            f"P{i}": f"S{random.randint(0, num_sites-1)}"
            for i in range(num_processes)
        }

    def request_resource(self, process):
        other = f"P{random.randint(0, self.num_processes-1)}"
        if other != process and other not in self.wait_graph[process]:
            self.wait_graph[process].append(other)

    def run(self):
        while True:
            yield self.env.timeout(1)
            process = f"P{random.randint(0, self.num_processes-1)}"
            self.request_resource(process)