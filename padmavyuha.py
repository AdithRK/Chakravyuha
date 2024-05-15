"""
Abhimanyu's attempt to exit Chakravyuha:

power   -> Abhimanyu's initial power
a       -> number of times Abhimanyu can skip a battle
b       -> number of times Abhimayu can regenerate his power
enemies -> list of enemy powers in order from inner to outer circle

"""

def chakravyuha(power,a,b,enemies) :
    def battle(power, enemy_power):
        if power >= enemy_power:
            return (power - enemy_power)        # Power after defeating enemy is initial power - enemy power
        else:
            return -1
    def result() :                              # Function to print result at end
        if power == -1:
            return ("Abhimanyu lost the battle")
        if i == 10:
            return ("Abhimanyu won the battle")

    max_power = power      # To store the initial power

    for i, enemy_power in enumerate(enemies):           # Main Loop
        
        
        if i == 2 or i ==6:         # 3rd & 7th enemy regenerates with half power and strikes along with current enemy
            enemy_power = enemy_power + (enemies[i-1]/2) 

        print(power,enemy_power)    # To display current battle status

        if power < enemy_power:     # Condition to trigger skip ability
            if a <= 0:
                if b <= 0:          # Condition to trigger regenerative ability
                    return ("Abhimanyu lost the battle")
                else:
                    power = max_power
                    b = b - 1      
                    power = battle(power, enemy_power)
                    result()
                    continue
            a = a-1
            continue
    
        power = battle(power, enemy_power)
        result()
    return ("Abhimanyu won the battle")

# Test Cases

test = [                            
    (25, 2, 2, [5, 7, 8, 6, 5, 7, 6, 4, 3, 5, 4]),
    (15, 2, 2, [5, 7, 8, 6, 5, 7, 6, 4, 3, 5, 4])
]

for power, a, b, enemies in test:
    print(chakravyuha(power, a, b, enemies))