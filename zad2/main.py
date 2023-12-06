from simulation import Simulation

# Example usage
simulation = Simulation(num_sheep=15, limit=10.0, sheep_movement=0.5, wolf_movement=1.0, max_rounds=50)
simulation.run()
