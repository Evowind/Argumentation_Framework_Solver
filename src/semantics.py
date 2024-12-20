#Module to compute stable and complete extensions
#semantics.py

#Make sure no arguments attack each other.
def is_conflict_free(arguments, attacks):
    for arg1 in arguments:
        for arg2 in arguments:
            #If two arguments attack each other, return False.
            if (arg1 != arg2) and ((arg1, arg2) in attacks or (arg2, arg1) in attacks):
                return False
    return True  #If no conflicts, we’re good!

#See if an argument is defended by a subset of arguments.
def defends(argument, arguments, attacks):
    #Get all attackers of the argument.
    attackers = {att[0] for att in attacks if att[1] == argument}
    #Check if every attacker is countered by at least one defender in the subset.
    return all(any((defender, attacker) in attacks for defender in arguments) for attacker in attackers)

#Function to compute stable extensions (conflict-free subsets that attack all external arguments).
def compute_stable_extensions(arguments, attacks):
    """
    Finds all stable extensions: subsets that are conflict-free and attack 
    every argument outside the subset.
    """
    stable_extensions = []
    subsets = power_set(arguments)  #Get all possible subsets of arguments.

    for subset in subsets:
        if is_conflict_free(subset, attacks):  #Check conflict-free first.
            #Arguments outside the subset.
            outside_arguments = arguments - subset

            #Make sure every outside argument is attacked by the subset.
            all_attacked = True
            for arg in outside_arguments:
                if not any((attacker, arg) in attacks for attacker in subset):
                    all_attacked = False
                    break

            if all_attacked:
                stable_extensions.append(subset)  #Add to the list if it passes.

    return stable_extensions

#Function to compute complete extensions (admissible sets defending all their arguments).
def compute_complete_extensions(arguments, attacks):
    """
    Finds all complete extensions: admissible subsets that include all arguments they defend.
    """
    complete_extensions = []
    subsets = power_set(arguments)  #Get all possible subsets of arguments.

    for subset in subsets:
        if not is_conflict_free(subset, attacks):  #Must be conflict-free.
            continue

        if not all(defends(arg, subset, attacks) for arg in subset):  #Must defend all its arguments.
            continue

        defended_arguments = {arg for arg in arguments if defends(arg, subset, attacks)}
        if not defended_arguments.issubset(subset):  #Defended args must all be in the subset.
            continue

        complete_extensions.append(subset)  #Passed all checks, add it.

    return complete_extensions

#Credulous acceptance: find arguments in *any* extension.
def compute_credulous_acceptance(arguments, attacks, extension_type="stable"):
    #Choose the type of extension to use.
    if extension_type == "stable":
        extensions = compute_stable_extensions(arguments, attacks)
    elif extension_type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        raise ValueError("Invalid extension type. Use 'stable' or 'complete'.")

    #Return arguments found in at least one extension.
    return {arg for ext in extensions for arg in ext}

#Skeptical acceptance: find arguments in *all* extensions.
def compute_skeptical_acceptance(arguments, attacks, extension_type="stable"):
    #Choose the type of extension to use.
    if extension_type == "stable":
        extensions = compute_stable_extensions(arguments, attacks)
    elif extension_type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        raise ValueError("Invalid extension type. Use 'stable' or 'complete'.")

    #Return arguments that show up in every extension.
    return {arg for arg in arguments if all(arg in ext for ext in extensions)}

#Helper function to compute the power set (all subsets) of a set.
def power_set(s):
    from itertools import chain, combinations
    #Use itertools to get all combinations of different sizes.
    return [set(comb) for comb in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]
