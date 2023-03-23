from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from django.shortcuts import redirect


class ProcessRequestMiddleware(MiddlewareMixin):
    @staticmethod
    def process_view(request, view_func, *view_args, **view_kwargs):
        current_url = resolve(request.path_info).url_name
        if current_url != 'login' \
                and current_url != 'register' \
                and current_url != 'schools' \
                and not request.user.is_authenticated:
            return redirect('login')
