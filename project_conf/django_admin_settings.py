DJANGO_ADMIN_JAZZMIN_SETTINGS = {
    # Заголовок окна (по умолчанию, если отсутствует или None, используется current_admin_site.site_title)
    "site_title": "QAINAR",

    # Заголовок на экране входа (максимум 19 символов) (по умолчанию, если отсутствует или None, используется current_admin_site.site_header)
    "site_header": "QAINAR",

    # Заголовок на бренде (максимум 19 символов) (по умолчанию, если отсутствует или None, используется current_admin_site.site_header)
    "site_brand": "АСОИ QAINAR",

    # Логотип для вашего сайта, должен присутствовать в статических файлах, используется для бренда в верхнем левом углу
    "site_logo": "logo.svg",

    # Логотип для формы входа (по умолчанию используется site_logo)
    "login_logo": "logo.png",

    # Логотип для формы входа в темных темах (по умолчанию используется login_logo)
    "login_logo_dark": "logo.png",

    # Классы CSS, применяемые к логотипу вверху
    "site_logo_classes": "img-circle",

    # Относительный путь к иконке сайта (по умолчанию используется site_logo, если отсутствует)
    "site_icon": "logo.png",

    # Приветственный текст на экране входа
    "welcome_sign": "АСОИ QAINAR",

    # Копирайт в подвале
    "copyright": "РГУ Агентство Республики Казахстан по регулированию и развитию финансового рынка",

    # Список модельных администраторов для поиска из строки поиска
    # Если вы хотите использовать единое поле поиска, вам не нужно использовать список, вы можете использовать простую строку
    # "search_model": ["auth.User", "auth.Group"],

    # Имя поля на модели пользователя, содержащее изображение аватара ImageField/URLField/CharField или callable, получающий пользователя
    # "user_avatar": None,

    ############
    # Верхнее меню #
    ############

    # Ссылки для размещения в верхнем меню
    "topmenu_links": [

        # URL, который будет изменен (можно добавить разрешения)
        {"name": "Главная",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # внешний URL, открывающийся в новом окне (можно добавить разрешения)
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # модельный админ, к которому добавлены ссылки (проверка разрешений по моделям)
        {"model": "account.models.Profile"},

        # Приложение с выпадающим меню ко всем страницам его моделей (проверка разрешений по моделям)
        {"app": "account"},
    ],

    #############
    # Меню пользователя #
    #############

    # Дополнительные ссылки для включения в меню пользователя в верхнем правом углу (тип url "app" не разрешен)
    "usermenu_links": [
        {"name": "Поддержка", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Боковое меню #
    #############

    # Показывать ли боковое меню
    "show_sidebar": True,

    # Автоматически раскрывать меню
    "navigation_expanded": True,

    # Скрыть эти приложения при создании бокового меню (например, auth)
    "hide_apps": [],

    # Скрыть эти модели при создании бокового меню (например, auth.user)
    "hide_models": [],

    # Список приложений (и/или моделей) для упорядочивания бокового меню (не обязательно содержать все приложения/модели)
    "order_with_respect_to": ["auth"],

    # Пользовательские ссылки для добавления к группам приложений, сгруппированным по имени приложения
    "custom_links": {
        "account": [{
            "name": "Создать аккаунт", 
            "url": "add_profile", 
            "icon": "fas fa-user",
            "permissions": ["account.add_profile"]
        }]
    },

    # Пользовательские значки для приложений/моделей бокового меню См. https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # для полного списка бесплатных значков 5.13.0
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Значки, используемые при отсутствии явно указанных
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Модальные окна #
    #################
    # Использовать модальные окна вместо всплывающих окон
    "related_modal_active": False,

    #############
    # Изменить вид #
    #############
    # Выводить представление изменения как единую форму или во вкладках
    # Доступные варианты:
    # - single
    # - horizontal_tabs (по умолчанию)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",
    # Переопределить формы изменений для каждого модельного администратора
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Добавить выпадающий список языков в администраторе
}



UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    # "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}

    