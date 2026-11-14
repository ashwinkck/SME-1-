import random
from deap import base, creator, tools, algorithms

def evaluate_all_ones(individual):
    """
    STAGE 2: EVALUATION (Our Fitness Function)
    This function counts how many '1's are in the individual's chromosome.
    The maximum possible score is 20 (the length of the chromosome).
    """
    # DEAP expects the fitness function to return a tuple, hence the comma
    return sum(individual),

def main():
    # --- STAGE 1: INITIALIZATION SETUP ---
    # We define that our objective is to MAXIMIZE a value (weight = 1.0)
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    
    # We define an Individual as a list that carries our FitnessMax settings
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # The toolbox holds all our structural configurations
    toolbox = base.Toolbox()
    
    # Define a single Gene: A random choice between 0 or 1
    toolbox.register("attr_binary", random.randint, 0, 1)
    
    # Define a Chromosome: A list repeating our binary gene 20 times
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_binary, n=20)
    
    # Define the Population: A list containing our individuals
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # --- LINKING THE STAGES ---
    toolbox.register("evaluate", evaluate_all_ones)               # Evaluation Step
    toolbox.register("mate", tools.cxTwoPoint)                     # STAGE 4: Two-Point Crossover
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)        # STAGE 5: Mutation (5% chance per gene)
    toolbox.register("select", tools.selTournament, tournsize=3)   # STAGE 3: Tournament Selection

    # --- RUNNING THE LIFECYCLE ---
    # Create an initial population of 100 completely random individuals
    pop = toolbox.population(n=100)
    
    # Track the statistics as the generations pass
    stats = tools.Statistics(lambda ind: ind.fitness.values[0])
    stats.register("Max Score", max)
    stats.register("Average", lambda x: round(sum(x)/len(x), 1))

    print("Starting Evolution Process...\n")
    
    # STAGE 6: REPLACEMENT (The algorithm runs the generational loop automatically)
    final_pop, logbook = algorithms.eaSimple(
        pop, 
        toolbox, 
        cxpb=0.7,    # 70% chance of crossover between parents
        mutpb=0.2,   # 20% chance an individual will undergo mutation
        ngen=30,     # Run for a maximum of 30 generations
        stats=stats, 
        verbose=True # This prints the grid map of statistics per generation
    )

    # Pull the single best candidate from the final generation pool
    best_individual = tools.selBest(final_pop, k=1)[0]
    print(f"\nEvolution Complete!")
    print(f"Best Chromosome Found: {best_individual}")
    print(f"Final Fitness Score:   {best_individual.fitness.values[0]} out of 20")

if __name__ == "__main__":
    main()
