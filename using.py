import re

def using(mod):
    """
    Imports all public values of module into the global namespace
    of current module.
    """
    # trying to reference a property of a module 
    # as if it were a lexicically scoped variable 
    # within a function call seems to cause problems.
    # so it is precomputed for use witin the closure
    name = mod.__name__

    def make_assignment_statement_string(val):
        return "globals()['" + val + "'] = " + name + "." + val

    pat = re.compile('^_.+')
    all_props = dir(module)
    props = [i for i in all_props if not pat.match(i)]

    
    assignments = [make_assignment_statement_string(i) for i in props]
    
    for assignment in assignments:
        exec(assignment)
