class FSM:
    def __init__(self):
        self.transition = {}  # {from_state: to_state}
        self.general_transition = lambda state: state

    def process(self, *state):
        if state in self.transition:
            return self.transition[state]
        return self.general_transition(state)