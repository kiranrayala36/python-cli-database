import sys

class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students[name] = grade
        return f"Added {name} with grade {grade}."
    
    def get_student(self, name):
        # .get() is perfect here. O(1) time complexity.
        return self.students.get(name, "Error: Student not found.")
    
    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            return f"Deleted {name}."
        else:
            return "Error: Student not found."

def main():
    db = StudentDatabase()
    print("Student Database Initialized. Type 'exit' to quit.")

    while True:
        try:
            raw_input = input("> ").strip()
            
            if not raw_input:
                continue
                
            cmd = raw_input.split()
            command = cmd[0].lower()

            if command == "add":
                
                if len(cmd) == 3:
                    print(db.add_student(cmd[1], cmd[2]))
                else:
                    print("Usage: add [name] [grade]")

            elif command == "lookup":
                if len(cmd) == 2:
                    print(db.get_student(cmd[1]))
                else:
                    print("Usage: lookup [name]")

            elif command == "delete":
                if len(cmd) == 2:
                    print(db.delete_student(cmd[1]))
                else:
                    print("Usage: delete [name]")
            
            elif command == "exit":
                print("Exiting database...")
                sys.exit()

            else:
                print("Invalid command. Available commands: add, lookup, delete, exit.")
                
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()