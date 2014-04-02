from decimal import getcontext


def slope_style_score(scores):
    getcontext().prec = 2
    for i in range(0, len(scores)):
        if scores[i] == max(scores):
            del scores[i]
            break
    for i in range(0, len(scores)):
        if scores[i] == min(scores):
            del scores[i]
            break
    return("%.2f" % round(sum(scores) / len(scores), 2))
