from django import template
import html

register = template.Library()

@register.filter
def get_evaluation_average(querySet, key):
    count = 0
    result = html.unescape("")
    average = querySet.get(key)
    if average is not None:
        while count < 5:
            if (average - count) >= 0.5:
                result = result + html.unescape(" &#9733;")
            else:
                result = result + html.unescape(" &#9734;")
            count += 1
        return result
    else:
        return "Nenhuma avaliação"