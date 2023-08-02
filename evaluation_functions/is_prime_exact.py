from typing import Dict, Optional


def eval_fun(inputs: Dict[str, str], output: str, target: Optional[str] = None) -> float:
    if target == 'prime':
        return float('[yes]' in output.lower())
    else:
        return float('[no]' in output.lower())
