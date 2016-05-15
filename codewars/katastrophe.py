def strong_enough(earthquake, age):
    building = 1000*0.99**age
    shockwave = [reduce(lambda q, p: p+q, tremor) for tremor in earthquake]
    sum_eq = reduce(lambda q, p: p*q, shockwave)

    return "Safe!" if building > sum_eq else "Needs Reinforcement!"

print strong_enough([[5, 8, 7], [3, 3, 1], [4, 1, 2]], 3)

