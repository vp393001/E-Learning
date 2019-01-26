
def checkuser(request):
    if request.user.is_authenticated:
        loggedin=True
    else:
        loggedin=False

    return {"loggedin":loggedin}
