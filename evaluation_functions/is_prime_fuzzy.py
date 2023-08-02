from typing import Dict, Optional


def eval_fun(inputs: Dict[str, str], output: str, target: Optional[str] = None) -> float:
    output = output.lower()
    if target == 'prime':
        underscore_yes = '[yes]' in output
        only_yes = 'yes' in output and 'no' not in output
        return float(underscore_yes or only_yes)
    else:
        return float('[no]' in output.lower())
