from difflib import get_close_matches
from experta import KnowledgeEngine, Fact, Rule, DefFacts, NOT

# Step 1: Define Facts
class QuantumFact(Fact):
    """Fact about a quantum concept and its explanation level."""
    concept = ""
    level = ""  # Explanation level: beginner, intermediate, advanced
    clarification_needed = False

# Step 2: Define Expert System
class QuantumExpertSystem(KnowledgeEngine):

    # List to track fired rules
    fired_rules = []

    # Initial facts or setup
    @DefFacts()
    def initial_facts(self):
        """Initialize with a default fact."""
        yield Fact(ready=True)

    # Step 3: Define Rules for Quantum Concepts

    @Rule(QuantumFact(concept='superposition', level='beginner'))
    def explain_superposition_beginner(self):
        print("Superposition is the ability of a quantum system to be in multiple states at the same time, like a coin being both heads and tails until you observe it.")
        self.fired_rules.append("explain_superposition_beginner")

    @Rule(QuantumFact(concept='superposition', level='intermediate'))
    def explain_superposition_intermediate(self):
        print("In quantum mechanics, superposition refers to a system existing simultaneously in multiple possible states, described by a wavefunction.")
        self.fired_rules.append("explain_superposition_intermediate")

    @Rule(QuantumFact(concept='superposition', level='advanced'))
    def explain_superposition_advanced(self):
        print("Superposition is the principle that a quantum system can be expressed as a linear combination of its basis states, where measurement collapses it to a single eigenstate.")
        self.fired_rules.append("explain_superposition_advanced")

    @Rule(QuantumFact(concept='entanglement', level='beginner'))
    def explain_entanglement_beginner(self):
        print("Entanglement is when two particles become linked so that the state of one instantly influences the state of the other, even if they are far apart.")
        self.fired_rules.append("explain_entanglement_beginner")

    @Rule(QuantumFact(concept='entanglement', level='intermediate'))
    def explain_entanglement_intermediate(self):
        print("Entanglement is a phenomenon where particles share a quantum state, so the measurement of one affects the other, no matter the distance between them.")
        self.fired_rules.append("explain_entanglement_intermediate")

    @Rule(QuantumFact(concept='entanglement', level='advanced'))
    def explain_entanglement_advanced(self):
        print("Quantum entanglement occurs when particles become correlated in such a way that their quantum states cannot be described independently, represented by a shared wavefunction.")
        self.fired_rules.append("explain_entanglement_advanced")

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

    # Step 5: Print Fired Rules (Resolution)
    def print_resolution(self):
        print("\n[Resolution] Fired rules:")
        for rule in self.fired_rules:
            print(f"- Rule: {rule}")
        self.fired_rules.clear()  # Reset fired rules after printing

# Step 6: User Interaction
def main():
    engine = QuantumExpertSystem()

    available_concepts = ['superposition', 'entanglement', 'superconductivity']
    available_levels = ['beginner', 'intermediate', 'advanced']
    
    while True:
        print("\n--- Quantum Concept Clarifier ---")
        print("Available concepts: superposition, entanglement, superconductivity")
        print("Explanation levels: beginner, intermediate, advanced")

        # Reset the engine before each new run
        engine.reset()

        # Get user input for concept and level
        concept = input("Enter a quantum concept (or type 'exit' to quit): ").lower().strip()
        if concept == 'exit':
            break

        # Check for partial matches (if user types incomplete concept)
        matches = get_close_matches(concept, available_concepts, n=3, cutoff=0.45)  # Adjusted n=3 for multiple matches
        if matches:
            if len(matches) > 1:
                # If multiple matches found, ask for confirmation
                print(f"Found possible matches: {', '.join(matches)}")
                confirm = input(f"Did you mean one of these concepts: {', '.join(matches)}? Select one Concept: ").lower().strip()
                if confirm in matches:
                    concept = confirm  # Assume the first match is selected
                else:
                    print("\nInvalid concept detected.")
                    engine.declare(QuantumFact(clarification_needed=True))
                    continue
            else:
                concept = matches[0]  # Select the only match
        else:
            print("\nInvalid concept detected.")
            engine.declare(QuantumFact(clarification_needed=True))
            continue

        # Handle explanation level with partial matching
        level_input = input("Enter explanation level (beginner, intermediate, advanced): ").lower().strip()

        # Check for partial matches for explanation level
        level_matches = get_close_matches(level_input, available_levels, n=3, cutoff=0.5)
        if level_matches:
            if len(level_matches) > 1:
                # If multiple matches found, ask for confirmation
                print(f"Found possible matches: {', '.join(level_matches)}")
                confirm_level = input(f"Did you mean one of these levels: {', '.join(level_matches)}? Select one Level: ").lower().strip()
                if confirm_level in level_matches:
                    level = confirm_level  # Use the selected level
                else:
                    print("\nInvalid level detected.")
                    engine.declare(QuantumFact(clarification_needed=True))
                    continue
            else:
                level = level_matches[0]  # Select the only match
        else:
            print("\nInvalid level detected.")
            engine.declare(QuantumFact(clarification_needed=True))
            continue

        # Declare the fact and run the engine
        if concept in available_concepts and level in available_levels:
            engine.declare(QuantumFact(concept=concept, level=level))

        # Run the expert system
        engine.run()

        # Print the conflict set and resolution after running the engine
        engine.print_conflict_set()
        engine.print_resolution()

        # Ask if the user wants to try again
        try_again = input("\nWould you like to try another concept? (yes/no): ").lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()
