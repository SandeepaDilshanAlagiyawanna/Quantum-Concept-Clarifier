from experta import KnowledgeEngine, Rule, DefFacts, Fact, MATCH

class QuantumFact(Fact):
    """A fact that contains information about a quantum concept."""
    concept = ""
    level = ""  # Explanation level: beginner, intermediate, advanced
    clarification_needed = False

class QuantumExpertSystem(KnowledgeEngine):
    # List to track fired rules
    fired_rules = []
    
    @DefFacts()
    def initial_facts(self):
        """Initialize with some default concepts."""
        yield Fact(ready=True)

    # Entanglement explanations
    @Rule(QuantumFact(concept='entanglement', level='beginner'))
    def explain_entanglement_beginner(self):
        print("Entanglement is when two particles become linked so that measuring one particle's state immediately "
              "determines the state of the other, regardless of distance.")
        self.fired_rules.append("explain_entanglement_beginner")

    @Rule(QuantumFact(concept='entanglement', level='intermediate'))
    def explain_entanglement_intermediate(self):
        print("Entanglement is a quantum phenomenon where particles share a combined quantum state. When you measure "
              "one, the other instantaneously assumes a correlated state, no matter how far apart they are.")
        self.fired_rules.append("explain_entanglement_intermediate")

    @Rule(QuantumFact(concept='entanglement', level='advanced'))
    def explain_entanglement_advanced(self):
        print("In entanglement, quantum systems exhibit correlations that cannot be described independently, "
              "forming a single quantum state with a non-local wavefunction. Measurement on one part influences the whole.")
        self.fired_rules.append("explain_entanglement_advanced")

    # Rules for Superposition
    @Rule(QuantumFact(concept='superposition', level='beginner'))
    def explain_superposition_beginner(self):
        print("Superposition is the ability of a quantum system to be in multiple states at once, like a coin being both heads and tails until observed.")
        self.fired_rules.append("explain_superposition_beginner")

    @Rule(QuantumFact(concept='superposition', level='intermediate'))
    def explain_superposition_intermediate(self):
        print("In quantum mechanics, superposition refers to a system existing simultaneously in multiple possible states, represented by a wavefunction.")
        self.fired_rules.append("explain_superposition_intermediate")

    @Rule(QuantumFact(concept='superposition', level='advanced'))
    def explain_superposition_advanced(self):
        print("Superposition allows a quantum state to be expressed as a linear combination of basis states. Measurement collapses it to one eigenstate.")
        self.fired_rules.append("explain_superposition_advanced")

    # Rules for Quantum Tunneling
    @Rule(QuantumFact(concept='quantum tunneling', level='beginner'))
    def explain_tunneling_beginner(self):
        print("Quantum tunneling is when particles pass through barriers they normally shouldn't, like a ball passing through a wall.")
        self.fired_rules.append("explain_tunneling_beginner")

    @Rule(QuantumFact(concept='quantum tunneling', level='intermediate'))
    def explain_tunneling_intermediate(self):
        print("Quantum tunneling allows particles to move through energy barriers, explained by their wave-like nature and probability distribution.")
        self.fired_rules.append("explain_tunneling_intermediate")

    @Rule(QuantumFact(concept='quantum tunneling', level='advanced'))
    def explain_tunneling_advanced(self):
        print("Quantum tunneling results from the non-zero probability of a particle's wavefunction existing on the other side of a potential barrier.")
        self.fired_rules.append("explain_tunneling_advanced")

    # Rules for Quantum Computing
    @Rule(QuantumFact(concept='quantum computing', level='beginner'))
    def explain_quantum_computing_beginner(self):
        print("Quantum computing uses quantum bits (qubits) that can be in multiple states at once to perform computations much faster than regular computers.")
        self.fired_rules.append("explain_quantum_computing_beginner")

    @Rule(QuantumFact(concept='quantum computing', level='intermediate'))
    def explain_quantum_computing_intermediate(self):
        print("Quantum computers leverage superposition and entanglement to perform parallel computations, making them powerful for certain tasks like factorization.")
        self.fired_rules.append("explain_quantum_computing_intermediate")

    @Rule(QuantumFact(concept='quantum computing', level='advanced'))
    def explain_quantum_computing_advanced(self):
        print("Quantum algorithms, like Shor's and Grover's, exploit quantum parallelism and interference to solve problems exponentially faster than classical algorithms.")
        self.fired_rules.append("explain_quantum_computing_advanced")

    # Rules for Heisenberg Uncertainty Principle
    @Rule(QuantumFact(concept='uncertainty principle', level='beginner'))
    def explain_uncertainty_beginner(self):
        print("The Uncertainty Principle says you can't precisely measure both the position and momentum of a particle at the same time.")
        self.fired_rules.append("explain_uncertainty_beginner")

    @Rule(QuantumFact(concept='uncertainty principle', level='intermediate'))
    def explain_uncertainty_intermediate(self):
        print("Heisenberg's Uncertainty Principle implies that measuring a particle's position more precisely makes its momentum less certain, and vice versa.")
        self.fired_rules.append("explain_uncertainty_intermediate")

    @Rule(QuantumFact(concept='uncertainty principle', level='advanced'))
    def explain_uncertainty_advanced(self):
        print("Mathematically, the Uncertainty Principle is expressed as Δx * Δp ≥ ħ/2, where Δx and Δp are the uncertainties in position and momentum.")
        self.fired_rules.append("explain_uncertainty_advanced")

    # Rules for Quantum Measurement
    @Rule(QuantumFact(concept='quantum measurement', level='beginner'))
    def explain_measurement_beginner(self):
        print("In quantum physics, measuring a system changes its state. For example, observing a particle collapses its wavefunction.")
        self.fired_rules.append("explain_measurement_beginner")

    @Rule(QuantumFact(concept='quantum measurement', level='intermediate'))
    def explain_measurement_intermediate(self):
        print("Quantum measurement involves collapsing a superposition into one of its possible states, determined probabilistically by the wavefunction.")
        self.fired_rules.append("explain_measurement_intermediate")

    @Rule(QuantumFact(concept='quantum measurement', level='advanced'))
    def explain_measurement_advanced(self):
        print("Measurement in quantum mechanics is a non-unitary process that collapses the system's state vector to an eigenstate of the observable.")
        self.fired_rules.append("explain_measurement_advanced")

    # Rules for Quantum Cryptography
    @Rule(QuantumFact(concept='quantum cryptography', level='beginner'))
    def explain_cryptography_beginner(self):
        print("Quantum cryptography uses the principles of quantum mechanics to secure communication, making it impossible to eavesdrop without being detected.")
        self.fired_rules.append("explain_cryptography_beginner")

    @Rule(QuantumFact(concept='quantum cryptography', level='intermediate'))
    def explain_cryptography_intermediate(self):
        print("Quantum cryptography relies on quantum key distribution (QKD), which ensures that any interception of the key changes its state, alerting the users.")
        self.fired_rules.append("explain_cryptography_intermediate")

    @Rule(QuantumFact(concept='quantum cryptography', level='advanced'))
    def explain_cryptography_advanced(self):
        print("Protocols like BB84 use quantum superposition and entanglement to establish secure communication channels, with security guaranteed by quantum mechanics.")
        self.fired_rules.append("explain_cryptography_advanced")

    # Rules for Superconductivity
    @Rule(QuantumFact(concept='superconductivity', level='beginner'))
    def explain_superconductivity_beginner(self):
        print("Superconductivity is a phenomenon where a material can conduct electricity without resistance at very low temperatures.")
        self.fired_rules.append("explain_superconductivity_beginner")

    @Rule(QuantumFact(concept='superconductivity', level='intermediate'))
    def explain_superconductivity_intermediate(self):
        print("Superconductivity is a state in which a material exhibits zero electrical resistance and the expulsion of magnetic fields, occurring below a critical temperature.")
        self.fired_rules.append("explain_superconductivity_intermediate")

    @Rule(QuantumFact(concept='superconductivity', level='advanced'))
    def explain_superconductivity_advanced(self):
        print("Superconductivity is a quantum mechanical phenomenon where electron pairs form Cooper pairs that move without scattering, resulting in zero resistance.")
        self.fired_rules.append("explain_superconductivity_advanced")
    
    # Handle unclear questions (clarification needed)
    @Rule(QuantumFact(clarification_needed=True))
    def ask_for_clarification(self):
        print("Can you clarify your question? For example, specify whether you want to learn about superposition, entanglement, or another topic.")
        self.fired_rules.append("ask_for_clarification")

    # Step 4: Print Conflict Set (Facts) without agenda
    def print_conflict_set(self):
        print("\n[Conflict Set] (Facts known to the engine):")
        for fact in self.facts.values():  # Iterate through all facts in the engine
            # Check if the fact is an instance of QuantumFact and contains 'concept' and 'level' keys
            if isinstance(fact, QuantumFact):
                if 'concept' in fact and 'level' in fact:
                    print(f"- Concept: {fact['concept']}, Level: {fact['level']}")
                else:
                    print(f"- Concept: Unknown")
    # Run the system and gather results
    def run_system(self):
        self.reset()  # Reset the engine
        self.run()  # Run the engine

    # Step 5: Print Fired Rules (Resolution)
    def print_resolution(self):
        print("\n[Resolution] Fired rules:")
        for rule in self.fired_rules:
            print(f"- Rule: {rule}")
        self.fired_rules.clear()  # Reset fired rules after printing


