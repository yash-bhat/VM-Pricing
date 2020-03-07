#VM Pricing

import math
n = 2
# n = 26
instances = [5,25,50,100,500]
prices = [0.0,0.0,0.0,0.0,54.25]
# instances = [1,2,-1,3,4,0,-1,5,0]
# prices = [5,2.46,2.58,2.0,2.25,3.0]
# prices = [27.32,23.13,21.25,18.00,15.50]

def interpolate_given(n,instances,prices):
    for i in range(len(prices)):
        if prices[i] <= 0:
            prices[i] = -99
            instances[i] = -99

    #remove/ignore all 0/-1 values
    instances = list(filter(lambda a: a != -99, instances))
    prices = list(filter(lambda a: a != -99, prices))
    print (instances)
    print(prices)

    #if n present in prior data
    if n in instances:
        return prices[instances.index(n)]

    elif len(prices) == 1:
        f = math.ceil((prices[0] * 100) / 100)
        print(f)
        return str(round(f, 2))

    #true n greater than all : extrapolate closer 2 values
    # elif n > all(instances):
    elif all(i < n for i in instances):
        # print("true n greater than all")

        x1,x2 = instances[-1],instances[-2]
        y1,y2 = prices[-1],prices[-2]


        f = y1 + ((n-x1) / (x2-x1)) * (y2-y1)

        return(f)

    #true n smaller than all : extrapolate closer 2 values
    # elif n < all(instances):
    elif all(i > n for i in instances):
        # print("true n smaller than all")
        print('2')

        x1, x2 = instances[1], instances[0]
        y1, y2 = prices[1], prices[0]

        f = y1 + ((n - x1) / (x2 - x1)) * (y2 - y1)

        return (f)

    # for n value between those in the instances given, interpolate close 2 between values
    else:
        for i in range(len(instances)):
            if n < instances[i]:
                x1, x2 = instances[i-1], instances[i]
                y1, y2 = prices[i-1], prices[i]

                f = ((y2-y1)/(x2-x1)) * (n-x1) + y1

                return f


res = interpolate_given(n,instances,prices)
print(res)
