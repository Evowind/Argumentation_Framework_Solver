# Module to calculate extensions (complete, stable)
def is_conflict_free(arguments, attacks):
    """
    Checks if a set of arguments is conflict-free.
    """
    for arg1 in arguments:
        for arg2 in arguments:
            if arg1 != arg2 and (arg1, arg2) in attacks:
                return False
    return True

def defends(argument, arguments, attacks):
    """
    Checks if a specific argument is defended by a set of arguments.
    """
    attackers = {att[0] for att in attacks if att[1] == argument}
    for attacker in attackers:
        if not any((defender, attacker) in attacks for defender in arguments):
            return False
    return True

def compute_stable_extensions(arguments, attacks):
    """
    Computes all stable extensions.
    A stable extension is conflict-free and attacks all arguments not in the extension.
    """
    stable_extensions = []
    subsets = power_set(arguments)

    for subset in subsets:
        if is_conflict_free(subset, attacks):
            # Check if the extension attacks all arguments not in the subset
            attacks_all_non_members = True
            for arg in arguments:
                if arg not in subset and not any((attacker, arg) in attacks for attacker in subset):
                    attacks_all_non_members = False
                    break
            if attacks_all_non_members:
                stable_extensions.append(subset)

    return stable_extensions

def compute_complete_extensions(arguments, attacks):
    """
    Computes all complete extensions.
    A complete extension is admissible and all defended arguments are part of the extension.
    """
    admissible_extensions = compute_stable_extensions(arguments, attacks)
    complete_extensions = [set()] # Empty element

    for extension in admissible_extensions:
        if all(defends(arg, extension, attacks) for arg in extension):
            complete_extensions.append(extension)

    return complete_extensions


def compute_credulous_acceptance(arguments, attacks, type):
    if type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        extensions = compute_stable_extensions(arguments, attacks)
    credulous_acceptance = set()
    for ext in extensions:
        for arg in ext:
            credulous_acceptance.add(arg)
    return credulous_acceptance

def compute_skeptical_acceptance(arguments, attacks, type):
    if  type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        extensions = compute_stable_extensions(arguments, attacks)
    skeptical_acceptance = set()
    for ext in extensions:
        for arg in ext:
            if all(arg in ext for ext in extensions):
                skeptical_acceptance.add(arg)
    return skeptical_acceptance

def power_set(s):
    """
    Generates the power set of a given set.
    """
    from itertools import chain, combinations
    return [set(comb) for comb in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]


