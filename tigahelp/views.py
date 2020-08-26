from django.shortcuts import render
from django.template.loader import TemplateDoesNotExist

# Create your views here.


def show_about(request, platform, language):
    context = {}
    # We ignore platform for now
    # if platform == 'ios':
    #     if language == 'ca':
    #         return render(request, 'tigahelp/about_ios_ca.html', context)
    #     if language == 'es':
    #         return render(request, 'tigahelp/about_ios_es.html', context)
    #     if language == 'en':
    #         return render(request, 'tigahelp/about_ios_en.html', context)
    # else:
    if language == 'ca':
        return render(request, 'tigahelp/about_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/about_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/about_en.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/about_zh.html', context)


def show_credit_image(request):
    context = {}
    return render(request, 'tigahelp/credit_image.html', context)


def show_help(request, platform, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/help_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/help_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/help_en.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/help_zh.html', context)


def show_license(request, platform, language):
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/license_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/license_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/license_en.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/license_zh.html', context)


def show_policies(request):
    context = {}
    return render(request, 'tigahelp/policies.html', context)


def show_privacy(request, version=None):
    language = request.LANGUAGE_CODE
    context = {}
    if version is None:
        try:
            return render(request, 'tigahelp/privacy_' + language +'.html', context)
        except TemplateDoesNotExist:
            return render(request, 'tigahelp/privacy_en.html', context)
    else:
        try:
            return render(request, 'tigahelp/privacy_versions/' + version + '/privacy_' + language +'.html', context)
        except TemplateDoesNotExist:
            return render(request, 'tigahelp/privacy_en.html', context)



def show_terms(request):
    language = request.LANGUAGE_CODE
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/terms_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/terms_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/terms_en.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/terms_zh.html', context)


def show_scoring(request):
    language = request.LANGUAGE_CODE
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/scoring_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/scoring_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/scoring_en.html', context)
    if language == 'de':
        return render(request, 'tigahelp/scoring_de.html', context)
    if language == 'sq':
        return render(request, 'tigahelp/scoring_sq.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/scoring_en.html', context)
    return render(request, 'tigahelp/scoring_en.html', context)


def show_about_us(request):
    language = request.LANGUAGE_CODE
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/about_us_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/about_us_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/about_us_en.html', context)
    if language == 'de':
        return render(request, 'tigahelp/about_us_de.html', context)
    if language == 'sq':
        return render(request, 'tigahelp/about_us_sq.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/about_us_en.html', context)
    return render(request, 'tigahelp/about_us_en.html', context)


def show_project_about(request):
    language = request.LANGUAGE_CODE
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/project_about_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/project_about_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/project_about_en.html', context)
    if language == 'de':
        return render(request, 'tigahelp/project_about_de.html', context)
    if language == 'sq':
        return render(request, 'tigahelp/project_about_sq.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/project_about_en.html', context)
    return render(request, 'tigahelp/scoring_en.html', context)


def show_app_license(request):
    language = request.LANGUAGE_CODE
    context = {}
    if language == 'ca':
        return render(request, 'tigahelp/app_license_ca.html', context)
    if language == 'es':
        return render(request, 'tigahelp/app_license_es.html', context)
    if language == 'en':
        return render(request, 'tigahelp/app_license_en.html', context)
    if language == 'zh-cn':
        return render(request, 'tigahelp/app_license_en.html', context)