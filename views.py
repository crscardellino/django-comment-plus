from django.http import HttpResponse
from django.contrib import comments
from django.shortcuts import get_object_or_404

from comments_plus import models as cmodels
def karma_add(request,id):
	comment = get_object_or_404(comments.get_model(),pk=id)
	cmodels.Karma.objects.get_or_create(user=request.user,comment=comment)
	return HttpResponse("")

def karma_remove(request,id):
	return HttpRespons("")
