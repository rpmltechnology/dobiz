from django import template

register = template.Library()

def addclass(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')
    css_classes += ' ' + arg
    value.field.widget.attrs['class'] = css_classes.strip()
    return value

def addplaceholder(value, arg):
    value.field.widget.attrs["placeholder"] = arg
    return value

def addvalue(value, arg):
    value.field.widget.attrs["value"] = arg
    return value

register.filter('addclass', addclass)
register.filter('addplaceholder', addplaceholder)
register.filter('addvalue', addvalue)
