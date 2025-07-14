# راهنما

## نصب

1. مخزن را کلون کنید:  
   ```bash
   git clone https://github.com/ararai1991/webarchive-wp-import
   cd webarchive-wp-import
   ```
2. نصب کتابخانه‌های مورد نیاز:  
   ```bash
   pip install -r requirements.txt
   ```

## کتابخانه‌های مورد نیاز

- `requests`  
- `beautifulsoup4`  
- `lxml`  
- `python-dateutil` (اختیاری، برای پارس تاریخ پیشرفته)  
- کتابخانه‌های استاندارد: `datetime`، `urllib`، `time`، `sys`، `re`، `random`

یا به‌صورت جداگانه:  
```bash
pip install requests beautifulsoup4 lxml python-dateutil
```

## پیکربندی

### `export.py`

در دیکشنری `params` مقدار جایگزین `url` را با آدرس سایت وردپرسی خود وارد کنید:

```python
params = {
    "url": "ENTER-YOUR-WEBSITE-URL-HERE/*",
    # …
}
```

### `request.py`

در بخش قالب WXR، مقادیر زیر را با عنوان سایت و آدرس خود جایگزین کنید:

```xml
<title>ENTER-YOUR-TITLE</title>
<link>ENTER-YOUR-WEBSITE-URL-HERE</link>
```

## نحوه کار

1. **export.py**  
   - با استفاده از API آرشیو اینترنت (CDX)، اسنپ‌شات‌های پست‌های بلاگ را بازیابی می‌کند.  
   - URL و تاریخ هر پست را در فایل `export-urls.txt` ذخیره می‌کند.

2. **request.py**  
   - فایل `export-urls.txt` را می‌خواند و هر اسنپ‌شات HTML را دانلود می‌کند.  
   - با استفاده از BeautifulSoup عنوان، محتوا، نویسنده و تاریخ را استخراج می‌کند.  
   - یک فایل XML WXR (`final_wp_import.xml`) برای ایمپورت در وردپرس تولید می‌کند.
