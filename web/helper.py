from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
def login_required(view_func):
    """
    Custom decorator to check if a user is logged in and set a session variable.

    Args:
        view_func (function): The view function to be decorated.

    Returns:
        function: The decorated view function.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.has_key('login') and request.session.has_key('pk'):
            # User is logged in, set the session variable to True
            # request.session['login'] = True
            return view_func(request, *args, **kwargs)
        else:
            # User is not logged in, you can handle this case as needed
            messages.error(request,"Please login your account")
            return redirect('login')  # Redirect to the login page

    return _wrapped_view
