import random

def estimate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        # Generate random (x, y) coordinates within the range [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the quarter-circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1

    # Calculate the estimated value of π
    estimated_pi = 4 * (points_inside_circle / num_points)
    
    return estimated_pi

# Define the number of random points to generate
num_points = 1000000  # You can increase this number for better accuracy

# Estimate π
estimated_pi = estimate_pi(num_points)

print(f"Estimated π with {num_points} random points: {estimated_pi}")
