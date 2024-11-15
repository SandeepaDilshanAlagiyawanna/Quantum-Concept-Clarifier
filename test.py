from difflib import get_close_matches
from knowledge_base import QuantumFact, QuantumExpertSystem

def main():
    engine = QuantumExpertSystem()

    available_concepts = [
        'superposition', 'entanglement', 'superconductivity',
        'quantum tunneling', 'quantum computing', 'uncertainty principle',
        'quantum measurement', 'quantum cryptography'
    ]
    available_levels = ['beginner', 'intermediate', 'advanced']

    while True:
        print("\n--- Quantum Concept Clarifier ---")
        print("Available concepts:", ", ".join(available_concepts))
        print("Explanation levels:", ", ".join(available_levels))

        # Reset the engine before each new run
        engine.reset()

        # Get user input for concept and level
        concept_input = input("Enter a quantum concept (or type 'exit' to quit): ").lower().strip()
        if concept_input == 'exit':
            break

        # Handle partial matches for concept
        matches = get_close_matches(concept_input, available_concepts, n=3, cutoff=0.45)
        conflict_set = []
        if matches:
            if len(matches) > 1:
                # If multiple matches found, store as conflict set
                print(f"Found possible matches: {', '.join(matches)}")
                conflict_set = matches
                confirm = input(f"Did you mean one of these concepts? Select one: ").lower().strip()
                if confirm in matches:
                    concept = confirm
                else:
                    print("\nInvalid concept selected.")
                    engine.declare(QuantumFact(clarification_needed=True))
                    continue
            else:
                concept = matches[0]
        else:
            print("\nInvalid concept detected.")
            engine.declare(QuantumFact(clarification_needed=True))
            continue

        # Handle explanation level with partial matching
        level_input = input("Enter explanation level (beginner, intermediate, advanced): ").lower().strip()
        level_matches = get_close_matches(level_input, available_levels, n=3, cutoff=0.5)
        if level_matches:
            if len(level_matches) > 1:
                print(f"Found possible matches: {', '.join(level_matches)}")
                confirm_level = input(f"Did you mean one of these levels? Select one: ").lower().strip()
                if confirm_level in level_matches:
                    level = confirm_level
                else:
                    print("\nInvalid level selected.")
                    engine.declare(QuantumFact(clarification_needed=True))
                    continue
            else:
                level = level_matches[0]
        else:
            print("\nInvalid level detected.")
            engine.declare(QuantumFact(clarification_needed=True))
            continue

        # Declare the fact and run the engine
        if concept in available_concepts and level in available_levels:
            engine.declare(QuantumFact(concept=concept, level=level))

        # Run the expert system
        engine.run()

        # Print the conflict set before displaying the resolution
        print("\n[Conflict Set]: ")
        if conflict_set:
            print(", ".join(conflict_set))
        else:
            print(f"- Concept: {concept}, Level: {level}")

        # Print the resolution steps taken by the engine
        engine.print_conflict_set()
        engine.print_resolution()

        # Ask if the user wants to try again
        try_again = input("\nWould you like to try another concept? (yes/no): ").lower()
        if try_again != 'yes':
            break

if __name__ == "__main__":
    main()
