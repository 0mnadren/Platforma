from django.shortcuts import render


def custom_bad_request_view(request, exception=None):
    return render(request, "error_handlers/400.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "error_handlers/403.html", {})


def custom_page_not_found_view(request, exception):
    return render(request, "error_handlers/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "error_handlers/500.html", {})
