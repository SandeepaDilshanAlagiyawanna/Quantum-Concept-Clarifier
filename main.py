from difflib import get_close_matches
from knowledge_base import QuantumFact,QuantumExpertSystem

def main():
    engine = QuantumExpertSystem()

    available_concepts = ['superposition', 'entanglement', 'superconductivity','quantum tunneling','quantum computing','uncertainty principle','quantum measurement','quantum cryptography']
    available_levels = ['beginner', 'intermediate', 'advanced']
    
    while True:
        print("\n--- Quantum Concept Clarifier ---")
        print("Available concepts: superposition, entanglement, superconductivity,quantum tunneling,quantum computing,uncertainty principle,quantum measurement,quantum cryptography")
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