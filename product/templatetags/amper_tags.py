from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key): # custom template tag that converts product title to the value of available items in the cart
    try:
        result = dictionary.get(key)
    except Exception:
        result = ""
    return result

@register.filter
def get_range(value):
  return range(int(value))

@register.filter
def get_subtraction(value):
	return range(int(5-value))
