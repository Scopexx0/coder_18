from django.http import HttpResponse
from django.template import loader

from family.models import Member

# def family(
#     self, name: str='name', dni: str='member', born_date: str='born_date'):
#     template = loader.get_template("flia_template.html")
    
#     user = Member(nombre=name, dni=dni, born_date=born_date)
#     user.save()
    
#     contexto = {
#         'user': user, 
#     }
#     render = template.render(contexto)
#     return HttpResponse(render)


def flia(self, id: int='id'):
    temp = loader.get_template('flia.html')

    flia = list(Member.objects.values_list()[id-1])
    flia1 = list(Member.objects.values_list()[id-1])
    flia2 = list(Member.objects.values_list()[id-1])
    flia3 = list(Member.objects.values_list()[id-1])

    context = {
        'flia': flia[0],
        'flia1': flia1[1],
        'flia2': flia2[2],
        'flia3': flia3[3],
    }

    render = temp.render(context)
    return HttpResponse(render)