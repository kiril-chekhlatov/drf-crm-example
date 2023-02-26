from django.http import HttpResponse


def get_protected_file(request, field_dir_path, filename):
    if request.user.is_staff:
        response = HttpResponse(status=200)
        response['Content-Type'] = ''
        response['X-Accel-Redirect'] = f'/protected/protected_files/{field_dir_path}/{filename}'
        return response
    else:
        return HttpResponse(status=401)
