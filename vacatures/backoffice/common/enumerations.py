from backoffice.common.utils import ChoiceEnum

class JobBranches(ChoiceEnum):
    Agrarisch = "JB.01"
    Financieel = "JB.02"
    ICT = "JB.03"
    Telecom = "JB.04"

class Organisations(ChoiceEnum):
    Gemeente_X = "x"
    Gemeente_Y = "y"