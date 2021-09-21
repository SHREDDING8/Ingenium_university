from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import View

from .forms import *
from .models import *


class Home(View):
    """
    Главная тсраница
    :param request:
    :return: главная страница
    """

    values = {
        "title": "Ingenium",
        'form': True,
        "header": True,
    }
    render_file = "home/home.html"

    def get(self, request):
        course1 = Course.objects.all()[:3]
        course2 = Course.objects.all()[3:6:]
        course1_mob = Course.objects.all()[:2]
        course2_mob = Course.objects.all()[2:4:]
        course3_mob = Course.objects.all()[4:6:]
        form = LendingHomeForm()
        self.values['course1'] = course1
        self.values['course2'] = course2

        self.values['course1_mob'] = course1_mob
        self.values['course2_mob'] = course2_mob
        self.values['course3_mob'] = course3_mob
        self.values['form_inputs'] = form
        return render(request, self.render_file, self.values)

    '''
    def post(self, request):
        bound_form = LendingHomeForm(request.POST)
        if bound_form.is_valid():
            # url = request.path + "?success=1"
            bound_form.save()
            return redirect(request.path + '#block_f')
        else:
            url = request.path  # + "?error=1"
            return redirect(url)
'''


class About(View):
    values = {
        "title": "О нас",
        'form': True,
        "color": 'about',
        "header": True,
    }
    render_file = 'about/about.html'

    def get(self, request):
        form = LendingHomeForm()
        form_review = ReviewFrom()
        reviews = Review.objects.all()[:3]
        reviews_2 = Review.objects.all()[:4]
        teachers = Teacher.objects.all()
        self.values['form_review'] = form_review
        self.values['form_inputs'] = form
        self.values['teachers'] = teachers
        self.values['reviews'] = reviews
        self.values['reviews_2'] = reviews_2
        self.values['user'] = request.user
        print(dir(request.user))

        return render(request, self.render_file, self.values)


class CallBack(View):
    def post(self, request):
        path = request.GET.get('next')
        bound_form = LendingHomeForm(request.POST)
        if bound_form.is_valid():
            # url = request.path + "?success=1"
            bound_form.save()
            return redirect(path + '#block_f')
        else:
            url = path  # + "?error=1"
            return redirect(url)


class Review_request(View):
    def post(self, request):
        path = request.GET.get('next')
        bound_form = ReviewFrom(request.POST)
        if bound_form.is_valid():
            # url = request.path + "?success=1"
            if request.user.is_authenticated:
                bound_form.save(first_name=request.user.first_name,second_name=request.user.last_name)
            else:
                bound_form.save()
            return redirect(path + '#review_f')
        else:
            url = path  # + "?error=1"
            return redirect(url)


