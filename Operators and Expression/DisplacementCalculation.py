def DisplacementCalculation(u, v, a):
    Displacement = (v*v - u*u) / (2*a)
    return Displacement


initial_velocity = int(input('Enter the initial_velocity: '))
final_velocity = int(input('Enter the final_velocitye: '))
acceleration = int(input('Enter the acceleration: '))

# initial_velocity, final_velocity, acceleration = map(int, input('Enter the initial velocity, final velocity and acceleration: ').split())

print("Displacement is: ", DisplacementCalculation(initial_velocity, final_velocity, acceleration))