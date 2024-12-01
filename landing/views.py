from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage
from django.core.exceptions import ValidationError

def landing(request):
    return render(request, "index.html")


def c404(request):
    return render(request, '404.html', status=404)

def contact_view(request):
    if request.method == 'POST':
        # دریافت داده‌ها از فرم
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')

        # بررسی اینکه هیچ فیلدی خالی نباشد
        if not name or not email or not subject or not message:
            return JsonResponse({'success': False, 'message': 'لطفاً تمام فیلدها را پر کنید.'})

        # اعتبارسنجی ایمیل
        if '@' not in email:
            return JsonResponse({'success': False, 'message': 'لطفاً یک ایمیل معتبر وارد کنید.'})

        try:
            # ذخیره پیام در دیتابیس
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            return JsonResponse({'success': True, 'message': 'پیام شما با موفقیت ارسال شد!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'خطا در ارسال پیام: {str(e)}'})

    return JsonResponse({'success': False, 'message': 'فقط درخواست POST معتبر است.'})
