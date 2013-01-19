from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.cache import cache
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
	# Get key
	ip = cache.get('ip', None)
	return render_to_response(
		'index.html',
		{
			'ip': ip,
		},
		context_instance=RequestContext(request)
		)


@csrf_exempt
def update_ip(request):
	# Only alow 'post' requests
	if request.method == 'POST':
		# Get ip
		ip = request.POST.get('ip', None)
		# Set ip in cache
		cache.set('ip', ip, 60)
		# Send okay response
		return HttpResponse('ok')
