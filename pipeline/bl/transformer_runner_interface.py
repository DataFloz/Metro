class TransforerRunnerInterface:
    '''Abstract class for transformation'''
    def __init__(self):
        pass

    def run_logic(self, msg):
        """ execute logic - meant to be override """
