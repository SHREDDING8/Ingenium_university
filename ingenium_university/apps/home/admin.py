from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


# Register your models here.


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_2', 'direction', 'how_long', 'recommend', 'preview')
    list_display_links = ('direction', 'name', 'name_2', 'how_long', 'preview')
    search_fields = ('direction', 'name', 'name_2', 'how_long', 'min_price')

    fields = (
        'direction', 'name', 'name_2', 'how_long', 'min_price', "standart_price", "vip_price",
        'teachers', 'type_study', "lvl_hard", 'image_course', 'background_color',
        'color_2', 'search_keys', 'recommend', 'preview')

    readonly_fields = ('preview',)

    def preview(self, obj):
        photo = ''
        background = '#fff'
        direction = ''
        name = ''
        name_2 = ''
        how_long = ''
        min_price = ''
        text_color = ''
        color_direction = ''

        if obj.image_course.url:
            photo = obj.image_course.url

        if obj.background_color:
            background = obj.background_color

        if obj.direction:
            direction = obj.direction

        if obj.name:
            name = obj.name

        if obj.name_2:
            name_2 = obj.name_2

        if obj.how_long:
            how_long = obj.how_long

        if obj.min_price:
            min_price = obj.min_price

        color_direction = '#4d4d4d'

        text_color = '#000'

        preview = f'''
        <style>
        .flex__title__img__course{{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .courses__item{{
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            width: 296px;
            height: 123px;
            box-shadow: 0px 2px 4px 0px rgba(102,102,102,0.34);
            border-radius: 20px;
            padding:40px 28px 27px 28px;
            color:{text_color};
        }}
        a:focus{{
        text-decoration:none;
        }}
        .course__title{{
            font-family: 'Roboto__Bold';
            font-size: 21px;
            line-height: 1.2;
            font-weight:700;
        }}
        .category{{
            position: absolute;
            font-size: 15px;
            font-family: 'Roboto', sans-serif;
            color: {color_direction};
            top: 26px;
        }}
        .flex__how__long__price{{
            font-family: 'Roboto__Bold';
            display: flex;
            justify-content: space-between;
            font-weight:700;
            font-size: 14px;
        }}
        </style>
        
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap" rel="stylesheet">
        <div>
            <div style="background-color:{background};" class="courses__item">
                <div class="category">{direction}</div>
                
                <div class="flex__title__img__course">
                    <div class="course__title">
                        <div class="first__title">
                            {name}
                        </div>
                        <div class="second__title">
                            {name_2}
                        </div>
                    </div>
                    <div class="img">
                        <img style='max-width:90px;' src="{photo}" alt="">
                    </div>
                </div>
    
                <div class="flex__how__long__price">
                    <div class="how_long">
                        {how_long}
                    </div>
                    <div class="price">
                         От {min_price} ₽
                    </div>
                </div>
            </div>
        </div>'''
        return mark_safe(preview)


class LendingHomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date')
    search_fields = ('name', 'phone', 'email')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', "profession", "preview")
    search_fields = ('first_name', 'second_name', 'profession')
    fields = ('first_name', 'second_name', "profession", "photo", "preview")
    readonly_fields = ('preview',)

    def preview(self, obj):
        r = f'''
        <style>
        .block{{
            width: 166px;
        }}
        .img{{
            width: 166px; 
            height: 166px; 
            background-color: #f0f0f0; 
            border:2px solid #3399ff; 
            border-radius: 1000px;
        }}
        .name{{
            margin-top:27px;
            font-size: 20px; 
            font-family: Roboto; 
            font-weight:700;
            text-align: center;
        }}
        .profession{{
            margin-top:11px;
            font-size: 17px;
            font-family: Roboto; 
            text-align: center;
        }}
        img{{
        border-radius:100px;
        }}
        </style>   
        
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap" rel="stylesheet">     
        <div class="block">
            <div class="img">
            <img width="100%" src="{obj.photo.url}">	
            </div>
            <div class="name">
            {obj.first_name} {obj.second_name}
            </div>
            <div class="profession">
            {obj.profession}
            </div>
        </div>
        '''
        return mark_safe(r)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'review', 'date')
    search_fields = ('first_name', 'second_name', 'review')
    readonly_fields = ('date',)


class WebinarAdmin(admin.ModelAdmin):
    list_display = ('name', "direction", "teacher", 'datetime', "recommend", "published", "kol_prosm")
    list_display_links = ('name', "direction", "teacher", 'datetime', "recommend", "published", "kol_prosm")

    fields = ('name', 'direction', "teacher", "datetime", "link",'description', 'files', 'photo_preview','preview','color','color_2','recommend','published','kol_prosm')

    readonly_fields = ('kol_prosm','preview')

    def preview(self, obj):
        r = f'''
        <style>
        .web__item .web__item_preview{{
        width: 256px;
        height: 144px;
        border: solid 2px #000;
    }}
        </style>
            <div class="web__item">
					<div class="web__item_preview">
						<img width="100%" height="100%" src="{obj.photo_preview.url}" alt="">
					</div>

					<div class="web__item__text">
						<p>{obj.name}</p>
						<div>
							15.07.2021   {obj.kol_prosm} просмотров
						</div>
					</div>
				</div>
            '''
        return mark_safe(r)


admin.site.register(models.Direction, DirectionAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.LendingHome, LendingHomeAdmin)

admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.Review, ReviewAdmin)



admin.site.register(models.Webinar,WebinarAdmin)
