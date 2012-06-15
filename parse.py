import logging
import word
import phrase
import parsecontext

def parse_nn(ctx, index, word) :
    '''
    Parser for noun
    '''
    log = logging.getLogger(__name__)
    if index == 0 :
        log.info("[R] noun at start")
        p = Phrase()
        p.index = 0
        p.type = 'NN'
        ctx.last_phrase = p
    elif word.pos in ctx.nn_prefix :
        log.info("[R] prefix + noun")
        ctx.last_phrase.end += 1
        if ctx.last_phrase.type == None :
            log.info("[R] hangphrase + noun -> noun")
            ctx.last_phrase.type = 'NN'
            ctx.center = word
    elif word.pos in ctx.nn_as_obj:
        log.info("[R] nnasobj + noun -> *obj_phra")
        if ctx.last_phrase.has_obj:
            
            
            
    
    
def parse_word(ctx, index, word) :
    log = logging.getLogger(__name__)
    if word.pos not it parsers:
        log.warning("Unrecognized pos: " + word[1])
        
    parser = ctx.parsers[word.pos]]
    parser(ctx, index, word)

def parse(ctx, sentence) :
    '''
    parse the whole sentence.
    '''
    log = logging.getLogger(__name__)
#    log.setLevel(INFO)
    for i, pair in enumerate(sentence) :
        # if parsing a word leads to consuming more words,
        # the num of words preconsumed should be recorded
        # in the ctx.
        word = Word(pair)
        parse_word(ctx, i, word)

def start(sentence) :
    ctx = ParseContext()
    ctx.parsers['NN'] = parse_nn
