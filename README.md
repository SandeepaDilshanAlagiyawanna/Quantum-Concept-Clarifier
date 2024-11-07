# Quantum Computing and Physics Expert System

This project is an expert system designed to help users explore and understand concepts in quantum computing and physics. It uses **Pyke** for the inference engine and allows users to switch between **forward chaining** and **backward chaining** search algorithms, making it adaptable to both general and targeted queries. The system displays conflict sets and resolution steps to help users gain insight into the reasoning process.

## Features

- **Interactive User Interface**: Built with Tkinter to enable easy interaction.
- **Dynamic Search Algorithm Selection**: Choose between forward chaining and backward chaining based on the type of query.
- **Conflict Set and Resolution Display**: Visualize the conflict set and selected rules for each query.
- **Knowledge Base**: Stores rules on quantum computing and physics, with the flexibility to expand for more complex concepts.

## Project Structure

  ```bash
  project_root/
  ├── knowledge_base.krb      # Knowledge base file defining rules about quantum computing and physics
  ├── expert_system.py        # Main code file containing the inference engine and UI setup
  ├── README.md               # Project documentation
```


## Requirements

- **Python 3.8**
- **Pyke**: Install using `pip install pyke`
- **Tkinter**: Comes pre-installed with most Python distributions.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SandeepaDilshanAlagiyawanna/Quantum-Concept-Clarifier.git
   cd Quantum-Concept-Clarifier

2. Install dependencies:
   ```bash
   pip install pyke
   
3. Run the program:
   ```bash
   python expert_system.py

## Usage

1. Launch the program by running `expert_system.py`.
2. Choose the **Search Algorithm**: Select between Forward Chaining and Backward Chaining.
3. Enter a **Query**: Type in a question about quantum computing or physics (e.g., "quantum_superposition").
4. View Results:
   - See the system’s inference results and conflict set.
   - Observe how the conflict resolution strategy works to select rules.

## Adding Rules to the Knowledge Base

To expand the system, you can add more rules to `knowledge_base.krb`. Follow the syntax of existing rules for consistency. Pyke will process these additional rules when you run the program.

## Example Queries

- **Forward Chaining**: `quantum_superposition` - Explores knowledge related to quantum uncertainty.
- **Backward Chaining**: `quantum_entanglement` - Verifies if a given relationship is classified as quantum entanglement.

## Future Improvements

- Enhance the knowledge base with more complex rules and relationships.
- Implement additional conflict resolution strategies.
- Integrate user-defined priority levels for more customized conflict handling.
  
## License
This project is licensed under the MIT License.



