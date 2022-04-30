# 断言意义在于,例如以下红路灯案例,代码本身不会报错,但是代码逻辑有问题,导致不会出现红灯,所以加上断言来判断,如果没有红灯就抛出异常
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}


def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(
    ), 'Neither light is red! ' + str(stoplight)


switchLights(market_2nd)
