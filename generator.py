# Codes By Vision
import secrets
import string
import sys

def generate_password(length):
    """Generates a secure, random password of the given length."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    print("-" * 40)
    print("      SECURE PASSWORD GENERATOR")
    print("-" * 40)
    
    try:
        length_input = input("Enter desired password length (e.g., 12, 16, 24): ").strip()
        if not length_input:
            length = 16
            print(f"Using default length: {length}")
        else:
            length = int(length_input)
            
        if length < 4:
            print("Password length too short for security. Setting to minimum: 8")
            length = 8
            
        count = 5
        print(f"\nSuggesting {count} strong passwords:\n")
        
        for i in range(1, count + 1):
            pwd = generate_password(length)
            print(f"  [{i}] {pwd}")
            
        print("\n" + "-" * 40)
        print("Stay secure!")
        print("-" * 40)
        
    except ValueError:
        print("Invalid input. Please enter a number for the password length.")
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
