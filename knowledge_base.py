from experta import KnowledgeEngine, Rule, DefFacts, Fact, MATCH

class QuantumFact(Fact):
    concept =""
    level =""
    confidence = 1.0
    # Store alternate explanations    

class QuantumExpertSystem(KnowledgeEngine):
    fired_rules = []
    explanation_output = ""
    alternate_solutions = ""
    confidence_scores = {}
    current_confidence=""
    
    def get_solution(self):
        return self.explanation_output
    
    # Use Experta's fact-handling system, not a manual list
    def get_alternate_solutions(self):
        return self.alternate_solutions

    @DefFacts()
    def initial_facts(self):
        """Initialize with some default concepts."""
        yield Fact(ready=True)
    
    def append_explanation(self, text, confidence):
        """Append explanations with confidence."""
        self.explanation_output += f"{text} (Confidence: {confidence * 100:.1f}%)\n"
        self.current_confidence = confidence

    # Modified method to provide alternate solutions
    def add_alternate_solution(self, solution, confidence):

        self.alternate_solutions=""
        """Add alternate explanations with confidence."""
        self.alternate_solutions += f"{solution} (Confidence: {confidence * 100:.1f}%)\n"

    @Rule(QuantumFact(concept='entanglement', level='beginner'))
    def explain_entanglement_beginner(self):
        confidence = 0.9  # High confidence for fundamental concept explanations
        self.append_explanation(
            "Entanglement is when two particles become linked so that measuring one particle's state immediately determines the state of the other, regardless of distance.",
            confidence
        )
        # Alternate solution
        self.add_alternate_solution(
            "In simpler terms, imagine two coins flipped at the same time. Even if they are far apart, if you see one coin as heads, you immediately know the other is tails.",
            0.85
        )
        self.fired_rules.append("explain_entanglement_beginner")
        self.confidence_scores["explain_entanglement_beginner"] = confidence

    @Rule(QuantumFact(concept='entanglement', level='intermediate'))
    def explain_entanglement_intermediate(self):
        confidence = 0.92
        self.append_explanation(
            "Entanglement is a quantum phenomenon where particles share a combined quantum state. When you measure one, the other instantaneously assumes a correlated state, no matter how far apart they are.",
            confidence
        )
        # Alternate solution
        self.add_alternate_solution(
            "Think of entanglement as a pair of dice: even when separated, the outcome of one die roll will determine the outcome of the other due to their quantum link.",
            0.88
        )
        self.fired_rules.append("explain_entanglement_intermediate")
        self.confidence_scores["explain_entanglement_intermediate"] = confidence

    @Rule(QuantumFact(concept='entanglement', level='advanced'))
    def explain_entanglement_advanced(self):
        confidence = 0.97
        self.append_explanation(
            "In entanglement, quantum systems exhibit correlations that cannot be described independently, forming a single quantum state with a non-local wavefunction. Measurement on one part influences the whole.",
            confidence
        )
        # Alternate solution
        self.add_alternate_solution(
            "Advanced entanglement involves non-locality and quantum correlations, where the measurement of one particle's state directly influences the state of its entangled partner, even if they are light-years apart.",
            0.95
        )
        self.fired_rules.append("explain_entanglement_advanced")
        self.confidence_scores["explain_entanglement_advanced"] = confidence

    # Rules for Superposition
    @Rule(QuantumFact(concept='superposition', level='beginner'))
    def explain_superposition_beginner(self):
        confidence = 0.88
        self.append_explanation(
            "Superposition is the ability of a quantum system to be in multiple states at once, like a coin being both heads and tails until observed.",
            confidence
        )
        self.fired_rules.append("explain_superposition_beginner")
        self.confidence_scores["explain_superposition_beginner"] = confidence

    @Rule(QuantumFact(concept='superposition', level='intermediate'))
    def explain_superposition_intermediate(self):
        confidence = 0.9
        self.append_explanation(
            "In quantum mechanics, superposition refers to a system existing simultaneously in multiple possible states, represented by a wavefunction.",
            confidence
        )
        # Alternate solution
        self.add_alternate_solution(
            "Superposition refers to a quantum system existing in a combination of possible states before measurement.",
            0.87
        )
        self.fired_rules.append("explain_superposition_intermediate")
        self.confidence_scores["explain_superposition_intermediate"] = confidence

    @Rule(QuantumFact(concept='superposition', level='advanced'))
    def explain_superposition_advanced(self):
        confidence = 0.96
        self.append_explanation(
            "Superposition allows a quantum state to be expressed as a linear combination of basis states. Measurement collapses it to one eigenstate.",
            confidence
        )
        # Alternate solution
        self.add_alternate_solution(
            "In quantum computing, superposition is used to allow qubits to exist in both 0 and 1 states simultaneously.",
            0.93
        )
        self.fired_rules.append("explain_superposition_advanced")
        self.confidence_scores["explain_superposition_advanced"] = confidence

    # Rules for Quantum Tunneling
    @Rule(QuantumFact(concept='quantum tunneling', level='beginner'))
    def explain_tunneling_beginner(self):
        confidence = 0.85
        self.append_explanation("Quantum tunneling is when particles pass through barriers they normally shouldn't, like a ball passing through a wall.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum tunneling occurs when particles pass through an energy barrier they classically couldn't overcome.", 0.75)
        self.fired_rules.append("explain_tunneling_beginner")
        self.confidence_scores["explain_tunneling_beginner"] = confidence

    @Rule(QuantumFact(concept='quantum tunneling', level='intermediate'))
    def explain_tunneling_intermediate(self):
        confidence = 0.90
        self.append_explanation("Quantum tunneling allows particles to move through energy barriers, explained by their wave-like nature and probability distribution.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Tunneling is a quantum phenomenon where particles have a probability of being found on the other side of a barrier.", 0.80)
        self.add_alternate_solution("In quantum mechanics, particles can tunnel through barriers due to the probabilistic nature of their wavefunctions.", 0.85)
        self.fired_rules.append("explain_tunneling_intermediate")
        self.confidence_scores["explain_tunneling_intermediate"] = confidence

    @Rule(QuantumFact(concept='quantum tunneling', level='advanced'))
    def explain_tunneling_advanced(self):
        confidence = 0.92
        self.append_explanation("Quantum tunneling results from the non-zero probability of a particle's wavefunction existing on the other side of a potential barrier.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum tunneling happens because the wavefunction of a particle extends beyond the potential barrier.", 0.90)
        self.add_alternate_solution("Tunneling arises from the probabilistic nature of quantum mechanics, where particles may appear on the other side of a classically forbidden barrier.", 0.88)
        self.fired_rules.append("explain_tunneling_advanced")
        self.confidence_scores["explain_tunneling_advanced"] = confidence


    # Rules for Quantum Computing
    @Rule(QuantumFact(concept='quantum computing', level='beginner'))
    def explain_quantum_computing_beginner(self):
        confidence = 0.85
        self.append_explanation("Quantum computing uses quantum bits (qubits) that can be in multiple states at once to perform computations much faster than regular computers.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum computing involves qubits that can exist in superposition, enabling faster computation for certain problems.", 0.75)
        self.add_alternate_solution("In quantum computing, qubits can be in multiple states simultaneously, which allows them to perform calculations in parallel.", 0.78)
        self.fired_rules.append("explain_quantum_computing_beginner")
        self.confidence_scores["explain_quantum_computing_beginner"] = confidence

    @Rule(QuantumFact(concept='quantum computing', level='intermediate'))
    def explain_quantum_computing_intermediate(self):
        confidence = 0.90
        self.append_explanation("Quantum computers leverage superposition and entanglement to perform parallel computations, making them powerful for certain tasks like factorization.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum computing uses qubits in superposition and entanglement to solve problems like prime factorization faster than classical computers.", 0.82)
        self.add_alternate_solution("Quantum computers exploit quantum mechanics to process information simultaneously in many states, enabling faster problem-solving.", 0.85)
        self.fired_rules.append("explain_quantum_computing_intermediate")
        self.confidence_scores["explain_quantum_computing_intermediate"] = confidence

    @Rule(QuantumFact(concept='quantum computing', level='advanced'))
    def explain_quantum_computing_advanced(self):
        confidence = 0.92
        self.append_explanation("Quantum algorithms, like Shor's and Grover's, exploit quantum parallelism and interference to solve problems exponentially faster than classical algorithms.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum computing algorithms, such as Shor's and Grover's, use quantum interference and parallelism to speed up computations exponentially.", 0.89)
        self.add_alternate_solution("In quantum computing, algorithms can achieve exponential speedup over classical methods by leveraging quantum superposition and entanglement.", 0.90)
        self.fired_rules.append("explain_quantum_computing_advanced")
        self.confidence_scores["explain_quantum_computing_advanced"] = confidence


    # Rules for Heisenberg Uncertainty Principle

    @Rule(QuantumFact(concept='uncertainty principle', level='beginner'))
    def explain_uncertainty_beginner(self):
        confidence = 0.85
        self.append_explanation("The Uncertainty Principle says you can't precisely measure both the position and momentum of a particle at the same time.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Heisenberg's Uncertainty Principle suggests that there are inherent limits to how much we can know about a particle's position and momentum simultaneously.", 0.80)
        self.add_alternate_solution("It is impossible to measure both the position and the momentum of a particle accurately at the same time, according to the Uncertainty Principle.", 0.78)
        self.fired_rules.append("explain_uncertainty_beginner")
        self.confidence_scores["explain_uncertainty_beginner"] = confidence

    @Rule(QuantumFact(concept='uncertainty principle', level='intermediate'))
    def explain_uncertainty_intermediate(self):
        confidence = 0.88
        self.append_explanation("Heisenberg's Uncertainty Principle implies that measuring a particle's position more precisely makes its momentum less certain, and vice versa.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("The more precisely we know a particle's position, the less certain we are about its momentum due to the Uncertainty Principle.", 0.82)
        self.add_alternate_solution("According to the Uncertainty Principle, there's a trade-off between precision in position and momentum measurements.", 0.85)
        self.fired_rules.append("explain_uncertainty_intermediate")
        self.confidence_scores["explain_uncertainty_intermediate"] = confidence

    @Rule(QuantumFact(concept='uncertainty principle', level='advanced'))
    def explain_uncertainty_advanced(self):
        confidence = 0.92
        self.append_explanation("Mathematically, the Uncertainty Principle is expressed as Δx * Δp ≥ ħ/2, where Δx and Δp are the uncertainties in position and momentum.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("The Heisenberg Uncertainty Principle mathematically states that the product of the uncertainties in position and momentum must be greater than or equal to ħ/2.", 0.90)
        self.add_alternate_solution("In quantum mechanics, the Uncertainty Principle places a lower bound on the product of position and momentum uncertainties.", 0.88)
        self.fired_rules.append("explain_uncertainty_advanced")
        self.confidence_scores["explain_uncertainty_advanced"] = confidence

    # Rules for Quantum Measurement
    @Rule(QuantumFact(concept='quantum measurement', level='beginner'))
    def explain_measurement_beginner(self):
        confidence = 0.85
        self.append_explanation("In quantum physics, measuring a system changes its state. For example, observing a particle collapses its wavefunction.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum measurement causes the collapse of the wavefunction, changing the state of the system being measured.", 0.80)
        self.add_alternate_solution("When a quantum system is measured, its wavefunction collapses, and it assumes a definite state.", 0.82)
        self.fired_rules.append("explain_measurement_beginner")
        self.confidence_scores["explain_measurement_beginner"] = confidence

    @Rule(QuantumFact(concept='quantum measurement', level='intermediate'))
    def explain_measurement_intermediate(self):
        confidence = 0.88
        self.append_explanation("Quantum measurement involves collapsing a superposition into one of its possible states, determined probabilistically by the wavefunction.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("In quantum mechanics, measurement results in the collapse of the superposition state into one of the possible outcomes.", 0.85)
        self.add_alternate_solution("When a quantum system is measured, the superposition collapses, and the system adopts a definite state based on probability.", 0.87)
        self.fired_rules.append("explain_measurement_intermediate")
        self.confidence_scores["explain_measurement_intermediate"] = confidence

    @Rule(QuantumFact(concept='quantum measurement', level='advanced'))
    def explain_measurement_advanced(self):
        confidence = 0.92
        self.append_explanation("Measurement in quantum mechanics is a non-unitary process that collapses the system's state vector to an eigenstate of the observable.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("In quantum measurement, the state vector of the system collapses to one of the eigenstates of the measured observable.", 0.90)
        self.add_alternate_solution("The process of measurement in quantum mechanics causes the collapse of the wavefunction, resulting in one definite outcome.", 0.91)
        self.fired_rules.append("explain_measurement_advanced")
        self.confidence_scores["explain_measurement_advanced"] = confidence


    # Rules for Quantum Cryptography
    @Rule(QuantumFact(concept='quantum cryptography', level='beginner'))
    def explain_cryptography_beginner(self):
        confidence = 0.85
        self.append_explanation("Quantum cryptography uses the principles of quantum mechanics to secure communication, making it impossible to eavesdrop without being detected.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum cryptography ensures that any attempt to intercept communication changes the quantum state, revealing the presence of the eavesdropper.", 0.82)
        self.add_alternate_solution("In quantum cryptography, the principles of quantum mechanics are used to create secure communication channels that detect any unauthorized interception.", 0.84)
        self.fired_rules.append("explain_cryptography_beginner")
        self.confidence_scores["explain_cryptography_beginner"] = confidence

    @Rule(QuantumFact(concept='quantum cryptography', level='intermediate'))
    def explain_cryptography_intermediate(self):
        confidence = 0.88
        self.append_explanation("Quantum cryptography relies on quantum key distribution (QKD), which ensures that any interception of the key changes its state, alerting the users.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Quantum key distribution (QKD) ensures the security of communication by detecting eavesdropping through changes in the quantum state of the key.", 0.85)
        self.add_alternate_solution("In quantum cryptography, any attempt to measure the quantum key will alter its state, making eavesdropping detectable.", 0.86)
        self.fired_rules.append("explain_cryptography_intermediate")
        self.confidence_scores["explain_cryptography_intermediate"] = confidence

    @Rule(QuantumFact(concept='quantum cryptography', level='advanced'))
    def explain_cryptography_advanced(self):
        confidence = 0.92
        self.append_explanation("Protocols like BB84 use quantum superposition and entanglement to establish secure communication channels, with security guaranteed by quantum mechanics.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("BB84 and other quantum cryptography protocols use quantum entanglement to ensure secure communication with a high level of protection against eavesdropping.", 0.90)
        self.add_alternate_solution("Quantum cryptographic protocols such as BB84 rely on the principles of quantum mechanics to establish a communication channel that guarantees security.", 0.91)
        self.fired_rules.append("explain_cryptography_advanced")
        self.confidence_scores["explain_cryptography_advanced"] = confidence


    # Rules for Superconductivity
    @Rule(QuantumFact(concept='superconductivity', level='beginner'))
    def explain_superconductivity_beginner(self):
        confidence = 0.85
        self.append_explanation("Superconductivity is a phenomenon where a material can conduct electricity without resistance at very low temperatures.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Superconductivity occurs when materials allow electricity to flow freely without any resistance at extremely low temperatures.", 0.80)
        self.add_alternate_solution("At low temperatures, some materials undergo a phase transition to a state where they can conduct electricity with zero resistance.", 0.82)
        self.fired_rules.append("explain_superconductivity_beginner")
        self.confidence_scores["explain_superconductivity_beginner"] = confidence

    @Rule(QuantumFact(concept='superconductivity', level='intermediate'))
    def explain_superconductivity_intermediate(self):
        confidence = 0.88
        self.append_explanation("Superconductivity is a state in which a material exhibits zero electrical resistance and the expulsion of magnetic fields, occurring below a critical temperature.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("Superconductivity occurs when a material exhibits perfect conductivity and excludes magnetic fields below a critical temperature.", 0.85)
        self.add_alternate_solution("In a superconducting state, a material has no electrical resistance and demonstrates the Meissner effect, where magnetic fields are expelled.", 0.87)
        self.fired_rules.append("explain_superconductivity_intermediate")
        self.confidence_scores["explain_superconductivity_intermediate"] = confidence

    @Rule(QuantumFact(concept='superconductivity', level='advanced'))
    def explain_superconductivity_advanced(self):
        confidence = 0.92
        self.append_explanation("Superconductivity is a quantum mechanical phenomenon where electron pairs form Cooper pairs that move without scattering, resulting in zero resistance.", confidence)
        # Add alternate solutions
        self.add_alternate_solution("In superconductivity, Cooper pairs form as a result of electron-electron interactions and move without resistance through the lattice.", 0.90)
        self.add_alternate_solution("Superconductivity arises from the formation of Cooper pairs, where electrons pair up and move without scattering, eliminating resistance.", 0.91)
        self.fired_rules.append("explain_superconductivity_advanced")
        self.confidence_scores["explain_superconductivity_advanced"] = confidence

    # Reset the output between runs
    def reset_output(self):
        self.explanation_output = ""
        self.alternate_solutions = ""
        self.fired_rules = []

    # Run the system and gather results
    def run_system(self):
        self.reset_output()  # Reset the output before each run
        self.reset()  # Reset the engine state
        self.run()  # Run the engine
        print(self.explanation_output)  # For debugging

    # Step 5: Print Fired Rules (Resolution)
    def print_resolution(self):
        """Returns a string with the resolution and confidence levels."""
        result = ""
        if not self.fired_rules:
            result += "No rules fired.\n"
        else:
            for rule in self.fired_rules:
                confidence = self.confidence_scores.get(rule, 1.0)
                result += f"- Rule: {rule} (Confidence: {confidence * 100:.1f}%)\n"
        self.fired_rules.clear()
        return result
    

   