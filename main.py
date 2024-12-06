import tkinter as tk
from tkinter import messagebox, scrolledtext, Listbox
from difflib import get_close_matches
from knowledge_base import QuantumFact, QuantumExpertSystem

class QuantumExpertSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Concept Clarifier")
        self.engine = QuantumExpertSystem()

        self.available_concepts = [
            'superposition', 'entanglement', 'superconductivity',
            'quantum tunneling', 'quantum computing', 'uncertainty principle',
            'quantum measurement', 'quantum cryptography'
        ]
        self.available_levels = ['beginner', 'intermediate', 'advanced']

        # Initialize the GUI layout
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Quantum Concept Clarifier", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Concept Input
        tk.Label(self.root, text="Enter Quantum Concept:").pack()
        self.concept_entry = tk.Entry(self.root, width=50)
        self.concept_entry.pack(pady=5)

        # Search Button
        self.search_button = tk.Button(self.root, text="Search", command=self.search_concept)
        self.search_button.pack(pady=5)

        # Listbox for Concept Suggestions
        tk.Label(self.root, text="Select the Correct Concept:").pack()
        self.concept_listbox = Listbox(self.root, width=50, height=5)
        self.concept_listbox.pack(pady=5)

        # Explanation Level Input
        tk.Label(self.root, text="Enter Explanation Level (beginner, intermediate, advanced):").pack()
        self.level_entry = tk.Entry(self.root, width=50)
        self.level_entry.pack(pady=5)

        # Run Button
        self.run_button = tk.Button(self.root, text="Run", command=self.run_expert_system)
        self.run_button.pack(pady=10)

        # Output Display
        tk.Label(self.root, text="Explanation Output:").pack()
        self.output_text = scrolledtext.ScrolledText(self.root, width=90, height=20)
        self.output_text.pack(padx=10, pady=10)

        # Control Buttons
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_fields)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Alternate Solutions Button (initially hidden)
        self.alternate_button = tk.Button(self.root, text="Alternate Solution", command=self.display_alternate_solution)
        self.alternate_button.pack(pady=10)
        self.alternate_button.pack_forget()  # Hide initially

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def search_concept(self):
        """Search for relevant concepts based on user input."""
        concept_input = self.concept_entry.get().lower().strip()
        if not concept_input:
            messagebox.showerror("Input Error", "Please enter a concept.")
            return

        # Find close matches for the concept
        matches = get_close_matches(concept_input, self.available_concepts, n=5, cutoff=0.45)
        self.concept_listbox.delete(0, tk.END)

        if matches:
            for match in matches:
                self.concept_listbox.insert(tk.END, match)
        else:
            messagebox.showerror("No Match", "No relevant concepts found. Please try again.")

    def run_expert_system(self):
        """Run the expert system with the selected concept and level."""
        self.output_text.delete(1.0, tk.END)
        selected_concept = self.concept_listbox.get(tk.ACTIVE)
        level_input = self.level_entry.get().lower().strip()

        # Validate concept selection
        if not selected_concept:
            messagebox.showerror("Selection Error", "Please select a concept from the list.")
            return

        # Handle incomplete or ambiguous level input
        if not level_input:
            level = "beginner"
            messagebox.showinfo("Clarification", "You did not enter a level. Defaulting to 'beginner'.")
        else:
            level_matches = get_close_matches(level_input, self.available_levels, n=1, cutoff=0.5)
            if not level_matches:
                messagebox.showerror("Level Error", "Invalid explanation level entered. Defaulting to 'beginner'.")
                level = "beginner"
            else:
                level = level_matches[0]

        # Reset the expert system before each run
        self.engine.reset()
        self.engine.fired_rules.clear()  # Clear fired rules
        self.engine.explanation_output = ""  

        # Declare the fact and check for uncertainty
        fact = QuantumFact(concept=selected_concept, level=level)
        # Proceed with normal processing
        self.engine.declare(fact)
        self.engine.run()

        # Clear previous output
        self.output_text.delete(1.0, tk.END)

        # Create a bold tag
        self.output_text.tag_configure("bold", font=("Helvetica", 12, "bold"))
        self.output_text.tag_configure("size", font=("Helvetica", 10))

        # Output explanation and rule results
        self.output_text.insert(tk.END, "Explanation: ", "bold")
        self.output_text.insert(tk.END, self.engine.get_solution() + "\n", "size")
        self.output_text.insert(tk.END, "Concept: ", "bold")
        self.output_text.insert(tk.END, f"{selected_concept.capitalize()}\n", "size")
        self.output_text.insert(tk.END, "Level: ", "bold")
        self.output_text.insert(tk.END, f"{level.capitalize()}\n", "size")
        self.output_text.insert(tk.END, "Explanation Confidence: ", "bold")
        self.output_text.insert(tk.END, f"{self.engine.current_confidence * 100:.1f}%\n", "size")

        resolution = self.engine.print_resolution()

        self.output_text.insert(tk.END, "\nRule Fired:\n", "bold")
        self.output_text.insert(tk.END, resolution + "\n", "size")

        # After output display logic:
        self.alternate_button.pack()  # Show the Alternate Solutions button

    def reset_fields(self):
        """Clear all input fields and the output text box."""
        result = messagebox.askokcancel(
        "Confirm Reset", 
        "Are you sure you want to clear all fields and output?"
        )
    
        if result:  # If OK is clicked
            self.concept_entry.delete(0, tk.END)
            self.level_entry.delete(0, tk.END)
            self.concept_listbox.delete(0, tk.END)
            self.output_text.delete(1.0, tk.END)
            
            # Reset alternate solutions (if needed)
            self.alternate_solutions = ""  # Assuming you have alternate_solutions variable
            self.alternate_button.pack_forget() 

    def display_alternate_solution(self):
        alternate_solutions = self.engine.get_alternate_solutions()
        self.output_text.delete(1.0, tk.END)
        if alternate_solutions:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Alternate Solutions: ", "bold")
            self.output_text.insert(tk.END, f"{alternate_solutions}\n", "size")
        else:
            messagebox.showinfo("No Alternate Solutions", "No alternate solutions available.")


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumExpertSystemGUI(root)
    root.mainloop()