class Courses_view(View):
    values = {
        "title": "Курсы",
        'form': True,
        "header": True,
        "color": 'courses',
    }
    render_file = "courses/courses/courses.html"

    def get(self, request):

        # запросы GET
        direction__checked = []
        lvl_hard = []
        checked__2 = {"direction": '0', "type": '0', "lvl_hard": '0'}
        try:
            for i in dict(request.GET)["direction"]:
                direction__checked.append(i)
            checked__2["direction"] = '1'
        except:
            pass

        try:
            for i in dict(request.GET)["type"]:
                direction__checked.append(i)
            checked__2["type"] = '1'
        except:
            pass

        try:
            for i in dict(request.GET)["lvl_hard"]:
                lvl_hard.append(i)
            checked__2["lvl_hard"] = '1'
        except:
            pass
        self.values['direction__checked'] = direction__checked
        self.values['lvl_hard'] = lvl_hard
        self.values['checked__2'] = checked__2

        form = LendingHomeForm()
        recommend = Course.objects.filter(recommend=True)
        # courses = Course.objects.all()
        directions = Direction.objects.all()
        self.values['form_inputs'] = form
        self.values['recommend'] = recommend
        self.values['directions'] = directions
        # поиск
        try:
            search_GET = dict(request.GET)['search']
        except:
            search_GET = ''

        search_path = ''
        filter = Q()
        if search_GET:
            for i in search_GET[0].split():
                filter |= Q(search_keys__icontains=i) | Q(name__icontains=i) | Q(name_2__icontains=i) | Q(
                    direction__name__icontains=i) | Q(direction__name_English__icontains=i)

            search_path = search_GET[0]

        try:
            directions_GET = dict(request.GET)['direction']
        except:
            directions_GET = dict(request.GET)['direction'] = ['all']

        try:
            type_study_GET = dict(request.GET)['type']
        except:
            type_study_GET = dict(request.GET)['type'] = ['Any']

        try:
            lvl_hard_GET = dict(request.GET)['lvl_hard']
        except:
            lvl_hard_GET = dict(request.GET)['lvl_hard'] = ['Any']

        if type_study_GET[0] == 'Any':
            type_study_GET = ['Profession', 'Course']
        if lvl_hard_GET[0] == 'Any':
            lvl_hard_GET = ['Easy', 'Hard']

        if search_GET:
            if directions_GET[0] == 'all':
                courses = Course.objects.filter(
                    (Q(lvl_hard__in=lvl_hard_GET) & Q(type_study__in=type_study_GET)) & (filter))
            else:
                courses = Course.objects.filter((Q(lvl_hard__in=lvl_hard_GET) & Q(type_study__in=type_study_GET) & Q(
                    direction__name_English__in=directions_GET)) & (filter))
        else:
            if directions_GET[0] == 'all':
                courses = Course.objects.filter((Q(lvl_hard__in=lvl_hard_GET) & Q(type_study__in=type_study_GET)))
            else:
                courses = Course.objects.filter(Q(lvl_hard__in=lvl_hard_GET) & Q(type_study__in=type_study_GET) & Q(
                    direction__name_English__in=directions_GET))
        # Пагинация
        paginator = Paginator(courses, 8)  # 8 поста на каждой странице
        page = request.GET.get('page')
        get_page = paginator.get_page(page)
        next = ''
        previous = ''
        # получем полный путь
        full_path = request.get_full_path()
        if dict(request.GET):
            if "page=" in full_path:
                if int(page) == 1:
                    previous = full_path.replace("page=1", "page=" + str(int(page)))
                else:
                    previous = full_path.replace("page=" + str(page), "page=" + str(int(page) - 1))
                if int(page) == paginator.num_pages:
                    next = full_path.replace("page=" + str(paginator.num_pages), "page=" + str(int(page)))
                else:
                    next = full_path.replace("page=" + str(page), "page=" + str(int(page) + 1))
            else:
                page = 1
                if int(page) == 1:
                    previous = full_path + '&page=' + str(int(page))
                else:
                    previous = full_path + '&page=' + str(int(page - 1))
                if int(page) == paginator.num_pages:
                    next = full_path + '&page=' + str(int(page))
                else:
                    next = full_path + '&page=' + str(int(page + 1))


        else:
            page = 1
            if int(page) == 1:
                previous = full_path + '?page=' + str(int(page))
            else:
                previous = full_path + '?page=' + str(int(page - 1))
            if int(page) == paginator.num_pages:
                next = full_path + '?page=' + str(int(page))
            else:
                next = full_path + '?page=' + str(int(page + 1))

        self.values['next'] = next
        self.values['previous'] = previous
        # страницы

        pages = []
        for i in paginator.page_range:
            if dict(request.GET):
                if "page=" in full_path:
                    pages.append({"number": str(i), "href": full_path.replace("page=" + str(page), "page=" + str(i))})
                else:
                    page = 1
                    pages.append({"number": str(i), "href": full_path + '&page=' + str(int(i))})
            else:
                page = 1
                pages.append({"number": str(i), "href": full_path + '?page=' + str(int(i))})

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            posts = paginator.page(paginator.num_pages)
        self.values['posts'] = posts
        self.values['page'] = str(page)
        self.values['max_page'] = str(paginator.num_pages)
        self.values['pages'] = pages
        self.values['search_path'] = search_path

        return render(request, self.render_file, self.values)


