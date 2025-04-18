from pet import Pet

def main():
    print("Creating pet: Max")
    my_pet = Pet("Max")
    
    # Test basic functionality
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    # Test training
    my_pet.train("roll over")
    my_pet.train("play dead")
    
    # Show status
    my_pet.get_status()
    
    # Show tricks
    my_pet.show_tricks()
    
    # Test edge cases
    print("\nTesting edge cases:")
    for _ in range(6):  # Exhaust energy
        my_pet.play()
    my_pet.get_status()
    my_pet.train("sit")  # Should fail
    my_pet.sleep()       # Recharge energy
    my_pet.train("sit")  # Should work now
    my_pet.get_status()

if __name__ == "__main__":
    main()