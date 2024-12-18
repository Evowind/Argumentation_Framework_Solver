def is_conflict_free(arguments, attacks):
    for arg1 in arguments:
        for arg2 in arguments:
            if (arg1 != arg2) and ((arg1, arg2) in attacks or (arg2, arg1) in attacks):
                return False
    return True


def defends(argument, arguments, attacks):
    attackers = {att[0] for att in attacks if att[1] == argument}
    return all(any((defender, attacker) in attacks for defender in arguments) for attacker in attackers)

def compute_stable_extensions(arguments, attacks):
    """
    Calcule toutes les extensions stables : un sous-ensemble est stable s'il est sans conflit
    et attaque tous les arguments qui ne lui appartiennent pas.
    """
    stable_extensions = []
    subsets = power_set(arguments)

    for subset in subsets:
        if is_conflict_free(subset, attacks):
            # Arguments hors du subset
            outside_arguments = arguments - subset

            # Vérifie si chaque argument hors du subset est attaqué par le subset
            all_attacked = True
            for arg in outside_arguments:
                attacked = any((attacker, arg) in attacks for attacker in subset)
                if not attacked:
                    all_attacked = False
                    break

            if all_attacked:
                stable_extensions.append(subset)

    return stable_extensions

def compute_complete_extensions(arguments, attacks):
    """
    Calcule toutes les extensions complètes : un ensemble admissible
    contenant tous les arguments qu'il défend.
    """
    complete_extensions = []
    subsets = power_set(arguments)

    for subset in subsets:
        # Vérifier si le subset est conflict-free
        if not is_conflict_free(subset, attacks):
            continue

        # Vérifier si le subset défend tous ses arguments
        if not all(defends(arg, subset, attacks) for arg in subset):
            continue

        # Vérifier si tous les arguments défendus par le subset sont dans le subset
        defended_arguments = {arg for arg in arguments if defends(arg, subset, attacks)}
        if not defended_arguments.issubset(subset):
            continue

        # Ajouter à la liste des extensions complètes
        complete_extensions.append(subset)

    return complete_extensions

def compute_credulous_acceptance(arguments, attacks, extension_type="stable"):
    if extension_type == "stable":
        extensions = compute_stable_extensions(arguments, attacks)
    elif extension_type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        raise ValueError("Invalid extension type. Use 'stable' or 'complete'.")

    return {arg for ext in extensions for arg in ext}

def compute_skeptical_acceptance(arguments, attacks, extension_type="stable"):
    if extension_type == "stable":
        extensions = compute_stable_extensions(arguments, attacks)
    elif extension_type == "complete":
        extensions = compute_complete_extensions(arguments, attacks)
    else:
        raise ValueError("Invalid extension type. Use 'stable' or 'complete'.")

    return {arg for arg in arguments if all(arg in ext for ext in extensions)}

def power_set(s):
    from itertools import chain, combinations
    return [set(comb) for comb in chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))]