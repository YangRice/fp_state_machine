import time
from state_machine import FSM


if __name__ == '__main__':
    # Initialize Light: [green, yellow, red]
    control_light = FSM()
    control_light.transition = {
        ('green', 0): ('yellow', 5),
        ('yellow', 0): ('red', 10),
        ('red', 0): ('green', 30),
    }
    control_light.general_transition = lambda args: (args[0], args[1] - 1) 

    # Initialize people, action = [stop, walk, run]
    people = FSM()
    people.transition = {
        ('green', 'stop'): 'walk',
        ('yellow', 'walk'): 'run',
        ('red', 'walk'): 'stop',
        ('red', 'run'): 'stop',
    }
    people.general_transition = lambda args: args[1]

    # Initialize states
    light, secs, action = 'green', 10, 'stop'

    # Main loop
    while True:
        print(light, secs, action)
        light, secs = control_light.process(light, secs)
        action = people.process(light, action)
        time.sleep(0.5)