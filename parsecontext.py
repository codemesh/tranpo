class ParseContext :
    def __init__(self) :
        self.root = None # root phrase
        self.has_predicate = false # Has the root predicate been found or not.
        self.last_phrase = None
        self.pre_consumed = 0 # num of words pre consumed
        self.parsers = {}
        self.nn_prefix = set(['NN', 'JJ', 'DT'])
        self.nn_as_obj = set(['IN', 'VB'])


    
