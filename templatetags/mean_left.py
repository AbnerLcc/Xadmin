from django import template

register = template.Library()

# 添加一层文件,以app名字命名,防止找错地方
@register.inclusion_tag("login/mean_left.html")
def mean_left(request):

    mean=request.session.get("mean","")

    return {"mean":mean,"request":request}