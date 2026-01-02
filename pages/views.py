from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home_page_view(request):
    return render(request, 'pages/home.html')

@login_required(login_url='account_login')
def dashboard_page_view(request):
    return render(request, 'pages/dashboard.html')

@login_required(login_url='account_login')
def profile_page_view(request):
    return render(request, 'pages/profile.html')

@login_required
def profile_update_view(request):
    if request.method == 'POST':
        user = request.user

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        photo = request.FILES.get('photo')
        delete_photo = request.POST.get('delete_photo')  # دریافت فلگ حذف عکس

        # آپدیت نام و نام خانوادگی
        user.first_name = first_name
        user.last_name = last_name

        # سناریوی ۱: کاربر عکس جدید آپلود کرده
        if photo:
            user.photo = photo

        # سناریوی ۲: کاربر دکمه حذف عکس رو زده (و عکس جدیدی هم آپلود نکرده)
        elif delete_photo == 'true':
            # اینجا مسیر پیش‌فرض که تو مدل تعریف کردی رو میدیم
            user.photo = 'media/users_photos/default.png'

        user.save()

        # پیام برای نمایش به کاربر (فلش مسیج)
        messages.success(request, 'تغییرات با موفقیت ذخیره شد!')

        # ریدایرکت به همون صفحه‌ای که فرم توش بود (مثلاً settings)
        return redirect('profile')

        # اگه کسی با متد GET اومد سراغ این url، پرتش کن بیرون
    return redirect('profile')