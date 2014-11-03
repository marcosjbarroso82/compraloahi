def css_folder(request):
    print(request.GET)
    if 'css_folder' in request.GET:
        request.session['css_folder'] = request.GET['css_folder']

    if 'css_folder' in request.session:
        css_folder = request.session.get('css_folder')
    else:
        css_folder = 'css'

    return {'css_folder': css_folder + "/"}
