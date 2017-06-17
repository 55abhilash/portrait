from django.conf.urls import url

urlpatterns = {
	url(r'^task_page/', 'portrait.task_page.views.send_task_list', name='send_task_list')
}
