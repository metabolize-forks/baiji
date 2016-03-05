from __future__ import print_function

def create_conditional_print(should_print):
    '''
    When should_print is True, returns a function which prints its inputs.
    When it's false, return a function which does nothing.

    Usage:

    def do_something(verbose=False):
        from bodylabs.util.console import create_conditional_print
        print_verbose = create_conditional_print(verbose)

        print_verbose('Here is something which might print')

    '''
    def noop(*args, **kwargs): # Yup, these args are unused in this no-op function... pylint: disable=unused-argument
        pass

    if should_print:
        return print
    else:
        return noop
