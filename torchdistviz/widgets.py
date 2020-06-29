from ipywidgets import FloatText, BoundedFloatText, FloatSlider
from torch.distributions import constraints


def support_range_widgets(support_constraint):
    if isinstance(support_constraint, constraints._Real):
        return {'x_min': FloatText(value=-10.),
                'x_max': FloatText(value=10.)}
    if isinstance(support_constraint, constraints._GreaterThan):
        lb = support_constraint.lower_bound
        return {'x_min': BoundedFloatText(value=lb, min=lb),
                'x_max': BoundedFloatText(value=lb + 10., min=lb)}
    raise NotImplementedError()


def arg_widgets(arg_constraint):
    if isinstance(arg_constraint, constraints._Real):
        return FloatSlider(value=0., min=-10, max=10)
    if isinstance(arg_constraint, constraints._GreaterThan):
        return FloatSlider(value=0, min=arg_constraint.lower_bound, max=arg_constraint.lower_bound + 10)
    raise NotImplementedError()


def get_widgets(p):
    sliders = {arg: arg_widgets(arg_constraint) for arg, arg_constraint in p.arg_constraints.items()}
    sliders.update(support_range_widgets(p.support))
    sliders.update({'x_step': BoundedFloatText(value=0.001, min=0)})
    return sliders