class Course_view(View):
    values = {
        'form': False,
        "header": False,
    }
    render_file = "Course/course/course.html"
    render_file_tik_tok = "Course/course/Tik-tok.html"
    render_file_404 = "Course/404/404.html"

    def get(self, request, id):

        try:
            course = Course.objects.get(pk=id)
            title = course.name + " " + course.name_2
            self.values['course'] = course
            self.values['title'] = title
            print(course.teachers.all())
            if title == 'Менеджер Tik-Tok аккаунта':
                return render(request, self.render_file_tik_tok, self.values)

            return render(request, self.render_file, self.values)
        except Exception as e:
            print(e)
            return render(request, self.render_file_404, self.values)


class Webinars_View(View):
    values = {
        "title": "Вебинары",
        "header": True,
        "color": 'webinars',
    }
    render_file = "webinars/webinars/webinars.html"

    def get(self, request):

        recommend = Webinar.objects.filter(recommend=True)
        dont_publish = Webinar.objects.filter(published=False)[:3]

        webinars = Webinar.objects.all()
        try:
            search_GET = dict(request.GET)['search']
            filter = Q()
            if search_GET:
                for i in search_GET[0].split():
                    filter |= Q(search__icontains=i)

            webinars = Webinar.objects.annotate(
                search=SearchVector('name', 'direction__name', 'teacher__first_name', 'teacher__second_name'),
            ).filter(filter)
        except Exception as e:
            print(e)

        self.values['recommend'] = recommend
        self.values['dont_publish'] = dont_publish

        paginator = Paginator(webinars, 24)  # 24 поста на каждой странице
        page = request.GET.get('page')

        full_path = request.get_full_path()
        if dict(request.GET):
            if "page=" in full_path:
                if int(page) == 1:
                    previous = full_path.replace("page=1", "page=" + str(int(page)))
                else:
                    previous = full_path.replace("page=" + str(page), "page=" + str(int(page) - 1))
                if int(page) == paginator.num_pages:
                    next = full_path.replace("page=" + str(paginator.num_pages), "page=" + str(int(page)))
                else:
                    next = full_path.replace("page=" + str(page), "page=" + str(int(page) + 1))
            else:
                page = 1
                if int(page) == 1:
                    previous = full_path + '&page=' + str(int(page))
                else:
                    previous = full_path + '&page=' + str(int(page - 1))
                if int(page) == paginator.num_pages:
                    next = full_path + '&page=' + str(int(page))
                else:
                    next = full_path + '&page=' + str(int(page + 1))


        else:
            page = 1
            if int(page) == 1:
                previous = full_path + '?page=' + str(int(page))
            else:
                previous = full_path + '?page=' + str(int(page - 1))
            if int(page) == paginator.num_pages:
                next = full_path + '?page=' + str(int(page))
            else:
                next = full_path + '?page=' + str(int(page + 1))

        self.values['next'] = next
        self.values['previous'] = previous
        # страницы

        pages = []
        for i in paginator.page_range:
            if dict(request.GET):
                if "page=" in full_path:
                    pages.append({"number": str(i), "href": full_path.replace("page=" + str(page), "page=" + str(i))})
                else:
                    page = 1
                    pages.append({"number": str(i), "href": full_path + '&page=' + str(int(i))})
            else:
                page = 1
                pages.append({"number": str(i), "href": full_path + '?page=' + str(int(i))})

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            posts = paginator.page(paginator.num_pages)
        self.values['posts'] = posts
        self.values['page'] = str(page)
        self.values['max_page'] = str(paginator.num_pages)
        self.values['pages'] = pages
        self.values['color'] = 'webinars_color'
        return render(request, self.render_file, self.values)


class Webinar_watch_View(View):
    values = {
        'form': False,
        "header": True,
        "title": "Курсы",
        "color": 'webinars_color',

    }
    render_file = 'webinars/webinar_watch/webinar_watch.html'
    render_file_404 = 'webinars/404/404.html'

    def get(self, request, id):
        try:
            webinar_watch = Webinar.objects.get(pk=id)
        except:
            self.values['header'] = False
            return render(request, self.render_file_404, self.values)

        if not webinar_watch.link or not webinar_watch.published:
            self.values['header'] = False
            return render(request, self.render_file_404, self.values)


        src = webinar_watch.link.split("v=")[1]

        self.values['header'] = True
        self.values['webinar_watch'] = webinar_watch
        self.values['src'] = src
        return render(request, self.render_file, self.values)


def lk(request):
    pass
