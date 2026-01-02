from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # ۱. ستون‌هایی که تو لیست یوزرها می‌بینی (عکس رو هم اضافه کردیم)
    list_display = ('username', 'email', 'first_name', 'last_name', 'show_photo', 'is_staff')

    # ۲. فیلدهایی که موقع ویرایش یوزر نشون داده میشه
    # ما باید فیلد photo رو به fieldsets پیش‌فرض اضافه کنیم
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {'fields': ('photo',)}),
    )

    # ۳. فیلدهایی که موقع ساختن یوزر جدید (Add User) نشون داده میشه
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('photo',)}),
    )

    # ۴. تابعی برای نمایش عکس کوچیک توی لیست
    def show_photo(self, obj):
        if obj.photo:
            # نمایش عکس با سایز ۴۰ در ۴۰ و گرد
            return format_html(
                '<img src="{}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;" />',
                obj.photo.url)
        return "بدون عکس"

    show_photo.short_description = 'تصویر پروفایل'
