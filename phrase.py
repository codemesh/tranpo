class Phrase :
    def __init__(self) :
        self.index = -1
        self.end = -1
        self.thread_prev = None
        self.thread_next = None
        self.syntax_parent = None
        self.syntax_next = None
        self.syntax_sibling = None
        self.syntax_accord = None
        self.subject = None
        self.object = None
        self.predicate = None
        self.predicative = None
        self.type = None # type of phrase
        self.center = None # reference to center word
        self.role = None # role as child of parent
        self.score = 0
        self.has_verb = false
        self.has_predicate = false
        
    
